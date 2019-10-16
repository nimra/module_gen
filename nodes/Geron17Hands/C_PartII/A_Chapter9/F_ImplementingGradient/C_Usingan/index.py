# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Using an Optimizer",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Using an Optimizer"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Usingan(HierNode):
    def __init__(self):
        super().__init__("Using an Optimizer")
        self.add(Content())

# eof
