import csv

from house import House
from battery import Battery
from sort import sort_function as sort


class Smartgrid():

    def __init__(self):
        sort(f"data/csv_bestanden/wijk1_huizen.csv")
        self.houses = self.load_houses(f"../data/csv_bestanden/sorted_houses.csv")
        self.batterys = self.load_batterys(f"../data/csv_bestanden/wijk1_batterijen.txt")
        self.calculate_distance()
        self.battery_sort_function()
        for battery in self.batterys:
            output_list = []
            for house in battery.list_of_houses:
                output_list.append(house.output)
            battery.current_input = sum(output_list)
            print(battery)


    def load_houses(self, filename):

        with open(filename, 'r') as csv_file:
            data = csv.DictReader(csv_file)
            houses = []
            id_number = 1

            for line in data:
                identification = id_number
                location_x = int(line['x'])
                location_y = int(line['y'])
                output = float(line['max. output'])
                battery_distances = str('empty')
                houses.append(House(identification, location_x, location_y, output, battery_distances))
                id_number += 1

            return houses

    def load_batterys(self, filename):

        with open(filename, "r") as f:
            data = f.readlines()
            del(data[0])
            id_number = 1
            batterys = []

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

        for battery in batterys:
            print(battery)

        return batterys

    def calculate_distance(self):

        for house in self.houses:
            battery_distances = {}
            for battery in self.batterys:
                x_distance = abs(house.location_x - battery.location_x)
                y_distance = abs(house.location_y - battery.location_y)
                distance = x_distance + y_distance
                battery_distances.update({battery.identification: distance})
            house.battery_distances = battery_distances
            print(house)

    def battery_sort_function(self):
        for house in self.houses:
            if int(house.identification) % 5 == 1:
                self.batterys[0].list_of_houses.append(house)
            elif int(house.identification) % 5 == 2:
                self.batterys[1].list_of_houses.append(house)
            elif int(house.identification) % 5 == 3:
                self.batterys[2].list_of_houses.append(house)
            elif int(house.identification) % 5 == 4:
                self.batterys[3].list_of_houses.append(house)
            elif int(house.identification) % 5 == 0:
                self.batterys[4].list_of_houses.append(house)


if __name__ == "__main__":
    smartgrid = Smartgrid()
