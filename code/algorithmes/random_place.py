'''
    File name: k_means.py
    Author: Mendel, Sam, Rutger
    Date created: 17/11/2018
    Date last modified: 17/12-2018
'''
import random

from helpers import add_house_to_battery as ad


def place_random(solution):

    '''Divide houses with k_means into 5 clusters and
    determine battery locations'''

    houses = solution.houses
    batterys = solution.batterys

    # assign random location to batterys
    for battery in batterys:
        battery.location_x = random.randint(0, 51)
        battery.location_x = random.randint(0, 51)

        # iterate through all houses
    for house in houses:
        place_battery = random.choice(batterys)
        ad(house, place_battery)

    solution.batterys = batterys

    return solution
