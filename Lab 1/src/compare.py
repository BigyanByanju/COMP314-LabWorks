from Qn_2.insertion_sort import insertion_sort
from Qn_2.selection_sort import selection_sort
import time
import random
import matplotlib.pyplot as plt


# Function to generate n random numbers
def generate_random(n: int):
    arr = []
    for i in range(n):
        arr.append(random.randint(-1000, 10000))
    return arr


# Function to compare the time taken by the sorting algorithms
def compare():
    input_size = 10000
    select_diff, insert_diff, insert_diff_best, insert_diff_worst = [], [], [], []
    number = []

    for i in range(10, input_size, 30):
        random_array = generate_random(i)

        # Time the sorting algorithms
        selection_start = time.time()
        selection_sorted = selection_sort(random_array.copy())
        selection_end = time.time()

        insertion_start = time.time()
        insertion_sorted = insertion_sort(random_array.copy())
        insertion_end = time.time()

        # Find best and worst case for insertion sort
        insertion_start_best = time.time()
        insertion_sort(insertion_sorted.copy())
        insertion_end_best = time.time()

        insertion_sorted_reverse = insertion_sorted[::-1]
        insertion_start_worst = time.time()
        insertion_sort(insertion_sorted_reverse.copy())
        insertion_end_worst = time.time()

       # Append the time differences to the respective lists
        select_diff.append(selection_end - selection_start)
        insert_diff.append(insertion_end - insertion_start)
        insert_diff_best.append(insertion_end_best - insertion_start_best)
        insert_diff_worst.append(insertion_end_worst - insertion_start_worst)
        number.append(i)

    # Make a plot of the time differences
    fig, ax = plt.subplots()
    ax.plot(number, insert_diff, label="Insertion Sort")
    ax.plot(number, select_diff, label="Selection Sort")
    ax.plot(number, insert_diff_best, label="Insertion Sort (Best Case)")
    ax.plot(number, insert_diff_worst, label="Insertion Sort (Worst Case)")

    ax.legend(loc="upper left")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (s)")
    plt.show()


if __name__ == "__main__":
    compare()
