

class Greedy():

    def greedy_1(self):

        house_counter = 0
        while house_counter < len(self.houses):
            bat_list = []
            for battery in self.batterys:
                bat_list.append(battery.current_input)
            battery_counter = bat_list.index(min(bat_list))
            # print(battery_counter)
            del(bat_list)

            if self.batterys[battery_counter].current_input + self.houses[house_counter].output < 1507:
                self.add_house_to_battery(self.houses[house_counter], self.batterys[battery_counter])
            else:
                print("het past gewoon godverdomme niet!")
            house_counter += 1

        # for house in self.houses:
            # print(house)
