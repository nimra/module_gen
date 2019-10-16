# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Considerationsfor.index import Considerationsfor as A_Considerationsfor
from .B_Considerationsfor.index import Considerationsfor as B_Considerationsfor

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# K-Means Clustering
# k-Means clustering is one of the most famous and widely used clustering algorithms
# in practice. It works by using a distance measurement (most commonly the
# Euclidean distance) to iteratively assign data points in a hyperspace to a set of non-
# overlapping clusters.
#     In K-means, the anticipated number of clusters, K, is chosen at the onset. The
# clusters are initialized by arbitrarily selecting at random one of the data points as
# an initial cluster for each K. The algorithm now works by iteratively assigning each
# point in the space to the cluster centroid that it is nearest to using the distance
# measurement.
#     After all the points have been assigned to their closest cluster point, the cluster
# centroid is adjusted to find a new center among the points in the cluster. This process is
# repeated until the algorithm converges, that is, when the cluster centroids stabilize and
# points do not readily swap clusters after every reassignment. These steps are illustrated
# in Figure 25-2.
# 
# 
# 
# 
# Figure 25-2. An illustration of k-means clustering with k = 2. Top left: Randomly
# pick a point for each k. Top right: Iteratively assign each point to its closest cluster
# centroid. Bottom: Update the cluster centroids for each of the k clusters. Typically,
# we repeat the iterative assignment of all the points and update the cluster centroid
# until the algorithm resolves in a stable clustering.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "K-Means Clustering",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# K-Means Clustering"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class KMeansClustering(HierNode):
    def __init__(self):
        super().__init__("K-Means Clustering")
        self.add(Content())
        self.add(A_Considerationsfor())
        self.add(B_Considerationsfor())

# eof
