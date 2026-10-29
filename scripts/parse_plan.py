import argparse
import ast
from pathlib import Path


def extract_subtask_names(plan_path):
    source = Path(plan_path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(plan_path))
    return [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]


def extract_thread_targets(plan_path):
    source = Path(plan_path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(plan_path))
    thread_targets = {}

    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not isinstance(node.value, ast.Call):
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("plan_path", help="Path to decomposed_plan.py")
    args = parser.parse_args()

    for name in extract_subtask_names(args.plan_path):
        print(name)
    print(extract_thread_targets(args.plan_path))
    for event in extract_execution_events(args.plan_path):
        print(event)
