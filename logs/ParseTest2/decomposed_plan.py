# Task Description: cook an egg then put it back inside the fridge and chill the bread from the counter then put it on the counter.

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Cook an Egg and put it back inside the Fridge. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject, SwitchOn, SwitchOff)
# SubTask 2: Chill the bread from the counter then put it on the counter. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject, )
# We can parallelize SubTask 1 and SubTask 2 because they don't depend on each other.

# CODE
def cook_egg_and_put_in_fridge():
    # 0: SubTask 1: Cook an Egg and put it back inside the Fridge
    # 1: go to the fridge
    GoToObject('Egg')
    # 2: pick up the egg
    PickupObject('Egg')
    # 3: walk towards the microwave
    GoToObject('Microwave')
    # 4: open the microwave door
    OpenObject('Microwave')
    # 5: Put the Egg inside the Microwave
    PutObject('Egg', 'Microwave')
    # 6: Close the Microwave
    CloseObject('Microwave')
    # 7: Switch on Microwave
    SwitchOn('Microwave')
    # 8: Wait for a while to let the egg cook.
    time.sleep(5)
    # 9: Switch off Microwave
    SwitchOff('Microwave')
    # 10: Open the Microwave door
    OpenObject('Microwave')
    # 11: Take the Egg out
    PickupObject('Egg')
    # 12: Close the Microwave
    CloseObject('Microwave')
    # 11: Go to the Fridge
    GoToObject('Fridge')
    # 12: Open the Fridge
    OpenObject('Fridge')
    # 13: Put the Egg inside to cool it
    PutObject('Egg', 'Fridge')
    # 14: Close the Fridge
    CloseObject('Fridge')

def chill_bread_and_put_on_counter():
    # 0: SubTask 2: Chill the bread from the counter then put it on the counter
    # 1: Go to the Bread
    GoToObject('Bread')
    # 2: Grab the bread
    PickupObject('Bread')
    # 3: Go to Fridge.
    GoToObject('Fridge')
    # 4: Open Fridge
    OpenObject('Fridge')
    # 5: Put Bread in Fridge
    PutObject('Bread', 'Fridge')
    # 6: Close Fridge
    CloseObject('Fridge')
    # 7: Wait for a while to let the bread c0ol.
    time.sleep(5)
    # 8: Open Fridge
    OpenObject('Fridge')
    # 9: Take bread out
    PickupObject('Bread')
    # 10: Close Fridge
    CloseObject('Fridge')
    # 11: Go to the counter.
    GoToObject('Countertop')
    # 12: Put the bread on the counter.
    PutObject('Bread', 'CounterTop')

# Parallelize SubTask 1 and SubTask 2
task1_thread = threading.Thread(target=cook_egg_and_put_in_fridge)
task2_thread = threading.Thread(target=chill_bread_and_put_on_counter)

# Start executing SubTask 1 and SubTask 2 in parallel
task1_thread.start()
task2_thread.start()

# Wait for both SubTask 1 and SubTask 2 to finish
task1_thread.join()
task2_thread.join()

# Task cook an egg then put it back inside the fridge and chill the bread from the counter then put it on the counter is done
