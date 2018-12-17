'''
    File name: k_means.py
    Author: Mendel, Sam, Rutger
    Date created: 17/11/2018
    Date last modified: 17/12-2018
'''

import random
from helpers import add_house_to_battery as ad
from helpers import battery_capacity_exceeded as cap_exc


def k_means(solution):

    '''Divide houses with k_means into 5 clusters and determine battery locations'''

    houses = solution.houses
    batterys = solution.batterys

    # as long as a capacity of a battery is exceeded
    while True:

        # assign random location to batterys
        batterys[0].location_x = random.randint(26, 51)
        batterys[0].location_x = random.randint(26, 51)

        batterys[1].location_x = random.randint(0, 26)
        batterys[1].location_y = random.randint(26, 51)

        batterys[2].location_x = random.randint(26, 51)
        batterys[2].location_y = random.randint(0, 26)

        batterys[3].location_x = random.randint(0, 26)
        batterys[3].location_y = random.randint(0, 26)

        batterys[4].location_x = random.randint(17, 33)
        batterys[4].location_y = random.randint(17, 33)


        # iterate through all houses
        while True:
            total_change = 0

            # empty list of houses and current input in every battery
            for battery in batterys:
                battery.list_of_houses = []
                battery.current_input = 0


            temp_df = solution.distances

            # go through all houses and select the closest battery
            counter = 1
            for house in houses:
                ad(house, batterys[(temp_df['closest_house'][counter]) - 1])
                counter += 1

            # go through each battery and calculate the mean position of all
            # houses present in that battery
            for battery in batterys:
                x_coordinates = list()
                y_coordinates = list()
                for house in battery.list_of_houses:
                    x_coordinates.append(house.location_x)
                    y_coordinates.append(house.location_y)

                # if no house is connect to a battery, fill it temporary
                if len(x_coordinates) == 0 or len(y_coordinates) == 0:
                    x_coordinates = [1]
                    y_coordinates = [1]
                mean_x = round(sum(x_coordinates)/len(x_coordinates))
                mean_y = round(sum(y_coordinates)/len(y_coordinates))

                # calculate the total changed distance for all batterys
                change_x = abs(battery.location_x - mean_x)
                change_y = abs(battery.location_y - mean_y)
                total_change += change_x + change_y

                # change battery location to mean values
                battery.location_x = mean_x
                battery.location_y = mean_y

            # if battery locations have not been changed check if battery
            # capacity is still exceeded
            if total_change < 1:
                break

        # if the capacity of the batterys is not exceeded, stop algorithm
        if cap_exc(batterys) is False:
            break

    return solution
