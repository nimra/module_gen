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
#                   Download from finelybook www.finelybook.com
#      and more attention and funding toward them, resulting in more and more pro‐
#      gress, and even more amazing products.
# 
# 
# Biological Neurons
# Before we discuss artificial neurons, let’s take a quick look at a biological neuron (rep‐
# resented in Figure 10-1). It is an unusual-looking cell mostly found in animal cerebral
# cortexes (e.g., your brain), composed of a cell body containing the nucleus and most
# of the cell’s complex components, and many branching extensions called dendrites,
# plus one very long extension called the axon. The axon’s length may be just a few
# times longer than the cell body, or up to tens of thousands of times longer. Near its
# extremity the axon splits off into many branches called telodendria, and at the tip of
# these branches are minuscule structures called synaptic terminals (or simply synap‐
# ses), which are connected to the dendrites (or directly to the cell body) of other neu‐
# rons. Biological neurons receive short electrical impulses called signals from other
# neurons via these synapses. When a neuron receives a sufficient number of signals
# from other neurons within a few milliseconds, it fires its own signals.
# 
# 
# 
# 
# Figure 10-1. Biological neuron3
# 
# Thus, individual biological neurons seem to behave in a rather simple way, but they
# are organized in a vast network of billions of neurons, each neuron typically connec‐
# ted to thousands of other neurons. Highly complex computations can be performed
# by a vast network of fairly simple neurons, much like a complex anthill can emerge
# from the combined efforts of simple ants. The architecture of biological neural net‐
# 
# 
# 
# 3 Image by Bruce Blaus (Creative Commons 3.0). Reproduced from https://en.wikipedia.org/wiki/Neuron.
# 
# 
# 
#                                                                  From Biological to Artificial Neurons   |   255
# 
#                 Download from finelybook www.finelybook.com
# works (BNN)4 is still the subject of active research, but some parts of the brain have
# been mapped, and it seems that neurons are often organized in consecutive layers, as
# shown in Figure 10-2.
# 
# 
# 
# 
# Figure 10-2. Multiple layers in a biological neural network (human cortex)5
# 
# Logical Computations with Neurons
# Warren McCulloch and Walter Pitts proposed a very simple model of the biological
# neuron, which later became known as an artificial neuron: it has one or more binary
# (on/off) inputs and one binary output. The artificial neuron simply activates its out‐
# put when more than a certain number of its inputs are active. McCulloch and Pitts
# showed that even with such a simplified model it is possible to build a network of
# artificial neurons that computes any logical proposition you want. For example, let’s
# build a few ANNs that perform various logical computations (see Figure 10-3),
# assuming that a neuron is activated when at least two of its inputs are active.
# 
# 
# 
# 
# Figure 10-3. ANNs performing simple logical computations
# 
# 
# 
# 
# 4 In the context of Machine Learning, the phrase “neural networks” generally refers to ANNs, not BNNs.
# 5 Drawing of a cortical lamination by S. Ramon y Cajal (public domain). Reproduced from https://en.wikipe
#   dia.org/wiki/Cerebral_cortex.
# 
# 
# 
# 256   |   Chapter 10: Introduction to Artificial Neural Networks
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Biological Neurons",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BiologicalNeurons(HierNode):
    def __init__(self):
        super().__init__("Biological Neurons")
        self.add(Content(), "content")

# eof
