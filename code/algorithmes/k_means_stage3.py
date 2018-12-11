import random
import copy

from helpers import add_house_to_battery as ad
from visualization import grid
from helpers import battery_capacity_exceeded as cap_exc



def k_means_stage3(solution):

    '''Verdeel huizen met greedy in 5 groepen met de korst mogelijke afstand'''
    # 1. random x,y aanmaken voor batterijen
    # 2. afstand tot elk huis berekenen
    # 3. clusters vormen waarbij huizen die dichstbij staan in cluster worden gezet
    # 4. herhalen totdat clusters niet veranderen

    houses = solution.houses
    batterys = solution.batterys
    for battery in batterys:
        battery.max_input = 1800

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

        x = 0
        # iterate through all houses
        while True:
            total_change = 0
            # counter = 0
            for battery in batterys:
                # counter += 1
                # print(counter)
                battery.list_of_houses = []
                battery.current_input = 0

            temp_df = solution.distances
            # print(solution.distances)
            # print(temp_df)
            counter = 1
            for house in houses:
                ad(house, batterys[(temp_df['closest_house'][counter]) - 1])
                counter += 1

            for battery in batterys:
                x_coordinates = list()
                y_coordinates = list()
                for house in battery.list_of_houses:
                    x_coordinates.append(house.location_x)
                    y_coordinates.append(house.location_y)
                if len(x_coordinates) == 0 or len(y_coordinates) == 0:
                    x_coordinates = [1]
                    y_coordinates = [1]
                mean_x = round(sum(x_coordinates)/len(x_coordinates))
                mean_y = round(sum(y_coordinates)/len(y_coordinates))

                change_x = abs(battery.location_x - mean_x)
                change_y = abs(battery.location_y - mean_y)
                total_change += change_x + change_y
                battery.location_x = mean_x
                battery.location_y = mean_y
            print(f"{x} vs {solution}")

            # solution.batterys = batterys
            grid(solution)
            for battery in batterys:
                print(battery)

            x = copy.deepcopy(solution)
            bat = battery_chosen_for_split(batterys)
            bat_new = split_battery(bat, batterys)
            solution.batterys.append(bat_new)
            grid(solution)

            # print(total_change)
            if total_change < 1:
                break

        if cap_exc(batterys) is False:
            break
        # if solution.score > 0.6:
        #     print("gelukt")
        #     for battery in batterys:
        #         print(battery)
        #     break
    return solution


def battery_chosen_for_split(batterys):

    score = 0
    for battery in batterys:
        if battery.distance_costs > score:
            score = battery.distance_costs
            bat1 = battery

    return bat1


def split_battery(battery_old, batterys):

    battery_new = copy.deepcopy(battery_old)

    battery_new.identification = len(batterys) + 1

    battery_old.max_input = (1/2) * battery_old.max_input
    battery_new.max_input = (1/2) * battery_new.max_input

    battery_new.location_x = battery_old.location_x + 1

    return battery_new
