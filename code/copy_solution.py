import copy
from solution import Solution
from battery import Battery


def copy_solution(solution):

    # for the new batterys
    new_batterys = []
    for battery in solution.batterys:
        identification = (battery.identification)
        location_x = (battery.location_x)
        location_y = (battery.location_y)
        max_input = (battery.max_input)
        list_of_houses = []
        current_input = 0
        for house in battery.list_of_houses:
            list_of_houses.append(house)
            current_input += house.output

        new_battery = Battery(identification, location_x, location_y, max_input, current_input, list_of_houses)
        new_batterys.append(new_battery)
    #
    new_solution = Solution(solution.houses, new_batterys)
    #
    return new_solution
