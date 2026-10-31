# CODE Solution

def put_apple_in_fridge(robot):
    # SubTask 1: Put apple in the fridge (assigned to robot1)
    GoToObject(robot, 'Apple')
    PickupObject(robot, 'Apple')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Apple', 'Fridge')
    CloseObject(robot, 'Fridge')

def switch_off_light(robot):
    # SubTask 2: Switch off the light (assigned to robot2)
    GoToObject(robot, 'LightSwitch')
    SwitchOff(robot, 'LightSwitch')

# Execute in parallel
task1_thread = threading.Thread(target=put_apple_in_fridge, args=(robots[0],))  # robot1
task2_thread = threading.Thread(target=switch_off_light, args=(robots[1],))     # robot2

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

# Task put apple in fridge and switch off the light is done