import random
from add_remove import add_house_to_battery


def random_greedy(houses, batterys):

    list = [0, 1, 2, 3, 4]
    list_2 = []

    i = 0
    while i < len(houses):

            counter = random.choice(list)

            if batterys[counter].current_input + houses[i].output <= float(batterys[counter].max_input):
                add_house_to_battery(houses[i], batterys[counter])
                i += 1

            else:
                list_2.append(counter)
                if set(list_2) == set(list):
                    for battery in batterys:
                        battery.current_input = 0
                        battery.list_of_houses = []
                    list_2.clear()
                    i = 0
