
class House(object):

    def __init__(self, identification, location_x, location_y, output, battery_distances):
        self.identification = identification
        self.location_x = location_x
        self.location_y = location_y
        self.output = output
        self.battery_distances = battery_distances

    def __str__(self):
        return f"ID: {self.identification}\nlocation: ({self.location_x},{self.location_y})\noutput: {self.output}\nbattery_distances: {self.battery_distances}\n"
