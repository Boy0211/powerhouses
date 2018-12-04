

def hillclimber(data_batterys):

    batterys = copy.deepcopy(data_batterys)

    while cap_exc(batterys) is not False:
        old_version = batterys



        print(batterys[0])
        distance_dict = {}
        while batterys[0].current_input > batterys[0].max_input:
            batterys[0].list_of_houses.sort(key=lambda x: x.output, reverse=True)

            temp_house = batterys[0].list_of_houses[0]
            rm(batterys[0].list_of_houses[0], batterys[0])

            for i in range(1, 5):
                # d1 = {batterys[i]:batterys[i](distance(temp_house, battery[i])}
                value = (distance(temp_house, batterys[i]))
                distance_dict.update({batterys[i]: value})

            while len(distance_dict) > 0:
                closest_battery = min(distance_dict, key=lambda k: distance_dict[k])
                if len(distance_dict) == 1:
                    ad(temp_house, closest_battery)
                    break
                elif temp_house.output + closest_battery.current_input <= closest_battery.max_input:
                    ad(temp_house, closest_battery)
                    break
                else:
                    del distance_dict[closest_battery]

            if old_


    batterys.sort(key=lambda x: x.identification, reverse=False)

    return batterys


def most_far_away_house(battery):


    for house in battery.list_of_houses:
        distance_to_current_battery = distance(house, battery)





        for battery_counter in range(1,5):
            x = distance(house, battery[battery_counter])

            if (distance_to_current_battery > x) and (house.output + batterys[battery_counter].current_input < batterys[battery_counter]):
                rm(house, batterys[0])
                ad(house, batterys[battery_counter])
                break
