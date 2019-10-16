# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Effects of Regularization on Bias vs. Variance
# The higher the value of λ (i.e., the regularization parameter), the more restricted the
# coefficients (or weights) of the cost function. Hence, if the value of λ is high, the model
# can result in a learning bias (i.e., it underfits the dataset).
# 
#     However, if the value of λ approaches zero, the regularization parameter has
# negligible effects on the model, hence resulting in overfitting the model. Regularization
# is an important technique and should be used when injecting polynomial features into
# linear or logistic regression classifiers to learn non-linear relationships.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Effects of Regularization on Bias vs. Variance",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Effects of Regularization on Bias vs. Variance"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Effectsof(HierNode):
    def __init__(self):
        super().__init__("Effects of Regularization on Bias vs. Variance")
        self.add(Content())

# eof
