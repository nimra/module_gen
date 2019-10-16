# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_DecisionFunction.index import DecisionFunction as A_DecisionFunction
from .B_TrainingObjective.index import TrainingObjective as B_TrainingObjective
from .C_QuadraticProgramming.index import QuadraticProgramming as C_QuadraticProgramming
from .D_TheDual.index import TheDual as D_TheDual
from .E_KernelizedSVM.index import KernelizedSVM as E_KernelizedSVM
from .F_OnlineSVMs.index import OnlineSVMs as F_OnlineSVMs

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Under the Hood",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Under the Hood"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Underthe(HierNode):
    def __init__(self):
        super().__init__("Under the Hood")
        self.add(Content())
        self.add(A_DecisionFunction())
        self.add(B_TrainingObjective())
        self.add(C_QuadraticProgramming())
        self.add(D_TheDual())
        self.add(E_KernelizedSVM())
        self.add(F_OnlineSVMs())

# eof
