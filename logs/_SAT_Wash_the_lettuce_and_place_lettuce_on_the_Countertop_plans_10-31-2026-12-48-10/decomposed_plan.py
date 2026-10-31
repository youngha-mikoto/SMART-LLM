# Task Description: Wash the lettuce and place lettuce on the Countertop

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Wash the Lettuce and place it on the CounterTop. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)
# We can execute SubTask 1.

# CODE
def wash_lettuce_and_place_on_counter():
    # 0: SubTask 1: Wash the Lettuce and place it on the CounterTop
    # 1: Go to the Lettuce.
    GoToObject('Lettuce')
    # 2: Pick up the Lettuce.
    PickupObject('Lettuce')
    # 3: Go to the Sink.
    GoToObject('Sink')
    # 4: Put the Lettuce in the Sink.
    PutObject('Lettuce', 'Sink')
    # 5: Switch on the Faucet to wash the Lettuce.
    SwitchOn('Faucet')
    # 6: Wait for a while to let the Lettuce wash.
    time.sleep(5)
    # 7: Switch off the Faucet.
    SwitchOff('Faucet')
    # 8: Pick up the washed Lettuce.
    PickupObject('Lettuce')
    # 9: Go to the CounterTop.
    GoToObject('CounterTop')
    # 10: Place the Lettuce on the CounterTop.
    PutObject('Lettuce', 'CounterTop')

# Execute SubTask 1
wash_lettuce_and_place_on_counter()

# Task Wash the lettuce and place lettuce on the Countertop is done