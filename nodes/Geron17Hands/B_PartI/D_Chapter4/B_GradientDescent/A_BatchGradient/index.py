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
# As you can see, on the left the Gradient Descent algorithm goes straight toward the
# minimum, thereby reaching it quickly, whereas on the right it first goes in a direction
# almost orthogonal to the direction of the global minimum, and it ends with a long
# march down an almost flat valley. It will eventually reach the minimum, but it will
# take a long time.
# 
#                          When using Gradient Descent, you should ensure that all features
#                          have a similar scale (e.g., using Scikit-Learn’s StandardScaler
#                          class), or else it will take much longer to converge.
# 
# 
# 
# This diagram also illustrates the fact that training a model means searching for a
# combination of model parameters that minimizes a cost function (over the training
# set). It is a search in the model’s parameter space: the more parameters a model has,
# the more dimensions this space has, and the harder the search is: searching for a nee‐
# dle in a 300-dimensional haystack is much trickier than in three dimensions. Fortu‐
# nately, since the cost function is convex in the case of Linear Regression, the needle is
# simply at the bottom of the bowl.
# 
# Batch Gradient Descent
# To implement Gradient Descent, you need to compute the gradient of the cost func‐
# tion with regards to each model parameter θj. In other words, you need to calculate
# how much the cost function will change if you change θj just a little bit. This is called
# a partial derivative. It is like asking “what is the slope of the mountain under my feet
# if I face east?” and then asking the same question facing north (and so on for all other
# dimensions, if you can imagine a universe with more than three dimensions). Equa‐
# tion 4-5 computes the partial derivative of the cost function with regards to parame‐
#                 ∂
# ter θj, noted ∂θ MSE θ .
#                      j
# 
# 
#       Equation 4-5. Partial derivatives of the cost function
# 
#        ∂           2 m T
#                    mi∑
#                              i
#            MSE θ =      θ · � − y i x ji
#       ∂θ j           =1
# 
# 
# Instead of computing these gradients individually, you can use Equation 4-6 to com‐
# pute them all in one go. The gradient vector, noted ∇θMSE(θ), contains all the partial
# derivatives of the cost function (one for each model parameter).
# 
# 
# 
# 
# 114    |   Chapter 4: Training Models
# 
#                   Download from finelybook www.finelybook.com
#     Equation 4-6. Gradient vector of the cost function
#                           ∂
#                              MSE θ
#                          ∂θ0
#                 ∂
#                    MSE θ  2 T
#     ∇θ MSE θ = ∂θ1       = � · �·θ−�
#                           m
#                     ⋮
#                 ∂
#                    MSE θ
#                ∂θn
# 
#                      Notice that this formula involves calculations over the full training
#                      set X, at each Gradient Descent step! This is why the algorithm is
#                      called Batch Gradient Descent: it uses the whole batch of training
#                      data at every step. As a result it is terribly slow on very large train‐
#                      ing sets (but we will see much faster Gradient Descent algorithms
#                      shortly). However, Gradient Descent scales well with the number of
#                      features; training a Linear Regression model when there are hun‐
#                      dreds of thousands of features is much faster using Gradient
#                      Descent than using the Normal Equation.
# 
# Once you have the gradient vector, which points uphill, just go in the opposite direc‐
# tion to go downhill. This means subtracting ∇θMSE(θ) from θ. This is where the
# learning rate η comes into play:6 multiply the gradient vector by η to determine the
# size of the downhill step (Equation 4-7).
# 
#     Equation 4-7. Gradient Descent step
#     θ next   step
#                     = θ − η∇θ MSE θ
# 
# Let’s look at a quick implementation of this algorithm:
#      eta = 0.1 # learning rate
#      n_iterations = 1000
#      m = 100
# 
#      theta = np.random.randn(2,1)              # random initialization
# 
#      for iteration in range(n_iterations):
#          gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
#          theta = theta - eta * gradients
# 
# 
# 
# 
# 6 Eta (η) is the 7th letter of the Greek alphabet.
# 
# 
# 
#                                                                                 Gradient Descent   |   115
# 
#                  Download from finelybook www.finelybook.com
# That wasn’t too hard! Let’s look at the resulting theta:
#       >>> theta
#       array([[ 4.21509616],
#              [ 2.77011339]])
# Hey, that’s exactly what the Normal Equation found! Gradient Descent worked per‐
# fectly. But what if you had used a different learning rate eta? Figure 4-8 shows the
# first 10 steps of Gradient Descent using three different learning rates (the dashed line
# represents the starting point).
# 
# 
# 
# 
# Figure 4-8. Gradient Descent with various learning rates
# 
# On the left, the learning rate is too low: the algorithm will eventually reach the solu‐
# tion, but it will take a long time. In the middle, the learning rate looks pretty good: in
# just a few iterations, it has already converged to the solution. On the right, the learn‐
# ing rate is too high: the algorithm diverges, jumping all over the place and actually
# getting further and further away from the solution at every step.
# To find a good learning rate, you can use grid search (see Chapter 2). However, you
# may want to limit the number of iterations so that grid search can eliminate models
# that take too long to converge.
# You may wonder how to set the number of iterations. If it is too low, you will still be
# far away from the optimal solution when the algorithm stops, but if it is too high, you
# will waste time while the model parameters do not change anymore. A simple solu‐
# tion is to set a very large number of iterations but to interrupt the algorithm when the
# gradient vector becomes tiny—that is, when its norm becomes smaller than a tiny
# number ϵ (called the tolerance)—because this happens when Gradient Descent has
# (almost) reached the minimum.
# 
# 
# 
# 
# 116   |   Chapter 4: Training Models
# 
#                      Download from finelybook www.finelybook.com
# 
#                                          Convergence Rate
#   When the cost function is convex and its slope does not change abruptly (as is the
#   case for the MSE cost function), it can be shown that Batch Gradient Descent with a
#                                                        1
#   fixed learning rate has a convergence rate of O iterations . In other words, if you divide
#   the tolerance ϵ by 10 (to have a more precise solution), then the algorithm will have
#   to run about 10 times more iterations.
# 
# 
# Stochastic Gradient Descent
# The main problem with Batch Gradient Descent is the fact that it uses the whole
# training set to compute the gradients at every step, which makes it very slow when
# the training set is large. At the opposite extreme, Stochastic Gradient Descent just
# picks a random instance in the training set at every step and computes the gradients
# based only on that single instance. Obviously this makes the algorithm much faster
# since it has very little data to manipulate at every iteration. It also makes it possible to
# train on huge training sets, since only one instance needs to be in memory at each
# iteration (SGD can be implemented as an out-of-core algorithm.7)
# On the other hand, due to its stochastic (i.e., random) nature, this algorithm is much
# less regular than Batch Gradient Descent: instead of gently decreasing until it reaches
# the minimum, the cost function will bounce up and down, decreasing only on aver‐
# age. Over time it will end up very close to the minimum, but once it gets there it will
# continue to bounce around, never settling down (see Figure 4-9). So once the algo‐
# rithm stops, the final parameter values are good, but not optimal.
# 
# 
# 
# 
# Figure 4-9. Stochastic Gradient Descent
# 
# 
# 
# 7 Out-of-core algorithms are discussed in Chapter 1.
# 
# 
# 
#                                                                         Gradient Descent   |   117
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Batch Gradient Descent",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BatchGradient(HierNode):
    def __init__(self):
        super().__init__("Batch Gradient Descent")
        self.add(Content(), "content")

# eof
