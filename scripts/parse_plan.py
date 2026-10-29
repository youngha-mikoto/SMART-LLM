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


def extract_used_objects(plan_path):
    source = Path(plan_path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(plan_path))
    used_objects = {}

    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue

        objects = []
        for statement in node.body:
            if not isinstance(statement, ast.Expr) or not isinstance(
                statement.value, ast.Call
            ):
                continue
            if not isinstance(statement.value.func, ast.Name):
                continue
            for arg in statement.value.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    if arg.value not in objects:
                        objects.append(arg.value)

        used_objects[node.name] = objects

    return used_objects


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("plan_path", help="Path to decomposed_plan.py")
    args = parser.parse_args()

    print("Subtasks:")
    for name in extract_subtask_names(args.plan_path):
        print(name)

    print("\nRequired skills:")
    required_skills = extract_required_skills(args.plan_path)
    for name, skills in required_skills.items():
        print(f"{name}: {skills}")

    output_path = Path(args.plan_path).with_name("required_skills.json")
    output_path.write_text(json.dumps(required_skills, indent=2) + "\n", encoding="utf-8")

    print("\nUsed objects:")
    for name, objects in extract_used_objects(args.plan_path).items():
        print(f"{name}: {objects}")

    print("\nThread targets:")
    print(extract_thread_targets(args.plan_path))

    print("\nExecution events:")
    for event in extract_execution_events(args.plan_path):
        print(event)

    print("\nDAG:")
    print(build_dag(extract_execution_events(args.plan_path)))
