# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hierarchical Clustering with the SciPy Package
# This example implements hierarchical or agglomerative clustering with SciPy. The
# ‘scipy.cluster.hierarchy’ package has simple methods for performing hierarchical
# clustering and plotting dendrograms. This example uses the ‘complete’ linkage method.
# The plot of the dendrogram is shown in Figure 25-10.
# 
# # import packages
# import matplotlib.pyplot as plt
# from scipy.cluster.hierarchy import dendrogram
# from scipy.cluster import hierarchy
# 
# Z = hierarchy.linkage(X, method='complete')
# 
# plt.figure()
# dn = hierarchy.dendrogram(Z, truncate_mode='lastp')
# 
# 
# 
# 
# 
# Figure 25-10. Dendrogram produced by hierarchical clustering
# 
#      This chapter reviewed the pros and cons of K-means and hierarchical clustering.
# Both hierarchical and K-means are susceptible to perturbations in the dataset and can
# give very different results if a few data points are removed or added. Also, it is crucial
# to standardize the dataset features (i.e., to subtract each element in the feature from its
# mean and divide by its standard deviation or by the range) before performing clustering.
# This ensures that the features are within similar numeric bounds and have tempered or
# measured distances in the feature space.
#      The results of these clustering algorithms also depend on a wide range of
# considerations such as the choice of K for K-means, and for hierarchical clustering, the
# choice of dissimilarity measure, the type of linkage, and where to cut the dendrogram
# all affect the final result of the clusters. Hence, to get the best out of clustering, it is best
# to perform a grid search and try out all these different configurations in order to get
# a measured view on the robustness of the results before applying into your learning
# pipeline or using as a model to explain the dataset.
#      In the next chapter, we will discuss principal component analysis (PCA) as an
# unsupervised machine learning algorithm for finding low-dimensional feature sub-­
# spaces that capture the variability in the dataset.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Hierarchical Clustering with the SciPy Package",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Hierarchical Clustering with the SciPy Package"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HierarchicalClustering(HierNode):
    def __init__(self):
        super().__init__("Hierarchical Clustering with the SciPy Package")
        self.add(Content())

# eof
