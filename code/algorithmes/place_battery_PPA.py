import random
import matplotlib.pyplot as plt

from helpers import remove_house_from_battery as rm
from helpers import add_house_to_battery as ad
from helpers import swap
from copy_solution import copy_solution


def battery_based_plant_propagation_algorithm(solutions):

    solutions_counter = len(solutions)

    index = 0
    temp_save = 0

    # list of scores for visualization
    list_of_scores = []

    while True:
        index += 1
        all_solutions = []

        for solution in solutions:

            old_solution = solution
            all_solutions.append(old_solution)
            new_solution = copy_solution(solution)

            x = [0, 1]
            y = [0, 1, 2]

            if solution.score >= 0.90:
                if random.choice(x) == 0:
                    all_solutions.append(swap_one_pair(new_solution))
                else:
                    all_solutions.append(move_battery(new_solution))
            elif solution.score < 0.90 and solution.score >= 0.50:
                if random.choice(y) == 0:
                    all_solutions.append(swap_one_pair(new_solution))
                elif random.choice(y) == 1:
                    all_solutions.append(move_battery(new_solution))
                else:
                    all_solutions.append(move_one_house(new_solution))
            else:
                if random.choice(y) == 0:
                    all_solutions.append(move_ten_houses(new_solution))
                elif random.choice(y) == 1:
                    all_solutions.append(move_battery(new_solution))
                else:
                    all_solutions.append(move_one_house(new_solution))

        all_solutions.sort(key=lambda x: x.score, reverse=True)
        solutions = all_solutions[:solutions_counter]

        print(solutions[0])

        if index % 100 == 0:
            if solutions[0].score == temp_save:
                print(f"Best score: {solutions[0].score}")
                break
            else:
                temp_save = solutions[0].score

        list_of_scores.append(solutions[0].score)

    for battery in solutions[0].batterys:
        print(battery)

    plt.plot(list_of_scores)
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
    if battery.current_input > battery.max_input:
        # battery x > y
        if battery.max_input == 450:
            battery.max_input = 900
        elif battery.max_input == 900:
            battery.max_input = 1800
    elif battery.current_input < battery.max_input:
        if battery.max_input == 1800:
            battery.max_input = 900
        elif battery.max_input == 900:
            battery.max_input = 450

    return solution
