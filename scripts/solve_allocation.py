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


def find_eligible_robots(requirements, robots):
    eligible_robots = {}
    for name, task in requirements["subtasks"].items():
        payload = task["required_max_payload_kg"]
        if payload is None:
            raise ValueError(f"Maximum payload is unknown for {name}.")

        skills = set(task["required_skills"])
        eligible_robots[name] = []
        for robot in robots:
            capacity = (
                robot["mass_capacity"] if "mass_capacity" in robot else robot["mass"]
            )
            if skills.issubset(robot["skills"]) and payload <= capacity:
                eligible_robots[name].append(robot["name"])

    return eligible_robots


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("requirements_path", type=Path)
    args = parser.parse_args()

    requirements = load_task_requirements(args.requirements_path)
    robots = load_robots(args.requirements_path.with_name("log.txt"))
    eligible_robots = find_eligible_robots(requirements, robots)
    print(json.dumps({
        "requirements": requirements,
        "robots": robots,
        "eligible_robots": eligible_robots,
    }, indent=2))
