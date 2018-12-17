'''
    File name: random_greedy.py
    Author: Mendel, Sam, Rutger
    Date created: 17/11/2018
    Date last modified: 17/12-2018
'''
import random
import matplotlib.pyplot as plt
import seaborn as sns

from helpers import add_house_to_battery
from randomHillclimber import random_hillclimber


def random_distribution(solution, attempts, bins):

    '''Function which creates a plot with a normal distribution'''

    # creates empty variables
    i = 0
    all_scores = []

    # while the attempts are not reached keep on trying
    while i < attempts:
        random_greedy(solution)
        random_hillclimber(solution)
        score = solution.score
        all_scores.append(score)
        i += 1

    # sort all the scores and create a normal distribution
    all_scores.sort()
    n, x, _ = plt.hist(all_scores, bins)
    bin_centers = 0.5*(x[1:]+x[:-1])
    sns.distplot(bin_centers, n)
    sns.set()
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
            if batterys[counter].current_input + houses[house_counter].output <= float(batterys[counter].max_input):
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
