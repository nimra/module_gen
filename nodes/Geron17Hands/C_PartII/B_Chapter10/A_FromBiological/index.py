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

from .A_BiologicalNeurons.index import BiologicalNeurons as A_BiologicalNeurons
from .B_LogicalComputations.index import LogicalComputations as B_LogicalComputations
from .C_ThePerceptron.index import ThePerceptron as C_ThePerceptron
from .D_MultiLayerPerceptron.index import MultiLayerPerceptron as D_MultiLayerPerceptron

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                         Download from finelybook www.finelybook.com
# From Biological to Artificial Neurons
# Surprisingly, ANNs have been around for quite a while: they were first introduced
# back in 1943 by the neurophysiologist Warren McCulloch and the mathematician
# Walter Pitts. In their landmark paper,2 “A Logical Calculus of Ideas Immanent in
# Nervous Activity,” McCulloch and Pitts presented a simplified computational model
# of how biological neurons might work together in animal brains to perform complex
# computations using propositional logic. This was the first artificial neural network
# architecture. Since then many other architectures have been invented, as we will see.
# The early successes of ANNs until the 1960s led to the widespread belief that we
# would soon be conversing with truly intelligent machines. When it became clear that
# this promise would go unfulfilled (at least for quite a while), funding flew elsewhere
# and ANNs entered a long dark era. In the early 1980s there was a revival of interest in
# ANNs as new network architectures were invented and better training techniques
# were developed. But by the 1990s, powerful alternative Machine Learning techniques
# such as Support Vector Machines (see Chapter 5) were favored by most researchers,
# as they seemed to offer better results and stronger theoretical foundations. Finally, we
# are now witnessing yet another wave of interest in ANNs. Will this wave die out like
# the previous ones did? There are a few good reasons to believe that this one is differ‐
# ent and will have a much more profound impact on our lives:
# 
#   • There is now a huge quantity of data available to train neural networks, and
#     ANNs frequently outperform other ML techniques on very large and complex
#     problems.
#   • The tremendous increase in computing power since the 1990s now makes it pos‐
#     sible to train large neural networks in a reasonable amount of time. This is in
#     part due to Moore’s Law, but also thanks to the gaming industry, which has pro‐
#     duced powerful GPU cards by the millions.
#   • The training algorithms have been improved. To be fair they are only slightly dif‐
#     ferent from the ones used in the 1990s, but these relatively small tweaks have a
#     huge positive impact.
#   • Some theoretical limitations of ANNs have turned out to be benign in practice.
#     For example, many people thought that ANN training algorithms were doomed
#     because they were likely to get stuck in local optima, but it turns out that this is
#     rather rare in practice (or when it is the case, they are usually fairly close to the
#     global optimum).
#   • ANNs seem to have entered a virtuous circle of funding and progress. Amazing
#     products based on ANNs regularly make the headline news, which pulls more
# 
# 
# 2 “A Logical Calculus of Ideas Immanent in Nervous Activity,” W. McCulloch and W. Pitts (1943).
# 
# 
# 
# 254   |   Chapter 10: Introduction to Artificial Neural Networks
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "From Biological to Artificial Neurons",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FromBiological(HierNode):
    def __init__(self):
        super().__init__("From Biological to Artificial Neurons")
        self.add(Content(), "content")
        self.add(A_BiologicalNeurons())
        self.add(B_LogicalComputations())
        self.add(C_ThePerceptron())
        self.add(D_MultiLayerPerceptron())

# eof
