def wash_lettuce(robot_list):
    # robot_list = [robot1]
    # 0: SubTask 1: Wash the Lettuce
    # 1: Go to the Lettuce using robot1.
    GoToObject(robot_list[0],'Lettuce')
    # 2: Pick up the Lettuce using robot1.
    PickupObject(robot_list[0],'Lettuce')
    # 3: Go to the Sink using robot1.
    GoToObject(robot_list[0],'Sink')
    # 4: Put the Lettuce in the Sink using robot1.
    PutObject(robot_list[0],'Lettuce', 'Sink')
    # 5: Switch on the Faucet to clean the Lettuce using robot1
    SwitchOn(robot_list[0],'Faucet')
    # 6: Wait for a while to let the Lettuce clean using robot1.
    time.sleep(5)
    # 7: Switch off the Faucet using robot1
    SwitchOff(robot_list[0],'Faucet')
    # 8: Pick up the clean Lettuce using robot1.
    PickupObject(robot_list[0],'Lettuce')

def place_lettuce_on_countertop(robot_list):
     # robot_list = [robot2]
     # 0: SubTask 2: Place Lettuce on the Countertop
     # 1: Go to the CounterTop using robot2.
     GoToObject(robot_list[0],'CounterTop')
     # 2: Put the Lettuce on the CounterTop using robot2.
     PutObject(robot_list[0],'Lettuce', 'CounterTop')

# Execute SubTask 1 with Robot1
wash_lettuce([robots[0]])

# Execute SubTask 2 with Robot2
place_lettuce_on_countertop([robots[1]])

# Task Wash the lettuce and place lettuce on the Countertop is done