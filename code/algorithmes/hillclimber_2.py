from helpers import swap
from helpers import remove_house_from_battery as rm
from helpers import add_house_to_battery as add
from helpers import capacity
from visualization import grid
# from helpers import house_battery_distance as distance
from helpers import battery_capacity_exceeded as cap_exc
import copy
import pandas as pd

# A function used to swap two houses from one list to another.
def replace(house, battery_A, battery_B):
    rm(house, battery_A)
    ad(house, battery_B)


# a function to get the battery with the lowest input.
def check_battery_highest_input(batterys):

    score = float(batterys[0].max_input)
    for battery in batterys:
        if battery.current_input > score:
            score = battery.current_input
            highest_input_battery = battery
    return highest_input_battery

def hillclimber_2(solution):
    batterys = solution.batterys
    #
    # if capacity is overgeschreden:
    #   kies batterij waarbij meeste overschrijding is:
    #       bereken voor alle huizen in deze batterij de kosten van de verplaatsing minimaal is
    #       verder mag max_input van nieuwe batterij niet worden overschredenself
    #       minimale verplaatsing: afstand nieuwe batterij - afstand oude batterij
    #       dus voor elke batterij moet dit worden berekent
    #       lukt dit voor geen batterij:
            #   swap
            #   if swap niet mogelijk:
            #      break
    # load_distances(houses, batterys)

    # print(solution.distances)

    while True:
        # grid(solution)
        y = 0
        # for battery in batterys:
        #     print(battery)
        # check of een batterij een max_input overschrijding heeft
        if cap_exc(batterys) is False:
            battery1 = check_battery_highest_input(batterys)

            # lijst me alle huis id nummers in battery1
            houses_list = []
            for house in battery1.list_of_houses:
                houses_list.append(house.identification)

            # overal -1 voor index
            houses_list[:] = [x - 1 for x in houses_list]

            # selecteer huizen van battery1 uit dataframe
            battery_houses = (solution.distances.iloc[houses_list])

            # selecteer alle rijen met andere batterijen
            selected_list = battery_houses[battery_houses.columns.difference([battery1.identification, "max_value", "min_value", "closest_house"])]
            # print(selected_list)
            # selecteer column nummers
            column_numbers = selected_list.columns.values

            # maak lijst met alle huizen in alle batterijen
            list_of_all_houses = []
            for i in range(len(column_numbers)):
                print(selected_list[column_numbers[i]].tolist())
                print(selected_list[column_numbers[i]].name)
                # list_of_all_houses += (selected_list[column_numbers[i]].tolist())
                for distances in selected_list[column_numbers[i]].tolist():
                    list_of_all_houses += [selected_list[column_numbers[i]].name, distances]

            # soorter van klein naar groot
            list_of_all_houses = sorted(list_of_all_houses)
            # print(list_of_all_houses)
            # print(len(list_of_all_houses))

            # house_counter neemt toe als een huis niet in een batterij passt
            # dus gaat op zoek naar eerstvolgende dichstbijzijnde huis
            house_counter = 0

            # solved = True is als een huis is verplaatst
            solved = False
            print("-----------")

            while True:
                # print(f"house counter: {house_counter}")

                # print(solved)
                # print(list_of_all_houses[house_counter])
                battery_n = selected_list[selected_list.apply(lambda row: row.astype(str).str.contains(f"{list_of_all_houses[house_counter]}").any(), axis=1)]
                # print(battery_n)
                # print(battery_n)

                replace_house = (battery_n.iloc[y].name)
                # print(y)
                # print(replace_house)
                # distance = (battery_n.iloc[0].min())
                # print(distance)
                dict = battery_n.to_dict('index')
                # print(dict)
                replace_battery = min(dict[replace_house].items(), key=lambda x: x[1])[0]
                # print(replace_battery)
                # print(f"xx{replace_battery}")
                # for value in dict:
                #     # print(dict[value].values())
                #     if distance in dict[value].values():
                #         replace_battery = value


                # print(replace_house)



            # for house in battery1.list_of_houses:
            #     print(replace_house)
            #     print(house)
                for house in battery1.list_of_houses:
                    if house.identification == replace_house:
                    # print("inside first if")
                        # print(f"house id {house.identification}")
                        # print(house.output + batterys[replace_battery-1].current_input)
                        if house.output + batterys[replace_battery-1].current_input < batterys[replace_battery-1].max_input:
                            # print(len(battery1.list_of_houses))
                            # print("booooooyyyyyaaaaaaaaa")
                            add(house, batterys[replace_battery-1])
                            rm(house, battery1)
                            # print(len(battery1.list_of_houses))
                            for battery in batterys:
                                print(battery)
                            solved = True
                            x = 0
                            break
                        else:
                            # print("last else")
                            # print(house.output + batterys[replace_battery-1].current_input)
                            house_counter += 1
                            # print(f"len_battery{len(battery_n)}")
                            # print(f"xx{x}")
                            if len(battery_n) == 1:
                                # print("11111111111")
                                y = 0
                            #     x = 0
                            elif len(battery_n) -1 == y and y > 0:
                                # print("eindeeeeeee")
                                y = 0
                            else:
                                y += 1
                                # print("increasseeeeee")
                                # x = 0
                            # elif len(battery_n) -1 > 1:
                            #     x += 1
                            #
                            # else:
                            #     x = 0
                        # for battery in batterys:
                        #     print(battery)
                    # print(" ik ben hieeeeerrr")
                if solved is True:
                    break
        else:
            break

        # battery_n['column'] = battery_n.apply(lambda x: battery_n.columns[x.argmax()], axis = 1)


        # for row in replace_house:
            # print(row)

        # print(battery_n.iloc[0].min().idxmin())
        # print(battery_n.loc(battery_n.min().min()))
        # replace_house = battery_n.iloc[0].idxmin().min()
        # print(replace_house)
        # print(battery_n[replace_house])
        # print(battery_n.idxmin().min())

        # print(selected_list[battery_n])

        # df = df.apply(lambda x: x.sort_values().values)
        # smallest_dict = dict()
        # for index, row in selected_list.iterrows():
        #     print(row)
        #     print(row.min())


            # smallest_dict[index] = row.nsmallest(1).index[0]
        # print(smallest_dict)
        # print(selected_list.min())
        # print(selected_list.min().nsmallest(1))

        # print(selected_list.idxmin())

        # get the battery that contains the smallest delta distance
        # for row in selected_list:
        #     print(row)
        # print(selected_list.min())
        # print(selected_list.min().nsmallest(2))

        min_battery = (selected_list.min().nsmallest(1)).index[0]

        # print(min_battery)

        battery_list = selected_list[min_battery]
        # print(battery_list)

        # lowest_num = battery_list.idxmin()

        # print(lowest_num)
        number = int(selected_list.min().nsmallest(1))
        # print(battery_list.iloc[number])
        # print(number)
        # print(battery_list)
        # print(battery_list[battery_list == int(number)].index.values)
        # print(battery_list.iloc[number])
        i = 0
        count = i
        for row in battery_list:
            if row == number:
                count = i
            i += 1
        # print((battery_list[battery_list[] == number]).index.values.astype(int))

        # temp_house = battery1.list_of_houses[lowest_num]

        # print(lowest_num)
        # print(len(battery1.list_of_houses))
        # add(battery1.list_of_houses[count], batterys[min_battery-1])
        # rm(battery1.list_of_houses[count], battery1)
        # #
        # print(len(battery1.list_of_houses))

        # print(selected_list[min_battery].index)
        # unique_index = pd.Index(list(selected_list[min_battery]))
        # unique_index.get_loc()
        # replace()
        # print(selected_list.get_loc(selected_list.min().nsmallest(1)))




        # welk huis heeft minste kostenverschil
        # print(battery1.identification)
        # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            # print((solution.distances[battery1.identification]))
        # print(solution.distances.to_string())
        # replace_house = (solution.distances[battery1.identification]).idxmin(axis='index')
        # for house in battery1.list_of_houses:
            # print(house.identification)
        # print(solution.distances[1])

        #     # bekijk per huis de batterijen
        #     for i in range(1, len(house.battery_distances) + 1):
        #         # bereken per batterij de verplaatsingsscore
        #         temp_score = house.battery_distances[i] - house.battery_distances[battery1.identification]
        #         # print(score)
        #
        #         # sla score op als deze kleiner is dan de vorige
        #         if temp_score < score and temp_score > 0:
        #             score = temp_score
        #             replace_battery = house.battery_distances[i]
        #             swap_house = house
        #             print(f"replace battery: {replace_battery}")
        #             print(house.battery_distances[i])
        #
        # # # ga op zoek naar de replace battery in het house en zet het daar naartoe
        # for battery_number in house.battery_distances.items():
        #     print(house.battery_distances[i])
        #     if replace_battery == house.battery_distances[i]:
        #         print("joe")
        #         print(batterys[battery_number -1])
        #
        #         # print("battery:")
        #         # print(battery_number)
        #         # print("------")
        #         # print(house)
        #         # print(battery1)
        #         # print(batterys[battery_number - 1])
        #         replace(house, battery1, batterys[battery_number - 1])
    # else:
        # break

    # for i in range(1):
    #
    #     if cap_exc(batterys) is not False:
    #         score = 1000
    #         battery1 = check_battery_highest_input(batterys)
    #         # ga alle huizen af op zoek naar huis met minste kostenverschil
    #         for house in battery1.list_of_houses:
    #             # bekijk per huis de batterijen
    #             for i in range(1, len(house.battery_distances) + 1):
    #
    #                 # bereken per batterij de verplaatsingsscore
    #                 temp_score = house.battery_distances[i] - house.battery_distances[house.connected_battery["id"]]
    #                 # print(score)
    #
    #                 # sla score op als deze kleiner is dan de vorige
    #                 if temp_score < score and temp_score > 0:
    #                     score = temp_score
    #                     replace_battery = house.battery_distances[i]
    #                     print(f"replace battery: {replace_battery}")
    #                     print(house.battery_distances[i])
    #
    #             # ga op zoek naar de replace battery in het house en zet het haar daar naartoe
    #             for battery_number, distance in house.battery_distances.items():
    #                 # print(house.battery_distances[i])
    #                 if replace_battery == house.battery_distances[i]:
    #                     print("joe")
    #                     print(batterys[battery_number -1])
    #
    #                     # print("battery:")
    #                     # print(battery_number)
    #                     # print("------")
    #                     # print(house)
    #                     # print(battery1)
    #                     # print(batterys[battery_number - 1])
    #                     replace(house, battery1, batterys[battery_number - 1])
    #     else:
    #         break



            # print("----")
