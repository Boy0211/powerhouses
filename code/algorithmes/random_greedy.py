import random
from datetime import datetime
import matplotlib.pyplot as plt

from add_remove import add_house_to_battery
from score import calculate_score
from hillclimber import hill_climber
from hillclimber import hill_climber_2


def random_greedy(houses, batterys):

    list_houses = list(range(0, 150))

    lijst = [0, 1, 2, 3, 4]
    list_2 = []

    i = 0
    while len(list_houses) > 0:

            house_counter = random.choice(list_houses)
            counter = random.choice(lijst)

            if batterys[counter].current_input + houses[house_counter].output <= 1.01 * float(batterys[counter].max_input):
                add_house_to_battery(houses[house_counter], batterys[counter])
                list_houses.remove(house_counter)

            else:
                list_2.append(counter)
                if set(list_2) == set(lijst):
                    for battery in batterys:
                        battery.current_input = 0
                        battery.list_of_houses = []
                    list_2.clear()
                    list_houses = list(range(0, 150))

def random_distribution(houses, batterys, attempts, bins):

    i = 0
    all_scores = []
    time_stamp = datetime.now()
    while i < attempts:
        random_greedy(houses, batterys)
        hill_climber_2(houses, batterys)
        score = calculate_score(houses)
        all_scores.append(score)
        i += 1

    print(datetime.now() - time_stamp)
    all_scores.sort()
    n,x,_ = plt.hist(all_scores, bins)
    bin_centers = 0.5*(x[1:]+x[:-1])
    plt.plot(bin_centers, n)
    plt.show()
