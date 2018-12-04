
class House(object):

    def __init__(self, identification, location_x, location_y, output,
                 battery_distances, connected_battery):
        self.identification = identification
        self.location_x = location_x
        self.location_y = location_y
        self.output = output
        self.battery_distances = battery_distances

    def __str__(self):
        return str(f"ID: {self.identification}\nLocatie: {self.location_x},"
                   f"{self.location_y}\nOutput: {self.output}\n")
