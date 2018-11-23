import os
import sys
import numpy as np

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
from hillclimber import hill_climber
from hillclimber import hill_climber_2


def main():

<<<<<<< HEAD
    smartgrid = Smartgrid(3)
    greedy_1(smartgrid.houses, smartgrid.batterys)
    grid(smartgrid.houses, smartgrid.batterys)
    # i = 0
    # all_scores = []
    # time_stamp = datetime.now()
    # while i < 100:
    #     random_greedy(smartgrid.houses, smartgrid.batterys)
    #     score = calculate_score(smartgrid.houses)
    #     all_scores.append(score)
    #     i += 1
    #
    # print(datetime.now() - time_stamp)
    # all_scores.sort()
    # bins = 25
    # n,x,_ = plt.hist(all_scores, bins)
    # bin_centers = 0.5*(x[1:]+x[:-1])
    # plt.plot(bin_centers, n)
    # plt.show()
    # for battery in smartgrid.batterys:
    #     print(battery)
=======
    smartgrids = []
    for i in range(5):
        smartgrid = Smartgrid(1)
        smartgrids.append(smartgrid)
    # grid(smartgrid.houses, smartgrid.batterys)

    ### poging 1 + score ###
    print("Poging 1: capaciteit greedy + oude hill climber")
    # greedy gebasseerd op capaciteit gevolgd door een random hill_climber
    greedy_1(smartgrids[0].houses, smartgrids[0].batterys)
    hill_climber(smartgrids[0].houses, smartgrids[0].batterys)
    print(calculate_score(smartgrids[0].houses))
    print("-------------------------------------")

    ### poging 2 + score ###
    print("Poging 2: capaciteit greedy + nieuwe hill climber")
    # gebasseerd op capaciteit gevolgd door een best choice hill hill_climber
    greedy_1(smartgrids[1].houses, smartgrids[1].batterys)
    hill_climber_2(smartgrids[1].houses, smartgrids[1].batterys)
    print(calculate_score(smartgrids[1].houses))
    print("-------------------------------------")

    ### poging 3 + score ###
    print("Poging 3: distance greedy + oude hill climber")
    # gebasseerd op een distance greedy gevolg door random hill_climber
    greedy_2(smartgrids[2].houses, smartgrids[2].batterys)
    hill_climber(smartgrids[2].houses, smartgrids[2].batterys)
    print(calculate_score(smartgrids[2].houses))
    for battery in smartgrids[2].batterys:
        print(battery)
    print("-------------------------------------")

    ### poging 4 + score ###
    print("Poging 4: distance greedy + nieuwe hill climber ")
    # gebaseerd op een distance greedy gevolgd door een best choice hill climber
    greedy_2(smartgrids[3].houses, smartgrids[3].batterys)
    hill_climber_2(smartgrids[3].houses, smartgrids[3].batterys)
    print(calculate_score(smartgrids[3].houses))
    for battery in smartgrids[2].batterys:
        print(battery)
    print("-------------------------------------")

    ### poging 5 + score ###
    # print("Poging 5:")
    # # gebaseerd op een random algoritme gevolgd door een hill climber
    # random_distribution(smartgrids[4].houses, smartgrids[4].batterys, 100, 15)
    # print("-------------------------------------")

>>>>>>> 371470cb15d26cd06db9d1efb43a2617f1c66886
    exit()


if __name__ == "__main__":
    main()
