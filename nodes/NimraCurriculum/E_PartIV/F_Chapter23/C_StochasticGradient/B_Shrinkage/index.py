# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                               Chapter 23   Ensemble Methods
# 
#      Gradient boosting evaluates the difference of the residuals for each tree and then
# uses that information to determine how to split the feature space in the successive tree.
#      Gradient boosting employs a pseudo-gradient in computing the residuals. This gradient
# is the direction of quickest improvement to the loss function. The residual variance is
# minimized as the gradient moves in the direction of steepest descent. This movement is the
# same as the stochastic gradient descent algorithm discussed in Chapter 16.
# 
# 
# Tree Depth/Number of Trees
# Gradient boosting can be controlled by choosing the tree depth as a hyper-parameter
# to the model. In practice, a tree depth of 1 performs well, as each tree consists of just a
# single split. Also, the number of trees can affect the model accuracy, because gradient
# boosting can overfit if the number of successive trees is vast.
# 
# 
# S
#  hrinkage
# The shrinkage hyper-parameter λ controls the learning rate of the gradient boosting
# model. An arbitrarily small value of λ may necessitate a larger number of trees to obtain a
# good model performance. However, with a small shrinkage size and tree depth d = 1, the
# residuals slowly improve by creating more varied trees to improve the worst performing
# areas of the model. Rule of thumb: shrinkage size is 0.01 or 0.001.
# 
# 
# Stochastic Gradient Boosting with Scikit-learn
# This section will implement SGB with Scikit-learn for both regression and classification
# use cases.
# 
# 
# 
# 
#                                                                                           281
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Shrinkage")
        self.add(MarkdownBlock("# Shrinkage"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Shrinkage(HierNode):
    def __init__(self):
        super().__init__("Shrinkage")
        self.add(Content())

# eof
