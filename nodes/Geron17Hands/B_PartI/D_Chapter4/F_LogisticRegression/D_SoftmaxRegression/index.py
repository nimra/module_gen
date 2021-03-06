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
#                     Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 4-24. Linear decision boundary
# 
# Just like the other linear models, Logistic Regression models can be regularized using
# ℓ1 or ℓ2 penalties. Scitkit-Learn actually adds an ℓ2 penalty by default.
# 
#                The hyperparameter controlling the regularization strength of a
#                Scikit-Learn LogisticRegression model is not alpha (as in other
#                linear models), but its inverse: C. The higher the value of C, the less
#                the model is regularized.
# 
# 
# Softmax Regression
# The Logistic Regression model can be generalized to support multiple classes directly,
# without having to train and combine multiple binary classifiers (as discussed in
# Chapter 3). This is called Softmax Regression, or Multinomial Logistic Regression.
# The idea is quite simple: when given an instance x, the Softmax Regression model
# first computes a score sk(x) for each class k, then estimates the probability of each
# class by applying the softmax function (also called the normalized exponential) to the
# scores. The equation to compute sk(x) should look familiar, as it is just like the equa‐
# tion for Linear Regression prediction (see Equation 4-19).
# 
#    Equation 4-19. Softmax score for class k
#    sk � = θkT · �
# 
# Note that each class has its own dedicated parameter vector θk. All these vectors are
# typically stored as rows in a parameter matrix Θ.
# Once you have computed the score of every class for the instance x, you can estimate
# the probability pk that the instance belongs to class k by running the scores through
# 
# 
# 
#                                                                        Logistic Regression   |   139
# 
#                  Download from finelybook www.finelybook.com
# the softmax function (Equation 4-20): it computes the exponential of every score,
# then normalizes them (dividing by the sum of all the exponentials).
# 
#       Equation 4-20. Softmax function
#                                  exp sk �
#       pk = σ � �     k   =
#                              ∑Kj = 1   exp s j �
# 
# 
#   • K is the number of classes.
#   • s(x) is a vector containing the scores of each class for the instance x.
#   • σ(s(x))k is the estimated probability that the instance x belongs to class k given
#     the scores of each class for that instance.
# 
# Just like the Logistic Regression classifier, the Softmax Regression classifier predicts
# the class with the highest estimated probability (which is simply the class with the
# highest score), as shown in Equation 4-21.
# 
#       Equation 4-21. Softmax Regression classifier prediction
#       y = argmax σ � �            k    = argmax sk � = argmax θkT · �
#                 k                           k             k
# 
# 
#   • The argmax operator returns the value of a variable that maximizes a function. In
#     this equation, it returns the value of k that maximizes the estimated probability
#     σ(s(x))k.
# 
# 
#                       The Softmax Regression classifier predicts only one class at a time
#                       (i.e., it is multiclass, not multioutput) so it should be used only with
#                       mutually exclusive classes such as different types of plants. You
#                       cannot use it to recognize multiple people in one picture.
# 
# 
# Now that you know how the model estimates probabilities and makes predictions,
# let’s take a look at training. The objective is to have a model that estimates a high
# probability for the target class (and consequently a low probability for the other
# classes). Minimizing the cost function shown in Equation 4-22, called the cross
# entropy, should lead to this objective because it penalizes the model when it estimates
# a low probability for a target class. Cross entropy is frequently used to measure how
# well a set of estimated class probabilities match the target classes (we will use it again
# several times in the following chapters).
# 
# 
# 
# 140    |   Chapter 4: Training Models
# 
#                 Download from finelybook www.finelybook.com
#    Equation 4-22. Cross entropy cost function
# 
#               1 m K i
#               mi∑   ∑
#    JΘ = −                yk log pki
#                 = 1k = 1
# 
# 
#   • yki is equal to 1 if the target class for the ith instance is k; otherwise, it is equal to
#     0.
# 
# Notice that when there are just two classes (K = 2), this cost function is equivalent to
# the Logistic Regression’s cost function (log loss; see Equation 4-17).
# 
# 
#                                       Cross Entropy
#   Cross entropy originated from information theory. Suppose you want to efficiently
#   transmit information about the weather every day. If there are eight options (sunny,
#   rainy, etc.), you could encode each option using 3 bits since 23 = 8. However, if you
#   think it will be sunny almost every day, it would be much more efficient to code
#   “sunny” on just one bit (0) and the other seven options on 4 bits (starting with a 1).
#   Cross entropy measures the average number of bits you actually send per option. If
#   your assumption about the weather is perfect, cross entropy will just be equal to the
#   entropy of the weather itself (i.e., its intrinsic unpredictability). But if your assump‐
#   tions are wrong (e.g., if it rains often), cross entropy will be greater by an amount
#   called the Kullback–Leibler divergence.
#   The cross entropy between two probability distributions p and q is defined as
#   H p, q = − ∑x p x log q x (at least when the distributions are discrete).
# 
# 
# The gradient vector of this cost function with regards to θk is given by Equation 4-23:
# 
#    Equation 4-23. Cross entropy gradient vector for class k
# 
#                 1 m
#                 mi∑
#                                  i
#    ∇θ J Θ =          pki − yki �
#       k           =1
# 
# 
# Now you can compute the gradient vector for every class, then use Gradient Descent
# (or any other optimization algorithm) to find the parameter matrix Θ that minimizes
# the cost function.
# Let’s use Softmax Regression to classify the iris flowers into all three classes. Scikit-
# Learn’s LogisticRegression uses one-versus-all by default when you train it on more
# than two classes, but you can set the multi_class hyperparameter to "multinomial"
# to switch it to Softmax Regression instead. You must also specify a solver that sup‐
# ports Softmax Regression, such as the "lbfgs" solver (see Scikit-Learn’s documenta‐
# 
# 
#                                                                        Logistic Regression   |   141
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Softmax Regression",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SoftmaxRegression(HierNode):
    def __init__(self):
        super().__init__("Softmax Regression")
        self.add(Content(), "content")

# eof
