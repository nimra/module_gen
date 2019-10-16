# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                 Download from finelybook www.finelybook.com
# There are many other variants of the LSTM cell. One particularly popular variant is
# the GRU cell, which we will look at now.
# 
# GRU Cell
# The Gated Recurrent Unit (GRU) cell (see Figure 14-14) was proposed by Kyunghyun
# Cho et al. in a 2014 paper7 that also introduced the Encoder–Decoder network we
# mentioned earlier.
# 
# 
# 
# 
# Figure 14-14. GRU cell
# 
# The GRU cell is a simplified version of the LSTM cell, and it seems to perform just as
# well8 (which explains its growing popularity). The main simplifications are:
# 
#   • Both state vectors are merged into a single vector h(t).
#   • A single gate controller controls both the forget gate and the input gate. If the
#     gate controller outputs a 1, the input gate is open and the forget gate is closed. If
# 
# 
# 
# 7 “Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation,” K. Cho
#   et al. (2014).
# 8 A 2015 paper by Klaus Greff et al., “LSTM: A Search Space Odyssey,” seems to show that all LSTM variants
#   perform roughly the same.
# 
# 
# 
# 404   |   Chapter 14: Recurrent Neural Networks
# 
#                  Download from finelybook www.finelybook.com
#     it outputs a 0, the opposite happens. In other words, whenever a memory must
#     be stored, the location where it will be stored is erased first. This is actually a fre‐
#     quent variant to the LSTM cell in and of itself.
#   • There is no output gate; the full state vector is output at every time step. How‐
#     ever, there is a new gate controller that controls which part of the previous state
#     will be shown to the main layer.
# 
# Equation 14-4 summarizes how to compute the cell’s state at each time step for a sin‐
# gle instance.
# 
#    Equation 14-4. GRU computations
#                  T            T
#     � t = σ �xz · � t + �hz · � t − 1
#                 T             T
#     � t = σ �xr · � t + �hr · � t − 1
#                      T                T
#    � t = tanh �xg · � t + �hg · � t ⊗ � t − 1
#                                   T
#    � t = 1 − � t ⊗ tanh �xg · � t − 1 + � t ⊗ �t
# 
# Creating a GRU cell in TensorFlow is trivial:
#     gru_cell = tf.contrib.rnn.GRUCell(num_units=n_neurons)
# LSTM or GRU cells are one of the main reasons behind the success of RNNs in recent
# years, in particular for applications in natural language processing (NLP).
# 
# Natural Language Processing
# Most of the state-of-the-art NLP applications, such as machine translation, automatic
# summarization, parsing, sentiment analysis, and more, are now based (at least in
# part) on RNNs. In this last section, we will take a quick look at what a machine trans‐
# lation model looks like. This topic is very well covered by TensorFlow’s awesome
# Word2Vec and Seq2Seq tutorials, so you should definitely check them out.
# 
# Word Embeddings
# Before we start, we need to choose a word representation. One option could be to
# represent each word using a one-hot vector. Suppose your vocabulary contains
# 50,000 words, then the nth word would be represented as a 50,000-dimensional vector,
# full of 0s except for a 1 at the nth position. However, with such a large vocabulary, this
# sparse representation would not be efficient at all. Ideally, you want similar words to
# have similar representations, making it easy for the model to generalize what it learns
# about a word to all similar words. For example, if the model is told that “I drink milk”
# is a valid sentence, and if it knows that “milk” is close to “water” but far from “shoes,”
# 
# 
#                                                              Natural Language Processing   |   405
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "GRU Cell",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# GRU Cell"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GRUCell(HierNode):
    def __init__(self):
        super().__init__("GRU Cell")
        self.add(Content())

# eof
