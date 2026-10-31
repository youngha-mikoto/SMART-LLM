# Task Description: Microwave a plate containing an egg and a tomato

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Assemble a plate with an Egg and a Tomato. (Skills Required: GoToObject, PickupObject, PutObject)
# SubTask 2: Microwave the assembled plate. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject, SwitchOn, SwitchOff)
# We must execute SubTask 1 first and then SubTask 2.

# CODE
def assemble_plate_with_egg_and_tomato():
    # 0: SubTask 1: Assemble a plate with an Egg and a Tomato
    # 1: Go to the Plate.
    GoToObject('Plate')
    # 2: Pick up the Plate.
    PickupObject('Plate')
    # 3: Go to the CounterTop.
    GoToObject('CounterTop')
    # 4: Place the Plate on the CounterTop.
    PutObject('Plate', 'CounterTop')
    # 5: Go to the Egg.
    GoToObject('Egg')
    # 6: Pick up the Egg.
    PickupObject('Egg')
    # 7: Go to the Plate.
    GoToObject('Plate')
    # 8: Place the Egg on the Plate.
    PutObject('Egg', 'Plate')
    # 9: Go to the Tomato.
    GoToObject('Tomato')
    # 10: Pick up the Tomato.
    PickupObject('Tomato')
    # 11: Go to the Plate.
    GoToObject('Plate')
    # 12: Place the Tomato on the Plate.
    PutObject('Tomato', 'Plate')

def microwave_plate_with_egg_and_tomato():
    # 0: SubTask 2: Microwave the assembled plate
    # 1: Go to the Microwave.
    GoToObject('Microwave')
    # 2: Open the Microwave.
    OpenObject('Microwave')
    # 3: Go to the Plate.
    GoToObject('Plate')
    # 4: Pick up the Plate (with Egg and Tomato).
    PickupObject('Plate')
    # 5: Go to the Microwave.
    GoToObject('Microwave')
    # 6: Put the Plate inside the Microwave.
    PutObject('Plate', 'Microwave')
    # 7: Close the Microwave.
    CloseObject('Microwave')
    # 8: Switch on the Microwave.
    SwitchOn('Microwave')
    # 9: Wait for a while to heat.
    time.sleep(5)
    # 10: Switch off the Microwave.
    SwitchOff('Microwave')
    # 11: Open the Microwave.
    OpenObject('Microwave')
    # 12: Take the Plate out.
    PickupObject('Plate')
    # 13: Close the Microwave.
    CloseObject('Microwave')
    # 14: Go to the CounterTop.
    GoToObject('CounterTop')
    # 15: Place the Plate on the CounterTop.
    PutObject('Plate', 'CounterTop')

# Execute SubTask 1 then SubTask 2
assemble_plate_with_egg_and_tomato()
microwave_plate_with_egg_and_tomato()

# Task Microwave a plate containing an egg and a tomato is done