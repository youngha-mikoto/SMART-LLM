SOLUTION

1) Determine allocation basis
- All robots have the same skill set. Objects have varying masses.
- Therefore, focus on Task Allocation based on Mass alone, while still confirming required skills are present.

2) Subtasks, required skills, and masses
- SubTask 1: Put apple in the fridge
  - Required skills: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
  - Mass-relevant object: Apple = 0.20
  - Other objects interacted with: Fridge (Open/Close; no lifting), mass = 0.0
- SubTask 2: Switch off the light
  - Required skills: GoToObject, SwitchOff
  - Mass-relevant object: none (LightSwitch mass = 0.0)

3) Check if robot teams are required (Mass-based)
- SubTask 1 (Pickup Apple): any single robot must have capacity ≥ 0.20. All robots have mass capacity = 100, so a single robot suffices.
- SubTask 2: no pickup; no mass constraint. A single robot suffices.
- Conclusion: No teams required.

4) Verify skill availability
- All robots have: GoToObject, PickupObject, OpenObject, PutObject, CloseObject, SwitchOff. Skills match for both subtasks.

5) Sequential vs parallel
- The subtasks are independent and can be performed in parallel.
- With multiple robots available and no conflicts, execute in parallel.

6) Allocation (use the minimum robots per subtask; parallelize overall)
- Assign SubTask 1 (Put apple in fridge) to robot1
  - Mass check: 100 ≥ 0.20 — OK
  - Skills: all required — OK
- Assign SubTask 2 (Switch off light) to robot2
  - Mass check: not applicable
  - Skills: all required — OK
- robot3 remains idle as reserve.

7) Execution plan
- Run SubTask 1 (robot1) and SubTask 2 (robot2) in parallel.
- No interdependencies; both can start immediately.
- No team coordination needed; all mass and skill constraints satisfied.