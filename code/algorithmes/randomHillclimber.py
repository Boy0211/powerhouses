import random

from helpers import swap
from helpers import capacity
from helpers import house_battery_distance as distance


def randomly(x):

    '''A function to randomize a list.'''

    shuffled = list(x)
    random.shuffle(shuffled)
    return shuffled


def random_hillclimber(solution):

    ''' A hill climber which swappes random houses if and only when a better
    solution is created '''

    # take the variable out of the solution which is used in the algorithm
    batterys = solution.batterys

    # while statement keep on trying swaps until there is no swap possible.
    counter = 0
    while True:
        temp_counter = counter
        for i in randomly(range(len(batterys))):
            battery_counter_1 = i
            for j in randomly(range(len(batterys[battery_counter_1]
                              .list_of_houses))):
                house_counter_1 = j
                for k in randomly(range(len(batterys))):
                    battery_counter_2 = k
                    for l in randomly(range(len(batterys[battery_counter_2]
                                      .list_of_houses))):
                        house_counter_2 = l

                        # creates variables to make the algorithm more readable
                        battery_A = batterys[battery_counter_1]
                        battery_B = batterys[battery_counter_2]
                        house_a = battery_A.list_of_houses[house_counter_1]
                        house_b = battery_B.list_of_houses[house_counter_2]

                        # if statement to check whether the possible swap is
                        # - bennificial.
                        # - doesn't surpass the capacity of the batterys.
                        if (distance(house_a, battery_A) +
                            distance(house_b, battery_B) >
                            distance(house_a, battery_B) +
                            distance(house_b, battery_A) and
                           (capacity(house_a, house_b, battery_A) is True)
                           and capacity(house_b, house_a, battery_B) is True):

                            # swap the houses.
                            swap(house_a, house_b, battery_A, battery_B)
                            counter = counter + 1

        if temp_counter == counter:
            break

    # save the used variable into the solution and return it
    solution.batterys = batterys
    return solution
