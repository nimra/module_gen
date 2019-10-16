# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_TheArchitecture.index import TheArchitecture as A_TheArchitecture

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 28
# 
# 
# 
# Neural Network
# Foundations
# Building on the inspiration of the biological neuron, the artificial neural network
# (ANN) is a society of connectionist agents that learn and transfer information from
# one artificial neuron to the other. As data transfers between neurons, a hierarchy
# of representations or a hierarchy of features is learned, hence the name deep
# representation learning or deep learning.
# 
# 
# 
# T he Architecture
# An artificial neural network is composed of
# 
#        •    An input layer
# 
#        •    Hidden layer(s)
# 
#        •    An output layer
# 
# 
# 
# 
#                                                                                           331
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_28
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 28: Neural Network Foundations",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Chapter 28: Neural Network Foundations"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter28(HierNode):
    def __init__(self):
        super().__init__("Chapter 28: Neural Network Foundations")
        self.add(Content())
        self.add(A_TheArchitecture())

# eof
