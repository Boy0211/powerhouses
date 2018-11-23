

def calculate_distance(house):

    '''Function used to calculate the actual distance to the connected
       battery '''

    distance = house.connected_battery["distance"]
    return distance

def calculate_score(houses):

    '''Function used to calculate results based on distance'''

    total_distance_min = 0
    for house in houses:
        distance_min = min(house.battery_distances.values())
        total_distance_min += distance_min
    # print(f"minimal distance: {total_distance_min}")

    total_distance_connected = 0
    for house in houses:
        distance = calculate_distance(house)
        total_distance_connected += distance
    # print(f"connected distance: {total_distance_connected}")

    total_distance_max = 0
    for house in houses:
        distance_max = max(house.battery_distances.values())
        total_distance_max += distance_max
    # print(f"maximal distance: {total_distance_max}")

    costs = (total_distance_connected * 9)  + 25000
    print(f"total costs: {costs}")

    costs_min = (total_distance_min * 9)  + 25000
    print(f"total min costs: {costs_min}")

    costs_max = (total_distance_max * 9)  + 25000
    print(f"total max costs: {costs_max}")
    score = 1 - ((total_distance_connected - total_distance_min) / (total_distance_max - total_distance_min))
    return score

def calculate_perfect(self):

    '''Function used to calculate how many houses are connected to the
       best option'''

    counter_first = 0
    counter_second = 0
    counter_third = 0
    counter_forth = 0
    counter_five = 0

    for house in self.houses:

        temp_sorted = (heapq.nsmallest(5, house.battery_distances.values()))

        if house.battery_distances[int(house.connected_battery)] == temp_sorted[0]:
            counter_first += 1
        elif house.battery_distances[int(house.connected_battery)] == temp_sorted[1]:
            counter_second += 1
        elif house.battery_distances[int(house.connected_battery)] == temp_sorted[2]:
            counter_third += 1
        elif house.battery_distances[int(house.connected_battery)] == temp_sorted[3]:
            counter_forth += 1
        elif house.battery_distances[int(house.connected_battery)] == temp_sorted[4]:
            counter_five += 1

    percentage_first = (counter_first / 150) * 100
    # print(f"percentage best connected houses: {round(percentage_first, 2)}%")

    percentage_second = (counter_second / 150) * 100
    # print(f"percentage second best connected houses: {round(percentage_second, 2)}%")

    percentage_third = (counter_third / 150) * 100
    # print(f"percentage third best connected houses: {round(percentage_third, 2)}%")

    percentage_forth = (counter_forth / 150) * 100
    # print(f"percentage fourth best connected houses: {round(percentage_forth, 2)}%")

    percentage_five = (counter_five / 150) * 100
    # print(f"percentage worst connected houses: {round(percentage_five, 2)}%")
    return(percentage_first)
