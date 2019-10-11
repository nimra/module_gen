# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                               Chapter 36   Recurrent Neural Networks (RNNs)
# 
# 
# 
# 
# Figure 36-14. Peephole connection
# 
# 
# Gated Recurrent Unit (GRU)
# The gated recurrent unit (GRU) is a more recent recurrent neural network architecture
# than the LSTM, and it is also comparable simpler to implement with respect to the
# number of components within the unit and their operations. Despite its comparative
# simplicity, GRUs are high-performing recurrent architectures and, in most cases, even
# perform better than the LSTM in sequence modeling problems.
#     GRUs combine the forget and the input gates to decide on what information should
# be committed to the long-term memory or the memory cell and what information
# should be left out. Moreover, the GRU combines the cell (i.e., long-term state) and
# short-term states into a single state vector ht. Also, the GRU removes the output gate and
# returns the state vector ht at each time instant. This is further illustrated in Figure 36-15.
# In TensorFlow 2.0, the GRU layer is implemented in the method ‘tf.keras.layers.GRU()’.
# 
# 
# 
# 
#                                                                                           457
# 
# Chapter 36   Recurrent Neural Networks (RNNs)
# 
# 
# 
# 
# Figure 36-15. Gated recurrent unit
# 
# 
#  ecurrent Neural Networks Applied to Sequence
# R
# Problems
# Recurrent neural networks have many application areas for using LSTM models for
# sequence tasks. A couple of problems under this domain include sentiment analysis,
# machine translation, image captioning, video captioning, and voice recognition. As
# mentioned earlier, these problems can be modeled as a one-to-many model, a many-to-­
# one model, or a many-to-many model. The section will survey a few LSTM architectures
# for tackling/modeling sequence problems:
#       •   Long-term recurrent convolutional neural network, also known as
#           CNN LSTM
# 
#       •   Encoder-Decoder LSTMs
# 
#       •   Bidirectional recurrent neural networks
# 
# 
# 
# 
# 458
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Gated Recurrent Unit (GRU)")
        self.add(MarkdownBlock("# Gated Recurrent Unit (GRU)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GatedRecurrent(HierNode):
    def __init__(self):
        super().__init__("Gated Recurrent Unit (GRU)")
        self.add(Content())

# eof
