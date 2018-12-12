import copy
import random

# from helpers import house_battery_distance as distance
# from helpers import capacity
from helpers import swap
from copy_solution import copy_solution
from helpers import remove_house_from_battery as rm
from helpers import add_house_to_battery as ad


def plant_propagation_algorithm(solutions):

    counter = 0
    length = len(solutions)
    temp_save = 0

    while True:
        counter += 1
        all_solutions = []

        for index, solution in enumerate(solutions, start=0):   # default is zero

            # make a deepcopy of the current solutions
            old_solution = solution
            all_solutions.append(old_solution)

            # x = [0, 1]
            # y = [0, 1, 2]


            if index < 10:
                all_solutions.append(swap1_random(copy_solution(solution)))
            elif index >= 10 and index < 20:
                all_solutions.append(swap1_random(copy_solution(solution)))
                all_solutions.append(move_one_house(copy_solution(solution)))
            else:
                all_solutions.append(swap2_random(copy_solution(solution)))
                all_solutions.append(swap1_random(copy_solution(solution)))
                all_solutions.append(move_one_house(copy_solution(solution)))

            # if solution.score >= 0.90:
            #     all_solutions.append(swap1_random(new_solution))
            # elif solution.score < 0.90 and solution.score >= 0.50:
            #     if random.choice(x) == 0:
            #         all_solutions.append(swap1_random(new_solution))
            #     else:
            #         all_solutions.append(move_one_house(new_solution))
            # else:
            #     if random.choice(y) == 0:
            #         all_solutions.append(swap2_random(new_solution))
            #     elif random.choice(y) == 1:
            #         all_solutions.append(swap1_random(new_solution))
            #     else:
            #         all_solutions.append(move_one_house(new_solution))

        all_solutions.sort(key=lambda x: x.score, reverse=True)
        solutions = all_solutions[:length]
        # print(solutions[0])

        if counter % 100 == 0:
            if solutions[0].score == temp_save:
                print(index)
                break
            else:
                temp_save = solutions[0].score
        # if counter % 50 == 0:
        #     for solution in solutions:
        #         swap2_random(solution)

    # for battery in solutions[0].batterys:
    #     print(battery)

    return solutions[0]


def swap1_random(solution):

    battery1 = random.choice(solution.batterys)
    while True:
        battery2 = random.choice(solution.batterys)
        if battery1 != battery2:
            break

    house1 = random.choice(battery1.list_of_houses)
    house2 = random.choice(battery2.list_of_houses)
    swap(house1, house2, battery1, battery2)

    return solution


def swap2_random(solution):

    for i in range(5):
        battery1 = random.choice(solution.batterys)
        while True:
            battery2 = random.choice(solution.batterys)
            if battery1 != battery2:
                break

        house1_1 = random.choice(battery1.list_of_houses)
        while True:
            house1_2 = random.choice(battery1.list_of_houses)
            if house1_1 != house1_2:
                break

        house2_1 = random.choice(battery2.list_of_houses)
        while True:
            house2_2 = random.choice(battery2.list_of_houses)
            if house2_1 != house2_2:
                break

        swap(house1_1, house2_1, battery1, battery2)
        swap(house1_2, house2_2, battery1, battery2)

    return solution


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
