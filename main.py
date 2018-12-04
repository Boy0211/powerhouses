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
from score import calculate_score
from visualization import grid
from randomHillclimber import random_hillclimber
from hillclimber import hill_climber
from new_score import new_score
from place_battery import k_means
from solution import Solution


def main():

    DataStructure = Smartgrid(1)
    Solution1 = Solution(DataStructure.houses, DataStructure.batterys)
    greedy_1(Solution1)

    for battery in Solution1.batterys:
        print(battery)
    print(Solution1)
    print(Solution1.costs)
    # DataStructuur exist of houses and batterys. The first algorithms are
    # on the concept that houses and batterys are placed. In the end only
    # houses are placed.

    # for battery in DataStructure.batterys:
    #     print(battery)
    # for house in DataStructure.houses:
    #     print(house)

    # print("---------------------")
    # print("SOLUTION 1:")
    # Solution_1 = greedy_1(DataStructure.houses, DataStructure.batterys)
    # # for battery in Solution_1:
    # #     print(battery)
    # grid(Solution_1)
    # new_score(Solution_1)
    #
    # print("---------------------")
    # print("SOLUTION 2:")
    # Solution_2 = greedy_2(DataStructure.houses, DataStructure.batterys)
    # # for battery in Solution_2:
    # #     print(battery)
    # grid(Solution_2)
    # new_score(Solution_2)
    #
    # print("---------------------")
    # print("SOLUTION 3:")
    # Solution_3 = random_hillclimber(Solution_1)
    # # for battery in Solution_3:
    # #     print(battery)
    # grid(Solution_3)
    # new_score(Solution_3)

    # print("---------------------")
    # print("SOLUTION 4:")
    # Solution_4 = random_hillclimber(Solution_2)
    # # for battery in Solution_4:
    # #     print(battery)
    # grid(Solution_4)
    # new_score(Solution_4)
    #
    # print("---------------------")
    # print("SOLUTION x1:")
    # Solution_x1 = hill_climber(Solution_1)
    # grid(Solution_x1)
    # new_score(Solution_x1)
    #
    # for battery in Solution_2:
    #     print(battery)
    #
    # print("---------------------")
    # print("SOLUTION x2:")
    # Solution_x2 = hill_climber(Solution_2)
    # grid(Solution_x2)
    # new_score(Solution_x2)
    #
    # exit()


if __name__ == "__main__":
    main()
