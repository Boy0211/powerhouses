import csv

country = []
value = []
data_dict = {}

# Opening the csv file, if the row length is equal to 3 and contains 'KTOE'
# as element, the right data is found
with open('OpgaveB_resultaten.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row == 'Capaciteits-Greedy':
            print("SKuuurt")
            # if row[5] == '2015':
            #     country.append(row[0].lstrip())
            #     value.append(row[6].lstrip())

# Creating a dictionary with the right keys and values
# for i in range(len(value)):
#     data_dict[country[i]] = {"Energy Production": value[i]}
#
#
# def main():
#     kosten = [101491, 73546, 56977, 56374, 56347, 42757]
#     labels = ("Upper bound", "Greedy capacity", "Greedy distance", "Hillclimber/Greedy capacity",  "Hillclimber/Greedy 2", "Lower bound")
#     # objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
#     y_pos = np.arange(len(labels))
#     # performance = [10,8,6,4,2,1]
#     font = {'family' : 'normal',
#         'weight' : 'bold',
#         'size'   : 7}
#
#     plt.rc('font', **font)
#     plt.bar(y_pos, kosten, align='center', alpha=0.5)
#     plt.xticks(y_pos, labels)
#     plt.ylabel('Total distance')
#     plt.title('Programming language usage')
#
#     plt.show()
#
#
#
#
# if __name__ == "__main__":
#     main()
