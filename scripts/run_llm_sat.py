import json


def print_tasks():
    with open("data/final_test/FloorPlan6.json", encoding="utf-8") as file:
        for line in file:
            print(json.loads(line)["task"])


if __name__ == "__main__":
    print_tasks()
