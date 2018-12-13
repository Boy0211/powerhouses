import os
import sys
import time

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithmes"))
sys.path.append(os.path.join(directory, "code", "classes"))

from random_greedy import random_distribution
from greedy import greedy_1
from greedy import greedy_2
from smartGRID import Smartgrid
from visualization import grid
from randomHillclimber import random_hillclimber
from hillclimber import hillclimber
from k_means import k_means
from k_means_stage3 import k_means_stage3
from solution import Solution
from place_battery_PPA import battery_based_plant_propagation_algorithm as BBPPA


def main():

    DataStructure = Smartgrid(1)
    x = Solution(DataStructure.houses, DataStructure.batterys)

    time_start2 = time.time()

    Solution_fixed = k_means_stage3(x)

    time_end2 = time.time()

    print(Solution_fixed)
    print(f"running time: {time_end2 - time_start2}")



if __name__ == "__main__":
    main()
