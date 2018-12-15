from scipy.spatial.distance import cdist
import copy
import pandas as pd

from helpers import house_battery_distance as distance


class Solution(object):

    '''Class created which represents a solution. All the information needed
    for the algorithm is saved in either instances or propertys'''

    # init with 2 instances, which represents the other 2 classes
    def __init__(self, houses, batterys):
        self.houses = houses
        self.batterys = self.load_batterys(batterys)

    # return function for when a solution is printed
    def __str__(self):
        return (f"Score: {self.score}\nCosts: {self.costs}\n")

    # when a solution is created, the batterys are deepcopied.
    def load_batterys(self, batterys):

        batterys = copy.deepcopy(batterys)
        return batterys

    @property
    def costs(self):

        # count all the battery costs
        total_battery_costs = 0
        for battery in self.batterys:
            total_battery_costs += battery.battery_costs

        # return the battery costs
        return total_battery_costs

    @property
    def score(self):

        # start both distance calculations at zero
        total_distance_min = 0
        total_distance_max = 0
        total_distance_connected = 0

        # for every house calculate the distance to the connected battery
        for battery in self.batterys:
            for house in battery.list_of_houses:
                total_distance_connected += (distance(house, battery))

        # do the same for the max and min distance
        # this can be calculated using the df self.distances
        total_distance_min = sum(self.distances["min_value"])
        total_distance_max = sum(self.distances["max_value"])

        # the distance score is calculated using the variables created above
        distance_score = 1 - ((total_distance_connected - total_distance_min) /
                              (total_distance_max - total_distance_min))

        # secondary the capacity score is calculated
        total_capacity_exceeded = 0
        for battery in self.batterys:
            if battery.current_input < battery.max_input:
                capacity_exceeded = 0
            else:
                capacity_exceeded = battery.current_input - battery.max_input
            total_capacity_exceeded += capacity_exceeded

        # and third a under range score is calculated when an battery is
        # far too empty
        capacity_under_range = 0
        for battery in self.batterys:
            if battery.current_input < battery.max_input * 0.80:
                capacity_under_range += 0.2
            else:
                capacity_under_range += 0.0

        # finally all the scores are definied in one number
        max_exceeded = 6000
        battery_score = (20*total_capacity_exceeded / max_exceeded)
        score = distance_score - battery_score - capacity_under_range

        # return the score
        return score

    @property
    def distances(self):

        # create two empty lists
        battery_ids = []
        battery_coordinates = []

        # for every battery in in the list of batterys
        for battery in self.batterys:

            # save the identification and the coordinates
            battery_ids.append(battery.identification)
            battery_coordinates.append([battery.location_x,
                                        battery.location_y])

        # do the same for the houses; 2 lists
        house_ids = []
        house_coordinates = []

        # for every house in the list of houses
        for house in self.houses:

            # save the identification and the coordinates of the houses
            house_ids.append(house.identification)
            house_coordinates.append([house.location_x, house.location_y])

        # create a df with the variables from above
        df_batterys = pd.DataFrame(battery_coordinates,
                                   columns=['xcord', 'ycord'],
                                   index=battery_ids)
        df_houses = pd.DataFrame(house_coordinates, columns=['xcord', 'ycord'],
                                 index=house_ids)
        df = pd.DataFrame(cdist(df_houses.values, df_batterys.values,
                                metric='cityblock'),
                          index=df_houses.index, columns=df_batterys.index)

        # add extra information in the dataframe
        df['max_value'] = df.max(axis=1)
        df['min_value'] = df.min(axis=1)
        df['closest_house'] = df.idxmin(axis=1)

        # return the df
        return df
