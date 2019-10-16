# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Introducing the Logit or Sigmoid Model
# The logistic function, also known as the logit or the sigmoid function, is responsible
# for constraining the output of the cost function so that it becomes a probability output
# between 0 and 1. The sigmoid function is formally written as
# 
#                                                         1
#                                         h (t ) =
#                                                      1 + e -t
# 
#     The logistic regression model is formally similar to the linear regression model
# except that it is acted upon by the sigmoid model. The following is the formal
# representation:
# 
#                                ŷ = q 0 + q1 x1 + q 2 x 2 +¼+ qn xn
# 
# 
#                                                        1
#                                         h ( yˆ ) =
#                                                      1+ e-y
#                                                           ˆ
# 
# 
# 
# 
# where 0 ≤ h(t) ≤ 1. The sigmoid function is graphically shown in Figure 20-4.
# 
# 
# 
# 
# Figure 20-4. Logistic function
# 
#     The sigmoid function, which looks like an S curve, rises from 0 and plateaus at 1.
# From the sigmoid function shown in Figure 20-4, as ŷ increases to positive infinity, the
# sigmoid output gets closer to 1, and as t decreases toward negative infinity, the sigmoid
# function outputs 0.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Introducing the Logit or Sigmoid Model",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Introducing the Logit or Sigmoid Model"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Introducingthe(HierNode):
    def __init__(self):
        super().__init__("Introducing the Logit or Sigmoid Model")
        self.add(Content())

# eof
