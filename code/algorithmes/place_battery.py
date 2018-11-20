# 5 batterijen
# 51 * 51 mogelijke plaatsen: 2601
# 2601^5 mogelijke oplossingen: 1.19*e^17
# 1.19*e^17 - opties waarbij batterijen op zelfde plek staan
# dus maak algorithme dat alle mogelijkheden afgaat
from hillclimber import hill_climber
from score import calculate_score
from random_greedy import random_greedy
from datetime import datetime
import matplotlib.pyplot as plt
import itertools

def load_distances(houses, batterys):

    '''Function to determine the distances from every house to
       every battery '''

    # for every house determine the distance to all batterys
    for house in houses:
        battery_distances = {}

        # for every battery determine the absolute distance to every house
        for battery in batterys:
            x_distance = abs(house.location_x - battery.location_x)
            y_distance = abs(house.location_y - battery.location_y)
            distance = x_distance + y_distance
            battery_distances.update({battery.identification: distance})

        # save it into the house class
        house.battery_distances = battery_distances


def place_battery(houses, batterys):


    coordinates = list()
    for i in range(5):
        for j in range(5):
            # print(f"({i},{j})")

            coordinates.append((i, j))
    print(coordinates)
    for i in range(3):
        for j in range(3):
            print(coordinates[i])
            print(coordinates[j])

    # stuff = [1, 2, 3]
    # for L in range(0, len(stuff)+1):
    #     for subset in itertools.combinations(stuff, L):
    #         print(subset)
