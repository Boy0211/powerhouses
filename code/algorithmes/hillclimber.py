import random

from add_remove import add_house_to_battery as ad
from add_remove import remove_house_from_battery as rm

def randomly(x):
    shuffled = list(x)
    random.shuffle(shuffled)
    return shuffled

def swap(house_a, house_b, battery_A, battery_B):
    rm(house_a, battery_A)
    ad(house_a, battery_B)
    rm(house_b, battery_B)
    ad(house_b, battery_A)

def hill_climber_2(houses, batterys):

    while True:
        houses = search_best_score(houses, batterys)
        if houses != False:
            battery1 = batterys[houses[0].connected_battery["id"] - 1]
            battery2 = batterys[houses[1].connected_battery["id"] - 1]
            swap(houses[0], houses[1], battery1, battery2)
        else:
            break

def swap_score(house_a, house_b):

    score = house_a.connected_battery["distance"] + house_b.connected_battery["distance"]
    score_new = house_a.battery_distances[house_b.connected_battery["id"]] + house_b.battery_distances[house_a.connected_battery["id"]]
    swap_score = score - score_new
    return swap_score

def capacity(house1, house2, battery):
    if battery.current_input - house1.output + house2.output <= float(battery.max_input):
        return True
    else:
        return False

def search_best_score(houses, batterys):

    score = 0.0
    for i in range(len(batterys)):
        battery_A = batterys[i]
        for j in range(len(batterys[i].list_of_houses)):
            house_a = battery_A.list_of_houses[j]
            for k in range(len(batterys)):
                battery_B = batterys[k]
                for l in range(len(batterys[k].list_of_houses)):
                    house_b = battery_B.list_of_houses[l]

                    new_score = swap_score(house_a, house_b)
                    if (capacity(house_a, house_b, battery_A) == True and capacity(house_b, house_a, battery_B) == True and new_score >= score):
                        score = new_score
                        house1 = house_a
                        house2 = house_b
    if score == 0.0:
        return False
    else:
        return [house1, house2]















def hill_climber(houses, batterys):

    counter = 0
    for i in randomly(range(len(batterys))):
        battery_counter_1 = i
        for j in randomly(range(len(batterys[battery_counter_1].list_of_houses))):
            house_counter_1 = j
            for k in randomly(range(len(batterys))):
                battery_counter_2 = k
                for l in randomly(range(len(batterys[battery_counter_2].list_of_houses))):
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

                        swap(house_a, house_b, battery_A, battery_B)
                        counter = counter + 1

    print(counter)
