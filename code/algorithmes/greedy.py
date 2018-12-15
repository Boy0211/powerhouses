from helpers import add_house_to_battery
from sort import sort_distance
import random
import copy


def greedy_1(solution):

    ''' Greedy algorithm that fills up the most empty battery'''

    # save the solution variables into local variables
    houses = solution.houses
    batterys = solution.batterys

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
        if batterys[battery_counter].current_input + houses[house_counter].output < float(batterys[battery_counter].max_input):
            add_house_to_battery(houses[house_counter], batterys[battery_counter])
        else:
            print("het past gewoon godverdomme niet!")
        house_counter += 1

    return solution


def greedy_2(solution):
    ''' Greedy algorithm that fills up based on distance'''

    # information for the solution
    houses = solution.houses
    batterys = solution.batterys

    # iterate through all houses
    sorted_houses = sort_distance(copy.deepcopy(houses))
    house_counter = 0
    temp_house_counter = 0
    temp_dict = dict()

    # while loop as long as there are houses for sorting
    while house_counter < len(sorted_houses):

        # als house_counter toeneemt, sla battery_distances op in nieuwe lijst
        if temp_house_counter == house_counter:
            temp_dict = dict()
            temp_dict = copy.deepcopy(sorted_houses[house_counter].battery_distances)

        # sorteer lijst van batterijen per huis
        battery_list = (list(temp_dict.values()))
        battery_list = sorted(battery_list)

        # neem eerste waarde in deze lijst(is minimale waarde)
        current_battery = (battery_list[0])

        # zoek key met bijbehorende afstand
        battery_number = (list(temp_dict.keys())[list(temp_dict.values()).index(current_battery)])
        if batterys[battery_number-1].current_input + sorted_houses[house_counter].output <= 1.01 * float(batterys[battery_number-1].max_input):
            add_house_to_battery(sorted_houses[house_counter], batterys[battery_number-1])

            house_counter += 1
            temp_house_counter = house_counter
        else:
            temp_house_counter += 1
            del temp_dict[battery_number]

    return solution
