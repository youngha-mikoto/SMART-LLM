# CODE Solution
def wash_lettuce_and_place_on_counter(robot_list):
    # robot_list = [robot1]
    # 0: SubTask 1: Wash the Lettuce and place it on the CounterTop
    # 1: Go to the Lettuce using robot1.
    GoToObject(robot_list[0], 'Lettuce')
    # 2: Pick up the Lettuce using robot1.
    PickupObject(robot_list[0], 'Lettuce')
    # 3: Go to the Sink using robot1.
    GoToObject(robot_list[0], 'Sink')
    # 4: Put the Lettuce in the Sink using robot1.
    PutObject(robot_list[0], 'Lettuce', 'Sink')
    # 5: Switch on the Faucet to wash the Lettuce using robot1.
    SwitchOn(robot_list[0], 'Faucet')
    # 6: Wait for a while to let the Lettuce wash using robot1.
    time.sleep(5)
    # 7: Switch off the Faucet using robot1.
    SwitchOff(robot_list[0], 'Faucet')
    # 8: Pick up the washed Lettuce using robot1.
    PickupObject(robot_list[0], 'Lettuce')
    # 9: Go to the CounterTop using robot1.
    GoToObject(robot_list[0], 'CounterTop')
    # 10: Place the Lettuce on the CounterTop using robot1.
    PutObject(robot_list[0], 'Lettuce', 'CounterTop')

# Execute SubTask 1 with robot1
wash_lettuce_and_place_on_counter([robots[0]])