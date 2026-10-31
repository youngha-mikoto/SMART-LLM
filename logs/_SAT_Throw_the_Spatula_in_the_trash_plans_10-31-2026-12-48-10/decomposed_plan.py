# Task Description: Throw the Spatula in the trash

# GENERAL TASK DECOMPOSITION
# SubTask 1: Throw the Spatula into the GarbageCan. (Skills Required: GoToObject, PickupObject, ThrowObject)

# CODE
def throw_spatula_in_trash():
    # 1: Go to the Spatula.
    GoToObject('Spatula')
    # 2: Pick up the Spatula.
    PickupObject('Spatula')
    # 3: Go to the GarbageCan (trash).
    GoToObject('GarbageCan')
    # 4: Throw the Spatula into the GarbageCan.
    ThrowObject('Spatula')

# Execute SubTask 1
throw_spatula_in_trash()

# Task Throw the Spatula in the trash is done