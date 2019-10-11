# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 21
# 
# 
# 
# Regularization for
# Linear Models
# Regularization is the technique of adding a parameter, λ, to the loss function of a
# learning algorithm to improve its ability to generalize to new examples by reducing
# overfitting. The role of the extra regularization parameter is to shrink or to minimize the
# measure of the weights (or parameters) of the other features in the model.
#     Regularization is applied to linear models such as polynomial linear regression and
# logistic regression which are susceptible to overfitting when high-order polynomial
# features are added to the set of features.
# 
# 
# 
# How Does Regularization Work
# During model building, the regularization parameter λ is calibrated to determine how
# much the magnitude of other features in the model is adjusted when training the model.
# The higher the value of the regularization, the more the magnitude of the feature weights
# is reduced.
#      If the regularization parameter is set too close to zero, it reduces the regularization
# effect on the feature weights of the model. At zero, the penalty the regularization term
# imposes is virtually non-existent, and the model is as if the regularization term was
# never present.
# 
# 
# 
# Effects of Regularization on Bias vs. Variance
# The higher the value of λ (i.e., the regularization parameter), the more restricted the
# coefficients (or weights) of the cost function. Hence, if the value of λ is high, the model
# can result in a learning bias (i.e., it underfits the dataset).
#                                                                                           251
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_21
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("How Does Regularization Work")
        self.add(MarkdownBlock("# How Does Regularization Work"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HowDoes(HierNode):
    def __init__(self):
        super().__init__("How Does Regularization Work")
        self.add(Content())

# eof
