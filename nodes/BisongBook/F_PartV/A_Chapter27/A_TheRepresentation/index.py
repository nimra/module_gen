# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 27
# 
# 
# 
# What Is Deep Learning?
# Deep learning is a class of machine learning algorithms called neural networks. Neural
# networks are mathematical models inspired by the structure of the brain. Deep learning
# enables the neural network algorithm to perform very well in building prediction
# models around complex problems such as computer vision and language modeling.
# Self-­driving cars and automatic speech translation, to mention just a few, are examples
# of technologies that have resulted from advances in deep learning.
# 
# 
# 
# The Representation Challenge
# Learning is a non-trivial task. The brain’s ability to learn complex tasks is not yet fully
# understood by research communities in neurological science, psychology, and other
# brain-related fields. What we consider trivial, and to some others natural, are a system
# of complex and intricate processes that have set us apart from other life forms as
# intelligent beings.
#      Examples of complex tasks performed by the human brain include the ability to
# recognize faces at a millionth of a second (probably much faster), the uncanny aptitude
# for learning and understanding deep linguistic representations, and forming symbols
# for intelligent communications. Also, the adept skills to compose and perform masterful
# musical pieces are examples of the marvel of natural intelligence.
#      The challenge of AI research and engineering is to build machines that can
# understand and decompose the structural patterns inherent in complex problems in
# order to mimic natural intelligence. Deep learning as an AI technique approaches the
# representation problem by learning the underlying fundamental structure inherent in
# the dataset. Deep learning is also called representation learning.
# 
# 
# 
# 
#                                                                                           327
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_27
# 
# Chapter 27   What Is Deep Learning?
# 
# 
# I nspiration from the Brain
# Scientists often look to nature for inspiration when performing incredible feats. Notably,
# the birds inspired the airplane. In that vein, there is no better type to study as an antitype
# of intelligence as the human brain.
#      We can view the brain as a society of intelligent agents that are networked together
# and communicate by passing information via electrical signals from one agent to
# another. These agents are known as neurons. Our principal interest here is to have a
# glimpse of what neurons are, what their components are, and how they pass information
# around to create intelligence.
#      A neuron is an autonomous agent in the brain and is a central part of the nervous
# system. Neurons are responsible for receiving and transmitting information to other cells
# within the body based on external or internal stimuli. Neurons react by firing electrical
# impulses generated at the stimuli source to the brain and other cells for the appropriate
# response. The intricate and coordinated workings of neurons are central to human
# intelligence.
#      The following are the three most essential components of neurons that are of
# primary interest to us:
# 
#       •   The axon
# 
#       •   The dendrite
# 
#       •   The synapse
# 
#     The axon is a long tail connected to the nucleus of the neuron as seen in
# Figure 27-­1. The axon is responsible for transmitting electrical signals from the
# nucleus to other neuron cells through the axon terminals. The dendrite, on the other
# hand, receives information as electrical impulses from other neuron cells through
# the synapses to the nucleus of a neuron cell.
# 
# 
# 
# 
# 328
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Representation Challenge",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# The Representation Challenge"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheRepresentation(HierNode):
    def __init__(self):
        super().__init__("The Representation Challenge")
        self.add(Content())

# eof
