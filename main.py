import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithmes"))
sys.path.append(os.path.join(directory, "code", "classes"))

from random_greedy import random_greedy
from greedy import greedy_1
from smartGRID import Smartgrid
from score import calculate_score
from visualization import grid


def main():

    smartgrid = Smartgrid(3)
    greedy_1(smartgrid.houses, smartgrid.batterys)
    grid(smartgrid.houses, smartgrid.batterys)
    # i = 0
    # all_scores = []
    # time_stamp = datetime.now()
    # while i < 100:
    #     random_greedy(smartgrid.houses, smartgrid.batterys)
    #     score = calculate_score(smartgrid.houses)
    #     all_scores.append(score)
    #     i += 1
    #
    # print(datetime.now() - time_stamp)
    # all_scores.sort()
    # bins = 25
    # n,x,_ = plt.hist(all_scores, bins)
    # bin_centers = 0.5*(x[1:]+x[:-1])
    # plt.plot(bin_centers, n)
    # plt.show()
    # for battery in smartgrid.batterys:
    #     print(battery)
    exit()


if __name__ == "__main__":
    main()
