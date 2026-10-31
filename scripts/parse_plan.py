import argparse
import ast
import json
from pathlib import Path


def extract_subtask_names(plan_path):
    source = Path(plan_path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(plan_path))
    return [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]


def extract_required_skills(plan_path):
    source = Path(plan_path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(plan_path))
    required_skills = {}

    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue

        skills = []
        for statement in node.body:
            if not isinstance(statement, ast.Expr) or not isinstance(
                statement.value, ast.Call
            ):
                continue
            func = statement.value.func
            if isinstance(func, ast.Name) and func.id not in skills:
                skills.append(func.id)

        required_skills[node.name] = skills

    return required_skills


def extract_thread_targets(plan_path):
    source = Path(plan_path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(plan_path))
    thread_targets = {}

    for node in tree.body:
        if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Call):
            continue
        if ast.unparse(node.value.func) != "threading.Thread":
            continue

        for keyword in node.value.keywords:
            if keyword.arg == "target":
                thread_targets[node.targets[0].id] = keyword.value.id

    return thread_targets


def extract_execution_events(plan_path):
    source = Path(plan_path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(plan_path))
    subtask_names = extract_subtask_names(plan_path)
    thread_targets = extract_thread_targets(plan_path)
    events = []

    for node in tree.body:
        if not isinstance(node, ast.Expr) or not isinstance(node.value, ast.Call):
            continue

        func = node.value.func
        if isinstance(func, ast.Name) and func.id in subtask_names:
            events.append(("call", func.id))
        elif isinstance(func, ast.Attribute) and func.attr in ("start", "join"):
            thread_name = ast.unparse(func.value)
            if thread_name in thread_targets:
                events.append((func.attr, thread_targets[thread_name]))

    return events


def build_dag(events):
    nodes = []
    edges = []
    predecessors = []

    for kind, name in events:
        if kind == "join":
            predecessors.append(name)
        else:
            nodes.append(name)
            edges.extend((previous, name) for previous in predecessors)
            if kind == "call":
                predecessors = [name]

    return {"nodes": nodes, "edges": edges}


def build_execution_layers(dag):
    nodes = dag["nodes"][:]
    edges = dag["edges"][:]
    layers = []

    while nodes:
        blocked = {target for source, target in edges}
        layer = [node for node in nodes if node not in blocked]
        layers.append(layer)
        nodes = [node for node in nodes if node not in layer]
        edges = [(source, target) for source, target in edges if source not in layer]

    return layers


def save_task_requirements(plan_path, required_skills, dag):
    requirements = {
        "subtasks": {
            name: {"required_skills": skills}
            for name, skills in required_skills.items()
        },
        "edges": dag["edges"],
        "execution_layers": build_execution_layers(dag),
    }
    output_path = Path(plan_path).with_name("task_requirements.json")
    output_path.write_text(json.dumps(requirements, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("plan_path", help="Path to decomposed_plan.py")
    args = parser.parse_args()

    print("Parsing Decomposed Plans...")
    required_skills = extract_required_skills(args.plan_path)
    events = extract_execution_events(args.plan_path)
    dag = build_dag(events)
    save_task_requirements(args.plan_path, required_skills, dag)
