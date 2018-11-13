import csv
import heapq

from house import House
from battery import Battery
from sort import sort_function as sort
from results import save_results


class Smartgrid():

    def __init__(self, district):

        # print the wijk which is worked with:
        print(f"This is wijk: {district}")

        # sort the given data, before further usage
        sort(f"data/csv_bestanden/wijk{district}_huizen.csv", district)

        # load both the houses and the batterys into the RAM
        self.houses = self.load_houses(f"../data/csv_bestanden/sorted_houses{district}.csv")
        self.batterys = self.load_batterys(f"../data/csv_bestanden/wijk{district}_batterijen.txt")
        self.load_distances()

        # calculate the results and save it in a csv file
        self.calculate_perfect()
        self.calculate_totals()
        save_results(self.batterys, self.calculate_perfect(), district)

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

    def add_house_to_battery(self, house, battery):

        ''' Function used to add houses to batterys '''

        battery.list_of_houses.append(house)
        battery.current_input += (house.output)
        house.connected_battery = int(battery.identification)

    def remove_house_from_battery(self, house, battery):

        ''' Function used to remove houses to batterys '''

        battery.list_of_houses.remove(house)
        battery.current_input -= (house.output)
        house.connected_battery = 'not connected'

    def calculate_distance(self, house):

        '''Function used to calculate the actual distance to the connected
           battery '''

        distance = house.battery_distances[house.connected_battery]
        return distance

    def calculate_totals(self):

        '''Function used to calculate results based on distance'''

        total_distance_min = 0
        for house in self.houses:
            distance_min = min(house.battery_distances.values())
            total_distance_min += distance_min
        print(f"minimal distance: {total_distance_min}")

        total_distance_connected = 0
        for house in self.houses:
            distance = self.calculate_distance(house)
            total_distance_connected += distance
        print(f"connected distance: {total_distance_connected}")

        total_distance_max = 0
        for house in self.houses:
            distance_max = max(house.battery_distances.values())
            total_distance_max += distance_max
        print(f"maximal distance: {total_distance_max}")

        print(f"total costs: {(total_distance_connected * 9)}")

    def calculate_perfect(self):

        '''Function used to calculate how many houses are connected to the
           best option'''

        counter_first = 0
        counter_second = 0
        counter_third = 0
        counter_forth = 0
        counter_five = 0

        for house in self.houses:

            temp_sorted = (heapq.nsmallest(5, house.battery_distances.values()))

            if house.battery_distances[int(house.connected_battery)] == temp_sorted[0]:
                counter_first += 1
            elif house.battery_distances[int(house.connected_battery)] == temp_sorted[1]:
                counter_second += 1
            elif house.battery_distances[int(house.connected_battery)] == temp_sorted[2]:
                counter_third += 1
            elif house.battery_distances[int(house.connected_battery)] == temp_sorted[3]:
                counter_forth += 1
            elif house.battery_distances[int(house.connected_battery)] == temp_sorted[4]:
                counter_five += 1

        percentage_first = (counter_first / 150) * 100
        # print(f"percentage best connected houses: {round(percentage_first, 2)}%")

        percentage_second = (counter_second / 150) * 100
        # print(f"percentage second best connected houses: {round(percentage_second, 2)}%")

        percentage_third = (counter_third / 150) * 100
        # print(f"percentage third best connected houses: {round(percentage_third, 2)}%")

        percentage_forth = (counter_forth / 150) * 100
        # print(f"percentage fourth best connected houses: {round(percentage_forth, 2)}%")

        percentage_five = (counter_five / 150) * 100
        # print(f"percentage worst connected houses: {round(percentage_five, 2)}%")
        return(percentage_first)

if __name__ == "__main__":
    smartgrid = Smartgrid("3")
