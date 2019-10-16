# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Why Logistic Regression?
# To develop our understanding of classification with logistic regression and why linear
# regression is unsuitable for learning categorical outputs, let us consider a binary or
# two-­class classification problem. The dataset illustrated in Figure 20-2 has the output y
# (i.e., eye disease) = {disease, no-disease} is an example of dataset with binary targets.
# 
# 
# 
# 
# Figure 20-2. Two-class classification problem
# 
#     From the illustration in Figure 20-3, the linear regression algorithm is susceptible
# to plot inaccurate decision boundaries especially in the presence of outliers (as seen
# toward the far right of the graph in Figure 20-3). Moreover, the linear regression model
# will be looking to learn a real-valued output, whereas a classification learning problem
# predicts the class membership of an observation using probability estimates.
# 
# 
# 
# 
# Figure 20-3. Linear regression on a classification dataset

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Why Logistic Regression?",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Why Logistic Regression?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WhyLogistic(HierNode):
    def __init__(self):
        super().__init__("Why Logistic Regression?")
        self.add(Content())

# eof
