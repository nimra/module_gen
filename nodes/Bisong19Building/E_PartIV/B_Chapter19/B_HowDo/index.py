# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# How Do We Interpret the Linear Regression Model?
# In machine learning, the focus of linear regression differs slightly from traditional
# statistics. In statistics, the goal of a regression model is to understand the relationships
# between the features and targets by interpreting p-values, whereas in machine learning,
# the goal of the linear regression model is to predict the targets given new samples.
#     Figure 19-4 shows a regression model with a line of best fit that optimizes the
# squared difference between the data features and the targets. This difference is also
# called the residuals (shown as the purple vertical lines in Figure 19-4). What we care
# about in a linear regression model is to minimize the error between the predicted labels
# and the actual labels in the dataset.
# 
# Figure 19-4. Linear regression model showing residuals
# 
#     If all the points in Figure 19-4 entirely fall on the predicted regression line, then the
# error will be 0. In interpreting the regression model, we want the error measure to be as
# low as possible.
#     However, our emphasis is to obtain a low error measure when we evaluate our model
# on the test dataset. Recall that the test of learning is when a model can generalize to
# examples that it was not exposed to during training.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "How Do We Interpret the Linear Regression Model?",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# How Do We Interpret the Linear Regression Model?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HowDo(HierNode):
    def __init__(self):
        super().__init__("How Do We Interpret the Linear Regression Model?")
        self.add(Content())

# eof
