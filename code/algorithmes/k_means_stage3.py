import random
import copy
from random import randint

from battery import Battery
from visualization import grid

from helpers import battery_capacity_exceeded as cap_exc
from helpers import add_house_to_battery as ad
from helpers import remove_house_from_battery as rm
from helpers import house_battery_distance as distance


def k_means_stage3(solution):

    # houses = solution.houses
    # solution.batterys = []
    #
    # # start with one battery
    # battery1 = Battery(1, 26, 26, 1800, 0, [])
    # for house in houses:
    #     ad(house, battery1)
    # solution.batterys.append(battery1)
    # # grid(solution)

    houses = solution.houses
    batterys = solution.batterys

    batterys[0].location_x = random.randint(26, 51)
    batterys[0].location_x = random.randint(26, 51)

    batterys[1].location_x = random.randint(0, 26)
    batterys[1].location_y = random.randint(26, 51)

    batterys[2].location_x = random.randint(26, 51)
    batterys[2].location_y = random.randint(0, 26)

    batterys[3].location_x = random.randint(0, 26)
    batterys[3].location_y = random.randint(0, 26)

    batterys[4].location_x = random.randint(17, 33)
    batterys[4].location_y = random.randint(17, 33)

    for battery in batterys:
        battery.max_input = 1800
        battery.list_of_houses = []
        battery.current_input = 0

    temp_df = solution.distances
    # print(solution.distances)

    counter = 1
    for house in houses:
        ad(house, batterys[(temp_df['closest_house'][counter]) - 1])
        counter += 1

    index = 0
    temp_save = solution.costs

    # initiate a while loop
    while True:

        for battery in solution.batterys:
            if 1050 < battery.current_input < 1350 and battery.max_input == 1800:

                old_list_of_houses = copy.deepcopy(battery.list_of_houses)
                battery.max_input = 900
                battery.list_of_houses.clear()
                battery.current_input = 0

                for house in old_list_of_houses:
                    maximum_distance = 0
                    if distance(house, battery) > maximum_distance:
                        most_far_away_house = house
                        maximum_distance = distance(house, battery)

                new_bat = Battery(len(solution.batterys) + 1, most_far_away_house.location_x + randint(-1, 1), most_far_away_house.location_y + randint(-1, 1), 450, 0, [])

                for house in old_list_of_houses:
                    if new_bat.current_input < new_bat.max_input and distance(house, new_bat) < distance(house, battery):
                        ad(house, new_bat)
                    else:
                        ad(house, battery)

                solution.batterys.append(new_bat)
                # grid(solution)

        # save solution
        x_solution = copy.deepcopy(solution)
        y_solution = copy.deepcopy(solution)

        # select a battery
        selected_battery_x = random.choice(x_solution.batterys)  # voorlopig even zo
        selected_battery_y = random.choice(y_solution.batterys)  #voorlopig

        # before splitting save score and list of houses
        old_list_of_houses_x = copy.deepcopy(selected_battery_x.list_of_houses)
        old_list_of_houses_y = copy.deepcopy(selected_battery_y.list_of_houses)

        # split the battery and append it to the solution
        splitted_batterys_x = split_battery_x(selected_battery_x, len(x_solution.batterys))
        splitted_batterys_y = split_battery_y(selected_battery_y, len(y_solution.batterys))

        # find the closest battery and add the house
        for house in old_list_of_houses_x:
            dis1 = distance(house, splitted_batterys_x[0])
            dis2 = distance(house, splitted_batterys_x[1])

            if dis1 < dis2:
                ad(house, splitted_batterys_x[0])
            else:
                ad(house, splitted_batterys_x[1])

        # do the same for y
        for house in old_list_of_houses_y:
            dis1 = distance(house, splitted_batterys_y[0])
            dis2 = distance(house, splitted_batterys_y[1])

            if dis1 < dis2:
                ad(house, splitted_batterys_y[0])
            else:
                ad(house, splitted_batterys_y[1])

        # place the battery in the middle of his connected houses
        for battery in splitted_batterys_x:
            x_coordinates = list()
            y_coordinates = list()
            for house in battery.list_of_houses:
                x_coordinates.append(house.location_x)
                y_coordinates.append(house.location_y)
            if len(x_coordinates) == 0 or len(y_coordinates) == 0:
                x_coordinates = [1]
                y_coordinates = [1]
            mean_x = round(sum(x_coordinates)/len(x_coordinates))
            mean_y = round(sum(y_coordinates)/len(y_coordinates))
            battery.location_x = mean_x
            battery.location_y = mean_y

        # place the battery in the middle of his connected houses
        for battery in splitted_batterys_y:
            x_coordinates = list()
            y_coordinates = list()
            for house in battery.list_of_houses:
                x_coordinates.append(house.location_x)
                y_coordinates.append(house.location_y)
            if len(x_coordinates) == 0 or len(y_coordinates) == 0:
                x_coordinates = [1]
                y_coordinates = [1]
            mean_x = round(sum(x_coordinates)/len(x_coordinates))
            mean_y = round(sum(y_coordinates)/len(y_coordinates))
            battery.location_x = mean_x
            battery.location_y = mean_y

        # # calculate the costs of the new batterys
        # print("-----")
        # print(splitted_batterys[0].battery_costs)
        # print(splitted_batterys[1].battery_costs)
        # print(old_costs)
        # print("-----")

        # append the splitted batterys to the solution and print them
        x_solution.batterys.append(splitted_batterys_x[1])
        # for battery in x_solution.batterys:
        #     print(battery)
        # print(x_solution)
        # grid(x_solution)

        y_solution.batterys.append(splitted_batterys_y[1])
        # for battery in y_solution.batterys:
        #     print(battery)
        # print(y_solution)
        # grid(y_solution)
        # grid(solution)

        solutions = []
        solutions.append(x_solution)
        solutions.append(y_solution)
        solutions.append(solution)
        solutions.sort(key=lambda x: x.costs, reverse=False)
        # for solution in solutions:
        #     print(solution.costs)
        solution = solutions[0]

        # failsafe = False
        # for battery in solution.batterys:
        #     if len(battery.list_of_houses) <= 1:
        #         failsafe = True
        #
        # if failsafe == True:
        #     for battery in solution.batterys:
        #         battery.list_of_houses = []
        #         battery.current_input = 0
        #
        #     temp_df = solution.distances
        #     # print(solution.distances)
        #
        #     counter = 1
        #     for house in houses:
        #         ad(house, batterys[(temp_df['closest_house'][counter]) - 1])
        #         counter += 1
        # print("----")
        # print(solution.costs)

        # for battery in solution.batterys:
        #     print(battery)

        if index % 30 == 0:
            # grid(solution)
            temp_value = 0
            for battery in solution.batterys:
                temp_value += battery.max_input
                # print(battery)
            if temp_value >= 7650:
                # grid(solution)
                break
        index += 1


    print(solution)
    # grid(solution)
    return solution




    # # if new solution is better, delete old one
    # # else delete the new one
    # if splitted_batterys[0].battery_costs + splitted_batterys[1].battery_costs < old_costs:
    #     solution.batterys.remove(selected_battery)
    # else:
    #     for battery in solution.batterys:
    #         if battery == splitted_batterys[0] or battery == splitted_batterys[1]:
    #             solution.batterys.remove(battery)
    # grid(solution)






