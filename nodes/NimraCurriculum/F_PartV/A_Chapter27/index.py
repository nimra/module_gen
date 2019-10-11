# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_TheRepresentation.index import TheRepresentation as A_TheRepresentation
from .B_Inspirationfrom.index import Inspirationfrom as B_Inspirationfrom

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Chapter 27: What Is Deep Learning?")
        self.add(MarkdownBlock("# Chapter 27: What Is Deep Learning?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter27(HierNode):
    def __init__(self):
        super().__init__("Chapter 27: What Is Deep Learning?")
        self.add(Content())
        self.add(A_TheRepresentation())
        self.add(B_Inspirationfrom())

# eof
