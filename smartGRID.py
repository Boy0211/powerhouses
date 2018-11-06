import csv

from house import House
from battery import Battery
from coordinates import Coordinates

class Smartgrid():

    def __init__():
        self.houses = self.load_houses
        self.batterys = self.load_batterys

    def load_houses():
        filename = f"csv_bestanden/wijk1_huizen.csv"

        with open(filename, 'r') as csv_file:
            data = csv.DictReader(csv_file)
            houses = []
            id_number = 1

            for line in data:
                print(line)
                identification = id_number
                location_x = int(line['x'])
                location_y = int(line['y'])
                output = float(line['max. output'])
                houses.append(House(identification, location_x, location_y, output))
                id_number += 1

            for house in houses:
                print(house)

            print(houses[0])

            return houses

    def load_batterys():
        filename = f"csv_bestanden/wijk1_batterijen.txt"

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
                batterys.append(Battery(identification, location_x, location_y, max_input, current_input))
                id_number += 1

        for battery in batterys:
            print(battery)

        return batterys

    def calculate_distance(house, battery):
        x_distance = abs(house.location_x - battery.location_x)
        y_distance = abs(house.location_y - battery.location_y)

        print("----------")
        print(x_distance)
        print(y_distance)
        print("----------")

        distance = x_distance + y_distance
        print(distance)

if __name__ == "__main__":
    houses = Smartgrid.load_houses()
    batterys = Smartgrid.load_batterys()
    Smartgrid.calculate_distance(houses[0], batterys[0])
