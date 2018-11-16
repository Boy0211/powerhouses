from add_remove import add_house_to_battery
from sort import sort_distance

def greedy_1(houses, batterys):

    ''' Greedy algorithm that fills up the most empty battery'''

    # iterate through all houses
    house_counter = 0
    while house_counter < len(houses):
        bat_list = []

        # append all batteries in new list and choose battery with lowest
        # current input
        for battery in batterys:
            bat_list.append(battery.current_input)
        battery_counter = bat_list.index(min(bat_list))

        del(bat_list)

        # if a house fits into the battery with the lowest input, put this
        # house inside this battery. Otherwise were scruwed because we have
        # reached the max capacity of all batteries
        if batterys[battery_counter].current_input + houses[house_counter].output < 1507:
            add_house_to_battery(houses[house_counter], batterys[battery_counter])
        else:
            print("het past gewoon godverdomme niet!")
        house_counter += 1

def greedy_2(houses, batterys):
    ''' Greedy algorithm that fills up the most empty battery on a sorted list'''

    houses = sort_distance(houses)
    # for house in houses:
    #     print(house)
    # for battery in batterys:
    #     print(battery)
    # iterate through all houses
    house_counter = 0
    try_battery = 0
    while house_counter < len(houses):

        # sorteer lijst van batterijen per huis
        battery_list = (list(houses[house_counter].battery_distances.values()))
        battery_list = sorted(battery_list)
        print(houses[house_counter].battery_distances)

        # neem eerste waarde in deze lijst(is minimale waarde)
        print(f"try battery: {try_battery}")
        print(battery_list)
        current_battery = (battery_list[try_battery])

        # zoek key met bijbehorende afstand
        battery_number = (list(houses[house_counter].battery_distances.keys())[list(houses[house_counter].battery_distances.values()).index(current_battery)])
        print(f"battery number: {battery_number}")
        print(f"try battery: {try_battery}")

        if batterys[battery_number-1].current_input + houses[house_counter].output < 1507:
            add_house_to_battery(houses[house_counter], batterys[battery_number-1])
            print(houses[house_counter].battery_distances)


            house_counter += 1
            try_battery = 0
            for battery in batterys:
                print(battery)
        else:
            print("niet gelukt")
            print(try_battery)
            print(houses[house_counter].output)
            del houses[house_counter].battery_distances[battery_number]

    for battery in batterys:
        print(battery)
