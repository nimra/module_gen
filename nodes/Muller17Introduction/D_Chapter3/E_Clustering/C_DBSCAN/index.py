# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# The y-axis in the dendrogram doesn’t just specify when in the agglomerative algo‐
# rithm two clusters get merged. The length of each branch also shows how far apart
# the merged clusters are. The longest branches in this dendrogram are the three lines
# that are marked by the dashed line labeled “three clusters.” That these are the longest
# branches indicates that going from three to two clusters meant merging some very
# far-apart points. We see this again at the top of the chart, where merging the two
# remaining clusters into a single cluster again bridges a relatively large distance.
# Unfortunately, agglomerative clustering still fails at separating complex shapes like
# the two_moons dataset. But the same is not true for the next algorithm we will look at,
# DBSCAN.
# 
# DBSCAN
# Another very useful clustering algorithm is DBSCAN (which stands for “density-
# based spatial clustering of applications with noise”). The main benefits of DBSCAN
# are that it does not require the user to set the number of clusters a priori, it can cap‐
# ture clusters of complex shapes, and it can identify points that are not part of any
# cluster. DBSCAN is somewhat slower than agglomerative clustering and k-means, but
# still scales to relatively large datasets.
# DBSCAN works by identifying points that are in “crowded” regions of the feature
# space, where many data points are close together. These regions are referred to as
# dense regions in feature space. The idea behind DBSCAN is that clusters form dense
# regions of data, separated by regions that are relatively empty.
# Points that are within a dense region are called core samples (or core points), and they
# are defined as follows. There are two parameters in DBSCAN: min_samples and eps.
# If there are at least min_samples many data points within a distance of eps to a given
# data point, that data point is classified as a core sample. Core samples that are closer
# to each other than the distance eps are put into the same cluster by DBSCAN.
# The algorithm works by picking an arbitrary point to start with. It then finds all
# points with distance eps or less from that point. If there are less than min_samples
# points within distance eps of the starting point, this point is labeled as noise, meaning
# that it doesn’t belong to any cluster. If there are more than min_samples points within
# a distance of eps, the point is labeled a core sample and assigned a new cluster label.
# Then, all neighbors (within eps) of the point are visited. If they have not been
# assigned a cluster yet, they are assigned the new cluster label that was just created. If
# they are core samples, their neighbors are visited in turn, and so on. The cluster
# grows until there are no more core samples within distance eps of the cluster. Then
# another point that hasn’t yet been visited is picked, and the same procedure is
# repeated.
# 
# 
# 
#                                                                          Clustering   |   187
# 
# In the end, there are three kinds of points: core points, points that are within distance
# eps of core points (called boundary points), and noise. When the DBSCAN algorithm
# is run on a particular dataset multiple times, the clustering of the core points is always
# the same, and the same points will always be labeled as noise. However, a boundary
# point might be neighbor to core samples of more than one cluster. Therefore, the
# cluster membership of boundary points depends on the order in which points are vis‐
# ited. Usually there are only few boundary points, and this slight dependence on the
# order of points is not important.
# Let’s apply DBSCAN on the synthetic dataset we used to demonstrate agglomerative
# clustering. Like agglomerative clustering, DBSCAN does not allow predictions on
# new test data, so we will use the fit_predict method to perform clustering and
# return the cluster labels in one step:
# In[65]:
#       from sklearn.cluster import DBSCAN
#       X, y = make_blobs(random_state=0, n_samples=12)
# 
#       dbscan = DBSCAN()
#       clusters = dbscan.fit_predict(X)
#       print("Cluster memberships:\n{}".format(clusters))
# 
# Out[65]:
#       Cluster memberships:
#       [-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1]
# 
# As you can see, all data points were assigned the label -1, which stands for noise. This
# is a consequence of the default parameter settings for eps and min_samples, which
# are not tuned for small toy datasets. The cluster assignments for different values of
# min_samples and eps are shown below, and visualized in Figure 3-37:
# In[66]:
#       mglearn.plots.plot_dbscan()
# 
# Out[66]:
#       min_samples:     2   eps:   1.000000    cluster:    [-1 0     0 -1    0 -1    1 1 0     1 -1 -1]
#       min_samples:     2   eps:   1.500000    cluster:    [0 1 1   1 1 0   2 2 1   2 2 0]
#       min_samples:     2   eps:   2.000000    cluster:    [0 1 1   1 1 0   0 0 1   0 0 0]
#       min_samples:     2   eps:   3.000000    cluster:    [0 0 0   0 0 0   0 0 0   0 0 0]
#       min_samples:     3   eps:   1.000000    cluster:    [-1 0     0 -1    0 -1    1 1 0     1 -1 -1]
#       min_samples:     3   eps:   1.500000    cluster:    [0 1 1   1 1 0   2 2 1   2 2 0]
#       min_samples:     3   eps:   2.000000    cluster:    [0 1 1   1 1 0   0 0 1   0 0 0]
#       min_samples:     3   eps:   3.000000    cluster:    [0 0 0   0 0 0   0 0 0   0 0 0]
#       min_samples:     5   eps:   1.000000    cluster:    [-1 -1   -1 -1   -1 -1   -1 -1 -1   -1 -1 -1]
#       min_samples:     5   eps:   1.500000    cluster:    [-1 0     0 0     0 -1   -1 -1 0    -1 -1 -1]
#       min_samples:     5   eps:   2.000000    cluster:    [-1 0     0 0     0 -1   -1 -1 0    -1 -1 -1]
#       min_samples:     5   eps:   3.000000    cluster:    [0 0 0   0 0 0   0 0 0   0 0 0]
# 
# 
# 
# 188   |   Chapter 3: Unsupervised Learning and Preprocessing
# 
# Figure 3-37. Cluster assignments found by DBSCAN with varying settings for the
# min_samples and eps parameters
# 
# In this plot, points that belong to clusters are solid, while the noise points are shown
# in white. Core samples are shown as large markers, while boundary points are dis‐
# played as smaller markers. Increasing eps (going from left to right in the figure)
# means that more points will be included in a cluster. This makes clusters grow, but
# might also lead to multiple clusters joining into one. Increasing min_samples (going
# from top to bottom in the figure) means that fewer points will be core points, and
# more points will be labeled as noise.
# The parameter eps is somewhat more important, as it determines what it means for
# points to be “close.” Setting eps to be very small will mean that no points are core
# samples, and may lead to all points being labeled as noise. Setting eps to be very large
# will result in all points forming a single cluster.
# The min_samples setting mostly determines whether points in less dense regions will
# be labeled as outliers or as their own clusters. If you decrease min_samples, anything
# that would have been a cluster with less than min_samples many samples will now be
# labeled as noise. min_samples therefore determines the minimum cluster size. You
# can see this very clearly in Figure 3-37, when going from min_samples=3 to min_sam
# ples=5 with eps=1.5. With min_samples=3, there are three clusters: one of four
# 
# 
#                                                                          Clustering   |   189
# 
# points, one of five points, and one of three points. Using min_samples=5, the two
# smaller clusters (with three and four points) are now labeled as noise, and only the
# cluster with five samples remains.
# While DBSCAN doesn’t require setting the number of clusters explicitly, setting eps
# implicitly controls how many clusters will be found. Finding a good setting for eps is
# sometimes easier after scaling the data using StandardScaler or MinMaxScaler, as
# using these scaling techniques will ensure that all features have similar ranges.
# Figure 3-38 shows the result of running DBSCAN on the two_moons dataset. The
# algorithm actually finds the two half-circles and separates them using the default
# settings:
# In[67]:
#       X, y = make_moons(n_samples=200, noise=0.05, random_state=0)
# 
#       # rescale the data to zero mean and unit variance
#       scaler = StandardScaler()
#       scaler.fit(X)
#       X_scaled = scaler.transform(X)
# 
#       dbscan = DBSCAN()
#       clusters = dbscan.fit_predict(X_scaled)
#       # plot the cluster assignments
#       plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap=mglearn.cm2, s=60)
#       plt.xlabel("Feature 0")
#       plt.ylabel("Feature 1")
# As the algorithm produced the desired number of clusters (two), the parameter set‐
# tings seem to work well. If we decrease eps to 0.2 (from the default of 0.5), we will
# get eight clusters, which is clearly too many. Increasing eps to 0.7 results in a single
# cluster.
# When using DBSCAN, you need to be careful about handling the returned cluster
# assignments. The use of -1 to indicate noise might result in unexpected effects when
# using the cluster labels to index another array.
# 
# 
# 
# 
# 190   |   Chapter 3: Unsupervised Learning and Preprocessing
# 
# Figure 3-38. Cluster assignment found by DBSCAN using the default value of eps=0.5
# 
# Comparing and Evaluating Clustering Algorithms
# One of the challenges in applying clustering algorithms is that it is very hard to assess
# how well an algorithm worked, and to compare outcomes between different algo‐
# rithms. After talking about the algorithms behind k-means, agglomerative clustering,
# and DBSCAN, we will now compare them on some real-world datasets.
# 
# Evaluating clustering with ground truth
# There are metrics that can be used to assess the outcome of a clustering algorithm
# relative to a ground truth clustering, the most important ones being the adjusted rand
# index (ARI) and normalized mutual information (NMI), which both provide a quanti‐
# tative measure between 0 and 1.
# Here, we compare the k-means, agglomerative clustering, and DBSCAN algorithms
# using ARI. We also include what it looks like when we randomly assign points to two
# clusters for comparison (see Figure 3-39):
# 
# 
# 
# 
#                                                                          Clustering   |   191
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "DBSCAN",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DBSCAN(HierNode):
    def __init__(self):
        super().__init__("DBSCAN")
        self.add(Content(), "content")

# eof
