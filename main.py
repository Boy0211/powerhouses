import os
import sys
import numpy as np

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithmes"))
sys.path.append(os.path.join(directory, "code", "classes"))

from random_greedy import random_distribution
from greedy import greedy_1
from smartGRID import Smartgrid
from score import calculate_score
from visualization import grid


def main():

    smartgrid = Smartgrid(1)
    # grid(smartgrid.houses, smartgrid.batterys)
    # greedy_1(smartgrid.houses, smartgrid.batterys)
    random_distribution(smartgrid.houses, smartgrid.batterys, 10000, 15)



    exit()


if __name__ == "__main__":
    main()
