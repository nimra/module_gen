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
#                  Download from finelybook www.finelybook.com
# tion for more details). It also applies ℓ2 regularization by default, which you can
# control using the hyperparameter C.
#       X = iris["data"][:, (2, 3)]      # petal length, petal width
#       y = iris["target"]
# 
#       softmax_reg = LogisticRegression(multi_class="multinomial",solver="lbfgs", C=10)
#       softmax_reg.fit(X, y)
# So the next time you find an iris with 5 cm long and 2 cm wide petals, you can ask
# your model to tell you what type of iris it is, and it will answer Iris-Virginica (class 2)
# with 94.2% probability (or Iris-Versicolor with 5.8% probability):
#       >>> softmax_reg.predict([[5, 2]])
#       array([2])
#       >>> softmax_reg.predict_proba([[5, 2]])
#       array([[ 6.33134078e-07,    5.75276067e-02,      9.42471760e-01]])
# Figure 4-25 shows the resulting decision boundaries, represented by the background
# colors. Notice that the decision boundaries between any two classes are linear. The
# figure also shows the probabilities for the Iris-Versicolor class, represented by the
# curved lines (e.g., the line labeled with 0.450 represents the 45% probability bound‐
# ary). Notice that the model can predict a class that has an estimated probability below
# 50%. For example, at the point where all decision boundaries meet, all classes have an
# equal estimated probability of 33%.
# 
# 
# 
# 
# Figure 4-25. Softmax Regression decision boundaries
# 
# Exercises
#  1. What Linear Regression training algorithm can you use if you have a training set
#     with millions of features?
#  2. Suppose the features in your training set have very different scales. What algo‐
#     rithms might suffer from this, and how? What can you do about it?
# 
# 
# 142   |   Chapter 4: Training Models
# 
#                 Download from finelybook www.finelybook.com
#  3. Can Gradient Descent get stuck in a local minimum when training a Logistic
#     Regression model?
#  4. Do all Gradient Descent algorithms lead to the same model provided you let
#     them run long enough?
#  5. Suppose you use Batch Gradient Descent and you plot the validation error at
#     every epoch. If you notice that the validation error consistently goes up, what is
#     likely going on? How can you fix this?
#  6. Is it a good idea to stop Mini-batch Gradient Descent immediately when the vali‐
#     dation error goes up?
#  7. Which Gradient Descent algorithm (among those we discussed) will reach the
#     vicinity of the optimal solution the fastest? Which will actually converge? How
#     can you make the others converge as well?
#  8. Suppose you are using Polynomial Regression. You plot the learning curves and
#     you notice that there is a large gap between the training error and the validation
#     error. What is happening? What are three ways to solve this?
#  9. Suppose you are using Ridge Regression and you notice that the training error
#     and the validation error are almost equal and fairly high. Would you say that the
#     model suffers from high bias or high variance? Should you increase the regulari‐
#     zation hyperparameter α or reduce it?
# 10. Why would you want to use:
#     • Ridge Regression instead of Linear Regression?
#     • Lasso instead of Ridge Regression?
#     • Elastic Net instead of Lasso?
# 
# 11. Suppose you want to classify pictures as outdoor/indoor and daytime/nighttime.
#     Should you implement two Logistic Regression classifiers or one Softmax Regres‐
#     sion classifier?
# 12. Implement Batch Gradient Descent with early stopping for Softmax Regression
#     (without using Scikit-Learn).
# 
# Solutions to these exercises are available in Appendix A.
# 
# 
# 
# 
#                                                                         Exercises   |   143
# 
# Download from finelybook www.finelybook.com
# 
#                   Download from finelybook www.finelybook.com
# 
# 
#                                                                             CHAPTER 5
#                                       Support Vector Machines
# 
# 
# 
# 
# A Support Vector Machine (SVM) is a very powerful and versatile Machine Learning
# model, capable of performing linear or nonlinear classification, regression, and even
# outlier detection. It is one of the most popular models in Machine Learning, and any‐
# one interested in Machine Learning should have it in their toolbox. SVMs are partic‐
# ularly well suited for classification of complex but small- or medium-sized datasets.
# This chapter will explain the core concepts of SVMs, how to use them, and how they
# work.
# 
# Linear SVM Classification
# The fundamental idea behind SVMs is best explained with some pictures. Figure 5-1
# shows part of the iris dataset that was introduced at the end of Chapter 4. The two
# classes can clearly be separated easily with a straight line (they are linearly separable).
# The left plot shows the decision boundaries of three possible linear classifiers. The
# model whose decision boundary is represented by the dashed line is so bad that it
# does not even separate the classes properly. The other two models work perfectly on
# this training set, but their decision boundaries come so close to the instances that
# these models will probably not perform as well on new instances. In contrast, the
# solid line in the plot on the right represents the decision boundary of an SVM classi‐
# fier; this line not only separates the two classes but also stays as far away from the
# closest training instances as possible. You can think of an SVM classifier as fitting the
# widest possible street (represented by the parallel dashed lines) between the classes.
# This is called large margin classification.
# 
# 
# 
# 
#                                                                                         145
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Exercises",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Exercises(HierNode):
    def __init__(self):
        super().__init__("Exercises")
        self.add(Content(), "content")

# eof
