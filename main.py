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
from solution import Solution
from place_battery_PPA import battery_based_plant_propagation_algorithm as BBPPA

def main():

    DataStructure = Smartgrid(1)

    time_start2 = time.time()
    Solutions = []
    for i in range(50):
        Solution_k = Solution(DataStructure.houses, DataStructure.batterys)
        k_means(Solution_k)
        Solutions.append(Solution_k)
        print("gelukt")
    for solution in Solutions:
        print(solution)
    Solution_ultimate = BBPPA(Solutions)
    grid(Solution_ultimate)
    time_end2 = time.time()

    hillclimber(Solution_ultimate)
    for battery in Solution_ultimate.batterys:
        print(battery)

    print(Solution_ultimate)
    print(f"running time: {time_end2 - time_start2}")



if __name__ == "__main__":
    main()
