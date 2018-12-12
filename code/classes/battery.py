
class Battery(object):

    def __init__(self, identification, location_x, location_y, max_input,
                 current_input, list_of_houses):
        self.identification = identification
        self.location_x = location_x
        self.location_y = location_y
        self.max_input = float(max_input)
        self.current_input = current_input
        self.list_of_houses = list_of_houses

    def __str__(self):
        return (f"ID: {self.identification}\ncurrent_input: {self.current_input}\nmax input: {self.max_input}\nHouses: {len(self.list_of_houses)}\nBattery Costs: {self.battery_costs}\n")

    @property
    def distance_costs(self):

        distance_costs = 0
        for house in self.list_of_houses:
            distance = abs(self.location_x - house.location_x) + abs(self.location_y - house.location_y)
            distance_costs += distance * 9

        return distance_costs

    @property
    def battery_type_costs(self):

        if self.max_input == 450:
            return 900
        elif self.max_input == 900:
            return 1350
        elif self.max_input == 1800:
            return 1800
        else:
            return 5000

    @property
    def battery_costs(self):
        return self.distance_costs + self.battery_type_costs
