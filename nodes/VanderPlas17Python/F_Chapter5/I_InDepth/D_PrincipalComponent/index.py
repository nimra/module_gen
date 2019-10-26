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
# The top row here shows the input images, while the bottom row shows the recon‐
# struction of the images from just 150 of the ~3,000 initial features. This visualization
# makes clear why the PCA feature selection used in “In-Depth: Support Vector
# Machines” on page 405 was so successful: although it reduces the dimensionality of
# the data by nearly a factor of 20, the projected images contain enough information
# that we might, by eye, recognize the individuals in the image. What this means is that
# our classification algorithm needs to be trained on 150-dimensional data rather than
# 3,000-dimensional data, which depending on the particular algorithm we choose, can
# lead to a much more efficient classification.
# 
# Principal Component Analysis Summary
# In this section we have discussed the use of principal component analysis for dimen‐
# sionality reduction, for visualization of high-dimensional data, for noise filtering, and
# for feature selection within high-dimensional data. Because of the versatility and
# interpretability of PCA, it has been shown to be effective in a wide variety of contexts
# and disciplines. Given any high-dimensional dataset, I tend to start with PCA in
# order to visualize the relationship between points (as we did with the digits), to
# understand the main variance in the data (as we did with the eigenfaces), and to
# understand the intrinsic dimensionality (by plotting the explained variance ratio).
# Certainly PCA is not useful for every high-dimensional dataset, but it offers a
# straightforward and efficient path to gaining insight into high-dimensional data.
# PCA’s main weakness is that it tends to be highly affected by outliers in the data. For
# this reason, many robust variants of PCA have been developed, many of which act to
# iteratively discard data points that are poorly described by the initial components.
# Scikit-Learn contains a couple interesting variants on PCA, including RandomizedPCA
# and SparsePCA, both also in the sklearn.decomposition submodule. Randomi
# zedPCA, which we saw earlier, uses a nondeterministic method to quickly approxi‐
# mate the first few principal components in very high-dimensional data, while
# SparsePCA introduces a regularization term (see “In Depth: Linear Regression” on
# page 390) that serves to enforce sparsity of the components.
# In the following sections, we will look at other unsupervised learning methods that
# build on some of the ideas of PCA.
# 
# In-Depth: Manifold Learning
# We have seen how principal component analysis can be used in the dimensionality
# reduction task—reducing the number of features of a dataset while maintaining the
# essential relationships between the points. While PCA is flexible, fast, and easily
# interpretable, it does not perform so well when there are nonlinear relationships
# within the data; we will see some examples of these below.
# 
# 
# 
#                                                             In-Depth: Manifold Learning   |   445
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Principal Component Analysis Summary",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PrincipalComponent(HierNode):
    def __init__(self):
        super().__init__("Principal Component Analysis Summary")
        self.add(Content())

# eof
