import random
from helpers import swap
from helpers import capacity
from helpers import house_battery_distance as distance


def randomly(x):

    '''A random function to randomize a list.'''

    shuffled = list(x)
    random.shuffle(shuffled)
    return shuffled


def random_hillclimber(solution):

    ''' A random Hill Climber '''

    batterys = solution.batterys

    # while statement keep on trying swaps until there is no swap possible.
    counter = 0
    while True:
        temp_counter = counter
        for i in range(len(batterys)):
            battery_counter_1 = i
            for j in range(len(batterys[battery_counter_1].list_of_houses)):
                house_counter_1 = j
                for k in range(len(batterys)):
                    battery_counter_2 = k
                    for l in range(len(batterys[battery_counter_2].list_of_houses)):
                        house_counter_2 = l
                        # print(i, j, k, l)
                        battery_A = batterys[battery_counter_1]
                        battery_B = batterys[battery_counter_2]
                        house_a = battery_A.list_of_houses[house_counter_1]
                        house_b = battery_B.list_of_houses[house_counter_2]

                        # if statement to check whether the possible swap is
                        # - bennificial.
                        # - doesn't surpass the capacity of the batterys.
                        if (distance(house_a, battery_A) + distance(house_b, battery_B) >
                           distance(house_a, battery_B) + distance(house_b, battery_A) and
                           (capacity(house_a, house_b, battery_A) is True)
                           and capacity(house_b, house_a, battery_B) is True):

                            # swap the houses.
                            swap(house_a, house_b, battery_A, battery_B)
                            counter = counter + 1

        if temp_counter == counter:
            break
