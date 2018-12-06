# import pandas as pd
from scipy.spatial.distance import cdist
import copy
import pandas as pd

from helpers import house_battery_distance as distance
from helpers import battery_capacity_exceeded as cap_exc


class Solution(object):

    def __init__(self, houses, batterys):
        # self.algorithm = ## mehode om te bepalen welk algorithme gebruikt is
        self.houses = houses
        self.batterys = self.load_batterys(batterys)

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

        total_distance_connected = 0

        for battery in self.batterys:
            for house in battery.list_of_houses:
                total_distance_connected += (distance(house, battery))

        total_distance_min = sum(self.distances["min_value"])
        total_distance_max = sum(self.distances["max_value"])

        score = 1 - ((total_distance_connected - total_distance_min) / (total_distance_max - total_distance_min))

        return score

    @property
    def distances(self):

        battery_ids = []
        battery_coordinates = []

        for battery in self.batterys:
            battery_ids.append(battery.identification)
            battery_coordinates.append([battery.location_x, battery.location_y])

        house_ids = []
        house_coordinates = []

        for house in self.houses:
            house_ids.append(house.identification)
            house_coordinates.append([house.location_x, house.location_y])

        df_batterys = pd.DataFrame(battery_coordinates, columns=['xcord', 'ycord'], index=battery_ids)
        df_houses = pd.DataFrame(house_coordinates, columns=['xcord', 'ycord'], index=house_ids)
        df = pd.DataFrame(cdist(df_houses.values, df_batterys.values, metric='cityblock'), index=df_houses.index, columns=df_batterys.index)
        df['max_value'] = df.max(axis=1)
        df['min_value'] = df.min(axis=1)
        df['closest_house'] = df.idxmin(axis=1)


        return df
