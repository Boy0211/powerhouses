
def add_house_to_battery(house, battery):

    ''' Function used to add houses to batterys '''

    battery.list_of_houses.append(house)
    battery.current_input += (house.output)


def remove_house_from_battery(house, battery):

    ''' Function used to remove houses to batterys '''

    battery.list_of_houses.remove(house)
    battery.current_input -= (house.output)


def swap(house_a, house_b, battery_A, battery_B):

    '''A function used to swap two houses from one list to another.'''

    add_house_to_battery(house_a, battery_B)
    remove_house_from_battery(house_a, battery_A)
    add_house_to_battery(house_b, battery_A)
    remove_house_from_battery(house_b, battery_B)


def capacity(house1, house2, battery):

    '''function used to determine the whether a swap is possible within
        the capacity of the batterys.'''

    if (battery.current_input - house1.output + house2.output
       <= float(battery.max_input)):
        return True
    else:
        return False


def house_battery_distance(house, battery):

    ''' Function used to find the distance between house and battery '''

    x_distance = abs(house.location_x - battery.location_x)
    y_distance = abs(house.location_y - battery.location_y)
    distance = x_distance + y_distance

    return distance


def battery_capacity_exceeded(batterys):

    '''a method to determine whether a battery capacity is exceeded.'''

    for battery in batterys:
        if battery.current_input > float(battery.max_input) * 1.20:
            return battery
    return False