def split_battery_x(bat1, counter):

    if bat1.current_input < bat1.max_input and bat1.max_input == 1800:
        bat1.max_input = 900
        bat2 = Battery(counter + 1, bat1.location_x + 5, bat1.location_y, 900, 0, [])

    elif bat1.current_input < bat1.max_input and bat1.max_input == 900:
        bat1.max_input = 450
        bat2 = Battery(counter + 1, bat1.location_x + 5, bat1.location_y, 450, 0, [])

    else:
        bat2 = Battery(counter + 1, bat1.location_x + 5, bat1.location_y, bat1.max_input, 0, [])

    bat1.list_of_houses.clear()
    bat1.current_input = 0

    return [bat1, bat2]


def split_battery_y(bat1, counter):

    if bat1.current_input < bat1.max_input and bat1.max_input == 1800:
        bat1.max_input = 900
        bat2 = Battery(counter + 1, bat1.location_x, bat1.location_y + 5, 900, 0, [])

    elif bat1.current_input < bat1.max_input and bat1.max_input == 900:
        bat1.max_input = 450
        bat2 = Battery(counter + 1, bat1.location_x , bat1.location_y + 5, 450, 0, [])

    else:
        bat2 = Battery(counter + 1, bat1.location_x, bat1.location_y + 5, bat1.max_input, 0, [])

    bat1.list_of_houses.clear()
    bat1.current_input = 0

    return [bat1, bat2]
