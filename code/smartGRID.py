import csv
import heapq

from house import House
from battery import Battery
from sort import sort_function as sort


class Smartgrid(object):

    def __init__(self, district):

        # print the wijk which is worked with:
        print(f"This is wijk: {district}")

        # sort the given data, before further usage
        sort(f"data/csv_bestanden/wijk{district}_huizen.csv", district)

        # load both the houses and the batterys into the RAM
        self.houses = self.load_houses(f"data/csv_bestanden/sorted_houses{district}.csv")
        self.batterys = self.load_batterys(f"data/csv_bestanden/wijk{district}_batterijen.txt")
        self.load_distances()
        # self.load_distance_houses()


    def load_houses(self, filename):

        '''Function which is used to load the houses into the RAM'''

        # open the file
        with open(filename, 'r') as csv_file:
            data = csv.DictReader(csv_file)
            houses = []
            id_number = 1

            # append all the data into the class house
            for line in data:
                identification = id_number
                location_x = int(line['x'])
                location_y = int(line['y'])
                output = float(line['max. output'])
                battery_distances = str('empty')
                connected_battery = 'not connected'
                distance_houses = str('empty')
                houses.append(House(identification, location_x, location_y, output, battery_distances, connected_battery))
                id_number += 1

            # return the houses
            return houses

    def load_batterys(self, filename):

        '''Function which is used to load the houses into the RAM'''

        # open the data file
        with open(filename, "r") as f:
            data = f.readlines()
            del(data[0])
            id_number = 1
            batterys = []

            # for every line in the data append certain data to the battery class
            for line in data:
                identification = id_number
                location, max_input = line.split('\t', 1)
                max_input = max_input.strip()
                location = location.replace("[", "")
                location = location.replace("]", "")
                location_x, location_y = location.split(",", 1)
                location_x = int(location_x)
                location_y = int(location_y.strip())
                current_input = 0
                list_of_houses = []
                batterys.append(Battery(identification, location_x, location_y, max_input, current_input, list_of_houses))
                id_number += 1

        # return the batterys
        return batterys

    def load_distances(self):

        '''Function to determine the distances from every house to
           every battery '''

        # for every house determine the distance to all batterys
        for house in self.houses:
            battery_distances = {}

            # for every battery determine the absolute distance to every house
            for battery in self.batterys:
                x_distance = abs(house.location_x - battery.location_x)
                y_distance = abs(house.location_y - battery.location_y)
                distance = x_distance + y_distance
                battery_distances.update({battery.identification: distance})

            # save it into the house class
            house.battery_distances = battery_distances

    def load_distance_houses(self):
        for house in self.houses:
            house_list = []
            x_1 = house.location_x
            y_1 = house.location_y
            for house_1 in self.houses:

                x_2 = house_1.location_x
                y_2 = house_1.location_y

                x_distance = abs(x_1 - x_2)
                y_distance = abs(y_1 - y_2)
                distance = x_distance + y_distance
                house_list.append(distance)
            house.distance_houses = house_list
