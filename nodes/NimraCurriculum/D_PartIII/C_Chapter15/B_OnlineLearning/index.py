# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 15   Batch vs. Online Learning
# 
# 
# 
# 
# Figure 15-1. Batch learning
# 
#     In a situation where there is a need to train the model with data that is generated
# continuously from the source, batch learning becomes inappropriate to deal with that
# situation. In such a circumstance, we want to be able to update our learning model on
# the go, based on the new data samples that are available.
# 
# 
# 
# O
#  nline Learning
# In online learning, data streams (either individually or in mini-batches) into the learning
# algorithm and updates the model. Online learning is ideal in situations where data is
# generated continuously in time, and we need to use real-time data samples to build a
# prediction model. A typical example of this case is in stock market prediction.
#     Online learning is illustrated in Figure 15-2.
# 
# 200
# 
#                                                       Chapter 15   Batch vs. Online Learning
# 
# 
# 
# 
# Figure 15-2. Online learning
# 
# 
#     This brief chapter explained the contrast between batch learning and online
# learning. In the next chapter, we will focus our attention on a vital optimization
# algorithm for machine learning, gradient descent.
# 
# 
# 
# 
#                                                                                         201
# 
# CHAPTER 16
# 
# 
# 
# Optimization for Machine
# Learning: Gradient
# Descent
# Gradient descent is an optimization algorithm that is used to minimize the cost function
# of a machine learning algorithm. Gradient descent is called an iterative optimization
# algorithm because, in a stepwise looping fashion, it tries to find an approximate solution
# by basing the next step off its present step until a terminating condition is reached that
# ends the loop.
#     Take the following convex function in Figure 16-1 as a visual of gradient descent
# finding the minimum point of a function space.
# 
# 
# 
# 
# Figure 16-1. Contour figure – gradient descent
# 
# 
#                                                                                           203
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_16
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Online Learning")
        self.add(MarkdownBlock("# Online Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OnlineLearning(HierNode):
    def __init__(self):
        super().__init__("Online Learning")
        self.add(Content())

# eof
