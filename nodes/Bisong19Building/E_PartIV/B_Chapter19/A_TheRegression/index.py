# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_AVisual.index import AVisual as A_AVisual
from .B_Findingthe.index import Findingthe as B_Findingthe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The Regression Model
# In linear regression, the prevailing assumption is that the target variable (i.e., the unit
# that we want to predict) can be modeled as a linear combination of the features.
#      A linear combination is simply the addition of a certain number of vectors that are
# scaled (or adjusted) by some arbitrary constant. A vector is a mathematical construct for
# representing a set of numbers.
#      For example, let us assume a randomly generated dataset consisting of two features
# and a target variable. The dataset has 50 observations (see Figure 19-1).
# 
# Figure 19-1. Sample dataset
# 
#       The vectors of this dataset are
# 
#          x1 = [ 40 31 81 57¼66 ] , x 2 = [73 5918 69¼20 ] , y = [105145128 116¼144 ]
# 
# 
#     In a linear regression model, every feature has an assigned “weight.” We can say
# that the weight parameterizes each feature in the dataset. The weights in the dataset are
# adjusted to take on values that capture the underlying relationship between the features
# that optimally approximate the target variable. The linear regression model is formally
# written as
# 
#                                    ŷ = q 0 + q1 x1 + q 2 x 2 +¼+ qn xn
# 
#       where
# 
#         •   ŷ (pronounced y-hat) is the approximate value of the output y that
#             we want to predict.
# 
#         •   θi, where i = {1, 2, …n}, is the weight assigned to each feature in the
#             dataset. The notation n is the size of features of the dataset.
# 
#         •   θ0 represents the “bias” term.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Regression Model",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# The Regression Model"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheRegression(HierNode):
    def __init__(self):
        super().__init__("The Regression Model")
        self.add(Content())
        self.add(A_AVisual())
        self.add(B_Findingthe())

# eof
