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
    Solution = Solution(DataStructure.houses, DataStructure.batterys)

    # greedy based on capacity
    Solution1 = Solution(DataStructure.houses, DataStructure.batterys)
    A = greedy_1(Solution1)

    # hillclimber on greedy_1 results
    B = hillclimber(Solution1)

    # greedy based on distance
    Solution2 = Solution(DataStructure.houses, DataStructure.batterys)
    C = greedy_2(Solution2)

    # hillclimber on greedy_2 results
    D = hillclimber(Solution2)

    # replacing batterys with k-means and plant propagation (PPA)
    time_start2 = time.time()
    Solutions = []
    for i in range(50):
        Solution_k = Solution(DataStructure.houses, DataStructure.batterys)
        k_means(Solution_k)
        Solutions.append(Solution_k)
        print("gelukt")
    for solution in Solutions:
        print(solution)
    E = BBPPA(Solutions)
    time_end2 = time.time()

    print("score van greedy_capacity:                 {}\n"
      "score van greedy_distance:                     {}\n"
      "score van greedy_distance + hillclimber:       {}\n"
      "score van greedy_capacity:                     {}\n"
      "score van greedy_capacity + hillclimber:       {}\n"
      "verplaatsen batterijen met k_means + PPA:      {}\n".format(
    score(A), score(B), score(C), score(D), score(E)
    ))


    # print(f"running time: {time_end2 - time_start2}")



if __name__ == "__main__":
    main()
