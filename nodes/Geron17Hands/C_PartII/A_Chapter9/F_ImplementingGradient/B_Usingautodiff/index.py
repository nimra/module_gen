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
#                        Download from finelybook www.finelybook.com
#                 if epoch % 100 == 0:
#                     print("Epoch", epoch, "MSE =", mse.eval())
#                 sess.run(training_op)
# 
#           best_theta = theta.eval()
# 
# 
# Using autodiff
# The preceding code works fine, but it requires mathematically deriving the gradients
# from the cost function (MSE). In the case of Linear Regression, it is reasonably easy,
# but if you had to do this with deep neural networks you would get quite a headache:
# it would be tedious and error-prone. You could use symbolic differentiation to auto‐
# matically find the equations for the partial derivatives for you, but the resulting code
# would not necessarily be very efficient.
# To understand why, consider the function f(x)= exp(exp(exp(x))). If you know calcu‐
# lus, you can figure out its derivative f′(x) = exp(x) × exp(exp(x)) × exp(exp(exp(x))).
# If you code f(x) and f′(x) separately and exactly as they appear, your code will not be
# as efficient as it could be. A more efficient solution would be to write a function that
# first computes exp(x), then exp(exp(x)), then exp(exp(exp(x))), and returns all three.
# This gives you f(x) directly (the third term), and if you need the derivative you can
# just multiply all three terms and you are done. With the naïve approach you would
# have had to call the exp function nine times to compute both f(x) and f′(x). With this
# approach you just need to call it three times.
# It gets worse when your function is defined by some arbitrary code. Can you find the
# equation (or the code) to compute the partial derivatives of the following function?
# Hint: don’t even try.
#       def my_func(a, b):
#           z = 0
#           for i in range(100):
#               z = a * np.cos(z + i) + z * np.sin(b - i)
#           return z
# Fortunately, TensorFlow’s autodiff feature comes to the rescue: it can automatically
# and efficiently compute the gradients for you. Simply replace the gradients = ...
# line in the Gradient Descent code in the previous section with the following line, and
# the code will continue to work just fine:
#       gradients = tf.gradients(mse, [theta])[0]
# 
# The gradients() function takes an op (in this case mse) and a list of variables (in this
# case just theta), and it creates a list of ops (one per variable) to compute the gradi‐
# ents of the op with regards to each variable. So the gradients node will compute the
# gradient vector of the MSE with regards to theta.
# 
# 
# 
# 
# 238   |   Chapter 9: Up and Running with TensorFlow
# 
#                    Download from finelybook www.finelybook.com
# There are four main approaches to computing gradients automatically. They are sum‐
# marized in Table 9-2. TensorFlow uses reverse-mode autodiff, which is perfect (effi‐
# cient and accurate) when there are many inputs and few outputs, as is often the case
# in neural networks. It computes all the partial derivatives of the outputs with regards
# to all the inputs in just noutputs + 1 graph traversals.
# 
# Table 9-2. Main solutions to compute gradients automatically
# Technique                 Nb of graph traversals to   Accuracy Supports          Comment
#                           compute all gradients                arbitrary code
# Numerical differentiation ninputs + 1                 Low      Yes               Trivial to implement
# Symbolic differentiation   N/A                        High      No               Builds a very different graph
# Forward-mode autodiff      ninputs                    High      Yes              Uses dual numbers
# Reverse-mode autodiff      noutputs + 1               High      Yes              Implemented by TensorFlow
# 
# If you are interested in how this magic works, check out Appendix D.
# 
# Using an Optimizer
# So TensorFlow computes the gradients for you. But it gets even easier: it also provides
# a number of optimizers out of the box, including a Gradient Descent optimizer. You
# can simply replace the preceding gradients = ... and training_op = ... lines
# with the following code, and once again everything will just work fine:
#     optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
#     training_op = optimizer.minimize(mse)
# If you want to use a different type of optimizer, you just need to change one line. For
# example, you can use a momentum optimizer (which often converges much faster
# than Gradient Descent; see Chapter 11) by defining the optimizer like this:
#     optimizer = tf.train.MomentumOptimizer(learning_rate=learning_rate,
#                                            momentum=0.9)
# 
# 
# Feeding Data to the Training Algorithm
# Let’s try to modify the previous code to implement Mini-batch Gradient Descent. For
# this, we need a way to replace X and y at every iteration with the next mini-batch. The
# simplest way to do this is to use placeholder nodes. These nodes are special because
# they don’t actually perform any computation, they just output the data you tell them
# to output at runtime. They are typically used to pass the training data to TensorFlow
# during training. If you don’t specify a value at runtime for a placeholder, you get an
# exception.
# To create a placeholder node, you must call the placeholder() function and specify
# the output tensor’s data type. Optionally, you can also specify its shape, if you want to
# 
# 
#                                                              Feeding Data to the Training Algorithm     |   239
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Using autodiff",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Usingautodiff(HierNode):
    def __init__(self):
        super().__init__("Using autodiff")
        self.add(Content(), "content")

# eof
