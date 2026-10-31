# Task Description: Cook the potato and put it in the Fridge

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Dependent subtasks (sequential):
# SubTask 1: Cook the Potato (Microwave). (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject, SwitchOn, SwitchOff)
# SubTask 2: Put the cooked Potato in the Fridge. (Skills Required: GoToObject, OpenObject, PutObject, CloseObject)

# CODE
def cook_potato_in_microwave():
    # 0: SubTask 1: Cook the Potato (Microwave)
    # 1: Go to the Potato.
    GoToObject('Potato')
    # 2: Pick up the Potato.
    PickupObject('Potato')
    # 3: Go to the Microwave.
    GoToObject('Microwave')
    # 4: Open the Microwave.
    OpenObject('Microwave')
    # 5: Put the Potato inside the Microwave.
    PutObject('Potato', 'Microwave')
    # 6: Close the Microwave.
    CloseObject('Microwave')
    # 7: Switch on the Microwave.
    SwitchOn('Microwave')
    # 8: Wait for a while to let the Potato cook.
    time.sleep(5)
    # 9: Switch off the Microwave.
    SwitchOff('Microwave')
    # 10: Open the Microwave.
    OpenObject('Microwave')
    # 11: Take the cooked Potato out.
    PickupObject('Potato')
    # 12: Close the Microwave.
    CloseObject('Microwave')

def put_cooked_potato_in_fridge():
    # 0: SubTask 2: Put the cooked Potato in the Fridge
    # 1: Go to the Fridge.
    GoToObject('Fridge')
    # 2: Open the Fridge.
    OpenObject('Fridge')
    # 3: Put the cooked Potato inside the Fridge.
    PutObject('Potato', 'Fridge')
    # 4: Close the Fridge.
    CloseObject('Fridge')

# Execute tasks sequentially
cook_potato_in_microwave()
put_cooked_potato_in_fridge()

# Task Cook the potato and put it in the Fridge is done