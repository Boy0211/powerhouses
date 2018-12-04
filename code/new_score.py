from helpers import house_battery_distance as distance
from helpers import battery_capacity_exceeded as cap_exc

def new_score(solution):

    total_distance = []
    for battery in solution:
        for house in battery.list_of_houses:
            total_distance.append(distance(house, battery))

    score = (5000 * len(solution)) + (9 * sum(total_distance))

    if cap_exc is False:
        print("non valid solution")
    else:
        print(score)
