# CODE Solution

def cook_potato_in_microwave(robot):
    # 0: SubTask 1: Cook the Potato (Microwave)
    # 1: Go to the Potato.
    GoToObject(robot, 'Potato')
    # 2: Pick up the Potato.
    PickupObject(robot, 'Potato')
    # 3: Go to the Microwave.
    GoToObject(robot, 'Microwave')
    # 4: Open the Microwave.
    OpenObject(robot, 'Microwave')
    # 5: Put the Potato inside the Microwave.
    PutObject(robot, 'Potato', 'Microwave')
    # 6: Close the Microwave.
    CloseObject(robot, 'Microwave')
    # 7: Switch on the Microwave.
    SwitchOn(robot, 'Microwave')
    # 8: Wait for a while to let the Potato cook.
    time.sleep(5)
    # 9: Switch off the Microwave.
    SwitchOff(robot, 'Microwave')
    # 10: Open the Microwave.
    OpenObject(robot, 'Microwave')
    # 11: Take the cooked Potato out.
    PickupObject(robot, 'Potato')
    # 12: Close the Microwave.
    CloseObject(robot, 'Microwave')

def put_cooked_potato_in_fridge(robot):
    # 0: SubTask 2: Put the cooked Potato in the Fridge
    # 1: Go to the Fridge.
    GoToObject(robot, 'Fridge')
    # 2: Open the Fridge.
    OpenObject(robot, 'Fridge')
    # 3: Put the cooked Potato inside the Fridge.
    PutObject(robot, 'Potato', 'Fridge')
    # 4: Close the Fridge.
    CloseObject(robot, 'Fridge')

# Execute tasks sequentially with Robot 1
cook_potato_in_microwave(robots[0])
put_cooked_potato_in_fridge(robots[0])