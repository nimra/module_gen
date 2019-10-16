# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#                  Download from finelybook www.finelybook.com
# When the cost function is very irregular (as in Figure 4-6), this can actually help the
# algorithm jump out of local minima, so Stochastic Gradient Descent has a better
# chance of finding the global minimum than Batch Gradient Descent does.
# Therefore randomness is good to escape from local optima, but bad because it means
# that the algorithm can never settle at the minimum. One solution to this dilemma is
# to gradually reduce the learning rate. The steps start out large (which helps make
# quick progress and escape local minima), then get smaller and smaller, allowing the
# algorithm to settle at the global minimum. This process is called simulated annealing,
# because it resembles the process of annealing in metallurgy where molten metal is
# slowly cooled down. The function that determines the learning rate at each iteration
# is called the learning schedule. If the learning rate is reduced too quickly, you may get
# stuck in a local minimum, or even end up frozen halfway to the minimum. If the
# learning rate is reduced too slowly, you may jump around the minimum for a long
# time and end up with a suboptimal solution if you halt training too early.
# This code implements Stochastic Gradient Descent using a simple learning schedule:
#       n_epochs = 50
#       t0, t1 = 5, 50       # learning schedule hyperparameters
# 
#       def learning_schedule(t):
#           return t0 / (t + t1)
# 
#       theta = np.random.randn(2,1)      # random initialization
# 
#       for epoch in range(n_epochs):
#           for i in range(m):
#               random_index = np.random.randint(m)
#               xi = X_b[random_index:random_index+1]
#               yi = y[random_index:random_index+1]
#               gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
#               eta = learning_schedule(epoch * m + i)
#               theta = theta - eta * gradients
# By convention we iterate by rounds of m iterations; each round is called an epoch.
# While the Batch Gradient Descent code iterated 1,000 times through the whole train‐
# ing set, this code goes through the training set only 50 times and reaches a fairly good
# solution:
#       >>> theta
#       array([[ 4.21076011],
#             [ 2.74856079]])
# Figure 4-10 shows the first 10 steps of training (notice how irregular the steps are).
# 
# 
# 
# 
# 118   |   Chapter 4: Training Models
# 
#                   Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 4-10. Stochastic Gradient Descent first 10 steps
# 
# Note that since instances are picked randomly, some instances may be picked several
# times per epoch while others may not be picked at all. If you want to be sure that the
# algorithm goes through every instance at each epoch, another approach is to shuffle
# the training set, then go through it instance by instance, then shuffle it again, and so
# on. However, this generally converges more slowly.
# To perform Linear Regression using SGD with Scikit-Learn, you can use the SGDRe
# gressor class, which defaults to optimizing the squared error cost function. The fol‐
# lowing code runs 50 epochs, starting with a learning rate of 0.1 (eta0=0.1), using the
# default learning schedule (different from the preceding one), and it does not use any
# regularization (penalty=None; more details on this shortly):
#     from sklearn.linear_model import SGDRegressor
#     sgd_reg = SGDRegressor(n_iter=50, penalty=None, eta0=0.1)
#     sgd_reg.fit(X, y.ravel())
# Once again, you find a solution very close to the one returned by the Normal Equa‐
# tion:
#     >>> sgd_reg.intercept_, sgd_reg.coef_
#     (array([ 4.18380366]), array([ 2.74205299]))
# 
# 
# Mini-batch Gradient Descent
# The last Gradient Descent algorithm we will look at is called Mini-batch Gradient
# Descent. It is quite simple to understand once you know Batch and Stochastic Gradi‐
# ent Descent: at each step, instead of computing the gradients based on the full train‐
# ing set (as in Batch GD) or based on just one instance (as in Stochastic GD), Mini-
# 
# 
#                                                                     Gradient Descent   |   119
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Stochastic Gradient Descent",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Stochastic Gradient Descent"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class StochasticGradient(HierNode):
    def __init__(self):
        super().__init__("Stochastic Gradient Descent")
        self.add(Content())

# eof
