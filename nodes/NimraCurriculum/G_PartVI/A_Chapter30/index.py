# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_NavigatingThrough.index import NavigatingThrough as A_NavigatingThrough

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 30
# 
# 
# 
# TensorFlow 2.0 and Keras
# TensorFlow (TF) is a specialized numerical computation library for deep learning. It is
# the preferred tool by numerous deep learning researchers and industry practitioners for
# developing deep learning models and architectures as well as for serving learned models
# into production servers and software products. This chapter is focused on TensorFlow 2.0.
# 
# 
# 
# Navigating Through the TensorFlow API
# Understanding the different levels of the TF API hierarchy is critical to working
# effectively with TF. The task of building a TF deep learning model may be addressed
# via different TF API levels. An understanding of the API hierarchy provides clarity on
# implementing neural network models with TF as well as navigating the TF ecosystem.
# The TF API hierarchy is primarily composed of three API levels, the high-level API, the
# mid-level API which provides components for building neural network models, and the
# low-level API. A diagrammatic representation of this is shown in Figure 30-1.
# 
# 
# 
# 
#                                                                                           347
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_30
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Chapter 30: TensorFlow 2.0 and Keras")
        self.add(MarkdownBlock("# Chapter 30: TensorFlow 2.0 and Keras"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter30(HierNode):
    def __init__(self):
        super().__init__("Chapter 30: TensorFlow 2.0 and Keras")
        self.add(Content())
        self.add(A_NavigatingThrough())

# eof
