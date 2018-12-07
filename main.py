import os
import sys

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
from place_battery import k_means
from solution import Solution


def main():

    DataStructure = Smartgrid(1)

    Solution1 = Solution(DataStructure.houses, DataStructure.batterys)
    # k_means(Solution1)
    # print(Solution1)
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



if __name__ == "__main__":
    main()
