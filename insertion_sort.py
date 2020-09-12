import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key


        print(array)
    fig, ax = plt.subplots()
    # ax.set_title(title)
    bar_rec = ax.bar(range(len(array)), array, align='edge')
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    plt.pause(0.05)
    plt.show()



    return array, bar_rec


if __name__ == '__main__':
    numbers = [10, 5, 4, 8, 9, 1, 6, 3, 7, 2]

    # plotter(numbers)
    sorted_array = insertion_sort(numbers)
    # plotter(sorted_array)
    # animation = anim.FuncAnimation(fig, insertion_sort, init_func=)


