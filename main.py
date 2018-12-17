import os
import argparse
import sys
import time

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithmes"))
sys.path.append(os.path.join(directory, "code", "classes"))

from greedy import greedy_1
from greedy import greedy_2
from solution import Solution
from smartGRID import Smartgrid
from visualization import grid
from random_greedy import random_distribution
from randomHillclimber import random_hillclimber
from hillclimber import hillclimber
from k_means import k_means
from k_means_2 import k_means as k_means_2
from solution import Solution
from place_battery_PPA import battery_based_plant_propagation_algorithm as BBPPA
from PPA import plant_propagation_algorithm as PPA


def main():
    parser = argparse.ArgumentParser(description="Smartgrid heuristieken: verbind huizen aan batterijen via een smartgrid")
    parser.add_argument("-wijk",
                        type=int,
                        default=1,
                        choices=[1, 2, 3],
                        help="kies het wijknummer dat je wilt analyseren")
    parser.add_argument("probleemset",
                        choices=["statisch", "dynamisch", "batterijen_toevoegen"],
                        help="kies de probleemset: statische batterijen, dynamische batterijen,"
                        " nieuwe batterijen toevoegen")
    parser.add_argument("algorithm",
                        choices=['greedy', 'k_means', 'k_means_2'],
                        help="kies het algoritme dat je wilt runnen")
    parser.add_argument("-g", "--greedy_type",
                        const='greedy_1',
                        default='greedy_1',
                        nargs='?',
                        choices=["greedy_1", "greedy_2"],
                        help="kies het type greedy")
    parser.add_argument("-a", "--additional",
                        const='hillclimber',
                        nargs='?',
                        choices=["hillclimber", "random_hillclimber"],
                        help="run een hillclimber/random_hillclimber op het resultaat van greedy/k_means")
    parser.add_argument("-ppa", "--plant_propagation",
                        action="store_true",
                        default=False,
                        help="run a plant prograpation algorithm on your hillclimber result")
    parser.add_argument("-i", "--iterations",
                        default=100,
                        help="choose the amount of iterations for ppa or random_hillclimber")
    parser.add_argument("-p", "--population",
                        default=30,
                        help="choose the population for ppa")

    args = parser.parse_args()
    print(args)
    DataStructure = Smartgrid(args.wijk)
    if args.probleemset == "statisch":
        if args.wijk == 2 or args.wijk == 3 and args.greedy_type == 'greedy_2':
            print("greedy_2 kan geen resultaat geven voor wijk 2 en 3 dat aan de constraints voldoet")
        elif (args.additional == "hillclimber" or args.additional == "random_hillclimber") and args.plant_propagation == True:
            print("het combineren van een hillclimber met een plant propagation algoritme is inefficient en daarom niet toegestaan")
        elif args.algorithm == "greedy" and args.additional == None and args.plant_propagation is False:
            if args.greedy_type == "greedy_1":
                print(f"run greedy: {args.greedy_type}")
                # greedy based on capacity
                Solution1 = Solution(DataStructure.houses, DataStructure.batterys)
                greedy_1(Solution1)
                print(Solution1)
                grid(Solution1)
            else:
                print(f"run greedy: {args.greedy_type}")
                # greedy based on capacity
                Solution1 = Solution(DataStructure.houses, DataStructure.batterys)
                greedy_2(Solution1)
                print(Solution1)
                grid(Solution1)
        elif args.algorithm == "greedy" and args.additional == "hillclimber" and args.plant_propagation is False:
            if args.greedy_type == "greedy_1":
                print(f"run greedy: {args.greedy_type} + hillclimber")
                # greedy based on capacity
                Solution1 = Solution(DataStructure.houses, DataStructure.batterys)
                greedy_1(Solution1)
                hillclimber(Solution1)
                print(Solution1)
                grid(Solution1)
            else:
                print(f"run greedy: {args.greedy_type} + hillclimber")
                # greedy based on capacity
                Solution1 = Solution(DataStructure.houses, DataStructure.batterys)
                greedy_2(Solution1)
                hillclimber(Solution1)
                print(Solution1)
                grid(Solution1)
                print(f"run greedy: {args.greedy_type} + hillclimber")
            # greedy based on capacity


        elif args.algorithm == "greedy" and args.additional == "random_hillclimber":
            if args.greedy_type == "greedy_1":
                print(f"run greedy: {args.greedy_type} + random_hillclimber")
                # greedy based on capacity
                Solution1 = Solution(DataStructure.houses, DataStructure.batterys)
                greedy_1(Solution1)
                random_distribution(Solution1, args.iterations, round(args.iterations/10))
                print(Solution1)
                grid(Solution1)
            else:
                print(f"run greedy: {args.greedy_type} + random_hillclimber")
                # greedy based on capacity
                Solution1 = Solution(DataStructure.houses, DataStructure.batterys)
                greedy_2(Solution1)
                random_distribution(Solution1, args.iterations, round(args.iterations/10))
                print(Solution1)
                grid(Solution1)
        elif args.algorithm == "greedy" and args.plant_propagation is True:
            print(f"run greedy: {args.greedy_type} + {args.additional} + ppa")
            if args.greedy_type == "greedy_1":
                time_start2 = time.time()
                Solutions = []
                for i in range(args.population):
                    Solution_k = Solution(DataStructure.houses, DataStructure.batterys)
                    greedy_1(Solution_k)
                    Solutions.append(Solution_k)
                for solution in Solutions:
                    print(solution)
                E = PPA(Solutions, args.iterations)
                print(E)
                grid(E)
                time_end2 = time.time()
            elif args.greedy_type == "greedy_2":
                time_start2 = time.time()
                Solutions = []
                for i in range(args.population):
                    Solution_k = Solution(DataStructure.houses, DataStructure.batterys)
                    greedy_2(Solution_k)
                    Solutions.append(Solution_k)
                for solution in Solutions:
                    print(solution)
                E = PPA(Solutions, args.iterations)
                print(E)
                grid(E)
                time_end2 = time.time()

    elif args.probleemset == "dynamisch":
        if args.wijk == 2 or args.wijk == 3 and args.greedy_type == 'greedy_2':
            print("greedy_2 kan geen resultaat geven voor wijk 2 en 3 dat aan de constraints voldoet")
        elif (args.additional == "hillclimber" or args.additional == "random_hillclimber") and args.plant_propagation == True:
            print("het combineren van een hillclimber met een plant propagation algoritme is inefficient en daarom niet toegestaan")
        elif args.algorithm == "k_means" and args.plant_propagation is False and args.additional is None:
            print("k_means")
            Solution2 = Solution(DataStructure.houses, DataStructure.batterys)
            k_means(Solution2)
            print(Solution2)
            grid(Solution2)
        elif args.algorithm == "k_means" and args.additional == "hillclimber" and args.plant_propagation == False:
            print("k_means + hillclimber")
            Solution2 = Solution(DataStructure.houses, DataStructure.batterys)
            k_means(Solution2)
            hillclimber(Solution2)
            print(Solution2)
            grid(Solution2)
        elif args.algorithm == "k_means" and args.additional == "random_hillclimber" and args.plant_propagation == False:
            print("k_means + random_hillclimber")
            Solution2 = Solution(DataStructure.houses, DataStructure.batterys)
            k_means(Solution2)
            random_distribution(Solution2, args.iterations, round(args.iterations/10))
            print(Solution2)
            grid(Solution2)
        elif args.algorithm == "k_means" and args.plant_propagation is True:
            print("k_means + PPA")
            time_start2 = time.time()
            Solutions = []
            for i in range(args.population):
                Solution_k = Solution(DataStructure.houses, DataStructure.batterys)
                k_means(Solution_k)
                Solutions.append(Solution_k)
            E = BBPPA(Solutions, args.iterations)
            print(E)
            grid(E)
            time_end2 = time.time()

    elif args.probleemset == "batterijen_toevoegen":
        if args.wijk == 2 or args.wijk == 3 and args.greedy_type == 'greedy_2':
            print("greedy_2 kan geen resultaat geven voor wijk 2 en 3 dat aan de constraints voldoet")
        elif (args.additional == "hillclimber" or args.additional == "random_hillclimber") and args.plant_propagation == True:
            print("het combineren van een hillclimber met een plant propagation algoritme is inefficient en daarom niet toegestaan")
        elif args.algorithm == "k_means_2" and args.plant_propagation is False and args.additional is None:
            print("k_means_2")
            Solution3 = Solution(DataStructure.houses, DataStructure.batterys)
            k_means_2(Solution3)
            print(Solution3)
            grid(Solution3)
        elif args.algorithm == "k_means_2" and args.additional == "hillclimber":
            print("k_means_2 + hillclimber")
            Solution5 = Solution(DataStructure.houses, DataStructure.batterys)
            k_means_2(Solution5)
            hillclimber(Solution5)
        elif args.algorithm == "k_means_2" and args.plant_propagation is True:
            print("k_means_2 + PPA")
            time_start2 = time.time()
            Solutions = []
            for i in range(args.population):
                Solution_k = Solution(DataStructure.houses, DataStructure.batterys)
                k_means_2(Solution_k)
                Solutions.append(Solution_k)
                print("nieuw k_means + Hillclimber resultaat")
            E = BBPPA(Solutions)
            print(E)
            grid(E)
            time_end2 = time.time()



if __name__ == "__main__":
    main()
