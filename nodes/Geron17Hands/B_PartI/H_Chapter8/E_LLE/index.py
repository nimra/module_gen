# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# You may be wondering how to perform this reconstruction. One solution is to train a
# supervised regression model, with the projected instances as the training set and the
# original instances as the targets. Scikit-Learn will do this automatically if you set
# fit_inverse_transform=True, as shown in the following code:7
#     rbf_pca = KernelPCA(n_components = 2, kernel="rbf", gamma=0.0433,
#                         fit_inverse_transform=True)
#     X_reduced = rbf_pca.fit_transform(X)
#     X_preimage = rbf_pca.inverse_transform(X_reduced)
# 
# 
#                    By default, fit_inverse_transform=False and KernelPCA has no
#                    inverse_transform() method. This method only gets created
#                    when you set fit_inverse_transform=True.
# 
# 
# 
# You can then compute the reconstruction pre-image error:
#     >>> from sklearn.metrics import mean_squared_error
#     >>> mean_squared_error(X, X_preimage)
#     32.786308795766132
# Now you can use grid search with cross-validation to find the kernel and hyperpara‐
# meters that minimize this pre-image reconstruction error.
# 
# LLE
# Locally Linear Embedding (LLE)8 is another very powerful nonlinear dimensionality
# reduction (NLDR) technique. It is a Manifold Learning technique that does not rely
# on projections like the previous algorithms. In a nutshell, LLE works by first measur‐
# ing how each training instance linearly relates to its closest neighbors (c.n.), and then
# looking for a low-dimensional representation of the training set where these local
# relationships are best preserved (more details shortly). This makes it particularly
# good at unrolling twisted manifolds, especially when there is not too much noise.
# For example, the following code uses Scikit-Learn’s LocallyLinearEmbedding class to
# unroll the Swiss roll. The resulting 2D dataset is shown in Figure 8-12. As you can
# see, the Swiss roll is completely unrolled and the distances between instances are
# locally well preserved. However, distances are not preserved on a larger scale: the left
# part of the unrolled Swiss roll is squeezed, while the right part is stretched. Neverthe‐
# less, LLE did a pretty good job at modeling the manifold.
# 
# 
# 7 Scikit-Learn uses the algorithm based on Kernel Ridge Regression described in Gokhan H. Bakır, Jason
#   Weston, and Bernhard Scholkopf, “Learning to Find Pre-images” (Tubingen, Germany: Max Planck Institute
#   for Biological Cybernetics, 2004).
# 8 “Nonlinear Dimensionality Reduction by Locally Linear Embedding,” S. Roweis, L. Saul (2000).
# 
# 
# 
#                                                                                                  LLE     |   221
# 
#                        Download from finelybook www.finelybook.com
#       from sklearn.manifold import LocallyLinearEmbedding
# 
#       lle = LocallyLinearEmbedding(n_components=2, n_neighbors=10)
#       X_reduced = lle.fit_transform(X)
# 
# 
# 
# 
# Figure 8-12. Unrolled Swiss roll using LLE
# 
# Here’s how LLE works: first, for each training instance x(i), the algorithm identifies its
# k closest neighbors (in the preceding code k = 10), then tries to reconstruct x(i) as a
# linear function of these neighbors. More specifically, it finds the weights wi,j such that
#                                                            j
# the squared distance between x(i) and ∑m      j = 1 wi, j�   is as small as possible, assuming
# wi,j = 0 if x(j) is not one of the k closest neighbors of x(i). Thus the first step of LLE is
# the constrained optimization problem described in Equation 8-4, where W is the
# weight matrix containing all the weights wi,j. The second constraint simply normalizes
# the weights for each training instance x(i).
# 
# 
# 
# 
# 222   |   Chapter 8: Dimensionality Reduction
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "LLE",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# LLE"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LLE(HierNode):
    def __init__(self):
        super().__init__("LLE")
        self.add(Content())

# eof