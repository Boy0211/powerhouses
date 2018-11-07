import csv

def sort_function(filename, district):

    INPUT_CSV = f"../data/csv_bestanden/wijk{district}_huizen.csv"
    OUTPUT_CSV = f"../data/csv_bestanden/sorted_houses{district}.csv"

    with open(INPUT_CSV, 'r') as csv_file:
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
