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
# Figure 3-47. Images from selected clusters found by agglomerative clustering when set‐
# ting the number of clusters to 40—the text to the left shows the index of the cluster and
# the total number of points in the cluster
# 
# Here, the clustering seems to have picked up on “dark skinned and smiling,” “collared
# shirt,” “smiling woman,” “Hussein,” and “high forehead.” We could also find these
# highly similar clusters using the dendrogram, if we did more a detailed analysis.
# 
# Summary of Clustering Methods
# This section has shown that applying and evaluating clustering is a highly qualitative
# procedure, and often most helpful in the exploratory phase of data analysis. We
# looked at three clustering algorithms: k-means, DBSCAN, and agglomerative cluster‐
# ing. All three have a way of controlling the granularity of clustering. k-means and
# agglomerative clustering allow you to specify the number of desired clusters, while
# DBSCAN lets you define proximity using the eps parameter, which indirectly influ‐
# ences cluster size. All three methods can be used on large, real-world datasets, are rel‐
# atively easy to understand, and allow for clustering into many clusters.
# Each of the algorithms has somewhat different strengths. k-means allows for a char‐
# acterization of the clusters using the cluster means. It can also be viewed as a decom‐
# position method, where each data point is represented by its cluster center. DBSCAN
# allows for the detection of “noise points” that are not assigned any cluster, and it can
# help automatically determine the number of clusters. In contrast to the other two
# methods, it allow for complex cluster shapes, as we saw in the two_moons example.
# DBSCAN sometimes produces clusters of very differing size, which can be a strength
# or a weakness. Agglomerative clustering can provide a whole hierarchy of possible
# partitions of the data, which can be easily inspected via dendrograms.
# 
# 
# 
# 
#                                                                            Clustering   |   207
# 
# Summary and Outlook
# This chapter introduced a range of unsupervised learning algorithms that can be
# applied for exploratory data analysis and preprocessing. Having the right representa‐
# tion of the data is often crucial for supervised or unsupervised learning to succeed,
# and preprocessing and decomposition methods play an important part in data prepa‐
# ration.
# Decomposition, manifold learning, and clustering are essential tools to further your
# understanding of your data, and can be the only ways to make sense of your data in
# the absence of supervision information. Even in a supervised setting, exploratory
# tools are important for a better understanding of the properties of the data. Often it is
# hard to quantify the usefulness of an unsupervised algorithm, though this shouldn’t
# deter you from using them to gather insights from your data. With these methods
# under your belt, you are now equipped with all the essential learning algorithms that
# machine learning practitioners use every day.
# We encourage you to try clustering and decomposition methods both on two-
# dimensional toy data and on real-world datasets included in scikit-learn, like the
# digits, iris, and cancer datasets.
# 
# 
# 
# 
# 208   |   Chapter 3: Unsupervised Learning and Preprocessing
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Summary of Clustering Methods",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Summaryof(HierNode):
    def __init__(self):
        super().__init__("Summary of Clustering Methods")
        self.add(Content(), "content")

# eof
