class Battery(object):

    '''Class created which represents a battery. All the information needed
    for the algorithm is saved in either instances or propertys'''

    # define the init of the class with different instannces
    def __init__(self, identification, location_x, location_y, max_input,
                 current_input, list_of_houses):
        self.identification = identification
        self.location_x = location_x
        self.location_y = location_y
        self.max_input = float(max_input)
        self.current_input = current_input
        self.list_of_houses = list_of_houses

    # define the return function when a battery is printed
    def __str__(self):
        return (f"ID: {self.identification}\ncurrent_input: "
                f"{self.current_input}\nmax input: {self.max_input}\nHouses: "
                f"{len(self.list_of_houses)}\nBattery Costs: "
                f"{self.battery_costs}\n")

    # property distance costs, beacause it is variabel.
    @property
    def distance_costs(self):

        # calculate the costs and start on zero
        distance_costs = 0

        # for every house in the battery, append the costs
        for house in self.list_of_houses:
            distance = (abs(self.location_x - house.location_x) +
                        abs(self.location_y - house.location_y))
            distance_costs += distance * 9

        # return the costs
        return distance_costs

    # property battery type costs, if the capacity is 450, 900 or 1800
    # adjust the costs
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

    # calculate the total costs
    @property
    def battery_costs(self):
        return self.distance_costs + self.battery_type_costs
