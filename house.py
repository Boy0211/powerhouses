
class House(object):

    def __init__(self, identification, location_x, location_y, output):
        self.identification = identification
        self.location_x = location_x
        self.location_y = location_y
        self.output = output

    def __str__(self):
        return f"ID: {self.identification}\n location: ({self.location_x},{self.location_y})\n output: {self.output}\n"
