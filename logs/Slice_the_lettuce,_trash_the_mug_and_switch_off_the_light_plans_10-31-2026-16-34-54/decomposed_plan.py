# Task Description: Slice the lettuce, trash the mug and switch off the light

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Slice the Lettuce. (Skills Required: GoToObject, PickupObject, SliceObject, PutObject)
# SubTask 2: Trash the Mug. (Skills Required: GoToObject, PickupObject, PutObject)
# SubTask 3: Switch off the Light. (Skills Required: GoToObject, SwitchOff)
# We can parallelize SubTask 1 and SubTask 2 because they don't depend on each other. Execute SubTask 3 after.

# CODE
def slice_lettuce():
    # 0: SubTask 1: Slice the Lettuce
    # 1: Go to the Knife.
    GoToObject('Knife')
    # 2: Pick up the Knife.
    PickupObject('Knife')
    # 3: Go to the Lettuce.
    GoToObject('Lettuce')
    # 4: Slice the Lettuce.
    SliceObject('Lettuce')
    # 5: Go to the CounterTop.
    GoToObject('CounterTop')
    # 6: Put the Knife on the CounterTop.
    PutObject('Knife', 'CounterTop')

def trash_mug():
    # 0: SubTask 2: Trash the Mug
    # 1: Go to the Mug.
    GoToObject('Mug')
    # 2: Pick up the Mug.
    PickupObject('Mug')
    # 3: Go to the GarbageCan.
    GoToObject('GarbageCan')
    # 4: Put the Mug in the GarbageCan.
    PutObject('Mug', 'GarbageCan')

def switch_off_light():
    # 0: SubTask 3: Switch off the Light
    # 1: Go to the LightSwitch.
    GoToObject('LightSwitch')
    # 2: Switch off the LightSwitch.
    SwitchOff('LightSwitch')

# Parallelize SubTask 1 and SubTask 2
task1_thread = threading.Thread(target=slice_lettuce)
task2_thread = threading.Thread(target=trash_mug)

# Start executing SubTask 1 and SubTask 2 in parallel
task1_thread.start()
task2_thread.start()

# Wait for both SubTask 1 and SubTask 2 to finish
task1_thread.join()
task2_thread.join()

# Execute SubTask 3 after SubTask 1 and SubTask 2 are complete
switch_off_light()

# Task slice the lettuce, trash the mug and switch off the light is done