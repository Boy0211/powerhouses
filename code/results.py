import csv
import datetime


def save_results(batterys, percentage, district):

    OUTPUT_CSV = 'results.csv'

    # update everytime smarGRID.py is run
    with open(OUTPUT_CSV, 'a', newline='') as output_file:
        writer = csv.writer(output_file)
        temp_list = []

        # store date
        now = str(datetime.date.today())
        temp_list.append(now)

        # store district number
        temp_list.append(district)

        # store percentage well placed
        temp_list.append(percentage)

        battery_current_input = []
        battery_list_of_houses = []

        # store current_input and number of houses in each battery
        for battery in batterys:
            battery_current_input.append(battery.current_input)
            battery_list_of_houses.append(len(battery.list_of_houses))
        temp_list.append(battery_current_input)
        temp_list.append(battery_list_of_houses)

        writer.writerow(temp_list)
