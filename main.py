import os
import sys
import time
import copy

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithmes"))
sys.path.append(os.path.join(directory, "code", "classes"))

from place_battery_PPA import battery_based_plant_propagation_algorithm as BBPPA
from PPA import plant_propagation_algorithm as ppa
from random_greedy import random_distribution
from random_greedy import random_greedy
from greedy import greedy_1
from greedy import greedy_2
from smartGRID import Smartgrid
from visualization import grid
from randomHillclimber import random_hillclimber
from hillclimber import hillclimber
from place_battery import k_means
from solution import Solution
from copy_solution import copy_solution


def main():

    DataStructure = Smartgrid(1)


    # time_start1 = time.time()
    # Solution1 = Solution(DataStructure.houses, DataStructure.batterys)
    # Solution1 = random_greedy(Solution1)
    # Solution1 = ppa(Solution1, 30)
    # time_end1 = time.time()
    # print(f"running time 1: {(time_end1-time_start1)} seconds")
    # grid(Solution1)
    time_start2 = time.time()
    Solutions = []
    for i in range(50):
        Solution_k = Solution(DataStructure.houses, DataStructure.batterys)
        k_means(Solution_k)
        Solutions.append(Solution_k)
        print("hallo")
    for solution in Solutions:
        print(solution)
    Solution_ultimate = BBPPA(Solutions)
    time_end2 = time.time()

    grid(Solution_ultimate)
    print(f"running time 2: {(time_end2-time_start2)} seconds")



if __name__ == "__main__":
    main()
