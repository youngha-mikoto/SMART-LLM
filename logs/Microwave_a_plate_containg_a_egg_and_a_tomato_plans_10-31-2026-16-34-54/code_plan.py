# CODE Solution

# Disambiguate robots by role based on skills
opener_robot = robots[0]   # has GoToObject, OpenObject, CloseObject
switch_robot = robots[1]   # has GoToObject, SwitchOn, SwitchOff
carrier_robot = robots[2]  # has GoToObject, PickupObject, PutObject

def assemble_plate_with_egg_and_tomato(robot):
    # SubTask 1: Assemble a plate with an Egg and a Tomato (single robot: carrier_robot)
    GoToObject(robot, 'Plate')
    PickupObject(robot, 'Plate')
    GoToObject(robot, 'CounterTop')
    PutObject(robot, 'Plate', 'CounterTop')

    GoToObject(robot, 'Egg')
    PickupObject(robot, 'Egg')
    GoToObject(robot, 'Plate')
    PutObject(robot, 'Egg', 'Plate')

    GoToObject(robot, 'Tomato')
    PickupObject(robot, 'Tomato')
    GoToObject(robot, 'Plate')
    PutObject(robot, 'Tomato', 'Plate')

def microwave_plate_with_egg_and_tomato(team):
    # SubTask 2: Microwave the assembled plate (team of opener + switcher + carrier)
    opener = team['opener']
    switcher = team['switcher']
    carrier = team['carrier']

    GoToObject(opener, 'Microwave')
    OpenObject(opener, 'Microwave')

    GoToObject(carrier, 'Plate')
    PickupObject(carrier, 'Plate')
    GoToObject(carrier, 'Microwave')
    PutObject(carrier, 'Plate', 'Microwave')

    CloseObject(opener, 'Microwave')

    GoToObject(switcher, 'Microwave')
    SwitchOn(switcher, 'Microwave')
    time.sleep(5)
    SwitchOff(switcher, 'Microwave')

    OpenObject(opener, 'Microwave')

    PickupObject(carrier, 'Plate')
    GoToObject(carrier, 'CounterTop')
    PutObject(carrier, 'Plate', 'CounterTop')

    CloseObject(opener, 'Microwave')

# Execute SubTask 1 then SubTask 2
assemble_plate_with_egg_and_tomato(carrier_robot)
microwave_plate_with_egg_and_tomato({'opener': opener_robot, 'switcher': switch_robot, 'carrier': carrier_robot})

# Task Microwave a plate containing an egg and a tomato is done