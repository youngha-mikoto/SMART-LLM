import argparse
import json


def print_tasks(floor_plan):
    with open(f"data/final_test/FloorPlan{floor_plan}.json", encoding="utf-8") as file:
        for line in file:
            print(json.loads(line)["task"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--floor-plan", type=int, required=True)
    args = parser.parse_args()

    print_tasks(args.floor_plan)
