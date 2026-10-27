import argparse
import ast
from pathlib import Path


def extract_subtask_names(plan_path):
    source = Path(plan_path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(plan_path))
    return [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("plan_path", help="Path to decomposed_plan.py")
    args = parser.parse_args()

    for name in extract_subtask_names(args.plan_path):
        print(name)
