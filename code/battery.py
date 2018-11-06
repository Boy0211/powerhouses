
class Battery(object):

    def __init__(self, identification, location_x, location_y, max_input, current_input, list_of_houses):
        self.identification = identification
        self.location_x = location_x
        self.location_y = location_y
        self.max_input = max_input
        self.current_input = current_input
        self.list_of_houses = list_of_houses

    def __str__(self):
        return f"ID: {self.identification}\n location: ({self.location_x},{self.location_y})\n max_input: {self.max_input}\n current_input: {self.current_input}\n list of houses: {len(self.list_of_houses)}\n"
