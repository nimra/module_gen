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

from .A_kMeansClustering.index import kMeansClustering as A_kMeansClustering
from .B_AgglomerativeClustering.index import AgglomerativeClustering as B_AgglomerativeClustering
from .C_DBSCAN.index import DBSCAN as C_DBSCAN
from .D_Comparingand.index import Comparingand as D_Comparingand
from .E_Summaryof.index import Summaryof as E_Summaryof

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# The result of t-SNE is quite remarkable. All the classes are quite clearly separated.
# The ones and nines are somewhat split up, but most of the classes form a single dense
# group. Keep in mind that this method has no knowledge of the class labels: it is com‐
# pletely unsupervised. Still, it can find a representation of the data in two dimensions
# that clearly separates the classes, based solely on how close points are in the original
# space.
# The t-SNE algorithm has some tuning parameters, though it often works well with
# the default settings. You can try playing with perplexity and early_exaggeration,
# but the effects are usually minor.
# 
# Clustering
# As we described earlier, clustering is the task of partitioning the dataset into groups,
# called clusters. The goal is to split up the data in such a way that points within a single
# cluster are very similar and points in different clusters are different. Similarly to clas‐
# sification algorithms, clustering algorithms assign (or predict) a number to each data
# point, indicating which cluster a particular point belongs to.
# 
# k-Means Clustering
# k-means clustering is one of the simplest and most commonly used clustering algo‐
# rithms. It tries to find cluster centers that are representative of certain regions of the
# data. The algorithm alternates between two steps: assigning each data point to the
# closest cluster center, and then setting each cluster center as the mean of the data
# points that are assigned to it. The algorithm is finished when the assignment of
# instances to clusters no longer changes. The following example (Figure 3-23) illus‐
# trates the algorithm on a synthetic dataset:
# In[47]:
#       mglearn.plots.plot_kmeans_algorithm()
# 
# 
# 
# 
# 168   | Chapter 3: Unsupervised Learning and Preprocessing
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Clustering",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Clustering(HierNode):
    def __init__(self):
        super().__init__("Clustering")
        self.add(Content(), "content")
        self.add(A_kMeansClustering())
        self.add(B_AgglomerativeClustering())
        self.add(C_DBSCAN())
        self.add(D_Comparingand())
        self.add(E_Summaryof())

# eof
