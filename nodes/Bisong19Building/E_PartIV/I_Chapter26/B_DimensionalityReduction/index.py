# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
    mbk("To reduce the dimensions of the original dataset using PCA, we multiply the desired number of components or loadings from the eigenvector matrix, A, by the design matrix X. Suppose the design matrix (or the original dataset) has m rows (or observations) and p columns (or features), if we want to reduce the dimensions of the original dataset to two dimensions, we will multiply the original dataset X by the first two columns of the eigenvector matrix, Areduced. The result will be a reduced matrix of m rows and 2 columns."),
    mbk("If X is a m × p matrix and Areduced is a p × 2 matrix,"),
    mbk("$$ T_{reduced} = X_{m \\times p} \\times A_{p \\times 2} $$"),
    mbk("Observe that the result Treduced is a m × 2 matrix. Hence, T is a 2-D representation of the original dataset X as shown in Figure 26-2."),
    ibk(None, "Figure 26-2. Reducing the dimension of the original dataset"),
    mbk("In plotting the reduced dataset, the principal components are ranked in order of importance with the first principal component more prominent than the second and so on. Figure 26-3 illustrates a plot of the first two principal components."),
    ibk(None, "Figure 26-3. Visualize the principal components"),
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Dimensionality Reduction with PCA",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Dimensionality Reduction with PCA"))
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DimensionalityReduction(HierNode):
    def __init__(self):
        super().__init__("Dimensionality Reduction with PCA")
        self.add(Content())

# eof
