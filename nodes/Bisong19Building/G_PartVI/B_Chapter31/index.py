# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_TheConcept.index import TheConcept as A_TheConcept
from .B_Choosingthe.index import Choosingthe as B_Choosingthe
from .C_MultilayerPerceptron.index import MultilayerPerceptron as C_MultilayerPerceptron

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 31
# 
# 
# 
# The Multilayer
# Perceptron (MLP)
# The multilayer perceptron (MLP) is the fundamental example of a deep neural network.
# The architecture of a MLP consists of multiple hidden layers to capture more complex
# relationships that exist in the training dataset. Another name for the MLP is the deep
# feedforward neural network (DFN). An illustration of an MLP is shown in Figure 31-1.
# 
# 
# 
# 
# Figure 31-1. Deep feedforward neural network
# 
# 
# The Concept of Hierarchies
# The more the number of hidden layers in a neural network, the deeper the network
# becomes. Deep networks are able to learn more sophisticated representations of the
# inputs. The concept of hierarchical representation is when each layer learns a set of
# features that describe the input and hierarchically pass that information across the
# hidden layers. Initially, the hidden layers closer to the input layer learn a simple set
# 
#                                                                                            401
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_31
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 31: The Multilayer Perceptron (MLP)",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 31: The Multilayer Perceptron (MLP)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter31(HierNode):
    def __init__(self):
        super().__init__("Chapter 31: The Multilayer Perceptron (MLP)")
        self.add(Content())
        self.add(A_TheConcept())
        self.add(B_Choosingthe())
        self.add(C_MultilayerPerceptron())

# eof
