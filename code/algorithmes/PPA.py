'''
    File name: PPA.py
    Author: Mendel, Sam, Rutger
    Date created: 17/11/2018
    Date last modified: 17/12-2018
'''
import copy
import random

from helpers import swap
from helpers import remove_house_from_battery as rm
from helpers import add_house_to_battery as ad


def plant_propagation_algorithm(solutions, iterations):

    '''Plant plant propagation algorithm whith short, medium
    and long runners'''

    counter = 0
    length = len(solutions)

    # while the amount of iterations is not reached
    while True:

        # create a empty list in which the solutions are saved
        all_solutions = []

        # a for loop which creates new solutions based on the concept of PPA
        for index, solution in enumerate(solutions, start=0):

            # save the current solution into a list
            old_solution = solution
            all_solutions.append(old_solution)

            # the first 10 solutions will get a short runner
            if index < 10:
                all_solutions.append(swap1_random(copy.deepcopy(solution)))

            # the second 10 solutions will get a medium runner
            elif index >= 10 and index < 20:
                all_solutions.append(swap1_random(copy.deepcopy(solution)))
                all_solutions.append(move_one_house(copy.deepcopy(solution)))

            # and all the others will get a long runner
            else:
                all_solutions.append(swap2_random(copy.deepcopy(solution)))
                all_solutions.append(swap1_random(copy.deepcopy(solution)))
                all_solutions.append(move_one_house(copy.deepcopy(solution)))

        # sort the solutions based on score
        all_solutions.sort(key=lambda x: x.score, reverse=True)

        # and keep the amount of solutions equal as the amount
        # of start solutions
        solutions = all_solutions[:length]

        # print the best solution
        print(solutions[0])

        # if the amount of iterations is reachted, break
        if counter == iterations:
            break
        else:
            counter += 1

    # return the best solution
    return solutions[0]


# from here on the different runners are definied.
def swap1_random(solution):

    '''randomly swap 1 house'''

    # choose one random battery
    battery1 = random.choice(solution.batterys)

    # choose a second battery, which can't be the same as the first
    while True:
        battery2 = random.choice(solution.batterys)
        if battery1 != battery2:
            break

    # choose from the batterys 2 houses which will be swapped
    house1 = random.choice(battery1.list_of_houses)
    house2 = random.choice(battery2.list_of_houses)
    swap(house1, house2, battery1, battery2)

    # return the solution
    return solution


def swap2_random(solution):

    '''random swap 10 (5 x 2) houses'''

    # loop 5 times
    for i in range(5):

        # randomly choose one battery
        battery1 = random.choice(solution.batterys)

        # choose a second battery which is not the same as the first
        while True:
            battery2 = random.choice(solution.batterys)
            if battery1 != battery2:
                break

        # choose 2 different houses from the first battery
        house1_1 = random.choice(battery1.list_of_houses)
        while True:
            house1_2 = random.choice(battery1.list_of_houses)
            if house1_1 != house1_2:
                break

        # choose 2 different houses from the second battery
        house2_1 = random.choice(battery2.list_of_houses)
        while True:
            house2_2 = random.choice(battery2.list_of_houses)
            if house2_1 != house2_2:
                break

        # swap the houses
        swap(house1_1, house2_1, battery1, battery2)
        swap(house1_2, house2_2, battery1, battery2)

    # return the solution
    return solution


def move_one_house(solution):

    '''Move one house from one battery into another'''

    # choose a battery and an house from the battery
    battery1 = random.choice(solution.batterys)
    house1 = random.choice(battery1.list_of_houses)

    # choose a battery which is not the same as the first
    while True:
        battery2 = random.choice(solution.batterys)
        if battery1 != battery2:
            break

    # remove the house from the first battery and add it to the second
    rm(house1, battery1)
    ad(house1, battery2)

    # return the solution
    return solution
