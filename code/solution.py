# import pandas as pd
# from scipy.spatial import distance_matrix
import copy

from helpers import house_battery_distance as distance
from helpers import battery_capacity_exceeded as cap_exc


class Solution(object):

    def __init__(self, houses, batterys):
        # self.algorithm = ## mehode om te bepalen welk algorithme gebruikt is
        self.houses = houses
        self.batterys = self.load_batterys(batterys)
        # self.distances = ## matrix tussen batterijen en huizen

    def __str__(self):
        return (f"algorithme: {self.score} \nCosts: {self.costs}\n")

    def load_batterys(self, batterys):

        batterys = copy.deepcopy(batterys)
        return batterys

    @property
    def costs(self):

        total_distance = []
        for battery in self.batterys:
            for house in battery.list_of_houses:
                total_distance.append(distance(house, battery))

        costs = (5000 * len(self.batterys)) + (9 * sum(total_distance))
        if cap_exc(self.batterys) is not False:
            costs = 0000

        return costs

    @property
    def score(self):

        # if self.algorithm is "k_means":
        #     return "non valid score calculation"
        # else:
        total_distance_min = 0
        total_distance_max = 0
        total_distance_connected = []
        for house in self.houses:
            distance_min = min(house.battery_distances.values())
            total_distance_min += distance_min
            distance_max = max(house.battery_distances.values())
            total_distance_max += distance_max

        for battery in self.batterys:
            for house in battery.list_of_houses:
                total_distance_connected.append(distance(house, battery))

        score = 1 - ((sum(total_distance_connected) - total_distance_min) / (total_distance_max - total_distance_min))

        return score

    # def distances_matrix(self, houses, batterys):
    #
    #     #  maken
