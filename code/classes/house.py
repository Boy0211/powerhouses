
class House(object):

    def __init__(self, identification, location_x, location_y, output, battery_distances, connected_battery):
        self.identification = identification
        self.location_x = location_x
        self.location_y = location_y
        self.output = output
        self.battery_distances = battery_distances
        self.connected_battery = connected_battery
        # self.distance_houses = distance_houses
    def __str__(self):
        return f"ID: {self.identification}\nlocation: ({self.location_x},{self.location_y})\noutput: {self.output}\nbattery_distances: {self.battery_distances}\nconnected battery: {self.connected_battery}\ndistance_houses: {self.distance_houses}\n"
