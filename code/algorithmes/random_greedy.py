import random
from datetime import datetime
import matplotlib.pyplot as plt

from helpers import add_house_to_battery
# from randomHillclimber import random_hillclimber
from hillclimber import hillclimber
from randomHillclimber import random_hillclimber


def random_distribution(solution, attempts, bins):

    i = 0
    all_scores = []
    time_stamp = datetime.now()
    while i < attempts:
        random_greedy(solution)
        random_hillclimber(solution)
        score = solution.score
        all_scores.append(score)
        i += 1

    print(datetime.now() - time_stamp)
    all_scores.sort()
    n, x, _ = plt.hist(all_scores, bins)
    bin_centers = 0.5*(x[1:]+x[:-1])
    plt.plot(bin_centers, n)
    plt.show()


def random_greedy(solution):

    houses = solution.houses
    batterys = solution.batterys

    list_houses = list(range(0, 150))
    lijst = [0, 1, 2, 3, 4]
    list_2 = []

    while len(list_houses) > 0:

            house_counter = random.choice(list_houses)
            counter = random.choice(lijst)

            if batterys[counter].current_input + houses[house_counter].output <= 1.00 * float(batterys[counter].max_input):
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

    return solution
