# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_KMeansClustering.index import KMeansClustering as A_KMeansClustering
from .B_KMeansClustering.index import KMeansClustering as B_KMeansClustering
from .C_HierarchicalClustering.index import HierarchicalClustering as C_HierarchicalClustering
from .D_HierarchicalClustering.index import HierarchicalClustering as D_HierarchicalClustering

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
    mbk("Clustering is an unsupervised machine learning technique for grouping homogeneous data points into partitions called clusters. In the example dataset illustrated in Figure 25-­1, suppose we have a set of n points and 2 features. A clustering algorithm can be applied to determine the number of distinct subclasses or groups among the data samples."),
    ibk(None, "Figure 25-1. An illustration of clustering in a 2-D space"),
    mbk("Clustering a 2-D dataset as seen in Figure 25-1 is relatively trivial. The real challenge arises when we have to perform clustering in higher-dimensional spaces. The question now is how do we ascertain or find out if a set of points are similar or if a set of points should be in the same group? In this section, we would cover two essential types of clustering algorithms known as k-means clustering and hierarchical clustering."),
    mbk("K-means clustering is used when the number of anticipated distinct classes or sub-­groups is known in advance. In hierarchical clustering, the exact number of clusters is not known, and the algorithm is tasked to find the optimal number of heterogeneous sub-groups in the dataset."),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 25: Clustering",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 25: Clustering"))
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter25(HierNode):
    def __init__(self):
        super().__init__("Chapter 25: Clustering")
        self.add(Content())
        self.add(A_KMeansClustering())
        self.add(B_KMeansClustering())
        self.add(C_HierarchicalClustering())
        self.add(D_HierarchicalClustering())

# eof
