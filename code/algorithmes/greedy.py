from add_remove import add_house_to_battery


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
