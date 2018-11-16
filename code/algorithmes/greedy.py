from add_remove import add_house_to_battery
from sort import sort_distance
import random
import copy

def greedy_1(houses, batterys):

    ''' Greedy algorithm that fills up the most empty battery'''

    # iterate through all houses
    house_counter = 0
    while house_counter < len(houses):
        bat_list = []

        # append all batteries in new list and choose battery with lowest
        # current input
        for battery in batterys:
            bat_list.append(battery.current_input)
        battery_counter = bat_list.index(min(bat_list))

        del(bat_list)

        # if a house fits into the battery with the lowest input, put this
        # house inside this battery. Otherwise were scruwed because we have
        # reached the max capacity of all batteries
        if batterys[battery_counter].current_input + houses[house_counter].output < 1507:
            add_house_to_battery(houses[house_counter], batterys[battery_counter])
        else:
            print("het past gewoon godverdomme niet!")
        house_counter += 1

def greedy_2(houses, batterys):
    ''' Greedy algorithm that fills up the most empty battery on a sorted list'''

    houses = sort_distance(houses)
    # for house in houses:
    #     print(house)
    # for battery in batterys:
    #     print(battery)
    # iterate through all houses

    house_counter = 0
    temp_house_counter = 0
    temp_dict = dict()
    # for house in houses:
        # print(house.battery_distances)
    # try_battery = 0
    while house_counter < len(houses):

        # als house_counter toeneemt, sla battery_distances op in nieuwe lijst
        if temp_house_counter == house_counter:
            # print(houses[house_counter].battery_distances)
            temp_dict = dict()
            # print(temp_dict)
            temp_dict = copy.deepcopy(houses[house_counter].battery_distances)
            # print(temp_dict)
            # print(houses[house_counter].battery_distances)


        # sorteer lijst van batterijen per huis
        battery_list = (list(temp_dict.values()))
        battery_list = sorted(battery_list)
        # print(houses[house_counter].battery_distances)

        # neem eerste waarde in deze lijst(is minimale waarde)
        # print(f"try battery: {try_battery}")
        # print(battery_list)
        current_battery = (battery_list[0])

        # zoek key met bijbehorende afstand
        battery_number = (list(temp_dict.keys())[list(temp_dict.values()).index(current_battery)])
        # print(f"battery number: {battery_number}")
        # print(f"try battery: {try_battery}")

        if batterys[battery_number-1].current_input + houses[house_counter].output <= float(batterys[battery_number-1].max_input):
            add_house_to_battery(houses[house_counter], batterys[battery_number-1])
            # print(houses[house_counter].battery_distances)


            house_counter += 1
            temp_house_counter = house_counter
            # try_battery = 0
            # for battery in batterys:
                # print(battery)
        else:
            # print("niet gelukt")
            # print(try_battery)
            # print(houses[house_counter].output)
            temp_house_counter += 1
            del temp_dict[battery_number]


    for house in houses:
        print(house)
    for battery in batterys:
        print(battery)
