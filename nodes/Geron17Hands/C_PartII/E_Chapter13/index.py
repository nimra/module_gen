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

from .A_TheArchitecture.index import TheArchitecture as A_TheArchitecture
from .B_ConvolutionalLayer.index import ConvolutionalLayer as B_ConvolutionalLayer
from .C_PoolingLayer.index import PoolingLayer as C_PoolingLayer
from .D_CNNArchitectures.index import CNNArchitectures as D_CNNArchitectures
from .E_Exercises.index import Exercises as E_Exercises

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                  Download from finelybook www.finelybook.com
# 
# 
#                                                                        CHAPTER 13
#                         Convolutional Neural Networks
# 
# 
# 
# 
# Although IBM’s Deep Blue supercomputer beat the chess world champion Garry Kas‐
# parov back in 1996, until quite recently computers were unable to reliably perform
# seemingly trivial tasks such as detecting a puppy in a picture or recognizing spoken
# words. Why are these tasks so effortless to us humans? The answer lies in the fact that
# perception largely takes place outside the realm of our consciousness, within special‐
# ized visual, auditory, and other sensory modules in our brains. By the time sensory
# information reaches our consciousness, it is already adorned with high-level features;
# for example, when you look at a picture of a cute puppy, you cannot choose not to see
# the puppy, or not to notice its cuteness. Nor can you explain how you recognize a cute
# puppy; it’s just obvious to you. Thus, we cannot trust our subjective experience: per‐
# ception is not trivial at all, and to understand it we must look at how the sensory
# modules work.
# Convolutional neural networks (CNNs) emerged from the study of the brain’s visual
# cortex, and they have been used in image recognition since the 1980s. In the last few
# years, thanks to the increase in computational power, the amount of available training
# data, and the tricks presented in Chapter 11 for training deep nets, CNNs have man‐
# aged to achieve superhuman performance on some complex visual tasks. They power
# image search services, self-driving cars, automatic video classification systems, and
# more. Moreover, CNNs are not restricted to visual perception: they are also successful
# at other tasks, such as voice recognition or natural language processing (NLP); however,
# we will focus on visual applications for now.
# In this chapter we will present where CNNs came from, what their building blocks
# look like, and how to implement them using TensorFlow. Then we will present some
# of the best CNN architectures.
# 
# 
# 
# 
#                                                                                      353
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 13. Convolutional Neural Networks",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter13(HierNode):
    def __init__(self):
        super().__init__("Chapter 13. Convolutional Neural Networks")
        self.add(Content(), "content")
        self.add(A_TheArchitecture())
        self.add(B_ConvolutionalLayer())
        self.add(C_PoolingLayer())
        self.add(D_CNNArchitectures())
        self.add(E_Exercises())

# eof
