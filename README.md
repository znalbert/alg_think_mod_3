# Comparison of Clustering Algorithms

In this assignment for Coursera's Algorthmic Thinking course we were to create two functions for clustering data into subsets of similar items.  We were then to analyze the performance of the functions in three areas:

* Efficiency
* Automation
* Quality

For the purposes of having data to perform operations on, we used data that correlated cancer risk by zip code in the United States.

## Clustering Algorithms
The two algorithms being analyzed were [hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering) and [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering).

### Hierarchical Clustering
The first function we were to create was one which performed the hierarchical clustering of data by first initializing all starting data points as a cluster, and then iteratively finding the two clusters with the closest centers and merging them.  This is done until we have only the number of desired clusters remaining.

### K-means Clustering
The second method involved initializing the desired number of clusters as empty clusters. For our purposes, we initialized the the desired empty clusters at locations that correlated to the highest population counties. The data is then clustered to those initial points by distance and the center is re-calculated. After this, the steps of clustering and re-centering is done a desired number of iterations.  

## Efficiency

![Plot of the function runtimes for hierarchical and k-means clustering algorithms](https://raw.githubusercontent.com/znalbert/alg_think_mod_3/master/img/runtimes.png)

Clear winner here is the k-means clustering function.  Asymptotically we can say that it's running at O(n) while the hierarchical algorithm is running at O(n<sup>2</sup>log<sup>2</sup>n).

## Automation

### Visualizing the Algorithms' data
Plot of hierarchical data for the 111 counties with the highest cancer rates clustered into nine regions:
![hierarchical Plot](https://raw.githubusercontent.com/znalbert/alg_think_mod_3/master/img/hierarchical-02-111-9.png)

Plot of k-means data for the 111 counties with the highest cancer rates clustered into nine regions
![K-means Plot](https://raw.githubusercontent.com/znalbert/alg_think_mod_3/master/img/kmeans-02-111-9-5.png)

Looking at the west coast we can already see some issues with the k-means graph clustering because of the initial given population centers in southern California should be one cluster and not two.  Mathematically, we can compute the distortion as the sum of the error for each cluster.  So, for the two plots we find that:

* Hierarchical Distortion: 1.752 x 10<sup>11</sup>
* K-means Distortion: 2.712 x 10<sup>11</sup>

Which leads me to believe that k-means requires a greater level of trial-and-error from a human trying to find a good set of starting points, whereas hierarchical can be left to run on its own, at least for this small dataset.

## Quality

### Distortion Comparison

Plot of distortions for 6 to 20 clusters on 111 counties.
![Plot of Distortions for 111 Counties](https://raw.githubusercontent.com/znalbert/alg_think_mod_3/master/img/distortions_111.png)

Plot of distortions for 6 to 20 clusters on 290 counties.
![Plot of Distortions for 290 Plot](https://raw.githubusercontent.com/znalbert/alg_think_mod_3/master/img/distortions_290.png)

Plot of distortions for 6 to 20 clusters on 896 counties.
![Plot of Distortions for 896 Plot](https://raw.githubusercontent.com/znalbert/alg_think_mod_3/master/img/distortions_896.png)

Initially, the hierarchical method clearly has the lower distortion, but as the dataset size increases we see that strength virtually evaporate.  Considering that I think scalability is important, I think that both the aspect of function speed and the positive trend in distortion values as dataset size increases would lead me to choose k-means as the superior clustering method.
