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






def main():
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    parser.add_argument("wijk",
                        type=int,
                        choices=[1, 2, 3],
                        help="kies het nummer van de wijk die je wilt analyseren")
    parser.add_argument("algorithm",
                        choices=['greedy', 'k_means', 'k_means_mendel'])
    parser.add_argument("-g", "--greedy_type",
                        const='greedy_1',
                        default='greedy_1',
                        nargs='?',
                        choices=["greedy_1", "greedy_2"],
                        help="choice the type of greedy")
    parser.add_argument("-a", "--additional",
                        const='hillclimber',
                        nargs='?',
                        choices=["hillclimber", "random_hillclimber"],
                        help="run een hillclimber/random_hillclimber op het resultaat van greedy/k_means")
    parser.add_argument("-ppa", "--plant_propagation",
                        action="store_true",
                        default=False,
                        help="run a plant prograpation algorithm on your hillclimber result")

    args = parser.parse_args()
    # if args.run_ppa:
    #     ppa = True
    # else:
    #     ppa = False
    print(args)
    if args.algorithm == "greedy" and args.additional is False:
        print(f"run greedy: {args.greedy_type}")
    elif args.algorithm == "greedy" and args.additional == "hillclimber":
        print(f"run greedy: {args.greedy_type} + hillclimber")

    elif args.algorithm == "greedy" and args.additional == "random_hillclimber":
        print(f"run greedy: {args.greedy_type} + random_hillclimber")

    if not args.additional and args.plant_propagation is True:
        print("plant_propagation zonder hillclimber, error")
    elif args.algorithm == "k_means" and args.plant_propagation is False and args.additional is False:
        print("k_means")
    elif args.algorithm == "k_means_mendel" and args.plant_propagation is False:
        print("k_means_mendel")
    elif args.algorithm == "k_means" and args.additional == "hillclimber":
        print("k_means + hillclimber")
    elif args.algorithm == "k_means" and args.plant_propagation is True:
        print("k_means + hillclimber + PPA")
    elif args.algorithm == "k_means_mendel" and args.additional == "hillclimber":
        print("k_means_mendel + hillclimber")
    elif args.algorithm == "k_means_mendel" and args.plant_propagation is True:
        print("k_means_mendel + hillclimber + PPA")


if __name__ == "__main__":
    main()
