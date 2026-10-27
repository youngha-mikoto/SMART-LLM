# Task Description: Put an Egg in the Fridge, and place a pot containing Apple slices into the refrigerator.

# GENERAL TASK DECOMPOSITION 
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Put an Egg in the Fridge. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
# SubTask 2: Prepare Apple Slices. (Skills Required: GoToObject, PickupObject, SliceObject, PutObject)
# SubTask 3: Place the Pot with Apple Slices in the Fridge. (Skills Required: GoToObject, PickupObject, PutObject, OpenObject, CloseObject)
# We can parallelize SubTask 1 and SubTask 2 because they don't depend on each other.

# CODE
def put_egg_in_fridge():
    # 0: SubTask 1: Put an Egg in the Fridge
    # 1: Go to the Egg.
    GoToObject('Egg')
    # 2: Pick up the Egg.
    PickupObject('Egg')
    # 3: go to the Fridge.
    GoToObject('Fridge')
    # 4: Open the Fridge.
    OpenObject('Fridge')
    # 5: place the Egg inside the Fridge
    PutObject('Egg', 'Fridge')
    # 6: Close the Fridge.
    CloseObject('Fridge')

def prepare_apple_slices():
    # 0: SubTask 2: Prepare Apple Slices
    # 1: Go to the Knife.
    GoToObject('Knife')
    # 2: Pick up the Knife.
    PickupObject('Knife')
    # 3: Go to the Apple.
    GoToObject('Apple')
    # 4: Cut the Apple into slices.
    SliceObject('Apple')
    # 5: Go to the diningtable.
    GoToObject('DiningTable')
    # 6: Put the Knife on the diningtable.
    PutObject('Knife', 'DiningTable')

def place_pot_with_apple_slices():
    # 0: SubTask 3: Place the Pot with Apple Slices in the Fridge
    # 1: Go to the Apple slice.
    GoToObject('Apple')
    # 2: Pick up a slice of Apple.
    PickupObject('Apple')
    # 3: Go to the pot.
    GoToObject('Pot')
    # 4: Place the Apple slice in the pot.
    PutObject('Apple', 'Pot')
    # 5: Pick up the pot.
    PickupObject('Pot')
    # 6: Go to the refrigerator.
    GoToObject('Fridge')
    # 7: Open the Fridge, 
    OpenObject('Fridge')
    # 8: Put the pot in the refrigerator.
    PutObject('Pot', 'Fridge')
    # 9: Close the Fridge.
    CloseObject('Fridge')

# Parallelize SubTask 1 and SubTask 2
task1_thread = threading.Thread(target=put_egg_in_fridge)
task2_thread = threading.Thread(target=prepare_apple_slices)

# Start executing SubTask 1 and SubTask 2 in parallel
task1_thread.start()
task2_thread.start()

# Wait for both SubTask 1 and SubTask 2 to finish
task1_thread.join()
task2_thread.join()

# Execute SubTask 3 after SubTask 1 and SubTask 2 are complete
place_pot_with_apple_slices()

# Task Put an Egg in the Fridge, and place a pot containing Apple slices into the refrigerator is done
