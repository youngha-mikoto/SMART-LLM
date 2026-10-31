# CODE Solution
def place_mug_in_coffee_machine(robot):
    # SubTask 1: Place the Mug in the CoffeeMachine (robot1)
    GoToObject(robot, 'Mug')
    PickupObject(robot, 'Mug')
    GoToObject(robot, 'CoffeeMachine')
    PutObject(robot, 'Mug', 'CoffeeMachine')

def switch_on_coffee_machine(robot):
    # SubTask 2: Switch on the CoffeeMachine (robot3)
    GoToObject(robot, 'CoffeeMachine')
    SwitchOn(robot, 'CoffeeMachine')

# Execute sequentially respecting dependency
place_mug_in_coffee_machine(robots[0])  # robot1
switch_on_coffee_machine(robots[2])     # robot3