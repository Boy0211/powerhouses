import random
from datetime import datetime
import matplotlib.pyplot as plt

from add_remove import add_house_to_battery
from score import calculate_score


def random_greedy(houses, batterys):

    list = [0, 1, 2, 3, 4]
    list_2 = []

    i = 0
    while i < len(houses):

            counter = random.choice(list)

            if batterys[counter].current_input + houses[i].output <= float(batterys[counter].max_input):
                add_house_to_battery(houses[i], batterys[counter])
                i += 1

            else:
                list_2.append(counter)
                if set(list_2) == set(list):
                    for battery in batterys:
                        battery.current_input = 0
                        battery.list_of_houses = []
                    list_2.clear()
                    i = 0

def random_distribution(houses, batterys, attempts, bins):

    i = 0
    all_scores = []
    time_stamp = datetime.now()
    while i < attempts:
        random_greedy(houses, batterys)
        score = calculate_score(houses)
        all_scores.append(score)
        i += 1

    print(datetime.now() - time_stamp)
    all_scores.sort()
    n,x,_ = plt.hist(all_scores, bins)
    bin_centers = 0.5*(x[1:]+x[:-1])
    plt.plot(bin_centers, n)
    plt.show()
