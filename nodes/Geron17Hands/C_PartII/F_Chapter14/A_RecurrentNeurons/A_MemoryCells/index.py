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
#                    Download from finelybook www.finelybook.com
# Notice that Y(t) is a function of X(t) and Y(t–1), which is a function of X(t–1) and Y(t–2),
# which is a function of X(t–2) and Y(t–3), and so on. This makes Y(t) a function of all the
# inputs since time t = 0 (that is, X(0), X(1), …, X(t)). At the first time step, t = 0, there are
# no previous outputs, so they are typically assumed to be all zeros.
# 
# Memory Cells
# Since the output of a recurrent neuron at time step t is a function of all the inputs
# from previous time steps, you could say it has a form of memory. A part of a neural
# network that preserves some state across time steps is called a memory cell (or simply
# a cell). A single recurrent neuron, or a layer of recurrent neurons, is a very basic cell,
# but later in this chapter we will look at some more complex and powerful types of
# cells.
# In general a cell’s state at time step t, denoted h(t) (the “h” stands for “hidden”), is a
# function of some inputs at that time step and its state at the previous time step: h(t) =
# f(h(t–1), x(t)). Its output at time step t, denoted y(t), is also a function of the previous
# state and the current inputs. In the case of the basic cells we have discussed so far, the
# output is simply equal to the state, but in more complex cells this is not always the
# case, as shown in Figure 14-3.
# 
# 
# 
# 
# Figure 14-3. A cell’s hidden state and its output may be different
# 
# Input and Output Sequences
# An RNN can simultaneously take a sequence of inputs and produce a sequence of
# outputs (see Figure 14-4, top-left network). For example, this type of network is use‐
# ful for predicting time series such as stock prices: you feed it the prices over the last N
# days, and it must output the prices shifted by one day into the future (i.e., from N – 1
# days ago to tomorrow).
# Alternatively, you could feed the network a sequence of inputs, and ignore all outputs
# except for the last one (see the top-right network). In other words, this is a sequence-
# to-vector network. For example, you could feed the network a sequence of words cor‐
# 
# 
# 382   |   Chapter 14: Recurrent Neural Networks
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Memory Cells",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MemoryCells(HierNode):
    def __init__(self):
        super().__init__("Memory Cells")
        self.add(Content(), "content")

# eof
