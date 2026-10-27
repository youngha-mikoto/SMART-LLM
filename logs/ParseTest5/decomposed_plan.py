# Task Description: Put apple in the fridge 

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Put apple in the fridge. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
# We can execute SubTask 1.

# CODE
def put_apple_in_fridge():
    # 0: SubTask 1: Put apple in the fridge
    # 1: Go to the Apple.
    GoToObject('Apple')
    # 2: Pick up the Apple.
    PickupObject('Apple')
    # 3: Go to the Fridge.
    GoToObject('Fridge')
    # 4: Open the Fridge.
    OpenObject('Fridge')
    # 5: Put Apple in the Fridge
    PutObject('Apple', 'Fridge')
    # 6: Close Fridge
    CloseObject('Fridge')

# Execute SubTask 1
put_apple_in_fridge()

# Task put apple in the fridge is done
