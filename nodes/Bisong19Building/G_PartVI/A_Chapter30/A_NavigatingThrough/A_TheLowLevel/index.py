# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 30   TensorFlow 2.0 and Keras
# 
# 
# 
# 
# Figure 30-1. TensorFlow API hierarchy
# 
# 
# The Low-Level TensorFlow APIs
# The low-level API gives the tools for building network graphs from the ground up using
# mathematical operations. This API level affords the greatest level of flexibility to tweak
# and tune the model as desired. Moreover, the higher-level APIs implement low-level
# operations under the hood.
# 
# 
# The Mid-Level TensorFlow APIs
# TensorFlow provides a set of reusable packages for simplifying the process involved in
# creating neural network models. Some examples of these functions include the layers
# (tf.keras.layers), Datasets (tf.data), metrics (tf.keras.metrics), loss (tf.keras.losses),
# and FeatureColumns (tf.feature_column) packages.
# 
# L ayers
# The layers package (tf.keras.layers) provides a handy set of functions to simplify the
# construction of layers in a neural network architecture. For example, consider the
# convolutional network architecture in Figure 30-2 and how the layers API simplifies the
# creation of the network layers.
# 
# 
# 
# 348
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Low-Level TensorFlow APIs",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# The Low-Level TensorFlow APIs"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheLowLevel(HierNode):
    def __init__(self):
        super().__init__("The Low-Level TensorFlow APIs")
        self.add(Content())

# eof
