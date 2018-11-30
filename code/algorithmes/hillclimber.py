import random
from add_remove import add_house_to_battery as ad
from add_remove import remove_house_from_battery as rm


# A random function to randomize a list.
def randomly(x):
    shuffled = list(x)
    random.shuffle(shuffled)
    return shuffled


# A function used to swap two houses from one list to another.
def swap(house_a, house_b, battery_A, battery_B):
    rm(house_a, battery_A)
    ad(house_a, battery_B)
    rm(house_b, battery_B)
    ad(house_b, battery_A)


# the main hill climber function.
def hill_climber_2(houses, batterys):

    # initializing a while loop with a counter on zero.
    counter = 0
    while True:
        # search for the best score in houses and batterys.
        # Best score is the score when swapped has to most impact.
        # the function returns False when there is no possible score left.
        houses = search_best_score(houses, batterys)

        # when there is an swap left, do the folowing:
        if houses is not False:

            # controls of one of the batterys has an input that surpasses his
            # capacity. If so, the function returns a battery, else the
            # function returns falseself.
            if battery_capacity_exceeded(batterys) is not False:

                # returns the battery which is exceeded and within that battery
                # the house with the highest output.
                battery1 = battery_capacity_exceeded(batterys)
                house1 = check_highest_output(battery1)

                # returns the battery with the lowest input and within that
                # batery, the house with the lowest output. Also, a counter is
                # used. This counter comes in handy when the swap between
                # biggest and smallest fails. Next try will be the second
                # smallest house.
                battery2 = check_battery_lowest_input(batterys)
                house2 = check_lowest_output(battery2, counter)
                counter += 1

                # swap the houses
                swap(house1, house2, battery1, battery2)
            # if no batterys are exceeded, excecute the following:
            else:

                # swap the houses with the highest score.
                battery1 = batterys[houses[0].connected_battery["id"] - 1]
                battery2 = batterys[houses[1].connected_battery["id"] - 1]
                swap(houses[0], houses[1], battery1, battery2)

        # when no swap is possible; break.
        else:
            break


# a function to determine whether a battery capacity is exceeded.
def battery_capacity_exceeded(batterys):
    for battery in batterys:
        if battery.current_input > float(battery.max_input):
            return battery
    return False


# a function to get the battery with the lowest input.
def check_battery_lowest_input(batterys):

    score = float(batterys[0].max_input)
    for battery in batterys:
        if battery.current_input < score:
            score = battery.current_input
            lowest_input_battery = battery
    return lowest_input_battery


# a function to get the house with the highest output in a battery.
def check_highest_output(battery):
    score = 0
    for house in battery.list_of_houses:
        if house.output > score:
            score = house.output
            highest_output_house = house
    return highest_output_house


# a function used to get the house with the lowest output in a battery.
def check_lowest_output(battery, counter):
    battery.list_of_houses.sort(key=lambda x: x.output, reverse=False)
    print(counter)
    return battery.list_of_houses[counter % 24]


# a function used to determine a score for swapping the houses.
def swap_score(house_a, house_b):
    score = (house_a.connected_battery["distance"] +
             house_b.connected_battery["distance"])
    score_new = (house_a.battery_distances[house_b.connected_battery["id"]] +
                 house_b.battery_distances[house_a.connected_battery["id"]])
    swap_score = score - score_new
    return swap_score


# function used to determine the whether a swap is possible within the capacity
# of the batterys.
def capacity(house1, house2, battery):
    if (battery.current_input - house1.output + house2.output
       <= float(battery.max_input)):
        return True
    else:
        return False


# function to determine the best possible swap.
def search_best_score(houses, batterys):

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
                    new_score = swap_score(house_a, house_b)

                    # checks whether the swap is possible and is better than
                    # last option.
                    if (capacity(house_a, house_b, battery_A) is True
                       and capacity(house_b, house_a, battery_B) is True
                       and new_score >= score):
                        score = new_score
                        house1 = house_a
                        house2 = house_b
    if score == 0.0:
        return False
    else:
        return [house1, house2]


# hill climber which swaps two houses the moment it finds a possible swap.
def hill_climber(houses, batterys):

    counter = 0
    for i in randomly(range(len(batterys))):
        battery_A = batterys[i]
        for j in randomly(range(len(batterys[i].list_of_houses))):
            house_a = battery_A.list_of_houses[j]
            for k in randomly(range(len(batterys))):
                battery_B = batterys[k]
                for l in randomly(range(len(batterys[k].list_of_houses))):
                    house_b = battery_B.list_of_houses[l]

                    # a huge if statement to check whether the possible swap:
                    # - the swap is bennificial
                    # - the swap doesn't surpass the capacity of the batterys
                    if ((house_a.connected_battery["distance"] +
                       house_b.connected_battery["distance"] >
                       house_a.battery_distances[k+1] +
                       house_b.battery_distances[i+1]) and
                       (battery_A.current_input - house_a.output +
                       house_b.output < float(battery_A.max_input))
                       and (battery_B.current_input - house_b.output +
                       house_a.output < float(battery_B.max_input))):

                        # swap the houses.
                        swap(house_a, house_b, battery_A, battery_B)
                        counter = counter + 1
