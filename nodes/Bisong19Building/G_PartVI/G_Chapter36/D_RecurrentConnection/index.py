# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 36   Recurrent Neural Networks (RNNs)
# 
# 
# 
# 
# Figure 36-6. Computations within a recurrent layer
# 
# 
# Recurrent Connection Schemes
# There are two main schemes for forming recurrent connections from one recurrent layer
# to another. The first is to have recurrent connections between hidden units, and the
# other is recurrent connections between the hidden unit and the output of the previous
# layer. The different schemes are visually illustrated in Figure 36-7.
# 
# 
# 
# 
# 448
# 
#                                      Chapter 36   Recurrent Neural Networks (RNNs)
# 
# 
# 
# 
# Figure 36-7. Recurrent connection schemes
# 
# 
# 
# 
#                                                                               449
# 
# Chapter 36   Recurrent Neural Networks (RNNs)
# 
#      The hidden-to-hidden recurrent configuration is found to be superior to the output-­
# to-­hidden form because it better captures the high-dimensional feature information
# about the past. In any case, the output-to-hidden recurrent form is less computationally
# expensive to train and can more easily be parallelized.
# 
# 
# 
# S
#  equence Mappings
# Recurrent neural networks can represent sequence problems in a variety of ways. The
# flexibility of RNN mappings is that it operates on inputs and outputs of the network as
# sequences, thus freeing the network from the fixed sized input-output constraints found
# in other neural network architectures such as MLP and CNN.
#     Here are a few examples of variating sequence problems solved using RNNs:
# 
#       1. An input to a sequence of output. This configuration is used
#          for image captioning problems when an image is passed as an
#          input to the network, and the output is a sequence of words. See
#          Figure 36-8.
# 
# 
# 
# 
# Figure 36-8. An input to a sequence of output
# 
# 
# 
# 
# 450
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Recurrent Connection Schemes",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Recurrent Connection Schemes"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RecurrentConnection(HierNode):
    def __init__(self):
        super().__init__("Recurrent Connection Schemes")
        self.add(Content())

# eof
