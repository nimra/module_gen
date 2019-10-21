# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Dropout.index import Dropout as A_Dropout
from .B_DataAugmentation.index import DataAugmentation as B_DataAugmentation
from .C_NoiseInjection.index import NoiseInjection as C_NoiseInjection
from .D_EarlyStopping.index import EarlyStopping as D_EarlyStopping

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 34
# 
# 
# 
# Regularization for Deep
# Learning
# Regularization is a technique for reducing the variance in the validation set, thus
# preventing the model from overfitting during training. In doing so, the model can better
# generalize to new examples. When training deep neural networks, a couple of strategies
# exist for use as a regularizer.
# 
# 
# 
# D
#  ropout
# Dropout is a regularization technique that prevents a deep neural network from
# overfitting by randomly discarding a number of neurons at every layer during training. In
# doing so, the neural network is not overly dominated by any one feature as it only makes
# use of a subset of neurons in each layer during training. In doing so, Dropout resembles
# an ensemble of neural networks as a similar but distinct neural network is trained at
# each layer. Dropout works by designating a probability that a neuron will be dropped in a
# layer. This probability value is called the Dropout rate. Figure 34-1 shows an example of a
# network with and without Dropout.
# 
# 
# 
# 
#                                                                                           415
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_34
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 34: Regularization for Deep Learning",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 34: Regularization for Deep Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter34(HierNode):
    def __init__(self):
        super().__init__("Chapter 34: Regularization for Deep Learning")
        self.add(Content())
        self.add(A_Dropout())
        self.add(B_DataAugmentation())
        self.add(C_NoiseInjection())
        self.add(D_EarlyStopping())

# eof
