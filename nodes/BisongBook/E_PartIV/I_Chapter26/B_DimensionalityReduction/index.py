# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Dimensionality Reduction with PCA
# To reduce the dimensions of the original dataset using PCA, we multiply the
# desired number of components or loadings from the eigenvector matrix, A, by the
# design matrix X. Suppose the design matrix (or the original dataset) has m rows (or
# observations) and p columns (or features), if we want to reduce the dimensions of
# the original dataset to two dimensions, we will multiply the original dataset X by
# the first two columns of the eigenvector matrix, Areduced. The result will be a reduced
# matrix of m rows and 2 columns.
#     If X is a m × p matrix and Areduced is a p × 2 matrix,
# 
#                                      Treduced = X m´ p ´ Ap´2
# 
# 
#     Observe that the result Treduced is a m × 2 matrix. Hence, T is a 2-D representation of
# the original dataset X as shown in Figure 26-2.
# 
# 
# 
# 
# Figure 26-2. Reducing the dimension of the original dataset
# 
#     In plotting the reduced dataset, the principal components are ranked in order of
# importance with the first principal component more prominent than the second and so
# on. Figure 26-3 illustrates a plot of the first two principal components.
# 
# 
# 
# 
# Figure 26-3. Visualize the principal components

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Dimensionality Reduction with PCA",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Dimensionality Reduction with PCA"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DimensionalityReduction(HierNode):
    def __init__(self):
        super().__init__("Dimensionality Reduction with PCA")
        self.add(Content())

# eof
