import random

from add_remove import add_house_to_battery as ad
from add_remove import remove_house_from_battery as rm


def hill_climber(houses, batterys):

    for i in range(len(batterys)):
        battery_counter_1 = i
        for j in range(len(batterys[battery_counter_1].list_of_houses)):
            house_counter_1 = j
            for k in range(len(batterys)):
                battery_counter_2 = k
                for l in range(len(batterys[battery_counter_2].list_of_houses)):
                    house_counter_2 = l
                    # print(i, j, k, l)

                    battery_A = batterys[battery_counter_1]
                    battery_B = batterys[battery_counter_2]
                    house_a = battery_A.list_of_houses[house_counter_1]
                    house_b = battery_B.list_of_houses[house_counter_2]

                    if ((house_a.connected_battery["distance"] + house_b.connected_battery["distance"] >
                    house_a.battery_distances[battery_counter_2+1] + house_b.battery_distances[battery_counter_1+1]) and
                    (battery_A.current_input - house_a.output + house_b.output < float(battery_A.max_input)) and
                    (battery_B.current_input - house_b.output + house_a.output < float(battery_B.max_input))):

                        rm(house_a, battery_A)
                        rm(house_b, battery_B)

                        ad(house_a, battery_B)
                        ad(house_b, battery_A)
