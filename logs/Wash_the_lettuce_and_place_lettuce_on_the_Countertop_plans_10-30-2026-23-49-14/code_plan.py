# CODE Solution

# Normalize/prepare robot list (unify capacity key)
robots = [
    {'name': 'robot1', 'skills': ['GoToObject', 'BreakObject', 'SwitchOn', 'SwitchOff', 'PickupObject', 'PutObject', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'], 'mass_capacity': 100},
    {'name': 'robot2', 'skills': ['GoToObject', 'PickupObject', 'PutObject'], 'mass_capacity': 100},
    {'name': 'robot3', 'skills': ['GoToObject', 'BreakObject', 'SliceObject', 'SwitchOn', 'SwitchOff', 'PickupObject', 'PutObject', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'], 'mass_capacity': 100}
]

# Helpers
def get_object_mass(name):
    for o in objects:
        if o['name'] == name:
            return o['mass']
    return 0.0

def has_skills(robot, needed):
    return all(s in robot['skills'] for s in needed)

def capacity_ok(robot, obj_name):
    return robot.get('mass_capacity', robot.get('mass', 0)) >= get_object_mass(obj_name)

# Allocation decision:
# Choose a single robot that covers GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff.
# Both robot1 and robot3 qualify; select robot3.
robot_ops = robots[2]

# Partial execution (will halt before cleaning due to missing CleanObject on all robots)
def wash_lettuce_and_place_partial(robot):
    required = ['GoToObject', 'PickupObject', 'PutObject', 'SwitchOn', 'SwitchOff']
    if not has_skills(robot, required):
        raise RuntimeError(f"{robot['name']} lacks required skills for pre/ post-clean steps: {required}")
    if not capacity_ok(robot, 'Lettuce'):
        raise RuntimeError(f"{robot['name']} lacks capacity for Lettuce")

    # 1: Move lettuce to sink
    GoToObject(robot, 'Lettuce')
    PickupObject(robot, 'Lettuce')
    GoToObject(robot, 'Sink')
    PutObject(robot, 'Lettuce', 'Sink')

    # 2: Turn on faucet to rinse
    GoToObject(robot, 'Faucet')
    SwitchOn(robot, 'Faucet')
    time.sleep(3)

    # 3: Cannot proceed: CleanObject is missing across all robots. Turn off faucet and abort.
    SwitchOff(robot, 'Faucet')
    raise RuntimeError("Task cannot be completed: no robot has CleanObject skill.")

# Execute with allocated robot (will raise at the missing CleanObject step)
try:
    wash_lettuce_and_place_partial(robot_ops)
except RuntimeError as e:
    print(e)

# If a robot with CleanObject becomes available (example):
# new_robot = {'name': 'robot_cleaner', 'skills': ['GoToObject', 'CleanObject'], 'mass_capacity': 5}
# def wash_lettuce_and_place_full(robot_move, robot_clean):
#     # Move to sink
#     GoToObject(robot_move, 'Lettuce')
#     PickupObject(robot_move, 'Lettuce')
#     GoToObject(robot_move, 'Sink')
#     PutObject(robot_move, 'Lettuce', 'Sink')
#     # Rinse + clean
#     GoToObject(robot_move, 'Faucet')
#     SwitchOn(robot_move, 'Faucet')
#     GoToObject(robot_clean, 'Lettuce')
#     CleanObject(robot_clean, 'Lettuce')
#     SwitchOff(robot_move, 'Faucet')
#     # Place on countertop
#     PickupObject(robot_move, 'Lettuce')
#     GoToObject(robot_move, 'CounterTop')
#     PutObject(robot_move, 'Lettuce', 'CounterTop')
# # wash_lettuce_and_place_full(robot_ops, new_robot)