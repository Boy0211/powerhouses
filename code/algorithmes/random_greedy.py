'''
    File name: random_greedy.py
    Author: Mendel, Sam, Rutger
    Date created: 17/11/2018
    Date last modified: 17/12-2018
'''
import copy
import random
import matplotlib.pyplot as plt

from helpers import add_possible
from helpers import add_house_to_battery
from randomHillclimber import random_hillclimber
from hillclimber import hillclimber
from greedy import greedy_2
from greedy import greedy_1


def random_distribution(solution, attempts, bins):

    '''Function which creates a plot with a normal distribution'''

    # creates empty variables
    i = 0
    all_scores = []
    solution_2 = copy.deepcopy(solution)

    # while the attempts are not reached keep on trying
    while i < attempts:
        random_greedy(solution)
        print(solution)
        all_scores.append(solution.costs)
        random_hillclimber(solution)
        print(solution)
        all_scores.append(solution.costs)
        i += 1

    # sort all the scores and create a normal distribution
    solution_distance = greedy_2(solution_2)
    solution_capacity = greedy_1(solution_2)
    plt.plot(solution_distance.costs)
    plt.plot(solution_capacity.costs)

    solution_hillclimber = hillclimber(solution_capacity)
    plt.plot(solution_hillclimber.costs)

    all_scores.sort()
    n, x, _ = plt.hist(all_scores, bins)
    bin_centers = 0.5*(x[1:]+x[:-1])
    plt.plot(bin_centers, n)
    # plt.set()
    plt.show()


def random_greedy(solution):

    '''Function which randomly distributes all the houses over the batterys'''

    # takes the variables out of the solution
    houses = solution.houses
    batterys = solution.batterys

    # creates variables used in the while loop
    list_houses = list(range(0, 150))
    lijst = [0, 1, 2, 3, 4]
    list_2 = []

    # keep's on trying until all the houses are distributed over the batterys
    while len(list_houses) > 0:

            # chooses a random house and a random battery
            house_counter = random.choice(list_houses)
            counter = random.choice(lijst)

            # if the house fits into the battery, put it there
            if add_possible(batterys[counter], houses[house_counter]):
                add_house_to_battery(houses[house_counter], batterys[counter])
                list_houses.remove(house_counter)

            # else append the battery into a seperate list
            else:
                list_2.append(counter)

                # if all the batterys are saved into this seperate list
                # the solution is not right, so all the batteries are emptied
                # and the algorithm runs again.
                if set(list_2) == set(lijst):
                    for battery in batterys:
                        battery.current_input = 0
                        battery.list_of_houses = []
                    list_2.clear()
                    list_houses = list(range(0, 150))

    return solution
