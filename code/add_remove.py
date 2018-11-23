

def add_house_to_battery(house, battery):

    ''' Function used to add houses to batterys '''

    battery.list_of_houses.append(house)
    battery.current_input += (house.output)
    value = house.battery_distances[battery.identification]
    house.connected_battery = {"id":int(battery.identification), "distance":value}

def remove_house_from_battery(house, battery):

    ''' Function used to remove houses to batterys '''

    battery.list_of_houses.remove(house)
    battery.current_input -= (house.output)
    house.connected_battery = 'not connected'
