# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_LocalReceptive.index import LocalReceptive as A_LocalReceptive
from .B_Advantagesof.index import Advantagesof as B_Advantagesof
from .C_AnExample.index import AnExample as C_AnExample
from .D_CNNfor.index import CNNfor as D_CNNfor

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 35
# 
# 
# 
# Convolutional Neural
# Networks (CNN)
# Convolutional neural networks (CNN) are a specific type of neural network systems that
# are particularly suited for computer vision problems such as image recognition. In such
# tasks, the dataset is represented as a 2-D grid of pixels. See Figure 35-1.
# 
# 
# 
# 
# Figure 35-1. 2-D representation of an image
# 
#     An image is depicted in the computer as a matrix of pixel intensity values ranging
# from 0 to 255. A grayscale (or black and white) image consists of a single channel with
# 0 representing the black areas and 255 the white regions with the values in between for
# various shades of gray.
#     For example, the image in Figure 35-2 is a 10 x 10 grayscale image with its matrix
# representation.
# 
# 
# 
# 
#                                                                                           423
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_35
# 
# Chapter 35   Convolutional Neural Networks (CNN)
# 
# 
# 
# 
# Figure 35-2. Grayscale image with matrix representation
# 
#     On the other hand, a colored image consists of three channels, red, green, and blue,
# with each channel also containing pixel intensity values from 0 to 255. A colored image
# has a matrix shape of [height x width x channel]. In Figure 35-3, we have an image of
# shape [10 x 10 x 3] indicating a 10 x 10 matrix with three channels.
# 
# 
# 
# 
# 424
# 
#                                           Chapter 35    Convolutional Neural Networks (CNN)
# 
# 
# 
# 
# Figure 35-3. Colored image with matrix representation
# 
# 
# Local Receptive Fields of the Visual Cortex
# The core concept of convolutional neural networks is built on understanding the
# local receptive fields found in the neurons of the visual cortex – the part of the brain
# responsible for processing visual information.
#      A local receptive field is an area on the neuron that excites or activates that neuron
# to fire information to other neurons. When viewing an image, the neurons in the visual
# cortex react to a small or limited area of the overall image due to the presence of a small
# local receptive field.
#                                                                                           425
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 35: Convolutional Neural Networks (CNN)",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Chapter 35: Convolutional Neural Networks (CNN)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter35(HierNode):
    def __init__(self):
        super().__init__("Chapter 35: Convolutional Neural Networks (CNN)")
        self.add(Content())
        self.add(A_LocalReceptive())
        self.add(B_Advantagesof())
        self.add(C_AnExample())
        self.add(D_CNNfor())

# eof
