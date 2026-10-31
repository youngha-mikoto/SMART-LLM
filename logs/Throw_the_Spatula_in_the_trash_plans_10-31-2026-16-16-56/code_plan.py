# CODE Solution
def throw_spatula_in_trash(robot_list):
    # robot_list = [robot1, robot2]
    # 0: SubTask 1: Throw the Spatula into the GarbageCan
    # 1: Go to the Spatula using robot2.
    GoToObject(robot_list[1], 'Spatula')
    # 2: Pick up the Spatula using robot2.
    PickupObject(robot_list[1], 'Spatula')
    # 3: Move to the GarbageCan together (robot2 carrying the Spatula).
    GoToObject(robot_list, 'GarbageCan')
    # 4: Throw the Spatula into the GarbageCan using robot1.
    ThrowObject(robot_list[0], 'Spatula')

# Execute SubTask 1 with team [robot1, robot2]
throw_spatula_in_trash([robots[0], robots[1]])