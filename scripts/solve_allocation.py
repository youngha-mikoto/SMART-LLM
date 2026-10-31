import argparse
import ast
import json
from pathlib import Path


def load_task_requirements(requirements_path):
    return json.loads(Path(requirements_path).read_text(encoding="utf-8"))


def load_robots(log_path):
    lines = Path(log_path).read_text(encoding="utf-8").splitlines()
    for line in lines:
        if line.startswith("robots = "):
            return ast.literal_eval(line.split(" = ", 1)[1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("requirements_path", type=Path)
    args = parser.parse_args()

    requirements = load_task_requirements(args.requirements_path)
    robots = load_robots(args.requirements_path.with_name("log.txt"))
    print(json.dumps({"requirements": requirements, "robots": robots}, indent=2))
