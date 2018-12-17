import random
import matplotlib.pyplot as plt
import copy

from helpers import remove_house_from_battery as rm
from helpers import add_house_to_battery as ad
from helpers import swap


def battery_based_plant_propagation_algorithm(solutions, iterations):

    '''Plant propagation algorithm used for dynamic batterys. It differs from
    the other PPA in the runners. This PPA has runners which can move the
    batterys'''

    # temporary variables saved for usage by the algorithm
    length = len(solutions)
    counter = 0

    # list of scores for visualization
    list_of_scores = []
    list_of_scores2 = []

    # keep on trying to create a better solution
    while True:

        # variables used in the algorithm
        counter += 1
        all_solutions = []

        # for loop
        for index, solution in enumerate(solutions, start=0):

            # append the old solution into the new list
            old_solution = solution
            all_solutions.append(old_solution)

            # create short runners
            if index < 10:
                all_solutions.append(swap_one_pair(copy.deepcopy(solution)))
                all_solutions.append(move_battery(copy.deepcopy(solution)))

            # create medium runners
            elif index >= 10 and index < 20:
                all_solutions.append(swap_one_pair(copy.deepcopy(solution)))
                all_solutions.append(move_battery(copy.deepcopy(solution)))
                all_solutions.append(move_one_house(copy.deepcopy(solution)))

            # create long runners
            else:
                all_solutions.append(move_one_house(copy.deepcopy(solution)))
                all_solutions.append(move_ten_houses(copy.deepcopy(solution)))
                all_solutions.append(change_battery(copy.deepcopy(solution)))
                all_solutions.append(place_bat_middle(copy.deepcopy(solution)))

        # sort all the solutions into a list, based on score
        all_solutions.sort(key=lambda x: x.score, reverse=True)

        # save the score into a list for visualization
        list_of_scores.append(all_solutions[0].score)
        list_of_scores2.append(all_solutions[length - 1].score)

        # keep the best solutions
        solutions = all_solutions[:length]

        # print the best solution
        print(solutions[0])

        # every 100 iterations a check will be done
        # if no better solution is created, the while loop will break
        # if the amount of iterations is reachted, break
        if counter == iterations:
            break
        else:
            counter += 1

    # plot a line graph showing the difference the PPA made.
    plt.plot(list_of_scores)
    plt.plot(list_of_scores2)
    plt.ylabel("score PPA")
    plt.show()

    # return the best solution
    return solutions[0]


def move_one_house(solution):

    '''Move one house from one battery into another'''

    # choose one battery and one house
    battery1 = random.choice(solution.batterys)
    house1 = random.choice(battery1.list_of_houses)

    # choose a second battery which can't be the same as the first
    while True:
        battery2 = random.choice(solution.batterys)
        if battery1 != battery2:
            break

    # move the house
    rm(house1, battery1)
    ad(house1, battery2)

    # return the solution
    return solution


def swap_one_pair(solution):

    ''''Swap one pair of houses'''

    # randomly choose one battery
    battery1 = random.choice(solution.batterys)

    # randomly choose a second battery which cna't be the same as the first
    while True:
        battery2 = random.choice(solution.batterys)
        if battery1 != battery2:
            break

    # randomly choose 2 houses out of the batterys
    house1 = random.choice(battery1.list_of_houses)
    house2 = random.choice(battery2.list_of_houses)

    # swap the houses
    swap(house1, house2, battery1, battery2)

    # return the solution
    return solution


def move_ten_houses(solution):

    '''Move ten houses from 10 random chosen batterys'''

    # start a for loop with a range of 10
    for i in range(10):

        # choose a battery and an house
        battery1 = random.choice(solution.batterys)
        house1 = random.choice(battery1.list_of_houses)

        # choose a second house, which can't be the same as the first
        while True:
            battery2 = random.choice(solution.batterys)
            if battery1 != battery2:
                break

        # move the house from the one battery into another
        rm(house1, battery1)
        ad(house1, battery2)

    # return the solution
    return solution


def move_battery(solution):

    '''Randomly move a battery one place on the grid'''

    # choose a random battery
    battery = random.choice(solution.batterys)

    # randomly choose whether you move the battery on the x or y-axis
    locatie = random.choice([battery.location_x, battery.location_y])

    # randomly choose whether battery move up vs down or left vs right
    locatie += random.choice([-1, 1])

    # return the solution
    return solution


def change_battery(solution):

    '''change the format of the battery'''

    # randomly choose one battery
    battery = random.choice(solution.batterys)

    # change the battery capacity
    if battery.current_input < battery.max_input:
        if battery.max_input == 1800:
            battery.max_input = 900
        elif battery.max_input == 900:
            battery.max_input = 450

    # return the solution
    return solution


def place_bat_middle(solution):

    '''place the battery in the middle of his connected houses'''

    # for every battery in the solution
    for battery in solution.batterys:

        # create a emtpy list for the x and y-coordinates
        x_coordinates = list()
        y_coordinates = list()

        # for every house in the battery
        for house in battery.list_of_houses:

            # append the x and y-coordinate into the list
            x_coordinates.append(house.location_x)
            y_coordinates.append(house.location_y)

        # failsafe for when a battery is empty
        if len(x_coordinates) == 0 or len(y_coordinates) == 0:
            x_coordinates = [1]
            y_coordinates = [1]

        # calculate the mean of all the coordinates
        mean_x = round(sum(x_coordinates)/len(x_coordinates))
        mean_y = round(sum(y_coordinates)/len(y_coordinates))

        # place the battery on this mean
        battery.location_x = mean_x
        battery.location_y = mean_y

    # return the solution
    return solution
