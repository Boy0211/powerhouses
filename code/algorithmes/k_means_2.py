'''
    File name: k_means_2.py
    Author: Mendel, Sam, Rutger
    Date created: 17/11/2018
    Date last modified: 17/12-2018
'''
import random
import copy

from helpers import add_house_to_battery as ad
from helpers import battery_capacity_exceeded as cap_exc
from battery import Battery


def k_means(solution):

    '''Verdeel huizen met greedy in 5 groepen met de korst mogelijke afstand'''

    original = copy.deepcopy(solution)

    index = 0
    temp_save = 50000
    split_battery = solution.batterys[0]
    new_battery = solution.batterys[0]

    # continue as long as capacity of a battery is exceeded
    while True:
        counter = 0
        old_solution = 0

        # save orignal solution
        solution = copy.deepcopy(original)

        # set battery capacity to max
        for battery in solution.batterys:
            battery.max_input = 1800

        # assign random location to batterys
        place_batterys(solution)

        x = 100000
        y = 0
        battery_type = 1800

        # iterate through all houses
        while True:

            # choose the new battery type, depending on the value of y
            if y > 2:
                y = 0
            total_change = 0
            if y == 0:
                battery_type = 1800
            elif y == 1:
                battery_type = 900
            else:
                battery_type = 450

            # save houses and empty batterys
            houses = solution.houses
            for battery in solution.batterys:
                battery.list_of_houses = []
                battery.current_input = 0

            temp_df = solution.distances
            counter = 1

            # go through all houses and select the closest battery
            for house in houses:
                ad(house, solution.batterys[(temp_df['closest_house'][counter]) - 1])
                counter += 1

            # go through each battery and calculate the mean position of all
            # houses present in that battery
            for battery in solution.batterys:
                x_coordinates = list()
                y_coordinates = list()
                for house in battery.list_of_houses:
                    x_coordinates.append(house.location_x)
                    y_coordinates.append(house.location_y)

                # if no house is connect to a battery, fill it temporary
                if len(x_coordinates) == 0 or len(y_coordinates) == 0:
                    x_coordinates = [1]
                    y_coordinates = [1]
                mean_x = round(sum(x_coordinates)/len(x_coordinates))
                mean_y = round(sum(y_coordinates)/len(y_coordinates))

                # calculate the total changed distance for all batterys
                change_x = abs(battery.location_x - mean_x)
                change_y = abs(battery.location_y - mean_y)
                total_change += change_x + change_y

                # change battery location to mean values
                battery.location_x = mean_x
                battery.location_y = mean_y

            index += 1
            if index % 10 == 0:
                if solution.costs == temp_save:
                    break
                else:
                    temp_save = solution.costs

            if total_change < 1:
                if solution.costs <= x:

                    # save previous solution
                    old_solution = copy.deepcopy(solution)
                    x = old_solution.costs

                    # if y is equal to zero, all available batterys are checked
                    # choose a new battery to split
                    if y == 0:
                        split_battery = battery_chosen_for_split(solution.batterys)

                    # create a new battery from a different type
                    new_battery = Battery((len(solution.batterys)+1),
                                          (split_battery.location_x+1),
                                          (split_battery.location_y+1),
                                          battery_type, 0, [])
                    solution.batterys.append(new_battery)
                    y += 1

                # if score is not improved, return old solution
                else:
                    solution = copy.deepcopy(old_solution)
                # print(index)
        x = 0
        for battery in solution.batterys:
            x += battery.max_input

        if cap_exc(solution.batterys) is False:
            break
        elif x > 7500 and x < 8000:
            break

    print(solution.costs)
    return solution


        # if cap_exc(batterys) is False:
        #     grid(solution)
        #     break
        # if solution.score > 0.6:
        #     print("gelukt")
        #     for battery in batterys:
        #         print(battery)
        #     break

    # bekijk of score hoger wordt als er tweede batterij wordt geplaatst
    # dit moet per batterij

def place_batterys(solution):

    solution.batterys[0].location_x = random.randint(26, 51)
    solution.batterys[0].location_x = random.randint(26, 51)

    solution.batterys[1].location_x = random.randint(0, 26)
    solution.batterys[1].location_y = random.randint(26, 51)

    solution.batterys[2].location_x = random.randint(26, 51)
    solution.batterys[2].location_y = random.randint(0, 26)

    solution.batterys[3].location_x = random.randint(0, 26)
    solution.batterys[3].location_y = random.randint(0, 26)

    solution.batterys[4].location_x = random.randint(17, 33)
    solution.batterys[4].location_y = random.randint(17, 33)


def battery_chosen_for_split(batterys):
    bat1 = random.choice(batterys)
    # score = 0
    # for battery in batterys:
    #     if battery.distance_costs > score:
    #         score = battery.distance_costs
    #         bat1 = battery

    return bat1


def choose_split_battery(battery):

    if battery.current_input > 900:
        battery.max_input = 1800
    elif battery.current_input > 450:
        battery.max_input = 900
    else:
        battery.max_input = 450


def choose_new_battery(solution):
    for battery in solution.batterys:
        if battery.current_input > 900:
            battery.max_input = 1800
        elif battery.current_input > 450:
            battery.max_input = 900
        else:
            battery.max_input = 450
