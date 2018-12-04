
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
        return (f"ID: {self.identification}\ncurrent_input: {self.current_input}\nmax input: {self.max_input}\n Houses: {len(self.list_of_houses)}\n")
