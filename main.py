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
    print(Solution1.score)
    # k_means(Solution1)
    # print(Solution1)
    # grid(Solution1)
    # print(Solution1.distances)
    Solution1 = greedy_1(Solution1)
    print(Solution1.batterys)
    grid(Solution1)
    # hillclimber(Solution2)
    # grid(Solution2)

    # Solution3 = Solution(DataStructure.houses, DataStructure.batterys)
    # k_means(Solution3)
    # grid(Solution3)

    # print(Solution3)
    print(Solution1.distances)
    # print(Solution2.distances)


if __name__ == "__main__":
    main()
