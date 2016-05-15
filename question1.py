"""
Assignment 3 - Question 1
"""

import alg_project3_solution as aps
import matplotlib.pyplot as plt

def plot_runtimes(fast, slow):
    """
    Plot an example with two curves with legends
    """
    y_values = range(2, 200)

    plt.plot(y_values, fast, '-b', label='fast_closest_pair')
    plt.plot(y_values, slow, '-r', label='slow_closest_pair')

    plt.legend(loc='upper left')
    plt.ylabel('Run Time')
    plt.xlabel('Number of Initial Clusters')
    plt.grid(True)
    plt.title('Comparison of Function Run Times\nPython Desktop Environment\n')
    plt.show()


fcp = aps.run_times(aps.fast_closest_pair)
scp = aps.run_times(aps.slow_closest_pair)

plot_runtimes(fcp, scp)
