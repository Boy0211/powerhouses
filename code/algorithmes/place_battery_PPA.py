import random
import matplotlib.pyplot as plt
import copy

from helpers import remove_house_from_battery as rm
from helpers import add_house_to_battery as ad
from helpers import swap
from copy_solution import copy_solution


def battery_based_plant_propagation_algorithm(solutions):

    solutions_counter = len(solutions)

    counter = 0
    temp_save = 0.0

    # list of scores for visualization
    list_of_scores = []
    list_of_scores2 = []

    while True:
        counter += 1
        all_solutions = []

        for index, solution in enumerate(solutions, start=0):

            old_solution = solution
            all_solutions.append(old_solution)

            # x = [0, 1]
            # y = [0, 1, 2]

            if index < 10:
                all_solutions.append(swap_one_pair(copy.deepcopy(solution)))
                all_solutions.append(move_battery(copy.deepcopy(solution)))
                print("x")
            elif index >= 10 and index < 20:
                all_solutions.append(swap_one_pair(copy.deepcopy(solution)))
                all_solutions.append(move_battery(copy.deepcopy(solution)))
                all_solutions.append(move_one_house(copy.deepcopy(solution)))
                print("xx")
            else:
                all_solutions.append(move_one_house(copy.deepcopy(solution)))
                all_solutions.append(move_ten_houses(copy.deepcopy(solution)))
                all_solutions.append(change_battery(copy.deepcopy(solution)))
                all_solutions.append(place_battery_middle(copy.deepcopy(solution)))
                print("xxx")

            # if solution.score >= 0.90:
            #     if random.choice(x) == 0:
            #         all_solutions.append(swap_one_pair(new_solution))
            #     else:
            #         all_solutions.append(move_battery(new_solution))
            # elif solution.score < 0.90 and solution.score >= 0.50:
            #     y1 = random.choice(y)
            #     if y1 == 0:
            #         all_solutions.append(swap_one_pair(new_solution))
            #     elif y1 == 1:
            #         all_solutions.append(move_battery(new_solution))
            #     else:
            #         all_solutions.append(move_one_house(new_solution))
            # else:
            #     y2 = random.choice(y)
            #     if y2 == 0:
            #         all_solutions.append(move_ten_houses(new_solution))
            #     elif y2 == 1:
            #         all_solutions.append(move_battery(new_solution))
            #     else:
            #         all_solutions.append(move_one_house(new_solution))

        all_solutions.sort(key=lambda x: x.score, reverse=True)
        list_of_scores.append(all_solutions[0].score)
        list_of_scores2.append(all_solutions[119].score)
        solutions = all_solutions[:solutions_counter]

        print(solutions[0])

        if counter % 1000 == 0:
            if solutions[0].score == temp_save:
                print(f"Best score: {solutions[0].score}")
                break
            else:
                temp_save = solutions[0].score



    for battery in solutions[0].batterys:
        print(battery)

    plt.plot(list_of_scores)
    plt.plot(list_of_scores2)
    plt.ylabel("score PPA")
    plt.show()

    return solutions[0]


def move_one_house(solution):
    battery1 = random.choice(solution.batterys)
    house1 = random.choice(battery1.list_of_houses)

    while True:
        battery2 = random.choice(solution.batterys)
        if battery1 != battery2:
            break

    rm(house1, battery1)
    ad(house1, battery2)

    return solution


def swap_one_pair(solution):

    battery1 = random.choice(solution.batterys)
    while True:
        battery2 = random.choice(solution.batterys)
        if battery1 != battery2:
            break

    house1 = random.choice(battery1.list_of_houses)
    house2 = random.choice(battery2.list_of_houses)
    swap(house1, house2, battery1, battery2)

    return solution


def move_ten_houses(solution):

    for i in range(10):
        battery1 = random.choice(solution.batterys)
        house1 = random.choice(battery1.list_of_houses)

        while True:
            battery2 = random.choice(solution.batterys)
            if battery1 != battery2:
                break

        rm(house1, battery1)
        ad(house1, battery2)

    return solution


def move_battery(solution):

    battery = random.choice(solution.batterys)
    locatie = random.choice([battery.location_x, battery.location_y])
    locatie += random.choice([-1, 1])

    return solution

    # list = [0, 1]
    # battery = random.choice(solution.batterys)
    # if random.choice(list) == 0:
    #     if random.choice(list) == 0:
    #         battery.location_x += 1
    #     elif random.choice(list) == 1:
    #         battery.location_y += 1
    # elif random.choice(list) == 1:
    #     if random.choice(list) == 0:
    #         battery.location_x -= 1
    #     elif random.choice(list) == 1:
    #         battery.location_y -= 1
    # return solution


def change_battery(solution):

    battery = random.choice(solution.batterys)
    # if battery.current_input > battery.max_input:
    #     if battery.max_input == 450:
    #         battery.max_input = 900
    #     elif battery.max_input == 900:
    #         battery.max_input = 1800
    if battery.current_input < battery.max_input:
        if battery.max_input == 1800:
            battery.max_input = 900
        elif battery.max_input == 900:
            battery.max_input = 450

    return solution


def place_battery_middle(solution):

    for battery in solution.batterys:
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

    return solution
