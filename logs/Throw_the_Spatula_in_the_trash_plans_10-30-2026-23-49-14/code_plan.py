# CODE Solution

def pick_up_spatula(robot_pick):
    # SubTask 1: Pick up the Spatula using robot2
    GoToObject(robot_pick, 'Spatula')
    PickupObject(robot_pick, 'Spatula')

def team_throw_spatula(robot_pick, robot_throw):
    # SubTask 2: Throw the Spatula into the GarbageCan using robot1
    # Rendezvous at the GarbageCan for coordinated action
    GoToObject(robot_pick, 'GarbageCan')
    GoToObject(robot_throw, 'GarbageCan')
    # Brief sync to ensure both robots are co-located
    time.sleep(0.5)
    # Robot1 performs the throw (assumes coordinated action with robot2 holding/positioning)
    ThrowObject(robot_throw, 'Spatula', 'GarbageCan')

# Assign robots per allocation: robot2 handles pickup; robot1 handles throw
robot_throw = robots[0]  # robot1 (GoToObject, ThrowObject)
robot_pick = robots[1]   # robot2 (GoToObject, PickupObject)

# Execute sequentially
pick_up_spatula(robot_pick)
team_throw_spatula(robot_pick, robot_throw)

# Task Throw the Spatula in the trash is done