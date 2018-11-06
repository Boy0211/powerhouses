import csv

from house import House
from battery import Battery
from sort import sort_function as sort


class Smartgrid():

    def __init__(self):
        sort(f"data/csv_bestanden/wijk3_huizen.csv")
        self.houses = self.load_houses(f"../data/csv_bestanden/sorted_houses3.csv")
        self.batterys = self.load_batterys(f"../data/csv_bestanden/wijk3_batterijen.txt")
        self.calculate_distance()
        self.battery_sort_function()
        for battery in self.batterys:
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

    def add_house_to_battery(self, house, battery):
        battery.list_of_houses.append(house)
        battery.current_input += (house.output)

    def remove_house_from_battery(self, house, battery):
        battery.list_of_houses.remove(house)
        battery.current_input -= (house.output)

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
            while self.batterys[0].current_input < 1507:
                self.add_house_to_battery(house, self.batterys[0])

            while self.batterys[1].current_input < 1507:
                self.add_house_to_battery(house, self.batterys[1])

            while self.batterys[2].current_input < 1507:
                self.add_house_to_battery(house, self.batterys[2])

            while self.batterys[3].current_input < 1507:
                self.add_house_to_battery(house, self.batterys[3])

            while self.batterys[4].current_input < 1507:
                self.add_house_to_battery(house, self.batterys[4])

        # for house in self.houses:
        #     if int(house.identification) % 5 == 1:
        #         self.add_house_to_battery(house, self.batterys[0])
        #     elif int(house.identification) % 5 == 2:
        #         self.add_house_to_battery(house, self.batterys[1])
        #     elif int(house.identification) % 5 == 3:
        #         self.add_house_to_battery(house, self.batterys[2])
        #     elif int(house.identification) % 5 == 4:
        #         self.add_house_to_battery(house, self.batterys[3])
        #     elif int(house.identification) % 5 == 0:
        #         self.add_house_to_battery(house, self.batterys[4])


if __name__ == "__main__":
    smartgrid = Smartgrid()
