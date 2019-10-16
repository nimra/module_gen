# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Key Considerations for Performing PCA
# It is vital to perform mean normalization and feature scaling on the variables of features
# of the original dataset before implementing PCA. This is because unscaled features
# can have stretched and narrow distance n-dimensional space, and this has a huge
# consequence when finding the principal components that explain the variance of the
# dataset (see Figure 26-4).
# 
# 
# 
# 
# Figure 26-4. Right: An illustration of PCA with scaled features. Left: An
# illustration of PCA with unscaled features.
# 
#     Again mean normalization ensures that every attribute or feature of the dataset
# has a zero mean, while feature scaling ensures all the features are within the same
# numeric range.
#     Finally, PCA is susceptible to vary wildly due to slight perturbations or changes
# in the dataset.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Key Considerations for Performing PCA",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Key Considerations for Performing PCA"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class KeyConsiderations(HierNode):
    def __init__(self):
        super().__init__("Key Considerations for Performing PCA")
        self.add(Content())

# eof
