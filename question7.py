"""
Assignment 3 Question 7 Answer
"""

import alg_project3_viz as viz
import alg_project3_solution as sol
import alg_cluster

data_table = viz.load_data_table(viz.DATA_111_URL)

hier_data_list = sol.make_data_list(data_table)
kmeans_data_list = sol.make_data_list(data_table)

hier_cluster_list = sol.hierarchical_clustering(hier_data_list, 9)
kmeans_cluster_list = sol.kmeans_clustering(kmeans_data_list, 9, 5)

print("hierarchical:", sol.compute_distortion(hier_cluster_list, data_table))
print("kmeans:", sol.compute_distortion(kmeans_cluster_list, data_table))


# Hierarchical: 175163886915.8305 or 1.752 x 10^11 with four significant figures
# K-means: 271254226924.20047 or 2.712 x 10^11
