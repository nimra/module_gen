# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_LocalReceptive.index import LocalReceptive as A_LocalReceptive
from .B_ConvolutionalKernels.index import ConvolutionalKernels as B_ConvolutionalKernels
from .C_PoolingLayers.index import PoolingLayers as C_PoolingLayers
from .D_ConstructingConvolutional.index import ConstructingConvolutional as D_ConstructingConvolutional
from .E_DilatedConvolutions.index import DilatedConvolutions as E_DilatedConvolutions

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# tional architectures to work on new datatypes. For example, graph convolutional
# architectures allow convolutional networks to be applied to molecular data such as
# the Tox21 dataset we encountered a few chapters ago! Convolutional architectures are
# also making a mark in genomics and in text processing and even language
# translation.
# In this chapter, we will introduce the basic concepts of convolutional networks. These
# will include the basic network components that constitute convolutional architec‐
# tures and an introduction to the design principles that guide how these pieces are
# joined together. We will also provide an in-depth example that demonstrates how to
# use TensorFlow to train a convolutional network. The example code for this chapter
# was adapted from the TensorFlow documentation tutorial on convolutional neural
# networks. We encourage you to access the original tutorial on the TensorFlow website
# if you’re curious about the changes we’ve made. As always, we encourage you to work
# through the scripts for this chapter in the associated GitHub repo for this book.
# 
# Introduction to Convolutional Architectures
# Most convolutional architectures are made up of a number of basic primitives. These
# primitives include layers such as convolutional layers and pooling layers. There’s also
# a set of associated vocabulary including local receptive field size, stride size, and
# number of filters. In this section, we will give you a brief introduction to the basic
# vocabulary and concepts underlying convolutional networks.
# 
# Local Receptive Fields
# The local receptive field concept originates in neuroscience, where the receptive field
# of a neuron is the part of the body’s sensory perception that affects the neuron’s firing.
# Neurons have a certain field of “view” as they process sensory input that the brain
# sees. This field of view is traditionally called the local receptive field. This “field of
# view” could correspond to a patch of skin or to a segment of a person’s visual field.
# Figure 6-1 illustrates a neuron’s local receptive field.
# 
# 
# 
# 
# 120   | Chapter 6: Convolutional Neural Networks
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Introduction to Convolutional Architectures",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Introduction to Convolutional Architectures"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Introductionto(HierNode):
    def __init__(self):
        super().__init__("Introduction to Convolutional Architectures")
        self.add(Content())
        self.add(A_LocalReceptive())
        self.add(B_ConvolutionalKernels())
        self.add(C_PoolingLayers())
        self.add(D_ConstructingConvolutional())
        self.add(E_DilatedConvolutions())

# eof
