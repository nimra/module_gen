# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Training the Logistic Regression Model
# The logistic regression cost function is formally written as
# 
#                  Cost ( h ( t ) ,y ) = {- log ( h ( t ) ) if y = 1 - log (1 - h ( t ) ) if y = 0
# 
# 
#      The cost function also known as log-loss is set up in this form to output the penalty
# of the algorithm if the model predicts a wrong class. To give more intuition, take, for
# example, a plot of − log (h(t)) when y = 1 in Figure 20-5.
# 
# 
# 
# 
# Figure 20-5. Plot of h(t) when y = 1
# 
#     In Figure 20-5, if the algorithm correctly predicts that the target is 1, then the cost
# tends toward 0. However, if the algorithm h(t) predicts incorrectly the target as 0, then
# the cost on the model grows exponentially large. The converse is the case with the plot of
# − log (1 − h(t)) when y = 0.
#     The logistic model is optimized using gradient descent to find the optimal values of
# the parameter θ that minimizes the cost function to predict the class with the highest
# probability estimate.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Training the Logistic Regression Model",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Training the Logistic Regression Model"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Trainingthe(HierNode):
    def __init__(self):
        super().__init__("Training the Logistic Regression Model")
        self.add(Content())

# eof
