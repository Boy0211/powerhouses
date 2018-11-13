import random
from add_remove import add_house_to_battery


def random_greedy(houses, batterys):

'''A function which randomly connects houses to a battery'''

    # a list of possible battery ID's
    list = [0, 1, 2, 3, 4]

    # while loop used to find a possible formation
    i = 0
    while i < len(houses):

        # boolian used to start a do/while loop
        boolian = 0
        while boolian == 0:

            # random battery chosen every time
            counter = random.choice(list)

            # if battery fits, add it
            if batterys[counter].current_input + houses[i].output < float(batterys[counter].max_input):
                add_house_to_battery(houses[i], batterys[counter])
                boolian = 1

            # else if; try the next battery
            elif batterys[(counter + 1) % 5].current_input + houses[i].output < float(batterys[(counter + 1) % 5].max_input):
                add_house_to_battery(houses[i], batterys[(counter + 1) % 5])
                boolian = 1

            # else erase all former, and start again
            else:
                i = -1
                for battery in batterys:
                    battery.current_input = 0
                    battery.list_of_houses = []
                boolian = 1

        # iterate trough loop
        i += 1
