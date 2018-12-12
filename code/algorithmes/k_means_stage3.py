import random
import copy

from battery import Battery
from visualization import grid

from helpers import battery_capacity_exceeded as cap_exc
from helpers import add_house_to_battery as ad
from helpers import remove_house_from_battery as rm
from helpers import house_battery_distance as distance


def k_means_stage3(solution):

    houses = solution.houses
    solution.batterys = []

    # start with one battery
    battery1 = Battery(1, 26, 26, 1800, 0, [])
    for house in houses:
        ad(house, battery1)
    solution.batterys.append(battery1)
    grid(solution)

    index = 0
    temp_save = solution.costs

    # initiate a while loop
    while True:

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
        # print("----")
        # print(solution.costs)

        for battery in solution.batterys:
            print(battery)

        if index % 5 == 0:
            grid(solution)
            if solution.costs == temp_save:
                solution = add_small_battery(solution)
            else:
                temp_save = solution.costs
                "het gaat lekker"
        index += 1


    for battery in solution.batterys:
        print(battery)
    grid(solution)



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


def add_small_battery(solution):

    solutions = []
    for i in range(4):
        solutions.append(copy.deepcopy(solution))

    for solution in solutions:
        battery = random.choice(solution.batterys)
        old_list_of_houses = copy.deepcopy(battery.list_of_houses)

        battery.list_of_houses.clear()
        battery.current_input = 0
        print("xxx")
        grid(solution)

        new_bat = Battery(len(solution.batterys) + 1, battery.location_x + 5, battery.location_y, 450, 0 ,[])

        for house in old_list_of_houses:
            if new_bat.current_input < new_bat.max_input:
                ad(house, new_bat)
            else:
                ad(house, battery)

        solution.batterys.append(new_bat)
        # for house in old_list_of_houses:
        #     ad(house, battery)

    solutions.sort(key=lambda x: x.costs, reverse=False)

    return solutions[0]
