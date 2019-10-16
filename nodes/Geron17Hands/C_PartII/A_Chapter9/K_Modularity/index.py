# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                         Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 9-5. A collapsed namescope in TensorBoard
# 
# Modularity
# Suppose you want to create a graph that adds the output of two rectified linear units
# (ReLU). A ReLU computes a linear function of the inputs, and outputs the result if it
# is positive, and 0 otherwise, as shown in Equation 9-1.
# 
#       Equation 9-1. Rectified linear unit
#       h�, b � = max � · � + b, 0
# 
# The following code does the job, but it’s quite repetitive:
#       n_features = 3
#       X = tf.placeholder(tf.float32, shape=(None, n_features), name="X")
# 
#       w1   =   tf.Variable(tf.random_normal((n_features, 1)), name="weights1")
#       w2   =   tf.Variable(tf.random_normal((n_features, 1)), name="weights2")
#       b1   =   tf.Variable(0.0, name="bias1")
#       b2   =   tf.Variable(0.0, name="bias2")
# 
#       z1 = tf.add(tf.matmul(X, w1), b1, name="z1")
#       z2 = tf.add(tf.matmul(X, w2), b2, name="z2")
# 
#       relu1 = tf.maximum(z1, 0., name="relu1")
#       relu2 = tf.maximum(z1, 0., name="relu2")
# 
#       output = tf.add(relu1, relu2, name="output")
# Such repetitive code is hard to maintain and error-prone (in fact, this code contains a
# cut-and-paste error; did you spot it?). It would become even worse if you wanted to
# 
# 
# 246    |   Chapter 9: Up and Running with TensorFlow
# 
#                  Download from finelybook www.finelybook.com
# add a few more ReLUs. Fortunately, TensorFlow lets you stay DRY (Don’t Repeat
# Yourself): simply create a function to build a ReLU. The following code creates five
# ReLUs and outputs their sum (note that add_n() creates an operation that will com‐
# pute the sum of a list of tensors):
#     def relu(X):
#         w_shape = (int(X.get_shape()[1]), 1)
#         w = tf.Variable(tf.random_normal(w_shape), name="weights")
#         b = tf.Variable(0.0, name="bias")
#         z = tf.add(tf.matmul(X, w), b, name="z")
#         return tf.maximum(z, 0., name="relu")
# 
#     n_features = 3
#     X = tf.placeholder(tf.float32, shape=(None, n_features), name="X")
#     relus = [relu(X) for i in range(5)]
#     output = tf.add_n(relus, name="output")
# Note that when you create a node, TensorFlow checks whether its name already
# exists, and if it does it appends an underscore followed by an index to make the name
# unique. So the first ReLU contains nodes named "weights", "bias", "z", and "relu"
# (plus many more nodes with their default name, such as "MatMul"); the second ReLU
# contains nodes named "weights_1", "bias_1", and so on; the third ReLU contains
# nodes named "weights_2", "bias_2", and so on. TensorBoard identifies such series
# and collapses them together to reduce clutter (as you can see in Figure 9-6).
# 
# 
# 
# 
# Figure 9-6. Collapsed node series
# 
# 
# 
# 
#                                                                       Modularity   |   247
# 
#                   Download from finelybook www.finelybook.com
# Using name scopes, you can make the graph much clearer. Simply move all the con‐
# tent of the relu() function inside a name scope. Figure 9-7 shows the resulting
# graph. Notice that TensorFlow also gives the name scopes unique names by append‐
# ing _1, _2, and so on.
#       def relu(X):
#           with tf.name_scope("relu"):
#               [...]
# 
# 
# 
# 
# Figure 9-7. A clearer graph using name-scoped units
# 
# Sharing Variables
# If you want to share a variable between various components of your graph, one sim‐
# ple option is to create it first, then pass it as a parameter to the functions that need it.
# For example, suppose you want to control the ReLU threshold (currently hardcoded
# to 0) using a shared threshold variable for all ReLUs. You could just create that vari‐
# able first, and then pass it to the relu() function:
#       def relu(X, threshold):
#           with tf.name_scope("relu"):
#               [...]
#               return tf.maximum(z, threshold, name="max")
# 
#       threshold = tf.Variable(0.0, name="threshold")
#       X = tf.placeholder(tf.float32, shape=(None, n_features), name="X")
#       relus = [relu(X, threshold) for i in range(5)]
#       output = tf.add_n(relus, name="output")
# 
# This works fine: now you can control the threshold for all ReLUs using the threshold
# variable. However, if there are many shared parameters such as this one, it will be
# painful to have to pass them around as parameters all the time. Many people create a
# Python dictionary containing all the variables in their model, and pass it around to
# every function. Others create a class for each module (e.g., a ReLU class using class
# variables to handle the shared parameter). Yet another option is to set the shared vari‐
# able as an attribute of the relu() function upon the first call, like so:
# 
# 
# 
# 248   |   Chapter 9: Up and Running with TensorFlow
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Modularity",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Modularity"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Modularity(HierNode):
    def __init__(self):
        super().__init__("Modularity")
        self.add(Content())

# eof
