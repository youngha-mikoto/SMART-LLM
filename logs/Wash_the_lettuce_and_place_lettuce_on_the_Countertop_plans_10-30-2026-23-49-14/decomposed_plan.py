# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Wash the Lettuce and place it on the CounterTop. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff, CleanObject)
# We can execute SubTask 1.

# CODE
def wash_lettuce_and_place():
    # 0: SubTask 1: Wash the Lettuce and place it on the CounterTop
    # 1: Go to the Lettuce.
    GoToObject('Lettuce')
    # 2: Pick up the Lettuce.
    PickupObject('Lettuce')
    # 3: Go to the Sink.
    GoToObject('Sink')
    # 4: Put the Lettuce in the Sink.
    PutObject('Lettuce', 'Sink')
    # 5: Turn on the Faucet to rinse.
    SwitchOn('Faucet')
    # 6: Clean the Lettuce.
    CleanObject('Lettuce')
    # 7: Wait briefly to ensure thorough washing.
    time.sleep(3)
    # 8: Turn off the Faucet.
    SwitchOff('Faucet')
    # 9: Pick up the clean Lettuce.
    PickupObject('Lettuce')
    # 10: Go to the CounterTop.
    GoToObject('CounterTop')
    # 11: Place the Lettuce on the CounterTop.
    PutObject('Lettuce', 'CounterTop')

# Execute SubTask 1
wash_lettuce_and_place()

# Task Wash the lettuce and place lettuce on the Countertop is done