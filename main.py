import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import time

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

    moment = time.time()
    smartgrid = Smartgrid(1)
    # grid(smartgrid.houses, smartgrid.batterys)
    # greedy_1(smartgrid.houses, smartgrid.batterys)
    i = 0
    all_scores = []
    while i < 100:
        random_greedy(smartgrid.houses, smartgrid.batterys)
        score = calculate_score(smartgrid.houses)
        all_scores.append(score)
        i += 1

    all_scores.sort()
    plt.plot(all_scores)
    plt.show()
    exit()


if __name__ == "__main__":
    main()
