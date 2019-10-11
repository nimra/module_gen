# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 36   Recurrent Neural Networks (RNNs)
# 
# 
# 
# 
# Figure 36-13. LSTM cell
# 
#     It is important to note that the components of the LSTM cells are all fully connected
# neural networks. There exist other variants of recurrent networks with memory cells, two
# of such are the peephole connections and the gated recurrent units.
# 
# 
# 
# P
#  eephole Connection
# The peephole connection extends the LSTM network by also using information from the
# memory cell or long-term state of the previous time instant ct − 1 as input to the LSTM
# gates. The goal of the peephole is to provide extra information into the LSTM unit by
# peeping at the stored long-term memory. This is further illustrated in Figure 36-14.
# In TensorFlow 2.0, the implementation of peephole connections to an LSTM layer is
# provided by the method ‘tf.keras.experimental.PeepholeLSTMCell()’.
# 
# 
# 
# 
# 456
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Peephole Connection")
        self.add(MarkdownBlock("# Peephole Connection"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PeepholeConnection(HierNode):
    def __init__(self):
        super().__init__("Peephole Connection")
        self.add(Content())

# eof
