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

from .A_ManuallyComputing.index import ManuallyComputing as A_ManuallyComputing
from .B_Usingautodiff.index import Usingautodiff as B_Usingautodiff
from .C_Usingan.index import Usingan as C_Usingan

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                  Download from finelybook www.finelybook.com
# Implementing Gradient Descent
# Let’s try using Batch Gradient Descent (introduced in Chapter 4) instead of the Nor‐
# mal Equation. First we will do this by manually computing the gradients, then we will
# use TensorFlow’s autodiff feature to let TensorFlow compute the gradients automati‐
# cally, and finally we will use a couple of TensorFlow’s out-of-the-box optimizers.
# 
#                When using Gradient Descent, remember that it is important to
#                first normalize the input feature vectors, or else training may be
#                much slower. You can do this using TensorFlow, NumPy, Scikit-
#                Learn’s StandardScaler, or any other solution you prefer. The fol‐
#                lowing code assumes that this normalization has already been
#                done.
# 
# 
# Manually Computing the Gradients
# The following code should be fairly self-explanatory, except for a few new elements:
# 
#   • The random_uniform() function creates a node in the graph that will generate a
#     tensor containing random values, given its shape and value range, much like
#     NumPy’s rand() function.
#   • The assign() function creates a node that will assign a new value to a variable.
#     In this case, it implements the Batch Gradient Descent step θ(next step) = θ –
#     η∇θMSE(θ).
#   • The main loop executes the training step over and over again (n_epochs times),
#     and every 100 iterations it prints out the current Mean Squared Error (mse). You
#     should see the MSE go down at every iteration.
# 
#     n_epochs = 1000
#     learning_rate = 0.01
# 
#     X = tf.constant(scaled_housing_data_plus_bias, dtype=tf.float32, name="X")
#     y = tf.constant(housing.target.reshape(-1, 1), dtype=tf.float32, name="y")
#     theta = tf.Variable(tf.random_uniform([n + 1, 1], -1.0, 1.0), name="theta")
#     y_pred = tf.matmul(X, theta, name="predictions")
#     error = y_pred - y
#     mse = tf.reduce_mean(tf.square(error), name="mse")
#     gradients = 2/m * tf.matmul(tf.transpose(X), error)
#     training_op = tf.assign(theta, theta - learning_rate * gradients)
# 
#     init = tf.global_variables_initializer()
# 
#     with tf.Session() as sess:
#         sess.run(init)
# 
#         for epoch in range(n_epochs):
# 
# 
#                                                           Implementing Gradient Descent   |   237
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Implementing Gradient Descent",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ImplementingGradient(HierNode):
    def __init__(self):
        super().__init__("Implementing Gradient Descent")
        self.add(Content(), "content")
        self.add(A_ManuallyComputing())
        self.add(B_Usingautodiff())
        self.add(C_Usingan())

# eof
