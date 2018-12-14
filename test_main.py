import os
import sys
import time
import copy

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
# from k_means import k_means
from k_means_mendel import k_means
from solution import Solution
from place_battery_PPA import battery_based_plant_propagation_algorithm as BBPPA
from k_means_stage3 import k_means_stage3


def main():

    DataStructure = Smartgrid(3)
    x = Solution(DataStructure.houses, DataStructure.batterys)

    time_start2 = time.time()

    solutions = []
    for i in range(30):
        solution = k_means_stage3(copy.deepcopy(x))
        solutions.append(solution)
        print("hihaho")

    y = BBPPA(solutions)
    time_end2 = time.time()

    print(y)
    print(f"running time: {time_end2 - time_start2}")
    grid(y)



if __name__ == "__main__":
    main()
