# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_WeightInitialization.index import WeightInitialization as A_WeightInitialization
from .B_BatchNormalization.index import BatchNormalization as B_BatchNormalization
from .C_GradientClipping.index import GradientClipping as C_GradientClipping

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 32
# 
# 
# 
# Other Considerations
# for Training the Network
# In this chapter, we will cover some other important techniques to consider when training
# a deep neural network.
# 
# 
# 
# W
#  eight Initialization
# Weight initialization is a technique for assigning initial values to the weights
# (parameters) of the neural network before training (see Figure 32-1). Proper weight
# initialization may mitigate the effects of vanishing and exploding gradients when
# training the network. It may also speed up the training process. Two commonly used
# methods for weight initializations are the Xavier and the He techniques. We will not
# go into the technical explanation of these initialization strategies. However, they are
# implemented in the standard deep learning framework libraries such as TensorFlow
# and Keras. In TensorFlow 2.0, the dense layer in ‘tf.keras.layers.Dense()’ has the Glorot
# uniform initializer, also called Xavier uniform initializer as its default kernel initializer.
# 
# 
# 
# 
#                                                                                            407
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_32
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 32: Other Considerations for Training the Network",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Chapter 32: Other Considerations for Training the Network"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter32(HierNode):
    def __init__(self):
        super().__init__("Chapter 32: Other Considerations for Training the Network")
        self.add(Content())
        self.add(A_WeightInitialization())
        self.add(B_BatchNormalization())
        self.add(C_GradientClipping())

# eof
