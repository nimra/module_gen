# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# How Does Regularization Work
# During model building, the regularization parameter λ is calibrated to determine how
# much the magnitude of other features in the model is adjusted when training the model.
# The higher the value of the regularization, the more the magnitude of the feature weights
# is reduced.
#      If the regularization parameter is set too close to zero, it reduces the regularization
# effect on the feature weights of the model. At zero, the penalty the regularization term
# imposes is virtually non-existent, and the model is as if the regularization term was
# never present.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "How Does Regularization Work",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# How Does Regularization Work"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HowDoes(HierNode):
    def __init__(self):
        super().__init__("How Does Regularization Work")
        self.add(Content())

# eof
