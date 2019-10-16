# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Regression Metrics
# You learned about regression metrics a few chapters ago. As a quick recap, the Pear‐
# son R2 and RMSE (root-mean-squared error) are good defaults.
# We only briefly covered the mathematical definition of R2 previously, but will delve
# into it more now. Let xi represent predictions and yi represent labels. Let x and y rep‐
# resent the mean of the predicted values and the labels, respectively. Then the Pearson
# R (note the lack of square) is
# 
#                   ∑N
#                    i = 1 xi − x y i − y
#       R=
#              ∑N
#               i = 1 xi − x
#                              2
#                                  ∑N
#                                   i = 1 yi − y
#                                                  2
# 
# 
# 
# This equation can be rewritten as
# 
#            cov x, y
#       R=
#            σxσ y
# 
# where cov represents the covariance and σ represents the standard deviation. Intui‐
# tively, the Pearson R measures the joint fluctuations of the predictions and labels
# from their means normalized by their respective ranges of fluctuations. If predictions
# and labels differ, these fluctuations will happen at different points and will tend to
# cancel, making R2 smaller. If predictions and labels tend to agree, the fluctuations will
# happen together and make R2 larger. We note that R2 is limited to a range between 0
# and 1.
# The RMSE measures the absolute quantity of the error between the predictions and
# the true quantities. It stands for root-mean-squared error, which is roughly analogous
# to the absolute value of the error between the true quantity and the predicted quan‐
# tity. Mathematically, the RMSE is defined as follows (using the same notation as
# before):
# 
#                    ∑N
#                     i = 1 xi − yi
#                                     2
#       RMSE =
#                           N
# 
# 
# Hyperparameter Optimization Algorithms
# As we mentioned earlier in the chapter, hyperparameter optimization methods are
# learning algorithms for finding values of the hyperparameters that optimize the
# chosen metric on the validation set. In general, this objective function cannot be dif‐
# ferentiated, so any optimization method must by necessity be a black box. In this
# section, we will show you some simple black-box learning algorithms for choosing
# 
# 110   |    Chapter 5: Hyperparameter Optimization
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Regression Metrics",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Regression Metrics"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RegressionMetrics(HierNode):
    def __init__(self):
        super().__init__("Regression Metrics")
        self.add(Content())

# eof
