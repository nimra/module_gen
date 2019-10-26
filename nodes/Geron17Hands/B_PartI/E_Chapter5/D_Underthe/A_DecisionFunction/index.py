# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                    Download from finelybook www.finelybook.com
# The following code produces the model represented on the left of Figure 5-11 using
# Scikit-Learn’s SVR class (which supports the kernel trick). The SVR class is the regres‐
# sion equivalent of the SVC class, and the LinearSVR class is the regression equivalent
# of the LinearSVC class. The LinearSVR class scales linearly with the size of the train‐
# ing set (just like the LinearSVC class), while the SVR class gets much too slow when
# the training set grows large (just like the SVC class).
#       from sklearn.svm import SVR
# 
#       svm_poly_reg = SVR(kernel="poly", degree=2, C=100, epsilon=0.1)
#       svm_poly_reg.fit(X, y)
# 
#                      SVMs can also be used for outlier detection; see Scikit-Learn’s doc‐
#                      umentation for more details.
# 
# 
# 
# 
# Under the Hood
# This section explains how SVMs make predictions and how their training algorithms
# work, starting with linear SVM classifiers. You can safely skip it and go straight to the
# exercises at the end of this chapter if you are just getting started with Machine Learn‐
# ing, and come back later when you want to get a deeper understanding of SVMs.
# First, a word about notations: in Chapter 4 we used the convention of putting all the
# model parameters in one vector θ, including the bias term θ0 and the input feature
# weights θ1 to θn, and adding a bias input x0 = 1 to all instances. In this chapter, we will
# use a different convention, which is more convenient (and more common) when you
# are dealing with SVMs: the bias term will be called b and the feature weights vector
# will be called w. No bias feature will be added to the input feature vectors.
# 
# Decision Function and Predictions
# The linear SVM classifier model predicts the class of a new instance x by simply com‐
# puting the decision function wT · x + b = w1 x1 + ⋯ + wn xn + b: if the result is posi‐
# tive, the predicted class ŷ is the positive class (1), or else it is the negative class (0); see
# Equation 5-2.
# 
#       Equation 5-2. Linear SVM classifier prediction
#                      T
#             0 if � · � + b < 0,
#       y=
#                      T
#             1 if � · � + b ≥ 0
# 
# 
# 
# 
# 156    |   Chapter 5: Support Vector Machines
# 
#                   Download from finelybook www.finelybook.com
# Figure 5-12 shows the decision function that corresponds to the model on the right of
# Figure 5-4: it is a two-dimensional plane since this dataset has two features (petal
# width and petal length). The decision boundary is the set of points where the decision
# function is equal to 0: it is the intersection of two planes, which is a straight line (rep‐
# resented by the thick solid line).3
# 
# 
# 
# 
# Figure 5-12. Decision function for the iris dataset
# 
# The dashed lines represent the points where the decision function is equal to 1 or –1:
# they are parallel and at equal distance to the decision boundary, forming a margin
# around it. Training a linear SVM classifier means finding the value of w and b that
# make this margin as wide as possible while avoiding margin violations (hard margin)
# or limiting them (soft margin).
# 
# Training Objective
# Consider the slope of the decision function: it is equal to the norm of the weight vec‐
# tor, ∥ w ∥. If we divide this slope by 2, the points where the decision function is equal
# to ±1 are going to be twice as far away from the decision boundary. In other words,
# dividing the slope by 2 will multiply the margin by 2. Perhaps this is easier to visual‐
# ize in 2D in Figure 5-13. The smaller the weight vector w, the larger the margin.
# 
# 
# 
# 
# 3 More generally, when there are n features, the decision function is an n-dimensional hyperplane, and the deci‐
#   sion boundary is an (n – 1)-dimensional hyperplane.
# 
# 
# 
#                                                                                         Under the Hood   |   157
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Decision Function and Predictions",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DecisionFunction(HierNode):
    def __init__(self):
        super().__init__("Decision Function and Predictions")
        self.add(Content(), "content")

# eof
