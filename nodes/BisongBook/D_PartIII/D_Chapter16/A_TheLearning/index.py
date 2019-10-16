# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The Learning Rate of Gradient Descent Algorithm
# Learning rate is a hyper-parameter that controls how big a step the gradient descent algorithm
# takes when tracing its path in the direction of steepest descent in the function space.
#     If the learning rate is too large, the algorithm takes a large step as it goes downhill. In
# doing so, gradient descent runs faster, but it has a high propensity of missing the global
# minimum. An overly small learning rate makes the algorithm slow to converge (i.e., to
# reach the global minimum), but it is more likely to converge to the global minimum
# steadily. Empirically, examples of good learning rates are values in the range of 0.001,
# 0.01, and 0.1. In Figure 16-2, with a good learning rate, the cost function C(θ) should
# decrease after every iteration.
# 
# 
# 
# 
# Figure 16-2. Learning rates. Left: Good learning rate. Right: Bad learning rate.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Learning Rate of Gradient Descent Algorithm",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# The Learning Rate of Gradient Descent Algorithm"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheLearning(HierNode):
    def __init__(self):
        super().__init__("The Learning Rate of Gradient Descent Algorithm")
        self.add(Content())

# eof
