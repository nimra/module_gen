# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Finding the Regression Line – How Do We Optimize
#  the Parameters of the Linear Model?
# To find the regression line, we need to define the cost function, which is also called the
# loss function. Remember that the cost in machine learning is the error measure that
# the learning algorithm minimizes. We can also define the cost as the penalty when the
# model outputs an incorrect prediction.
#      In the case of the linear regression model, the cost function is defined as half the sum
# of the squared difference between the predicted value and the actual value. The linear
# regression cost function is called the squared error cost function and is written as
# 
#                                              1
#                                      C (q ) = å ( yˆ - y )
#                                                            2
# 
#                                              2
# 
#     To put it more simply, the closer the approximate value of the target variable ŷ is to
# the actual variable y, the lower our cost and the better our model.
#     Having defined the cost function, an optimization algorithm such as gradient
# descent is used to minimize the cost C(θ) by updating the weights of the linear
# regression model.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Finding the Regression Line – How Do We Optimize the Parameters of the Linear Model?",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Finding the Regression Line – How Do We Optimize the Parameters of the Linear Model?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Findingthe(HierNode):
    def __init__(self):
        super().__init__("Finding the Regression Line – How Do We Optimize the Parameters of the Linear Model?")
        self.add(Content())

# eof
