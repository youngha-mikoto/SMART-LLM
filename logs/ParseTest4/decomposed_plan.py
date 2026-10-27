# Task Description: fry the potato 

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Prepare the Potato. (Skills Required: GoToObject, PickupObject, SliceObject, PutObject)
# SubTask 2: Fry the Potato. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff, )
# We can execute SubTask 1 first and then SubTask 2, since they cannot be parallized. 

# CODE
def prepare_potato():
    # 0: SubTask 1: Prepare the Potato
    # 1: Go to the Knife.
    GoToObject('Knife')
    # 2: Pick up the Knife.
    PickupObject('Knife')
    # 3: Go to the Potato.
    GoToObject('Potato')
    # 4: Slice the Potato.
    SliceObject('Potato')
    # 5: Go to the countertop.
    GoToObject('CounterTop')
    # 6: Put the Knife back on the CounterTop.
    PutObject('Knife', 'CounterTop')

def fry_potato():
    # 0: SubTask 2: Fry the Potato
    # 1: Go to the sliced Potato.
    GoToObject('Potato')
    # 2: Pick up the sliced Potato.
    PickupObject('Potato')
    # 3: Go to the Pan.
    GoToObject('Pan')
    # 4: Put the sliced Potato in the Pan.
    PutObject('Potato', 'Pan')
    # 5: Pick up the pan with potato in it.
    PickupObject('Pan')
    # 6: Go to the StoveBurner.
    GoToObject('StoveBurner')
    # 7: Put the Pan on the stove burner.
    PutObject('Pan', 'StoveBurner')
    # 7: Switch on the StoveKnob.
    SwitchOn('StoveKnob')
    # 7: Wait for a while to let the Potato fry.
    time.sleep(5)
    # 8: Switch off the StoveKnob.
    SwitchOff('StoveKnob')
    # 9: Go to the Potato.
    GoToObject('Potato')
    # 10: Pick up the Potato.
    PickupObject('Potato')
    # 11: Go to the Plate.
    GoToObject('Plate')
    # 12: Put the fried Potato on the Plate.
    PutObject('Potato', 'Plate')

# Execute SubTask 1
prepare_potato()

# Execute SubTask 2
fry_potato()

# Task fry the potato is done
