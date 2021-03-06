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
#                  Download from finelybook www.finelybook.com
#    Equation 8-4. LLE step 1: linearly modeling local relationships
#                          m              m                     2
#     � = argmin         ∑ ∥�i
#                       i=1
#                                    −    ∑ wi, j� j
#                                        j=1
#                                                           ∥
#                 �
#                                             j                                            i
#                     wi, j = 0      if �         is not one of the k c.n. of �
#     subject to       m
#                      ∑ wi, j = 1
#                     j=1
#                                    for i = 1, 2, ⋯, m
# 
# 
# After this step, the weight matrix � (containing the weights wi, j) encodes the local
# linear relationships between the training instances. Now the second step is to map the
# training instances into a d-dimensional space (where d < n) while preserving these
# local relationships as much as possible. If z(i) is the image of x(i) in this d-dimensional
#                                                                              j
# space, then we want the squared distance between z(i) and ∑m     j = 1 wi, j� to be as small
# as possible. This idea leads to the unconstrained optimization problem described in
# Equation 8-5. It looks very similar to the first step, but instead of keeping the instan‐
# ces fixed and finding the optimal weights, we are doing the reverse: keeping the
# weights fixed and finding the optimal position of the instances’ images in the low-
# dimensional space. Note that Z is the matrix containing all z(i).
# 
#    Equation 8-5. LLE step 2: reducing dimensionality while preserving relationships
#                      m             m                  2
#    � = argmin        ∑
#                     i=1
#                              i
#                           ∥� −     ∑
#                                  j=1
#                                         wi, j�
#                                                  j
#                                                      ∥
#             �
# 
# 
# Scikit-Learn’s LLE implementation has the following computational complexity:
# O(m log(m)n log(k)) for finding the k nearest neighbors, O(mnk3) for optimizing the
# weights, and O(dm2) for constructing the low-dimensional representations. Unfortu‐
# nately, the m2 in the last term makes this algorithm scale poorly to very large datasets.
# 
# Other Dimensionality Reduction Techniques
# There are many other dimensionality reduction techniques, several of which are
# available in Scikit-Learn. Here are some of the most popular:
# 
#   • Multidimensional Scaling (MDS) reduces dimensionality while trying to preserve
#     the distances between the instances (see Figure 8-13).
# 
# 
# 
# 
#                                                                   Other Dimensionality Reduction Techniques   |   223
# 
#                  Download from finelybook www.finelybook.com
#   • Isomap creates a graph by connecting each instance to its nearest neighbors, then
#     reduces dimensionality while trying to preserve the geodesic distances9 between
#     the instances.
#   • t-Distributed Stochastic Neighbor Embedding (t-SNE) reduces dimensionality
#     while trying to keep similar instances close and dissimilar instances apart. It is
#     mostly used for visualization, in particular to visualize clusters of instances in
#     high-dimensional space (e.g., to visualize the MNIST images in 2D).
#   • Linear Discriminant Analysis (LDA) is actually a classification algorithm, but dur‐
#     ing training it learns the most discriminative axes between the classes, and these
#     axes can then be used to define a hyperplane onto which to project the data. The
#     benefit is that the projection will keep classes as far apart as possible, so LDA is a
#     good technique to reduce dimensionality before running another classification
#     algorithm such as an SVM classifier.
# 
# 
# 
# 
# Figure 8-13. Reducing the Swiss roll to 2D using various techniques
# 
# Exercises
#  1. What are the main motivations for reducing a dataset’s dimensionality? What are
#     the main drawbacks?
#  2. What is the curse of dimensionality?
#  3. Once a dataset’s dimensionality has been reduced, is it possible to reverse the
#     operation? If so, how? If not, why?
#  4. Can PCA be used to reduce the dimensionality of a highly nonlinear dataset?
#  5. Suppose you perform PCA on a 1,000-dimensional dataset, setting the explained
#     variance ratio to 95%. How many dimensions will the resulting dataset have?
# 
# 
# 9 The geodesic distance between two nodes in a graph is the number of nodes on the shortest path between
#   these nodes.
# 
# 
# 
# 224   |   Chapter 8: Dimensionality Reduction
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Other Dimensionality Reduction Techniques",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OtherDimensionality(HierNode):
    def __init__(self):
        super().__init__("Other Dimensionality Reduction Techniques")
        self.add(Content(), "content")

# eof
