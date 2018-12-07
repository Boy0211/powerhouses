import matplotlib.pyplot as plt
import numpy as np

def main():
    kosten = [101491, 73546, 56977, 56374, 56347, 42757]
    labels = ("Upper bound", "Greedy capacity", "Greedy distance", "Hillclimber/Greedy capacity",  "Hillclimber/Greedy 2", "Lower bound")
    # objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    y_pos = np.arange(len(labels))
    # performance = [10,8,6,4,2,1]
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 7}

    plt.rc('font', **font)
    plt.bar(y_pos, kosten, align='center', alpha=0.5)
    plt.xticks(y_pos, labels)
    plt.ylabel('Total distance')
    plt.title('Programming language usage')

    plt.show()




if __name__ == "__main__":
    main()
