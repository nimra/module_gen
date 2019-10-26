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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                        Download from finelybook www.finelybook.com
# The Architecture of the Visual Cortex
# David H. Hubel and Torsten Wiesel performed a series of experiments on cats in
# 19581 and 19592 (and a few years later on monkeys3), giving crucial insights on the
# structure of the visual cortex (the authors received the Nobel Prize in Physiology or
# Medicine in 1981 for their work). In particular, they showed that many neurons in
# the visual cortex have a small local receptive field, meaning they react only to visual
# stimuli located in a limited region of the visual field (see Figure 13-1, in which the
# local receptive fields of five neurons are represented by dashed circles). The receptive
# fields of different neurons may overlap, and together they tile the whole visual field.
# Moreover, the authors showed that some neurons react only to images of horizontal
# lines, while others react only to lines with different orientations (two neurons may
# have the same receptive field but react to different line orientations). They also
# noticed that some neurons have larger receptive fields, and they react to more com‐
# plex patterns that are combinations of the lower-level patterns. These observations
# led to the idea that the higher-level neurons are based on the outputs of neighboring
# lower-level neurons (in Figure 13-1, notice that each neuron is connected only to a
# few neurons from the previous layer). This powerful architecture is able to detect all
# sorts of complex patterns in any area of the visual field.
# 
# 
# 
# 
# Figure 13-1. Local receptive fields in the visual cortex
# 
# These studies of the visual cortex inspired the neocognitron, introduced in 1980,4
# which gradually evolved into what we now call convolutional neural networks. An
# important milestone was a 1998 paper5 by Yann LeCun, Léon Bottou, Yoshua Bengio,
# 
# 
# 1 “Single Unit Activity in Striate Cortex of Unrestrained Cats,” D. Hubel and T. Wiesel (1958).
# 2 “Receptive Fields of Single Neurones in the Cat’s Striate Cortex,” D. Hubel and T. Wiesel (1959).
# 3 “Receptive Fields and Functional Architecture of Monkey Striate Cortex,” D. Hubel and T. Wiesel (1968).
# 4 “Neocognitron: A Self-organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected
#   by Shift in Position,” K. Fukushima (1980).
# 5 “Gradient-Based Learning Applied to Document Recognition,” Y. LeCun et al. (1998).
# 
# 
# 
# 354   |   Chapter 13: Convolutional Neural Networks
# 
#                     Download from finelybook www.finelybook.com
# and Patrick Haffner, which introduced the famous LeNet-5 architecture, widely used
# to recognize handwritten check numbers. This architecture has some building blocks
# that you already know, such as fully connected layers and sigmoid activation func‐
# tions, but it also introduces two new building blocks: convolutional layers and pooling
# layers. Let’s look at them now.
# 
#                    Why not simply use a regular deep neural network with fully con‐
#                    nected layers for image recognition tasks? Unfortunately, although
#                    this works fine for small images (e.g., MNIST), it breaks down for
#                    larger images because of the huge number of parameters it
#                    requires. For example, a 100 × 100 image has 10,000 pixels, and if
#                    the first layer has just 1,000 neurons (which already severely
#                    restricts the amount of information transmitted to the next layer),
#                    this means a total of 10 million connections. And that’s just the first
#                    layer. CNNs solve this problem using partially connected layers.
# 
# 
# Convolutional Layer
# The most important building block of a CNN is the convolutional layer:6 neurons in
# the first convolutional layer are not connected to every single pixel in the input image
# (like they were in previous chapters), but only to pixels in their receptive fields (see
# Figure 13-2). In turn, each neuron in the second convolutional layer is connected
# only to neurons located within a small rectangle in the first layer. This architecture
# allows the network to concentrate on low-level features in the first hidden layer, then
# assemble them into higher-level features in the next hidden layer, and so on. This
# hierarchical structure is common in real-world images, which is one of the reasons
# why CNNs work so well for image recognition.
# 
# 
# 
# 
# 6 A convolution is a mathematical operation that slides one function over another and measures the integral of
#   their pointwise multiplication. It has deep connections with the Fourier transform and the Laplace transform,
#   and is heavily used in signal processing. Convolutional layers actually use cross-correlations, which are very
#   similar to convolutions (see http://goo.gl/HAfxXd for more details).
# 
# 
# 
#                                                                                     Convolutional Layer   |   355
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Architecture of the Visual Cortex",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheArchitecture(HierNode):
    def __init__(self):
        super().__init__("The Architecture of the Visual Cortex")
        self.add(Content(), "content")

# eof
