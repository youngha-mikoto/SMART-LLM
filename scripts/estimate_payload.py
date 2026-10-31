import json


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
        "Each value must contain required_max_payload_kg and assumption.\n\n"
        f"Objects (mass in kg):\n{json.dumps(objects, indent=2)}\n\n"
        f"Plan:\n{plan}"
    )
