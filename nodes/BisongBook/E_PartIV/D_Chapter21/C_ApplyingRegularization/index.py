# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_LinearRegression.index import LinearRegression as A_LinearRegression
from .B_LogisticRegression.index import LogisticRegression as B_LogisticRegression

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Applying Regularization to Models with Scikit-learn
# The technique of adding a penalty to restrain the values of the parameters of the model
# is also known as Ridge regression or Tikhonov regularization. In this section we will
# build a linear and logistic regression model with regularization.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Applying Regularization to Models with Scikit-learn",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Applying Regularization to Models with Scikit-learn"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ApplyingRegularization(HierNode):
    def __init__(self):
        super().__init__("Applying Regularization to Models with Scikit-learn")
        self.add(Content())
        self.add(A_LinearRegression())
        self.add(B_LogisticRegression())

# eof
