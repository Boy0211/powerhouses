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

    plt.scatter([x], [y], s=10)
    plt.subplot()
    plt.grid()
    plt.scatter([x_battery], [y_battery], color='red')
    plt.axis([-5, 60, -5, 60])
    plt.ylim(-5, 60)
    plt.show()
