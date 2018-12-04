# 5 batterijen
# 51 * 51 mogelijke plaatsen: 2601
# 2601^5 mogelijke oplossingen: 1.19*e^17
# 1.19*e^17 - opties waarbij batterijen op zelfde plek staan
# dus maak algorithme dat alle mogelijkheden afgaat

from datetime import datetime
import matplotlib.pyplot as plt
import random
import copy
from helpers import add_house_to_battery

from numpy import mean
from visualization import grid


def calculate_score(x):
    # herschrijven ivm solution class
    x = 1
    x += 1

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
    for i in range(51):
        for j in range(51):
            # print(f"({i},{j})")

            coordinates.append((i, j))
    # print(len(coordinates))
    best_score = []
    best_distance = 3132
    count = 0
    distances = []
    i = 0
    all_scores = []
    time_stamp = datetime.now()
    for h in range(len(coordinates)):
        # print(f"battery 1: {coordinates[i]}")
        batterys[0].location_x = coordinates[h][0]
        batterys[0].location_y = coordinates[h][1]
        # print(batterys[0])
        load_distances(houses, batterys)
        # random_greedy(houses, batterys)
        min_distance = calculate_score(houses)
        distances.append(min_distance)
        count += 1
        print(count)

        if min_distance < best_distance:
            best_distance = min_distance
            best_score = batterys
            # print(batterys)

        for g in range(len(coordinates)):
            batterys[0].location_x = coordinates[g][0]
            batterys[0].location_y = coordinates[g][1]
            # print(batterys[0])
            load_distances(houses, batterys)
            # random_greedy(houses, batterys)
            min_distance = calculate_score(houses)
            distances.append(min_distance)
            if min_distance < best_distance:
                best_distance = min_distance
                best_score = batterys
                # print(batterys)
            count += 1
            print(count)
            for k in range(len(coordinates)):
                # print(f"battery 3: {coordinates[k]}")
                batterys[0].location_x = coordinates[k][0]
                batterys[0].location_y = coordinates[k][1]
                # print(batterys[0])
                load_distances(houses, batterys)
                # random_greedy(houses, batterys)
                min_distance = calculate_score(houses)
                distances.append(min_distance)
                if min_distance < best_distance:
                    best_distance = min_distance
                    best_score = batterys
                    # print(batterys)
                count += 1
                print(count)

                for l in range(len(coordinates)):
                    # print(f"battery 4: {coordinates[l]}")
                    batterys[0].location_x = coordinates[l][0]
                    batterys[0].location_y = coordinates[l][1]
                    # print(batterys[0])
                    load_distances(houses, batterys)
                    # random_greedy(houses, batterys)
                    min_distance = calculate_score(houses)
                    distances.append(min_distance)
                    if min_distance < best_distance:
                        best_distance = min_distance
                        best_score = batterys
                        # print(batterys)
                    count += 1
                    print(count)
                    for m in range(len(coordinates)):
                        # print(f"battery 5: {coordinates[m]}")
                        batterys[0].location_x = coordinates[m][0]
                        batterys[0].location_y = coordinates[m][1]
                        # print(batterys[0])
                        load_distances(houses, batterys)
                        # random_greedy(houses, batterys)
                        min_distance = calculate_score(houses)
                        distances.append(min_distance)
                        if min_distance < best_distance:
                            best_score = batterys
                            # print(batterys)
                        count += 1
                        print(count)

    # print(distances)
    for battery in best_score:
        print(battery)
    bins = 15
    print(datetime.now() - time_stamp)
    distances.sort()
    n,x,_ = plt.hist(distances, bins)
    bin_centers = 0.5*(x[1:]+x[:-1])
    plt.plot(bin_centers, n)
    plt.show()
    # print(count)
    # stuff = [1, 2, 3]
    # for L in range(0, len(stuff)+1):
    #     for subset in itertools.combinations(stuff, L):
    #         print(subset)

'''Verdeel huizen met greedy in 5 groepen met de korst mogelijke afstand'''
def k_means(houses, batterys):
    # 1. random x,y aanmaken voor batterijen
    # 2. afstand tot elk huis berekenen
    # 3. clusters vormen waarbij huizen die dichstbij staan in cluster worden gezet
    # 4. herhalen totdat clusters niet veranderen

    # for house in houses:
    #     print(house)

    # assign random location to batterys
    for battery in batterys:
        battery.location_x = random.randint(0, 51)
        battery.location_y = random.randint(0, 51)

    # load_distances(houses, batterys)

    # for battery in batterys:
    #     print(battery)

    # houses = sort_distance(houses)

    # iterate through all houses


    while True:
        total_change = 0
        for battery in batterys:
            battery.list_of_houses = []
            battery.current_input = 0
        temp_dict = dict()
        load_distances(houses, batterys)
        for house in houses:

            temp_dict = dict()
            temp_dict = copy.deepcopy(house.battery_distances)

            # sorteer lijst van batterijen per huis
            battery_list = (list(temp_dict.values()))
            battery_list = sorted(battery_list)

            # neem eerste waarde in deze lijst(is minimale waarde)
            current_battery = (battery_list[0])

            # zoek key met bijbehorende afstand
            battery_number = (list(temp_dict.keys())[list(temp_dict.values()).index(current_battery)])

            add_house_to_battery(house, batterys[battery_number-1])

        # grid(houses, batterys)

        for battery in batterys:
            x_coordinates = list()
            y_coordinates = list()
            for house in battery.list_of_houses:
                x_coordinates.append(house.location_x)
                y_coordinates.append(house.location_y)
            mean_x = round(mean(x_coordinates))
            mean_y = round(mean(y_coordinates))

            change_x = abs(battery.location_x - mean_x)
            change_y = abs(battery.location_y - mean_y)
            total_change += change_x + change_y
            battery.location_x = mean_x
            battery.location_y = mean_y

            # print(total_change)
        # print("----------------")
        if total_change < 1:
            break





        temp_batterys = copy.deepcopy(batterys)
        # grid(houses, batterys)
    return houses, batterys

def greedy_2(houses, batterys):
    ''' Greedy algorithm that fills up the most empty battery on a sorted list'''

    houses = sort_distance(houses)

    # iterate through all houses
    house_counter = 0
    temp_house_counter = 0
    temp_dict = dict()

    while house_counter < len(houses):

        # als house_counter toeneemt, sla battery_distances op in nieuwe lijst
        if temp_house_counter == house_counter:
            temp_dict = dict()
            temp_dict = copy.deepcopy(houses[house_counter].battery_distances)

        # sorteer lijst van batterijen per huis
        battery_list = (list(temp_dict.values()))
        battery_list = sorted(battery_list)

        # neem eerste waarde in deze lijst(is minimale waarde)
        current_battery = (battery_list[0])

        # zoek key met bijbehorende afstand
        battery_number = (list(temp_dict.keys())[list(temp_dict.values()).index(current_battery)])

        if batterys[battery_number-1].current_input + houses[house_counter].output <= float(batterys[battery_number-1].max_input) + 0.01 * float(batterys[battery_number-1].max_input):
            add_house_to_battery(houses[house_counter], batterys[battery_number-1])

            house_counter += 1
            temp_house_counter = house_counter
        else:
            temp_house_counter += 1
            del temp_dict[battery_number]
