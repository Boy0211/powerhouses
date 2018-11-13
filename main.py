import os
import sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "algorithmes"))
sys.path.append(os.path.join(directory, "code", "classes"))

from greedy import greedy_1
from smartGRID import Smartgrid


def main():
    smartgrid = Smartgrid(1)
    greedy_1(smartgrid.houses, smartgrid.batterys)
    for battery in smartgrid.batterys:
        print(battery)


if __name__ == "__main__":
    main()