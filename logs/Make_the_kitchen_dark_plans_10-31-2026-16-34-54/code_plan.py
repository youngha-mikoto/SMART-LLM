# CODE Solution
robots = [{'name': 'robot1', 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'SwitchOn', 'SwitchOff', 'PickupObject', 'PutObject', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'], 'mass': 100}]

def make_kitchen_dark(robot_list):
    # SubTask 1: Switch off the kitchen lights (sequential due to single robot)
    GoToObject(robot_list[0], 'LightSwitch')
    SwitchOff(robot_list[0], 'LightSwitch')
    # SubTask 2: Block outside light by closing blinds and window
    GoToObject(robot_list[0], 'Blinds')
    CloseObject(robot_list[0], 'Blinds')
    GoToObject(robot_list[0], 'Window')
    CloseObject(robot_list[0], 'Window')

# Execute with robot1
make_kitchen_dark([robots[0]])