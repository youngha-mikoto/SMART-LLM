# Task Description: Wash the lettuce and place lettuce on the CounterTop

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Wash the Lettuce and place it on the CounterTop. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff, CleanObject)
# We can execute SubTask 1.

# CODE
def wash_and_place_lettuce():
    # 0: SubTask 1: Wash the Lettuce and place it on the CounterTop
    # 1: Go to the Lettuce.
    GoToObject('Lettuce')
    # 2: Pick up the Lettuce.
    PickupObject('Lettuce')
    # 3: Go to the Sink.
    GoToObject('Sink')
    # 4: Put the Lettuce in the Sink.
    PutObject('Lettuce', 'Sink')
    # 5: Turn on the Faucet.
    SwitchOn('Faucet')
    # 6: Clean the Lettuce under running water.
    CleanObject('Lettuce')
    # 7: Wait briefly to ensure it's washed.
    time.sleep(3)
    # 8: Turn off the Faucet.
    SwitchOff('Faucet')
    # 9: Pick up the washed Lettuce.
    PickupObject('Lettuce')
    # 10: Go to the CounterTop.
    GoToObject('CounterTop')
    # 11: Place the Lettuce on the CounterTop.
    PutObject('Lettuce', 'CounterTop')

# Execute SubTask 1
wash_and_place_lettuce()

# Task Wash the lettuce and place lettuce on the CounterTop is done