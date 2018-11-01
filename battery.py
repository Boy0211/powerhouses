
class Battery(object):

    def __init__(self, identification, location_x, location_y, max_input, current_input):
        self.identification = identification
        self.location_x = location_x
        self.location_y = location_y
        self.max_input = max_input
        self.current_input = current_input

    def __str__(self):
        return f"ID: {self.identification}\n location: ({self.location_x},{self.location_y})\n max_input: {self.max_input}\n current_input: {self.current_input}\n"
