# Task Description: put mug in the coffee machine and switch on the coffee machine

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Place the Mug in the CoffeeMachine. (Skills Required: GoToObject, PickupObject, PutObject)
# SubTask 2: Switch on the CoffeeMachine. (Skills Required: SwitchOn)
# We will execute these subtasks sequentially.

# CODE
def put_mug_in_coffee_machine_and_switch_on():
    # 0: SubTask 1: Place the Mug in the CoffeeMachine
    # 1: Go to the Mug.
    GoToObject('Mug')
    # 2: Pick up the Mug.
    PickupObject('Mug')
    # 3: Go to the CoffeeMachine.
    GoToObject('CoffeeMachine')
    # 4: Place the Mug in the CoffeeMachine.
    PutObject('Mug', 'CoffeeMachine')
    # 5: Switch on the CoffeeMachine.
    SwitchOn('CoffeeMachine')

# Execute the task
put_mug_in_coffee_machine_and_switch_on()

# Task put mug in the coffee machine and switch on the coffee machine is done