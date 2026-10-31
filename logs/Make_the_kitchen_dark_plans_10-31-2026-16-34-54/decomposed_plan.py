# Task Description: Make the kitchen dark

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Switch off the kitchen lights. (Skills Required: GoToObject, SwitchOff)
# SubTask 2: Block outside light by closing blinds and window. (Skills Required: GoToObject, CloseObject)
# We can parallelize SubTask 1 and SubTask 2 because they don't depend on each other.

# CODE
def switch_off_lights():
    # 0: SubTask 1: Switch off the kitchen lights
    # 1: Go to the LightSwitch
    GoToObject('LightSwitch')
    # 2: Switch off the LightSwitch
    SwitchOff('LightSwitch')

def block_outside_light():
    # 0: SubTask 2: Block outside light
    # 1: Go to the Blinds
    GoToObject('Blinds')
    # 2: Close the Blinds
    CloseObject('Blinds')
    # 3: Go to the Window
    GoToObject('Window')
    # 4: Close the Window
    CloseObject('Window')

# Parallelize SubTask 1 and SubTask 2
task1_thread = threading.Thread(target=switch_off_lights)
task2_thread = threading.Thread(target=block_outside_light)

# Start executing SubTask 1 and SubTask 2 in parallel
task1_thread.start()
task2_thread.start()

# Wait for both SubTask 1 and SubTask 2 to finish
task1_thread.join()
task2_thread.join()

# Task Make the kitchen dark is done