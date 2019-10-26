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

from .A_IntroducingkMeans.index import IntroducingkMeans as A_IntroducingkMeans
from .B_kMeansAlgorithm.index import kMeansAlgorithm as B_kMeansAlgorithm
from .C_Examples.index import Examples as C_Examples

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# Figure 5-109. Isomap embedding of only the 1s within the digits data
# 
# The result gives you an idea of the variety of forms that the number “1” can take
# within the dataset. The data lies along a broad curve in the projected space, which
# appears to trace the orientation of the digit. As you move up the plot, you find ones
# that have hats and/or bases, though these are very sparse within the dataset. The pro‐
# jection lets us identify outliers that have data issues (i.e., pieces of the neighboring
# digits that snuck into the extracted images).
# Now, this in itself may not be useful for the task of classifying digits, but it does help
# us get an understanding of the data, and may give us ideas about how to move for‐
# ward, such as how we might want to preprocess the data before building a classifica‐
# tion pipeline.
# 
# In Depth: k-Means Clustering
# In the previous few sections, we have explored one category of unsupervised machine
# learning models: dimensionality reduction. Here we will move on to another class of
# unsupervised machine learning models: clustering algorithms. Clustering algorithms
# 
# 
# 462   | Chapter 5: Machine Learning
# 
# seek to learn, from the properties of the data, an optimal division or discrete labeling
# of groups of points.
# Many clustering algorithms are available in Scikit-Learn and elsewhere, but perhaps
# the simplest to understand is an algorithm known as k-means clustering, which is
# implemented in sklearn.cluster.KMeans. We begin with the standard imports:
#     In[1]: %matplotlib inline
#            import matplotlib.pyplot as plt
#            import seaborn as sns; sns.set()    # for plot styling
#            import numpy as np
# 
# 
# Introducing k-Means
# The k-means algorithm searches for a predetermined number of clusters within an
# unlabeled multidimensional dataset. It accomplishes this using a simple conception of
# what the optimal clustering looks like:
# 
#   • The “cluster center” is the arithmetic mean of all the points belonging to the
#     cluster.
#   • Each point is closer to its own cluster center than to other cluster centers.
# 
# Those two assumptions are the basis of the k-means model. We will soon dive into
# exactly how the algorithm reaches this solution, but for now let’s take a look at a sim‐
# ple dataset and see the k-means result.
# First, let’s generate a two-dimensional dataset containing four distinct blobs. To
# emphasize that this is an unsupervised algorithm, we will leave the labels out of the
# visualization (Figure 5-110):
#     In[2]: from sklearn.datasets.samples_generator import make_blobs
#            X, y_true = make_blobs(n_samples=300, centers=4,
#                                   cluster_std=0.60, random_state=0)
#            plt.scatter(X[:, 0], X[:, 1], s=50);
# By eye, it is relatively easy to pick out the four clusters. The k-means algorithm does
# this automatically, and in Scikit-Learn uses the typical estimator API:
#     In[3]: from sklearn.cluster import KMeans
#            kmeans = KMeans(n_clusters=4)
#            kmeans.fit(X)
#            y_kmeans = kmeans.predict(X)
# 
# 
# 
# 
#                                                             In Depth: k-Means Clustering   |   463
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "In Depth: k-Means Clustering",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class InDepth(HierNode):
    def __init__(self):
        super().__init__("In Depth: k-Means Clustering")
        self.add(Content())
        self.add(A_IntroducingkMeans())
        self.add(B_kMeansAlgorithm())
        self.add(C_Examples())

# eof
