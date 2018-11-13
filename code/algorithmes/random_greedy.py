import random
from add_remove import add_house_to_battery

def random_greedy(houses, batterys):
    list = [0, 1, 2, 3, 4]
    i = 0
    poging = 0
    while i < len(houses):
        boolian = 0
        while boolian == 0:
            counter = random.choice(list)
            if batterys[counter].current_input + houses[i].output < float(batterys[counter].max_input):
                add_house_to_battery(houses[i], batterys[counter])
                boolian = 1
            elif batterys[(counter + 1) % 5].current_input + houses[i].output < float(batterys[(counter + 1) % 5].max_input):
                add_house_to_battery(houses[i], batterys[(counter + 1) % 5])
                boolian = 1
            else:
                i = -1
                for battery in batterys:
                    battery.current_input = 0
                    battery.list_of_houses = []
                boolian = 1
        i += 1
        poging += 1
