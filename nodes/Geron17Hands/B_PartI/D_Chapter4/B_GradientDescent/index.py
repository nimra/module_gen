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

from .A_BatchGradient.index import BatchGradient as A_BatchGradient
from .B_StochasticGradient.index import StochasticGradient as B_StochasticGradient
from .C_MinibatchGradient.index import MinibatchGradient as C_MinibatchGradient

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                  Download from finelybook www.finelybook.com
# Gradient Descent
# Gradient Descent is a very generic optimization algorithm capable of finding optimal
# solutions to a wide range of problems. The general idea of Gradient Descent is to
# tweak parameters iteratively in order to minimize a cost function.
# Suppose you are lost in the mountains in a dense fog; you can only feel the slope of
# the ground below your feet. A good strategy to get to the bottom of the valley quickly
# is to go downhill in the direction of the steepest slope. This is exactly what Gradient
# Descent does: it measures the local gradient of the error function with regards to the
# parameter vector θ, and it goes in the direction of descending gradient. Once the gra‐
# dient is zero, you have reached a minimum!
# Concretely, you start by filling θ with random values (this is called random initializa‐
# tion), and then you improve it gradually, taking one baby step at a time, each step
# attempting to decrease the cost function (e.g., the MSE), until the algorithm converges
# to a minimum (see Figure 4-3).
# 
# 
# 
# 
# Figure 4-3. Gradient Descent
# 
# An important parameter in Gradient Descent is the size of the steps, determined by
# the learning rate hyperparameter. If the learning rate is too small, then the algorithm
# will have to go through many iterations to converge, which will take a long time (see
# Figure 4-4).
# 
# 
# 
# 
#                                                                     Gradient Descent   |   111
# 
#                        Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 4-4. Learning rate too small
# 
# On the other hand, if the learning rate is too high, you might jump across the valley
# and end up on the other side, possibly even higher up than you were before. This
# might make the algorithm diverge, with larger and larger values, failing to find a good
# solution (see Figure 4-5).
# 
# 
# 
# 
# Figure 4-5. Learning rate too large
# 
# Finally, not all cost functions look like nice regular bowls. There may be holes, ridges,
# plateaus, and all sorts of irregular terrains, making convergence to the minimum very
# difficult. Figure 4-6 shows the two main challenges with Gradient Descent: if the ran‐
# dom initialization starts the algorithm on the left, then it will converge to a local mini‐
# mum, which is not as good as the global minimum. If it starts on the right, then it will
# take a very long time to cross the plateau, and if you stop too early you will never
# reach the global minimum.
# 
# 
# 
# 
# 112   |   Chapter 4: Training Models
# 
#                        Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 4-6. Gradient Descent pitfalls
# 
# Fortunately, the MSE cost function for a Linear Regression model happens to be a
# convex function, which means that if you pick any two points on the curve, the line
# segment joining them never crosses the curve. This implies that there are no local
# minima, just one global minimum. It is also a continuous function with a slope that
# never changes abruptly.4 These two facts have a great consequence: Gradient Descent
# is guaranteed to approach arbitrarily close the global minimum (if you wait long
# enough and if the learning rate is not too high).
# In fact, the cost function has the shape of a bowl, but it can be an elongated bowl if
# the features have very different scales. Figure 4-7 shows Gradient Descent on a train‐
# ing set where features 1 and 2 have the same scale (on the left), and on a training set
# where feature 1 has much smaller values than feature 2 (on the right).5
# 
# 
# 
# 
# Figure 4-7. Gradient Descent with and without feature scaling
# 
# 
# 
# 4 Technically speaking, its derivative is Lipschitz continuous.
# 5 Since feature 1 is smaller, it takes a larger change in θ1 to affect the cost function, which is why the bowl is
#   elongated along the θ1 axis.
# 
# 
# 
#                                                                                            Gradient Descent    |     113
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Gradient Descent",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GradientDescent(HierNode):
    def __init__(self):
        super().__init__("Gradient Descent")
        self.add(Content(), "content")
        self.add(A_BatchGradient())
        self.add(B_StochasticGradient())
        self.add(C_MinibatchGradient())

# eof
