# 5 batterijen
# 51 * 51 mogelijke plaatsen: 2601
# 2601^5 mogelijke oplossingen: 1.19*e^17
# 1.19*e^17 - opties waarbij batterijen op zelfde plek staan
# dus maak algorithme dat alle mogelijkheden afgaat

from datetime import datetime
import matplotlib.pyplot as plt
import random
import copy
from battery import Battery
from helpers import add_house_to_battery as ad
from helpers import battery_capacity_exceeded as cap_exc
from helpers import house_battery_distance

# from numpy import mean
from visualization import grid


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


# def place_battery(houses, batterys):
#
#     coordinates = list()
#     for i in range(51):
#         for j in range(51):
#             # print(f"({i},{j})")
#
#             coordinates.append((i, j))
#     # print(len(coordinates))
#     best_score = []
#     best_distance = 3132
#     count = 0
#     distances = []
#     i = 0
#     all_scores = []
#     time_stamp = datetime.now()
#     for h in range(len(coordinates)):
#         # print(f"battery 1: {coordinates[i]}")
#         batterys[0].location_x = coordinates[h][0]
#         batterys[0].location_y = coordinates[h][1]
#         # print(batterys[0])
#         load_distances(houses, batterys)
#         # random_greedy(houses, batterys)
#         min_distance = 8 ## calculate_score(houses)
#         distances.append(min_distance)
#         count += 1
#         print(count)
#
#         if min_distance < best_distance:
#             best_distance = min_distance
#             best_score = batterys
#             # print(batterys)
#
#         for g in range(len(coordinates)):
#             batterys[0].location_x = coordinates[g][0]
#             batterys[0].location_y = coordinates[g][1]
#             # print(batterys[0])
#             load_distances(houses, batterys)
#             # random_greedy(houses, batterys)
#             min_distance = calculate_score(houses)
#             distances.append(min_distance)
#             if min_distance < best_distance:
#                 best_distance = min_distance
#                 best_score = batterys
#                 # print(batterys)
#             count += 1
#             print(count)
#             for k in range(len(coordinates)):
#                 # print(f"battery 3: {coordinates[k]}")
#                 batterys[0].location_x = coordinates[k][0]
#                 batterys[0].location_y = coordinates[k][1]
#                 # print(batterys[0])
#                 load_distances(houses, batterys)
#                 # random_greedy(houses, batterys)
#                 min_distance = calculate_score(houses)
#                 distances.append(min_distance)
#                 if min_distance < best_distance:
#                     best_distance = min_distance
#                     best_score = batterys
#                     # print(batterys)
#                 count += 1
#                 print(count)
#
#                 for l in range(len(coordinates)):
#                     # print(f"battery 4: {coordinates[l]}")
#                     batterys[0].location_x = coordinates[l][0]
#                     batterys[0].location_y = coordinates[l][1]
#                     # print(batterys[0])
#                     load_distances(houses, batterys)
#                     # random_greedy(houses, batterys)
#                     min_distance = calculate_score(houses)
#                     distances.append(min_distance)
#                     if min_distance < best_distance:
#                         best_distance = min_distance
#                         best_score = batterys
#                         # print(batterys)
#                     count += 1
#                     print(count)
#                     for m in range(len(coordinates)):
#                         # print(f"battery 5: {coordinates[m]}")
#                         batterys[0].location_x = coordinates[m][0]
#                         batterys[0].location_y = coordinates[m][1]
#                         # print(batterys[0])
#                         load_distances(houses, batterys)
#                         # random_greedy(houses, batterys)
#                         min_distance = calculate_score(houses)
#                         distances.append(min_distance)
#                         if min_distance < best_distance:
#                             best_score = batterys
#                             # print(batterys)
#                         count += 1
#                         print(count)
#
#     # print(distances)
#     for battery in best_score:
#         print(battery)
#     bins = 15
#     print(datetime.now() - time_stamp)
#     distances.sort()
#     n,x,_ = plt.hist(distances, bins)
#     bin_centers = 0.5*(x[1:]+x[:-1])
#     plt.plot(bin_centers, n)
#     plt.show()
#     # print(count)
#     # stuff = [1, 2, 3]
#     # for L in range(0, len(stuff)+1):
#     #     for subset in itertools.combinations(stuff, L):
#     #         print(subset)


