# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                      Download from finelybook www.finelybook.com
# Lifecycle of a Node Value
# When you evaluate a node, TensorFlow automatically determines the set of nodes
# that it depends on and it evaluates these nodes first. For example, consider the follow‐
# ing code:
#     w   =   tf.constant(3)
#     x   =   w + 2
#     y   =   x + 5
#     z   =   x * 3
# 
#     with tf.Session() as sess:
#         print(y.eval()) # 10
#         print(z.eval()) # 15
# First, this code defines a very simple graph. Then it starts a session and runs the
# graph to evaluate y: TensorFlow automatically detects that y depends on w, which
# depends on x, so it first evaluates w, then x, then y, and returns the value of y. Finally,
# the code runs the graph to evaluate z. Once again, TensorFlow detects that it must
# first evaluate w and x. It is important to note that it will not reuse the result of the
# previous evaluation of w and x. In short, the preceding code evaluates w and x twice.
# All node values are dropped between graph runs, except variable values, which are
# maintained by the session across graph runs (queues and readers also maintain some
# state, as we will see in Chapter 12). A variable starts its life when its initializer is run,
# and it ends when the session is closed.
# If you want to evaluate y and z efficiently, without evaluating w and x twice as in the
# previous code, you must ask TensorFlow to evaluate both y and z in just one graph
# run, as shown in the following code:
#     with tf.Session() as sess:
#         y_val, z_val = sess.run([y, z])
#         print(y_val) # 10
#         print(z_val) # 15
# 
#                    In single-process TensorFlow, multiple sessions do not share any
#                    state, even if they reuse the same graph (each session would have its
#                    own copy of every variable). In distributed TensorFlow (see Chap‐
#                    ter 12), variable state is stored on the servers, not in the sessions, so
#                    multiple sessions can share the same variables.
# 
# 
# Linear Regression with TensorFlow
# TensorFlow operations (also called ops for short) can take any number of inputs and
# produce any number of outputs. For example, the addition and multiplication ops
# each take two inputs and produce one output. Constants and variables take no input
# 
# 
#                                                                         Lifecycle of a Node Value   |   235
# 
#                   Download from finelybook www.finelybook.com
# (they are called source ops). The inputs and outputs are multidimensional arrays,
# called tensors (hence the name “tensor flow”). Just like NumPy arrays, tensors have a
# type and a shape. In fact, in the Python API tensors are simply represented by NumPy
# ndarrays. They typically contain floats, but you can also use them to carry strings
# (arbitrary byte arrays).
# In the examples so far, the tensors just contained a single scalar value, but you can of
# course perform computations on arrays of any shape. For example, the following code
# manipulates 2D arrays to perform Linear Regression on the California housing data‐
# set (introduced in Chapter 2). It starts by fetching the dataset; then it adds an extra
# bias input feature (x0 = 1) to all training instances (it does so using NumPy so it runs
# immediately); then it creates two TensorFlow constant nodes, X and y, to hold this
# data and the targets,4 and it uses some of the matrix operations provided by Tensor‐
# Flow to define theta. These matrix functions—transpose(), matmul(), and
# matrix_inverse()—are self-explanatory, but as usual they do not perform any com‐
# putations immediately; instead, they create nodes in the graph that will perform them
# when the graph is run. You may recognize that the definition of theta corresponds to
# the Normal Equation (θ = XT · X)–1 · XT · y; see Chapter 4). Finally, the code creates a
# session and uses it to evaluate theta.
#       import numpy as np
#       from sklearn.datasets import fetch_california_housing
# 
#       housing = fetch_california_housing()
#       m, n = housing.data.shape
#       housing_data_plus_bias = np.c_[np.ones((m, 1)), housing.data]
# 
#       X = tf.constant(housing_data_plus_bias, dtype=tf.float32, name="X")
#       y = tf.constant(housing.target.reshape(-1, 1), dtype=tf.float32, name="y")
#       XT = tf.transpose(X)
#       theta = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT, X)), XT), y)
# 
#       with tf.Session() as sess:
#           theta_value = theta.eval()
# The main benefit of this code versus computing the Normal Equation directly using
# NumPy is that TensorFlow will automatically run this on your GPU card if you have
# one (provided you installed TensorFlow with GPU support, of course; see Chapter 12
# for more details).
# 
# 
# 
# 
# 4 Note that housing.target is a 1D array, but we need to reshape it to a column vector to compute theta.
#   Recall that NumPy’s reshape() function accepts –1 (meaning “unspecified”) for one of the dimensions: that
#   dimension will be computed based on the array’s length and the remaining dimensions.
# 
# 
# 
# 236   |   Chapter 9: Up and Running with TensorFlow
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Linear Regression with TensorFlow",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Linear Regression with TensorFlow"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LinearRegression(HierNode):
    def __init__(self):
        super().__init__("Linear Regression with TensorFlow")
        self.add(Content())

# eof
