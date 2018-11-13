

class Greedy():

    def greedy_1(self):

        ''' Greedy algorithm that fills up the most empty battery'''

        # iterate through all houses
        house_counter = 0
        while house_counter < len(self.houses):
            bat_list = []

            # append all batteries in new list and choose battery with lowest
            # current input
            for battery in self.batterys:
                bat_list.append(battery.current_input)
            battery_counter = bat_list.index(min(bat_list))

            del(bat_list)

            # if a house fits into the battery with the lowest input, put this
            # house inside this battery. Otherwise were scruwed because we have
            # reached the max capacity of all batteries
            if self.batterys[battery_counter].current_input + self.houses[house_counter].output < 1507:
                self.add_house_to_battery(self.houses[house_counter], self.batterys[battery_counter])
            else:
                print("het past gewoon godverdomme niet!")
            house_counter += 1
