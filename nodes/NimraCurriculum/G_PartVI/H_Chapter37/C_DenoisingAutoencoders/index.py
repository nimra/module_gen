# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                                Chapter 37   Autoencoders
# 
# 
# D
#  enoising Autoencoders
# Denoising autoencoders add a different type of constraint to the network by imputing
# some Gaussian noise into the inputs. This noise injection forces the autoencoder to
# learn the uncorrupted form of the input features; by doing so, the autoencoder learns the
# internal representation of the dataset without memorizing the inputs.
#      Another way a denoising autoencoder constrains the input is by deactivating some
# input neurons in a similar fashion to the Dropout technique. Denoising autoencoders
# use an overcomplete network architecture. This means that the dimensions of the
# hidden Encoder and Decoder layers are not restricted; hence, they are overcomplete. An
# illustration of a denoising autoencoder architecture is shown in Figure 37-4.
# 
# 
# 
# 
# Figure 37-4. Denoising autoencoder. Constraint is applied by either adding
# Gaussian noise or by switching off some a random selection of the input neurons.
# 
# 
# 
#                                                                                      481
# 
# Chapter 37   Autoencoders
# 
#     This chapter discussed how deep neural networks can be employed in an
# unsupervised fashion to reconstruct the inputs to the network as the network’s output.
# This is the final chapter in Part 6 that provides a general theoretical background to deep
# neural networks and how they are implemented in TensorFlow 2.0. In Part 7, we will
# discuss doing advanced analytics and machine learning on Google Cloud Platform.
# 
# 
# 
# 
# 482
# 
# PART VII
# 
# Advanced Analytics/
# Machine Learning on
# Google Cloud Platform
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Denoising Autoencoders")
        self.add(MarkdownBlock("# Denoising Autoencoders"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DenoisingAutoencoders(HierNode):
    def __init__(self):
        super().__init__("Denoising Autoencoders")
        self.add(Content())

# eof
