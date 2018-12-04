import csv

def sort_function(filename, district):

    ''' Sort houses in order of output'''

    OUTPUT_CSV = f"data/csv_bestanden/sorted_houses{district}.csv"

    with open(filename, 'r') as csv_file:
        data = csv.DictReader(csv_file)
        sortedlist = sorted(data, key=lambda row: row["max. output"], reverse=True)
        # print(sortedlist)

    with open(OUTPUT_CSV, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['x', 'y', 'max. output'])

        for house in sortedlist:
            templist = list()
            x_value = house['x']
            y_value = house['y']
            max_output = house['max. output']
            templist.append(x_value)
            templist.append(y_value)
            templist.append(max_output)
            writer.writerow(templist)


def sort_distance(houses):
    # bubble sort function. Copied and edited from https://repl.it/@farooqimdd/BubbleSort

    n = len(houses)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if (min(houses[j].battery_distances.values())) > (min(houses[j+1].battery_distances.values())):
                houses[j], houses[j+1] = houses[j+1], houses[j]

    return houses
