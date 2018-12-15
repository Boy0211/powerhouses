from helpers import swap
from helpers import capacity
from helpers import house_battery_distance as distance
from helpers import battery_capacity_exceeded as cap_exc


def hillclimber(solution):

    '''The main hill climber function.'''

    # get the batterys out of the solution
    batterys = solution.batterys

    # initializing a while loop with a counter on zero.
    counter = 0
    while True:
        # search for the best score in houses and batterys.
        # Best score is the score when swapped has to most impact.
        # the function returns False when there is no possible score left.
        best_swap = search_best_score(batterys)

        # when there is an swap left, do the folowing:
        if best_swap is not False:

            # controls of one of the batterys has an input that surpasses his
            # capacity. If so, the function returns a battery, else the
            # function returns falseself.
            if cap_exc(batterys) is not False:

                # returns the battery which is exceeded and within that battery
                # the house with the highest output.
                batterys.sort(key=lambda x: x.current_input, reverse=True)
                battery1 = batterys[0]

                battery1.list_of_houses.sort(key=lambda x: x.output,
                                             reverse=True)
                house1 = battery1.list_of_houses[0]

                # returns the battery with the lowest input and within that
                # batery, the house with the lowest output. Also, a counter is
                # used. This counter comes in handy when the swap between
                # biggest and smallest fails. Next try will be the second
                # smallest house.
                battery2 = batterys[-1]
                battery2.list_of_houses.sort(key=lambda x: x.output,
                                             reverse=True)
                difference = battery1.current_input - battery1.max_input
                for house in battery2.list_of_houses:
                    if house.output < house1.output - difference:
                        house2 = house
                        swap(house1, house2, battery1, battery2)
                        break

                    elif abs(counter) > len(batterys):
                        print("capacity switch not possible")
                        exit()
                    else:
                        counter -= 1

            # if no batterys are exceeded, excecute the following:
            else:
                # swap the houses with the highest score.
                swap(best_swap[0], best_swap[1], best_swap[2], best_swap[3])

        # when no swap is possible; break.
        else:
            break

    return solution


# a function used to determine a score for swapping the houses.
def swap_score(house_a, house_b, battery_A, battery_B):
    score = distance(house_a, battery_A) + distance(house_b, battery_B)
    score_new = distance(house_a, battery_B) + distance(house_b, battery_A)
    swap_score = score - score_new
    return swap_score


# function to determine the best possible swap.
def search_best_score(batterys):

    # score starts at 0.0 and will be replaced when a better score is found
    score = 0.0

    # using 4 for loops to check for the best score.
    for i in range(len(batterys)):
        battery_A = batterys[i]
        for j in range(len(batterys[i].list_of_houses)):
            house_a = battery_A.list_of_houses[j]
            for k in range(len(batterys)):
                battery_B = batterys[k]
                for l in range(len(batterys[k].list_of_houses)):
                    house_b = battery_B.list_of_houses[l]
                    new_score = swap_score(house_a, house_b, battery_A,
                                           battery_B)

                    # checks whether the swap is possible and is better than
                    # last option.
                    if (capacity(house_a, house_b, battery_A) is True
                       and capacity(house_b, house_a, battery_B) is True
                       and new_score >= score):
                        score = new_score
                        house1 = house_a
                        house2 = house_b
                        battery1 = battery_A
                        battery2 = battery_B
    if score == 0.0:
        return False
    else:
        return [house1, house2, battery1, battery2]
