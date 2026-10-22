def slice_tomato(robot_list):
    # robot_list = [robot1,robot2,robot3]
    # 0: SubTask 1: Slice the Tomato
    # 1: Go to the Knife using robot1.
    GoToObject(robot_list[0],'Knife')
    # 2: Pick up the Knife using robot1.
    PickupObject(robot_list[0],'Knife')
    # 3: Go to the Tomato using robot2.
    GoToObject(robot_list[1],'Tomato')
    # 4: Slice the Tomato using robot3.
    SliceObject(robot_list[2],'Tomato')
    # 5: Go to the countertop using robot1.
    GoToObject(robot_list[0],'CounterTop')
    # 6: Put the Knife back on the CounterTop using robot1.
    PutObject(robot_list[0],'Knife', 'CounterTop')

# Execute SubTask 1
slice_tomato([robots[0],robots[1],robots[2]])

# Task Slice the tomato is done