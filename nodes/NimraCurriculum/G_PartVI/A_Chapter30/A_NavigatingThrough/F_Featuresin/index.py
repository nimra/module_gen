# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 30    TensorFlow 2.0 and Keras
# 
# 
# Features in TensorFlow 2.0
# TensorFlow 2.0 comes with new features for building machine learning models. Some of
# these new features include
# 
#         •   A more pythonic feel to model design and debugging with eager
#             execution as the de facto execution mode.
# 
#         •   Eager execution enables instant evaluation of TensorFlow operations.
#             This is opposed to previous versions of Tensorflow where we first
#             construct a computational graph and then execute it in a session.
# 
#         •   Using tf.function to transform a Python method into
#             high-­performance TensorFlow graphs.
# 
#         •   Using Keras as the core high-level API for model design.
# 
#         •   Using FeatureColumns to parse data as input into Keras models.
# 
#         •   The ease of training on distributed architectures and devices.
# 
#       To install and work with TensorFlow 2.0 on Google Colab, run
# 
#         !pip install -q tensorflow==2.0.0-beta0
# 
#       The GCP Deep Learning VM has images with TensorFlow 2.0 pre-configured.
# 
# 
# 
# A Simple TensorFlow Program
# Let’s start by building a simple TF program. Here, we will build a graph to find the roots
# of the quadratic expression x2 + 3x − 4 = 0.
# 
# # import tensorflow
# import tensorflow as tf
# 
# #   Quadratic expression: x**2 + 3x - 4 = 0.
# a   = tf.constant(1.0)
# b   = tf.constant(3.0)
# c   = tf.constant(-4.0)
# 
# 
# 
# 
# 358
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Features in TensorFlow 2.0")
        self.add(MarkdownBlock("# Features in TensorFlow 2.0"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Featuresin(HierNode):
    def __init__(self):
        super().__init__("Features in TensorFlow 2.0")
        self.add(Content())

# eof
