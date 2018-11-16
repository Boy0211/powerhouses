import numpy as np
import matplotlib.pyplot as plt


def grid(houses, batterys):
    x = []
    y = []
    for house in houses:
        x.append(house.location_x)
        y.append(house.location_y)

    x_battery = []
    y_battery = []
    for battery in batterys:
        x_battery.append(battery.location_x)
        y_battery.append(battery.location_y)



    x_grid = np.linspace(0, 59, 60)
    y_grid = np.linspace(0, 59, 60)
    plt.axis([-5, 60, -5, 60])
    plt.xticks(x_grid)
    plt.yticks(y_grid)
    plt.scatter([x], [y], s=10)
    plt.grid()
    plt.scatter([x_battery], [y_battery], color='red')
    plt.ylim(-5, 60)
    plt.xlim(-5,60)
    plt.show()
