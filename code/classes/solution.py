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
        return (f"Score: {self.score}\nCosts: {self.costs}\n")

    def load_batterys(self, batterys):

        batterys = copy.deepcopy(batterys)
        return batterys

    @property
    def costs(self):

        total_battery_costs = 0
        for battery in self.batterys:
            total_battery_costs += battery.battery_costs

        return total_battery_costs

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

        distance_score = 1 - ((total_distance_connected - total_distance_min) /
                              (total_distance_max - total_distance_min))

        # capacity score
        total_capacity_exceeded = 0
        for battery in self.batterys:
            if battery.current_input < battery.max_input:
                capacity_exceeded = 0
            else:
                capacity_exceeded = battery.current_input - battery.max_input
            total_capacity_exceeded += capacity_exceeded

        capacity_under_range = 0
        for battery in self.batterys:
            if battery.current_input < battery.max_input * 0.80:
                capacity_under_range += 0.2
            else:
                capacity_under_range += 0.0


        max_exceeded = 6000
        battery_score = (20*total_capacity_exceeded / max_exceeded)
        score = distance_score - battery_score - capacity_under_range

        # print(f"distance score = {distance_score}")
        # print(f"battery score = {battery_score}")
        # print(f"capacity under range score = {capacity_under_range}")

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
