"""
Assignment 3 - Question 1
"""

import matplotlib.pyplot as plt
import alg_project3_viz as viz
import alg_project3_solution as sol

data_table = viz.load_data_table(viz.DATA_111_URL)
hier_cluster_list = sol.make_data_list(data_table)
kmeans_cluster_list = sol.make_data_list(data_table)


def compute_hier_distortions(cluster_list):
    distortions = []

    for iteration in range(20, 5, -1):
        new_list = sol.hierarchical_clustering(cluster_list, iteration)
        cluster_list = new_list
        distortions.append(sol.compute_distortion(new_list, data_table))

    distortions.reverse()
    return distortions


def compute_kmeans_distortions(cluster_list):
    distortions = []

    for iteration in range(6, 21):
        new_list = sol.kmeans_clustering(cluster_list, iteration, 5)
        distortions.append(sol.compute_distortion(new_list, data_table))

    return distortions


def plot_distortions(hierarchical_data, kmeans_data):
    """
    Plot an example with two curves with legends
    """
    y_values = range(6, 21)

    plt.plot(y_values, hierarchical_data, '-b', label='hierarchical_clustering')
    plt.plot(y_values, kmeans_data, '-r', label='kmeans_clustering')

    plt.legend(loc='upper right')
    plt.ylabel('Distortion')
    plt.xlabel('Number of Clusters')
    plt.grid(True)
    plt.title('Comparison of Function Distortions for 111 Data Points\nPython Desktop Environment\n')
    plt.show()



hier_distortions = compute_hier_distortions(hier_cluster_list)
kmeans_distortions = compute_kmeans_distortions(kmeans_cluster_list)

plot_distortions(hier_distortions, kmeans_distortions)
