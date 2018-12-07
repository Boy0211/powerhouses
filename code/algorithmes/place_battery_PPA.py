import random

from helpers import remove_house_from_battery as rm
from helpers import add_house_to_battery as ad
from helpers import swap
from copy_solution import copy_solution


def battery_based_plant_propagation_algorithm(solutions):

    solutions_counter = len(solutions)

    index = 0
    temp_save = 0

    while True:
        index += 1
        all_solutions = []
        counter = 0
        for solution in solutions:

            old_solution = solution
            all_solutions.append(old_solution)
            new_solution = copy_solution(solution)

            if counter % 3 == 0:
                all_solutions.append(move_one_house(new_solution))
            elif counter % 3 == 1:
                all_solutions.append(swap_one_pair(new_solution))
            elif counter % 3 == 2:
                all_solutions.append(move_ten_houses(new_solution))
            counter += 1

        all_solutions.sort(key=lambda x: x.score, reverse=True)
        solutions = all_solutions[:solutions_counter]
        print(solutions[0])

        if index % 100 == 0:
            if solutions[0].score <= temp_save:
                print(index)
                break
            else:
                temp_save = solutions[0].score

    for battery in solutions[0].batterys:
        print(battery)

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
