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

from .A_ConstructionPhase.index import ConstructionPhase as A_ConstructionPhase
from .B_ExecutionPhase.index import ExecutionPhase as B_ExecutionPhase
from .C_Usingthe.index import Usingthe as C_Usingthe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                  Download from finelybook www.finelybook.com
# Training a DNN Using Plain TensorFlow
# If you want more control over the architecture of the network, you may prefer to use
# TensorFlow’s lower-level Python API (introduced in Chapter 9). In this section we
# will build the same model as before using this API, and we will implement Mini-
# batch Gradient Descent to train it on the MNIST dataset. The first step is the con‐
# struction phase, building the TensorFlow graph. The second step is the execution
# phase, where you actually run the graph to train the model.
# 
# Construction Phase
# Let’s start. First we need to import the tensorflow library. Then we must specify the
# number of inputs and outputs, and set the number of hidden neurons in each layer:
#     import tensorflow as tf
# 
#     n_inputs = 28*28   # MNIST
#     n_hidden1 = 300
#     n_hidden2 = 100
#     n_outputs = 10
# Next, just like you did in Chapter 9, you can use placeholder nodes to represent the
# training data and targets. The shape of X is only partially defined. We know that it will
# be a 2D tensor (i.e., a matrix), with instances along the first dimension and features
# along the second dimension, and we know that the number of features is going to be
# 28 x 28 (one feature per pixel), but we don’t know yet how many instances each train‐
# ing batch will contain. So the shape of X is (None, n_inputs). Similarly, we know
# that y will be a 1D tensor with one entry per instance, but again we don’t know the
# size of the training batch at this point, so the shape is (None).
#     X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")
#     y = tf.placeholder(tf.int64, shape=(None), name="y")
# 
# Now let’s create the actual neural network. The placeholder X will act as the input
# layer; during the execution phase, it will be replaced with one training batch at a time
# (note that all the instances in a training batch will be processed simultaneously by the
# neural network). Now you need to create the two hidden layers and the output layer.
# The two hidden layers are almost identical: they differ only by the inputs they are
# connected to and by the number of neurons they contain. The output layer is also
# very similar, but it uses a softmax activation function instead of a ReLU activation
# function. So let’s create a neuron_layer() function that we will use to create one layer
# at a time. It will need parameters to specify the inputs, the number of neurons, the
# activation function, and the name of the layer:
#     def neuron_layer(X, n_neurons, name, activation=None):
#         with tf.name_scope(name):
#             n_inputs = int(X.get_shape()[1])
# 
# 
# 
#                                                      Training a DNN Using Plain TensorFlow   |   265
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Training a DNN Using Plain TensorFlow",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Traininga(HierNode):
    def __init__(self):
        super().__init__("Training a DNN Using Plain TensorFlow")
        self.add(Content(), "content")
        self.add(A_ConstructionPhase())
        self.add(B_ExecutionPhase())
        self.add(C_Usingthe())

# eof
