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
#                   Download from finelybook www.finelybook.com
# linearly with the number of training instances and the number of features: its training
# time complexity is roughly O(m × n).
# The algorithm takes longer if you require a very high precision. This is controlled by
# the tolerance hyperparameter ϵ (called tol in Scikit-Learn). In most classification
# tasks, the default tolerance is fine.
# The SVC class is based on the libsvm library, which implements an algorithm that sup‐
# ports the kernel trick.2 The training time complexity is usually between O(m2 × n)
# and O(m3 × n). Unfortunately, this means that it gets dreadfully slow when the num‐
# ber of training instances gets large (e.g., hundreds of thousands of instances). This
# algorithm is perfect for complex but small or medium training sets. However, it scales
# well with the number of features, especially with sparse features (i.e., when each
# instance has few nonzero features). In this case, the algorithm scales roughly with the
# average number of nonzero features per instance. Table 5-1 compares Scikit-Learn’s
# SVM classification classes.
# 
# Table 5-1. Comparison of Scikit-Learn classes for SVM classification
# Class                  Time complexity           Out-of-core support Scaling required Kernel trick
# LinearSVC              O(m × n)                  No                  Yes              No
# SGDClassifier O(m × n)                           Yes                 Yes               No
# SVC                    O(m² × n) to O(m³ × n) No                     Yes               Yes
# 
# 
# SVM Regression
# As we mentioned earlier, the SVM algorithm is quite versatile: not only does it sup‐
# port linear and nonlinear classification, but it also supports linear and nonlinear
# regression. The trick is to reverse the objective: instead of trying to fit the largest pos‐
# sible street between two classes while limiting margin violations, SVM Regression
# tries to fit as many instances as possible on the street while limiting margin violations
# (i.e., instances off the street). The width of the street is controlled by a hyperparame‐
# ter ϵ. Figure 5-10 shows two linear SVM Regression models trained on some random
# linear data, one with a large margin (ϵ = 1.5) and the other with a small margin (ϵ =
# 0.5).
# 
# 
# 
# 
# 2 “Sequential Minimal Optimization (SMO),” J. Platt (1998).
# 
# 
# 
# 154     |   Chapter 5: Support Vector Machines
# 
#                   Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 5-10. SVM Regression
# 
# Adding more training instances within the margin does not affect the model’s predic‐
# tions; thus, the model is said to be ϵ-insensitive.
# You can use Scikit-Learn’s LinearSVR class to perform linear SVM Regression. The
# following code produces the model represented on the left of Figure 5-10 (the train‐
# ing data should be scaled and centered first):
#     from sklearn.svm import LinearSVR
# 
#     svm_reg = LinearSVR(epsilon=1.5)
#     svm_reg.fit(X, y)
# To tackle nonlinear regression tasks, you can use a kernelized SVM model. For exam‐
# ple, Figure 5-11 shows SVM Regression on a random quadratic training set, using a
# 2nd-degree polynomial kernel. There is little regularization on the left plot (i.e., a large
# C value), and much more regularization on the right plot (i.e., a small C value).
# 
# 
# 
# 
# Figure 5-11. SVM regression using a 2nd-degree polynomial kernel
# 
#                                                                         SVM Regression   |   155
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "SVM Regression",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SVMRegression(HierNode):
    def __init__(self):
        super().__init__("SVM Regression")
        self.add(Content(), "content")

# eof
