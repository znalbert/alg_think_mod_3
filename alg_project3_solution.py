"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster

######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a
    list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices
    for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the
    clusters cluster_list[idx1] and cluster_list[idx2] have minimum distance
    dist.
    """
    dist_tuple = (float("inf"), -1, -1)
    for cluster1 in range(0, len(cluster_list)):
        for cluster2 in range(cluster1 + 1, len(cluster_list)):
            dist = pair_distance(cluster_list, cluster1, cluster2)
            if dist[0] < dist_tuple[0]:
                dist_tuple = dist

    return dist_tuple


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal
    positions of their centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    cluster_list.sort(key = lambda cluster: cluster.horiz_center())
    clusters_len = len(cluster_list)

    if clusters_len <= 3:
        dist_tuple = slow_closest_pair(cluster_list)
    else:
        half_len = clusters_len / 2
        fcp1 = cluster_list[0 : half_len]
        fcp2 = cluster_list[half_len:]
        fcp_dist_tup1 = fast_closest_pair(fcp1)
        fcp_dist_tup2 = fast_closest_pair(fcp2)
        if fcp_dist_tup1[0] <= fcp_dist_tup2[0]:
            dist_tuple = fcp_dist_tup1
        else:
            dist_tuple = (fcp_dist_tup2[0],
                fcp_dist_tup2[1] + half_len,
                fcp_dist_tup2[2] + half_len)
        cl1_end = cluster_list[half_len - 1].horiz_center()
        cl2_begin = cluster_list[half_len].horiz_center()
        mid = (cl1_end + cl2_begin) / 2
        cps_dist_tup = closest_pair_strip(cluster_list, mid, dist_tuple[0])
        if dist_tuple[0] > cps_dist_tup[0]:
            dist_tuple = cps_dist_tup

    return dist_tuple


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal
    distance that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the
    clusters cluster_list[idx1] and cluster_list[idx2] lie in the strip and have
    minimum distance dist.
    """

    strip = []
    for cluster in range(0, len(cluster_list)):
        if abs(cluster_list[cluster].horiz_center() - horiz_center) < half_width:
            strip.append(cluster)
    strip.sort(key = lambda cluster: cluster_list[cluster].vert_center())
    len_strip = len(strip)
    dist_tuple = (float("inf"), -1, -1)
    for point1 in range(0, len_strip - 1):
        for point2 in range(point1 + 1, min(point1 + 4, len_strip)):
            dist = pair_distance(cluster_list, strip[point1], strip[point2])
            if dist_tuple[0] > dist[0]:
                dist_tuple = dist

    return dist_tuple



######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """

    while len(cluster_list) > num_clusters:
        closest = fast_closest_pair(cluster_list)
        to_merge = cluster_list.pop(closest[2])
        cluster_list[closest[1]].merge_clusters(to_merge)
    return cluster_list

######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of
    iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations

    len_clusters = len(cluster_list)

    centers = list(cluster_list)
    centers.sort(key = lambda cluster: cluster.total_population(), reverse=True)
    centers = centers[0:num_clusters]

    for _ in range(num_iterations):
        new_clusters = [alg_cluster.Cluster(set([]), 0, 0, 0, 0) for _ in range(num_clusters)]

        for cluster in range(len_clusters):
            dist_center = float("inf")
            num_center = -1
            for center in range(len(centers)):
                dist = cluster_list[cluster].distance(centers[center])
                if dist < dist_center:
                    dist_center = dist
                    num_center = center
            new_clusters[num_center].merge_clusters(cluster_list[cluster])

        for center in range(len(centers)):
            centers[center] = new_clusters[center]

    return centers
