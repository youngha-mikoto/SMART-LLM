# Task Description: Make a sandwich with sliced lettuce, sliced tomato, sliced bread and serve it on a washed plate.

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Slice the Lettuce, Tomato, and Bread. (Skills Required: GoToObject, PickupObject, SliceObject, PutObject)
# SubTask 2: Wash the Plate. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)
# SubTask 3: Assemble the Sandwich. (Skills Required: GoToObject, PickupObject, PutObject)
# We can parallelize SubTask 1 and SubTask 2 because they don't depend on each other.

# CODE
def slice_ingredients():
    # 0: SubTask 1: Slice the Lettuce, Tomato, and Bread
    # 1: Go to the Knife.
    GoToObject('Knife')
    # 2: Pick up the Knife.
    PickupObject('Knife')
    # 3: Go to the Lettuce.
    GoToObject('Lettuce')
    # 4: Slice the Lettuce.
    SliceObject('Lettuce')
    # 5: Go to the Tomato.
    GoToObject('Tomato')
    # 6: Slice the Tomato.
    SliceObject('Tomato')
    # 7: Go to the Bread.
    GoToObject('Bread')
    # 8: Slice the Bread.
    SliceObject('Bread')
    # 9: Go to the countertop.
    GoToObject('CounterTop')
    # 10: Put the Knife back on the CounterTop.
    PutObject('Knife', 'CounterTop')

def wash_plate():
    # 0: SubTask 2: Wash the Plate
    # 1: Go to the Plate.
    GoToObject('Plate')
    # 2: Pick up the Plate.
    PickupObject('Plate')
    # 3: Go to the Sink.
    GoToObject('Sink')
    # 4: Put the plate inside the sink
    PutObject('Plate', 'Sink')
    # 5: Switch on the Faucet to clean the Plate
    SwitchOn('Faucet')
    # 6: Wait for a while to let the plate clean.
    time.sleep(5)
    # 7: Switch off the Faucet
    SwitchOff('Faucet')
    # 8: Pick up the clean Plate.
    PickupObject('Plate')
    # 9: Go to the CounterTop.
    GoToObject('CounterTop')
    # 10: Place the Plate on the CounterTop
    PutObject('Plate', 'CounterTop')

def assemble_sandwich():
    # 0: SubTask 3: Assemble the Sandwich
    # 1: Go to the Bread slice.
    GoToObject('Bread')
    # 2: Pick up the Bread slice.
    PickupObject('Bread')
    # 3: Go to the Plate.
    GoToObject('Plate')
    # 4: Place a slice of Bread on the Plate
    PutObject('Bread', 'Plate')
    # 5: Go to the Lettuce.
    GoToObject('Lettuce')
    # 6: Pick up the Lettuce.
    PickupObject('Lettuce')
    # 7: Go to the Plate.
    GoToObject('Plate')
    # 8: Place a slice of Lettuce on the Plate
    PutObject('Lettuce', 'Plate')
    # 9: Go to the Tomato.
    GoToObject('Tomato')
    # 10: Pick up the Tomato.
    PickupObject('Tomato')
    # 11: Go to the Plate.
    GoToObject('Plate')
    # 12: Place a slice of Tomato on the Plate
    PutObject('Tomato', 'Plate')
    # 13: Go to another Bread slice.
    GoToObject('Bread')
    # 14: Pick up the Bread slice.
    PickupObject('Bread')
    # 15: Go to the Plate.
    GoToObject('Plate')
    # 17: Place another slice of Bread on top of the Plate.
    PutObject('Bread', 'Plate')

# Parallelize SubTask 1 and SubTask 2
task1_thread = threading.Thread(target=slice_ingredients)
task2_thread = threading.Thread(target=wash_plate)

# Start executing SubTask 1 and SubTask 2 in parallel
task1_thread.start()
task2_thread.start()

# Wait for both SubTask 1 and SubTask 2 to finish
task1_thread.join()
task2_thread.join()

# Execute SubTask 3 after SubTask 1 and SubTask 2 are complete
assemble_sandwich()

# Task Make a sandwich with sliced lettuce, sliced tomato, sliced bread and serve it on a washed plate is done
