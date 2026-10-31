# SMART-LLM + SAT Solver

- 개별연구(CSC 현장실습-모바일 로봇 인공지능 기술 개발)

## Key Implementations

| File | Description |
| --- | --- |
| [estimate_payload.py](scripts/estimate_payload.py) | Estimates each subtask's maximum payload using an LLM and saves the results and token usage. |
| [parse_plan.py](scripts/parse_plan.py) | Extracts required skills, DAG edges, and execution layers from plan code using AST analysis. |
