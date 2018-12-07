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

            random_list = [1, 2, 3, 4]
            if random.choice(random_list) == 1:
                all_solutions.append(move_one_house(new_solution))
            if random.choice(random_list) == 2:
                all_solutions.append(swap_one_pair(new_solution))
            if random.choice(random_list) == 3:
                all_solutions.append(move_ten_houses(new_solution))
            if random.choice(random_list) == 4:
                all_solutions.append(move_battery(new_solution))

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

    list = [0, 1]
    battery = random.choice(solution.batterys)
    if random.choice(list) == 0:
        if random.choice(list) == 0:
            battery.location_x += 1
        elif random.choice(list) == 1:
            battery.location_y += 1
    elif random.choice(list) == 1:
        if random.choice(list) == 0:
            battery.location_x -= 1
        elif random.choice(list) == 1:
            battery.location_y -= 1
    return solution
