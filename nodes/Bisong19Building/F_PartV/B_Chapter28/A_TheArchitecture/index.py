# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


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
# Chapter 28   Neural Network Foundations
# 
# 
# 
# 
# Figure 28-1. Neural network architecture
# 
#     The input layer receives information from the features of the dataset, after which
# some computation takes place, and information that captures the learned patterns
# of the data is propagated across the hidden layer(s) with hopes to improve the
# learned patterns.
#     The hidden layer(s) is where the workhorse of deep learning occurs. The hidden
# layer(s) can consist of multiple neuron modules as shown in Figure 28-1. Each hidden
# network layer learns a more sophisticated set of feature representations. The decision
# on the number of neurons in a layer (network width) and the number of hidden layers
# (network depth) which forms the network topology is a design choice when training
# deep learning networks. The techniques for training a deep neural network are discussed
# in the next chapter.
# 
# 
# 
# 
# 332
# 
# CHAPTER 29
# 
# 
# 
# Training a Neural Network
# This chapter gives an overview of the techniques for training a deep neural network.
# Here, we briefly discuss
# 
#        •    How learned information flows through a neural network
# 
#        •    The role of the cost function at the output layer of the network
# 
#        •    One-hot encoding and the softmax activation function for
#             determining class membership at the output layer of a classification
#             problem
# 
#        •    The backpropagation algorithm for improving the learned
#             parameters of the network
# 
#        •    Activation functions that enable the neural network to learn non-­
#             linear patterns
# 
#     In this chapter, as we discuss the methods involved in training a neural network, we
# will use the example of a classification problem with two possible outputs. In designing
# a neural network, the number of neurons in the input layer is typically the number of
# features of the dataset, while the number of neurons in the output layer is the number of
# classes in the target variable that the neural network is learning to classify.
#     As illustrated in Figure 29-1, the dataset features are the inputs to the neural network,
# while the classes in the target variable determine the number of output neurons. In this
# example, the network learns two classes, 0 and 1.
# 
# 
# 
# 
#                                                                                           333
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_29
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Architecture",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# The Architecture"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheArchitecture(HierNode):
    def __init__(self):
        super().__init__("The Architecture")
        self.add(Content())

# eof
