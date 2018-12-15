import numpy as np
import matplotlib.pyplot as plt


def grid(solution):

    # get the batterys out of the solution
    batterys = solution.batterys

    # list of colours used for visualization
    color_list = ['red', 'orange', 'blue', 'purple', 'green', 'yellow',
                  'orchid', 'aqua', 'grey', 'black', 'teal', 'goldenrod',
                  'darkblue', 'pink', 'darkgrey', 'springgreen', 'crimson']

    # for every battery in the list of batterys
    for i in range(len(batterys)):

        # empty lists for the house coordinates
        x = []
        y = []

        # empty lists for the battery coordinates
        x_battery = []
        y_battery = []

        # for every house in the batterys
        for house in batterys[i].list_of_houses:

            # append the coordinates into the lists
            x.append(house.location_x)
            x.append(batterys[i].location_x)
            y.append(house.location_y)
            y.append(batterys[i].location_y)
            x_battery.append(batterys[i].location_x)
            y_battery.append(batterys[i].location_y)

            # plot the lines and the dots
            plt.plot(x, y, linewidth=0.5, color=color_list[i])
            plt.scatter(x, y, s=10, color=color_list[i])
            plt.scatter(x_battery, y_battery, s=70, color=color_list[i])

            # add the identification number of the batterys into the grid
            plt.text(batterys[i].location_x, batterys[i].location_y,
                     batterys[i].identification, fontsize=10)

    # plot the grid
    x_grid = np.linspace(0, 59, 60)
    y_grid = np.linspace(0, 59, 60)

    # create empty lists needed for the ticks
    x_tick = []
    y_tick = []

    # tick for every 10 iterations on the x-axis
    for x in range(60):
        if x % 10 == 0:
            x_tick.append(x)
        else:
            x_tick.append("")

    # tick for every 10 iterations on the y-axis
    for y in range(60):
        if y % 10 == 0:
            y_tick.append(y)
        else:
            y_tick.append("")

    # plot everything and show the plot
    plt.xticks(x_grid, x_tick)
    plt.yticks(y_grid, y_tick)
    plt.grid(True)
    plt.show()
