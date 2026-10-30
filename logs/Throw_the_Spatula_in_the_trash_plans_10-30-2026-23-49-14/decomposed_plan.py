# Task Description: Throw the Spatula in the trash

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Pick up the Spatula. (Skills Required: GoToObject, PickupObject)
# SubTask 2: Throw the Spatula into the GarbageCan. (Skills Required: GoToObject, ThrowObject)
# We can execute SubTask 1 first and then SubTask 2.

# CODE
def throw_spatula_in_trash():
    # 0: SubTask 1: Pick up the Spatula
    # 1: Go to the Spatula.
    GoToObject('Spatula')
    # 2: Pick up the Spatula.
    PickupObject('Spatula')
    # 3: Go to the GarbageCan.
    GoToObject('GarbageCan')
    # 4: Throw the Spatula towards/into the GarbageCan.
    ThrowObject('Spatula')

# Execute the task
throw_spatula_in_trash()

# Task Throw the Spatula in the trash is done