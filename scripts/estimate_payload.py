import argparse
import ast
import json
from pathlib import Path

import openai


def load_object_masses(log_path):
    lines = Path(log_path).read_text(encoding="utf-8").splitlines()
    for line in lines:
        if line.startswith("objects = "):
            return ast.literal_eval(line.split(" = ", 1)[1])


def build_payload_prompt(plan, objects):
    return (
        "Estimate the maximum payload in kg for each subtask function.\n"
        "Use the supplied object masses. Do not invent missing masses.\n"
        "Find the maximum total mass carried at one time, not the sum of all "
        "objects used during the subtask. Include carried tools and container contents.\n"
        "Use the full plan to track contents added by earlier subtasks.\n"
        "State any assumptions about slices, quantities, or object selection. "
        "Use null if the payload cannot be estimated from the supplied data.\n"
        "Return only JSON without Markdown fences, keyed by subtask function name.\n"
        "Use the exact top-level function names as JSON keys.\n"
        "Do not split or rename functions based on subtask comments.\n"
        "Each value must contain required_max_payload_kg and assumption.\n\n"
        f"Objects (mass in kg):\n{json.dumps(objects, indent=2)}\n\n"
        f"Plan:\n{plan}"
    )


def build_payload_prompt_from_file(plan_path):
    plan_path = Path(plan_path)
    plan = plan_path.read_text(encoding="utf-8")
    objects = load_object_masses(plan_path.with_name("log.txt"))
    return build_payload_prompt(plan, objects)


def set_api_key(api_key_path):
    openai.api_key = Path(api_key_path).read_text(encoding="utf-8").strip()


def estimate_payload(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=8192,
        response_format={"type": "json_object"},
    )
    choice = response["choices"][0]
    if choice["finish_reason"] != "stop":
        raise ValueError(f"Payload estimation did not finish: {choice['finish_reason']}")
    return json.loads(choice["message"]["content"]), response["usage"]


def save_token_usage(log_path, usage):
    log_path = Path(log_path)
    lines = log_path.read_text(encoding="utf-8").splitlines()
    usage_line = next(line for line in lines if line.startswith("token_usage = "))
    token_usage = json.loads(usage_line.split(" = ", 1)[1])
    token_usage["payload_estimation"] = usage
    total_usage = {
        key: sum(stage[key] for stage in token_usage.values())
        for key in ("prompt_tokens", "completion_tokens", "total_tokens")
    }

    for index, line in enumerate(lines):
        if line.startswith("token_usage = "):
            lines[index] = f"token_usage = {json.dumps(token_usage)}"
        elif line.startswith("total_token_usage = "):
            lines[index] = f"total_token_usage = {json.dumps(total_usage)}"

    lines = [line for line in lines if not line.startswith("payload_token_usage = ")]
    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def save_payload_estimates(requirements_path, estimates):
    requirements_path = Path(requirements_path)
    requirements = json.loads(requirements_path.read_text(encoding="utf-8"))
    if set(estimates) != set(requirements["subtasks"]):
        raise ValueError("Estimated subtask names do not match task requirements.")

    for name, estimate in estimates.items():
        requirements["subtasks"][name]["required_max_payload_kg"] = estimate[
            "required_max_payload_kg"
        ]
        requirements["subtasks"][name]["assumption"] = estimate["assumption"]

    requirements_path.write_text(
        json.dumps(requirements, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("plan_path", help="Path to decomposed_plan.py")
    parser.add_argument("--api-key-file", default="api_key.txt")
    args = parser.parse_args()

    prompt = build_payload_prompt_from_file(args.plan_path)
    set_api_key(args.api_key_file)
    estimates, usage = estimate_payload(prompt)
    save_token_usage(Path(args.plan_path).with_name("log.txt"), usage)
    save_payload_estimates(Path(args.plan_path).with_name("task_requirements.json"), estimates)
    print(json.dumps(estimates, indent=2, ensure_ascii=False))
