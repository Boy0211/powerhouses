from battery import Battery
from house import House


def battery_sort_function(houses, batterys):

    for house in houses:
        if int(house.identification) % 5 == 1:
            batterys[0].list_of_houses.append(house)

        elif int(house.identification) % 5 == 2:
            batterys[1].list_of_houses.append(house)

        elif int(house.identification) % 5 == 3:
            batterys[2].list_of_houses.append(house)

        elif int(house.identification) % 5 == 4:
            batterys[3].list_of_houses.append(house)

        elif int(house.identification) % 5 == 0:
            batterys[4].list_of_houses.append(house)