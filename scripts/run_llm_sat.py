import argparse
import json
import sys
from pathlib import Path

from ai2thor.controller import Controller

sys.path.append(str(Path(__file__).resolve().parents[1]))

from resources.actions import ai2thor_actions


def load_actions():
    return ai2thor_actions


def load_tasks(floor_plan):
    with open(f"data/final_test/FloorPlan{floor_plan}.json", encoding="utf-8") as file:
        return [json.loads(line)["task"] for line in file]


def load_decomposition_examples():
    return Path("data/pythonic_plans/train_task_decompose.py").read_text(
        encoding="utf-8"
    )


def build_decomposition_prompt(task, actions, examples):
    return (
        "Follow the examples to decompose the task. Return only Python code.\n\n"
        f"Available actions: {actions}\n\n"
        f"{examples}\n\n"
        f"# Task Description: {task}"
    )


def load_objects(floor_plan):
    controller = Controller(scene=f"FloorPlan{floor_plan}")
    objects = [
        {"name": obj["objectType"], "mass": obj["mass"]}
        for obj in controller.last_event.metadata["objects"]
    ]
    controller.stop()
    return objects


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--floor-plan", type=int, required=True)
    args = parser.parse_args()

    tasks = load_tasks(args.floor_plan)
    for task in tasks:
        print(task)
