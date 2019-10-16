# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Improving the Performance of a Linear Regression
#  Model
# The following techniques are options that can be explored to improve the performance
# of a linear regression model.
#     In the case of Bias (i.e., poor MSE on training data)
# 
#       •   Perform feature selection to reduce the parameter space. Feature
#           selection is the process of eliminating variables that do not contribute
#           to learning the prediction model. There are various automatic
#           methods for feature selection with linear regression. A couple of
#           them are backward selection, forward propagation, and stepwise
#           regression. Features can also be pruned manually by systematically
#           going through each feature in the dataset and determining its
#           relevance to the learning problem.
# 
#       •   Remove features with high correlation. Correlation occurs when
#           two predictor features are strongly dependent on one another.
#           Empirically, highly correlated features in the datasets may hurt the
#           model accuracy.
#       •   Use higher-order features. A more flexible fit may better capture the
#           variance in the dataset.
# 
#       •   Rescale your data before training. Unscaled features negatively affect
#           the prediction quality of a regression model. Because of the different
#           feature scales in multi-dimensional space, it becomes difficult for the
#           model to find the optimal weights that capture the learning problem.
#           As mentioned in Chapter 16, gradient descent performs better with
#           feature scaling.
# 
#       •   In a rare case, we may need to collect more data. However, this is
#           potentially costly.
# 
#    In the case of variance (i.e., the MSE is good when evaluated on training data, but
# poor on the test data)
# 
#       •   A standard practice, in this case, is to apply regularization (more on
#           this in Chapter 21) to the regression model. This can do a good job at
#           preventing overfitting.
#     This chapter provides an overview on the linear regression machine learning
# algorithm for learning real-valued targets. Also, the chapter provided practical steps for
# implementing linear regression models with Scikit-learn. In the next chapter, we will
# examine logistic regression for learning classification problems.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Improving the Performance of a Linear Regression Model",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Improving the Performance of a Linear Regression Model"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Improvingthe(HierNode):
    def __init__(self):
        super().__init__("Improving the Performance of a Linear Regression Model")
        self.add(Content())

# eof
