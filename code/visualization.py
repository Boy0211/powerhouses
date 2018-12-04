import numpy as np
import matplotlib.pyplot as plt


def grid(houses, batterys):

    color_list = ['red', 'orange', 'blue', 'purple', 'green']
    for i in range(len(batterys)):
        x = []
        y = []
        x_battery = []
        y_battery = []
        for house in batterys[i].list_of_houses:
            x.append(house.location_x)
            x.append(batterys[i].location_x)
            y.append(house.location_y)
            y.append(batterys[i].location_y)
            x_battery.append(batterys[i].location_x)
            y_battery.append(batterys[i].location_y)
            plt.plot(x, y, linewidth=0.5, color=color_list[i])
            plt.scatter(x, y, s=10, color=color_list[i])
            plt.scatter(x_battery, y_battery, s=70, color=color_list[i])
            plt.text(house.location_x, house.location_y, house.output, fontsize=5)

    x_grid = np.linspace(0, 59, 60)
    y_grid = np.linspace(0, 59, 60)
    plt.xlabel('x-axis')
    x_tick = []
    y_tick = []
    for x in range(60):
        if x % 5 == 0:
            x_tick.append(x)
        else:
            x_tick.append("")

    for y in range(60):
        if y % 5 == 0:
            y_tick.append(y)
        else:
            y_tick.append("")

    plt.xticks(x_grid, x_tick)
    plt.yticks(y_grid, y_tick)
    plt.grid(True)
    plt.show()
