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
# The equivalent code using Scikit-Learn looks like this:3
#       >>> from sklearn.linear_model import LinearRegression
#       >>> lin_reg = LinearRegression()
#       >>> lin_reg.fit(X, y)
#       >>> lin_reg.intercept_, lin_reg.coef_
#       (array([ 4.21509616]), array([[ 2.77011339]]))
#       >>> lin_reg.predict(X_new)
#       array([[ 4.21509616],
#              [ 9.75532293]])
# 
# 
# Computational Complexity
# The Normal Equation computes the inverse of XT · X, which is an n × n matrix
# (where n is the number of features). The computational complexity of inverting such a
# matrix is typically about O(n2.4) to O(n3) (depending on the implementation). In
# other words, if you double the number of features, you multiply the computation
# time by roughly 22.4 = 5.3 to 23 = 8.
# 
#                      The Normal Equation gets very slow when the number of features
#                      grows large (e.g., 100,000).
# 
# 
# 
# 
# On the positive side, this equation is linear with regards to the number of instances in
# the training set (it is O(m)), so it handles large training sets efficiently, provided they
# can fit in memory.
# Also, once you have trained your Linear Regression model (using the Normal Equa‐
# tion or any other algorithm), predictions are very fast: the computational complexity
# is linear with regards to both the number of instances you want to make predictions
# on and the number of features. In other words, making predictions on twice as many
# instances (or twice as many features) will just take roughly twice as much time.
# Now we will look at very different ways to train a Linear Regression model, better
# suited for cases where there are a large number of features, or too many training
# instances to fit in memory.
# 
# 
# 
# 
# 3 Note that Scikit-Learn separates the bias term (intercept_) from the feature weights (coef_).
# 
# 
# 
# 110   |   Chapter 4: Training Models
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Computational Complexity",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ComputationalComplexity(HierNode):
    def __init__(self):
        super().__init__("Computational Complexity")
        self.add(Content(), "content")

# eof
