import numpy as np
import matplotlib.pyplot as plt


def grid(houses, batterys):
    x_1 = []
    y_1 = []
    for house in batterys[0].list_of_houses:
        for i in range(len(batterys[0].list_of_houses)):
            x_1.append(house.location_x)
            x_1.append(batterys[0].location_x)
            y_1.append(house.location_y)
            y_1.append(batterys[0].location_y)

    x_2 = []
    y_2 = []
    for house in batterys[1].list_of_houses:
        for i in range(len(batterys[1].list_of_houses)):
            x_2.append(house.location_x)
            x_2.append(batterys[1].location_x)
            y_2.append(house.location_y)
            y_2.append(batterys[1].location_y)

    x_3 = []
    y_3 = []
    for house in batterys[2].list_of_houses:
        for i in range(len(batterys[2].list_of_houses)):
            x_3.append(house.location_x)
            x_3.append(batterys[2].location_x)
            y_3.append(house.location_y)
            y_3.append(batterys[2].location_y)

    x_4 = []
    y_4 = []
    for house in batterys[3].list_of_houses:
        for i in range(len(batterys[3].list_of_houses)):
            x_4.append(house.location_x)
            x_4.append(batterys[3].location_x)
            y_4.append(house.location_y)
            y_4.append(batterys[3].location_y)

    x_5 = []
    y_5 = []
    for house in batterys[4].list_of_houses:
        for i in range(len(batterys[4].list_of_houses)):
            x_5.append(house.location_x)
            x_5.append(batterys[4].location_x)
            y_5.append(house.location_y)
            y_5.append(batterys[4].location_y)

    x_battery_1 = []
    y_battery_1 = []

    x_battery_1.append(batterys[0].location_x)
    y_battery_1.append(batterys[0].location_y)

    x_battery_2 = []
    y_battery_2 = []

    x_battery_2.append(batterys[1].location_x)
    y_battery_2.append(batterys[1].location_y)

    x_battery_3 = []
    y_battery_3 = []

    x_battery_3.append(batterys[2].location_x)
    y_battery_3.append(batterys[2].location_y)

    x_battery_4 = []
    y_battery_4 = []

    x_battery_4.append(batterys[3].location_x)
    y_battery_4.append(batterys[3].location_y)

    x_battery_5 = []
    y_battery_5 = []

    x_battery_5.append(batterys[4].location_x)
    y_battery_5.append(batterys[4].location_y)

    # x_line = [5, 30]
    # y_line = [5, 25]

    plt.scatter([x_1], [y_1], s=10, color='red')
    plt.scatter([x_2], [y_2], s=10, color='orange')
    plt.scatter([x_3], [y_3], s=10, color='blue')
    plt.scatter([x_4], [y_4], s=10, color='purple')
    plt.scatter([x_5], [y_5], s=10, color='green')
    plt.axis([-5, 60, -5, 60])
    x_grid = np.linspace(0, 59, 60)
    y_grid = np.linspace(0, 59, 60)
    plt.xticks(x_grid)
    plt.yticks(y_grid)
    plt.grid()
    plt.scatter([x_battery_1], [y_battery_1], s=70, color='red')
    plt.scatter([x_battery_2], [y_battery_2], s=70, color='orange')
    plt.scatter([x_battery_3], [y_battery_3], s=70, color='blue')
    plt.scatter([x_battery_4], [y_battery_4], s=70, color='purple')
    plt.scatter([x_battery_5], [y_battery_5], s=70, color='green')

    plt.plot(x_1, y_1, linewidth=0.5, color="red")
    plt.plot(x_2, y_2, linewidth=0.5, color="orange")
    plt.plot(x_3, y_3, linewidth=0.5, color="blue")
    plt.plot(x_4, y_4, linewidth=0.5, color="purple")
    plt.plot(x_5, y_5, linewidth=0.5, color="green")
    for house in batterys[0].list_of_houses:
        plt.scatter(house.location_x, house.location_y, house.output)
    plt.show()