def k_means(solution):

    '''Verdeel huizen met greedy in 5 groepen met de korst mogelijke afstand'''
    # 1. random x,y aanmaken voor batterijen
    # 2. afstand tot elk huis berekenen
    # 3. clusters vormen waarbij huizen die dichstbij staan in cluster worden gezet
    # 4. herhalen totdat clusters niet veranderen

    houses = solution.houses
    batterys = solution.batterys

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
            # counter = 0
            for battery in batterys:
                # counter += 1
                # print(counter)
                battery.list_of_houses = []
                battery.current_input = 0

            temp_df = solution.distances
            # print(solution.distances)

            counter = 1
            for house in houses:
                ad(house, batterys[(temp_df['closest_house'][counter]) - 1])
                counter += 1
            grid(solution)
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
                # grid(solution)
                battery.location_x = mean_x
                battery.location_y = mean_y
            grid(solution)
            print(total_change)
            if total_change < 1:
                break

        # solution.batterys = batterys

        for battery in batterys:
            print(battery)
        # merge_battery1, merge_battery2 = search_best_merge(batterys)
        # battery_new = merge_batterys(merge_battery1, merge_battery2)
        # print(merge_battery1)
        # batterys.remove(merge_battery1)
        # print(merge_battery2)
        # batterys.remove(merge_battery2)
        # batterys.append(battery_new)
        # for battery in batterys:
        #     print(battery)
        # grid(solution)


        if cap_exc(batterys) is False:
            break
        # if solution.score > 0.6:
        #     print("gelukt")
        #     for battery in batterys:
        #         print(battery)
        #     break
    return solution


    # solution.batterys = []
    # for i in range(17):
    #     identification = i + 1
    #     location_x = random.randint(0, 51)
    #     location_y = random.randint(0, 51)
    #     max_input = 450
    #     current_input = 0
    #     list_of_houses = []
    #     solution.batterys.append(Battery(identification, location_x, location_y, max_input, current_input, list_of_houses))


# def search_best_merge(batterys):
#
#     score_merge = 0.0
#     merge_battery1 = "none"
#     merge_battery2 = "none"
#     for i in range(len(batterys)):
#         battery1 = batterys[i]
#         for j in range(len(batterys)):
#             battery2 = batterys[j]
#
#             if battery2 == battery1:
#                 battery2 = batterys[(j + 1) % len(batterys)]
#
#             total_costs_before = battery1.battery_costs + battery2.battery_costs
#             print('-----')
#             # print(total_costs_before)
#
#             coordinate_x = round((battery1.location_x + battery2.location_x)/2)
#             coordinate_y = round((battery1.location_y + battery2.location_y)/2)
#
#             # print(f"{battery1.location_x}, {coordinate_x}, {battery2.location_x}")
#
#             temp_ds = 0
#             for house in battery1.list_of_houses:
#                 temp_ds += abs(coordinate_x - house.location_x)
#                 temp_ds += abs(coordinate_y - house.location_y)
#             for house in battery2.list_of_houses:
#                 temp_ds += abs(coordinate_x - house.location_x)
#                 temp_ds += abs(coordinate_y - house.location_y)
#
#             total_costs_after = temp_ds * 9 + 1350
#             # print(f'x{battery1.battery_type_costs}')
#             # print(total_costs_after)
#
#             if total_costs_before - total_costs_after > score_merge:
#                 merge_battery1 = battery1
#                 merge_battery2 = battery2
#                 print(merge_battery1)
#                 print(merge_battery2)
#
#     return merge_battery1, merge_battery2
#
#
# def merge_batterys(battery1, battery2):
#
#     identification = f"[{battery1.identification}_{battery2.identification}]"
#     location_x = round((battery1.location_x + battery2.location_x)/2)
#     location_y = round((battery1.location_y + battery2.location_y)/2)
#     max_input = battery1.max_input + battery2.max_input
#     current_input = 0
#     list_of_houses = []
#     battery_new = Battery(identification, location_x, location_y, max_input, current_input, list_of_houses)
#
#     for house in battery1.list_of_houses:
#         ad(house, battery_new)
#     for house in battery2.list_of_houses:
#         ad(house, battery_new)
#
#     return battery_new
