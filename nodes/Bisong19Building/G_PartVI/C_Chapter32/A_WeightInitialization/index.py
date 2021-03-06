# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


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
# Chapter 32   Other Considerations for Training the Network
# 
# 
# 
# 
# Figure 32-1. Weight initialization
# 
# 
# B
#  atch Normalization
# The technique of batch normalization involves normalizing the data (to have zero
# mean and unit variance), as well as scaling and shifting the data batch at each layer
# of the neural network during the training phase. Batch normalization occurs after the
# affine transformation of the input matrix and their weights, but before passing the
# transformation into the activation function (see Figure 32-2).
# 
# 
# 
# 
# 408
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Weight Initialization",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Weight Initialization"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WeightInitialization(HierNode):
    def __init__(self):
        super().__init__("Weight Initialization")
        self.add(Content())

# eof
