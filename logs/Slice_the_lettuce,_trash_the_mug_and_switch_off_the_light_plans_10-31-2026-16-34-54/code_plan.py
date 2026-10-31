# CODE Solution

# Robot selection per allocation plan
robots = [
    {'name': 'robot1', 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'SwitchOn', 'SwitchOff', 'PickupObject', 'PutObject', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'], 'mass_capacity': 0.4},
    {'name': 'robot2', 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'SwitchOn', 'SwitchOff', 'PickupObject', 'PutObject', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'], 'mass_capacity': 2.1},
    {'name': 'robot3', 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'SwitchOn', 'SwitchOff', 'PickupObject', 'PutObject', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'], 'mass_capacity': 1.0}
]

def slice_lettuce(robot):
    # Assigned: robot1
    # 1: Go to the Knife.
    GoToObject(robot, 'Knife')
    # 2: Pick up the Knife.
    PickupObject(robot, 'Knife')
    # 3: Go to the Lettuce.
    GoToObject(robot, 'Lettuce')
    # 4: Slice the Lettuce.
    SliceObject(robot, 'Lettuce')
    # 5: Go to the CounterTop.
    GoToObject(robot, 'CounterTop')
    # 6: Put the Knife on the CounterTop.
    PutObject(robot, 'Knife', 'CounterTop')

def trash_mug(robot):
    # Assigned: robot3
    # 1: Go to the Mug.
    GoToObject(robot, 'Mug')
    # 2: Pick up the Mug.
    PickupObject(robot, 'Mug')
    # 3: Go to the GarbageCan.
    GoToObject(robot, 'GarbageCan')
    # 4: Put the Mug in the GarbageCan.
    PutObject(robot, 'Mug', 'GarbageCan')

def switch_off_light(robot):
    # Assigned after parallel phase: robot1
    # 1: Go to the LightSwitch.
    GoToObject(robot, 'LightSwitch')
    # 2: Switch off the LightSwitch.
    SwitchOff(robot, 'LightSwitch')

# Parallel execution of SubTask 1 and SubTask 2
r1 = robots[0]  # robot1 for slicing lettuce
r3 = robots[2]  # robot3 for trashing mug

task1_thread = threading.Thread(target=slice_lettuce, args=(r1,))
task2_thread = threading.Thread(target=trash_mug, args=(r3,))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

# Sequential execution of SubTask 3 after both threads finish
switch_off_light(r1)

# Task slice the lettuce, trash the mug and switch off the light is done