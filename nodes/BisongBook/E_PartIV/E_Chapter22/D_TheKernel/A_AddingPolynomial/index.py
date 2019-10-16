# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Adding Polynomial Features
# The feature space of the dataset can be extended by adding higher-order polynomial
# terms or interaction terms. For example, instead of training the classifier with linear
# features, we can add polynomial features or add interaction terms to our model.
#     Depending on the dimensions of the dataset, the combinations for extending
# the feature space can quickly become unmanageable, and this can easily lead to a
# model that overfits the test set and also become expensive to compute with a larger
# feature space.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Adding Polynomial Features",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Adding Polynomial Features"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AddingPolynomial(HierNode):
    def __init__(self):
        super().__init__("Adding Polynomial Features")
        self.add(Content())

# eof
