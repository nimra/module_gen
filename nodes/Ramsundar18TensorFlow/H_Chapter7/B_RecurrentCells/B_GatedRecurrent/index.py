# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Gated Recurrent Units (GRU)
# The complexity, both conceptual and computational, for LSTM cells has motivated a
# number of researchers to attempt to simplify the LSTM equations while retaining the
# performance gains and modeling capabilities of the original equations.
# There are a number of contenders for LSTM replacement, but one of the frontrun‐
# ners is the gated recurrent unit (GRU), shown in Figure 7-5. The GRU removes one
# of the subcomponents of the LSTM but empirically seems to achieve performance
# similar to that of the LSTM. The GRU might be a suitable replacement for LSTM cells
# on sequence modeling projects.
# 
# 
# 
# 
# Figure 7-5. A gated recurrent unit (GRU) cell. GRUs preserve many of the benefits of
# LSTMs at lower computational cost.
# 
# Applications of Recurrent Models
# While recurrent neural networks are useful tools for modeling time-series datasets,
# there are a host of other applications of recurrent networks. These include applica‐
# tions such as natural language modeling, machine translation, chemical retrosynthe‐
# sis, and arbitrary computation with Neural Turing machines. In this section, we
# provide a brief tour of some of these exciting applications.
# 
# Sampling from Recurrent Networks
# So far, we’ve taught you how recurrent networks can learn to model the time evolu‐
# tion of sequences of data. It stands to reason that if you understand the evolution rule
# for a set of sequences, you ought to be able to sample new sequences from the distri‐
# bution of training sequences. And indeed, it turns out that that good sequences can
# be sampled from trained models. The most useful application thus far is in language
# modeling. Being able to generate realistic sentences is a very useful tool that under‐
# pins systems such as autocomplete and chatbots.
# 
# 
# 154   |   Chapter 7: Recurrent Neural Networks
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Gated Recurrent Units (GRU)",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Gated Recurrent Units (GRU)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GatedRecurrent(HierNode):
    def __init__(self):
        super().__init__("Gated Recurrent Units (GRU)")
        self.add(Content())

# eof
