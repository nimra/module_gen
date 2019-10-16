# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Optimizing the Logistic Regression Model
# This section surveys a few techniques to consider in optimizing/improving the
# performance of logistic regression models.
#     In the case of Bias (i.e., when the accuracy is poor with training data)
# 
#         •   Remove highly correlated features. Logistic regression is susceptible
#             to degraded performance when highly correlated features are present
#             in the dataset.
# 
#         •   Logistic regression will benefit from standardizing the predictors by
#             applying feature scaling.
# 
#         •   Good feature engineering to remove redundant features or
#             recombine features based on intuition into the learning problem can
#             improve the classification model.
# 
#         •   Applying log transforms to normalize the dataset can boost logistic
#             regression classification accuracy.
# 
#     In the case of variance (i.e., when the accuracy is good with training data, but
# poor on test data)
#     Applying regularization (more on this in Chapter 21) is a good technique to prevent
# overfitting.
#     This chapter provides a brief overview of logistic regression for building classification
# models. The chapter includes practical steps for implementing a logistic regression
# classifier with Scikit-learn. In the next chapter, we will examine the concept of applying
# regularization to linear models to mitigate the problem of overfitting.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Optimizing the Logistic Regression Model",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Optimizing the Logistic Regression Model"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Optimizingthe(HierNode):
    def __init__(self):
        super().__init__("Optimizing the Logistic Regression Model")
        self.add(Content())

# eof
