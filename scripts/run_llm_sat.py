import argparse
import json


def load_tasks(floor_plan):
    with open(f"data/final_test/FloorPlan{floor_plan}.json", encoding="utf-8") as file:
        return [json.loads(line)["task"] for line in file]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--floor-plan", type=int, required=True)
    args = parser.parse_args()

    tasks = load_tasks(args.floor_plan)
    for task in tasks:
        print(task)
