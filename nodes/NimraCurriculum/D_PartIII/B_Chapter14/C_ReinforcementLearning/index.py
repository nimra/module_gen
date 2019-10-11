# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                            Chapter 14   Principles of Learning
# 
# 
# R
#  einforcement Learning
# Reinforcement learning presents an approach to learning that is quite different from
# what we have seen so far in supervised and unsupervised machine learning techniques.
# In reinforcement learning, an agent interacts with an environment in a feedback
# configuration and updates its strategy for choosing an action based on the responses it
# gets from the environment. An illustration of this scenario is shown in Figure 14-18.
# 
# 
# 
# 
# Figure 14-18. Reinforcement learning model
# 
#     This book will not cover reinforcement learning techniques as it presents a different
# approach to the problem of learning from random environments that is distinct from the
# approach used in supervised and unsupervised learning problems.
#     In this chapter, we covered the three main components of machine learning, which
# are supervised, unsupervised, and reinforcement learning. The chapter largely focused
# on the principles for performing supervised machine learning such as framing a
# problem as a regression or classification task; splitting the dataset into training, test, and
# validation sets; understanding the bias/variance trade-off and consequently issues of
# overfitting and underfitting; and the evaluation metrics for assessing the performance of
# a learning model.
#     In the next chapter, we will briefly look at the differences between batch and online
# learning.
# 
# 
# 
# 
#                                                                                           197
# 
# CHAPTER 15
# 
# 
# 
# Batch vs. Online Learning
# Data is a vital component for building learning models. There are two design choices for
# how data is used in the modeling pipeline. The first is to build your learning model with
# data at rest (batch learning), and the other is when the data is flowing in streams into
# the learning algorithm (online learning). This flow can be as individual sample points in
# your dataset, or it can be in small batch sizes. Let’s briefly discuss these concepts.
# 
# 
# 
# B
#  atch Learning
# In batch learning the machine learning model is trained using the entire dataset that
# is available at a certain point in time. Once we have a model that performs well on the
# test set, the model is shipped for production and thus learning ends. This process is also
# called offline learning. If in the process of time, new data becomes available, and there is
# need to update the model based on the new data, the model is trained from scratch all
# over again using both the previous data samples and the new data samples.
#      This pipeline is further illustrated in Figure 15-1.
# 
# 
# 
# 
#                                                                                           199
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_15
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Reinforcement Learning")
        self.add(MarkdownBlock("# Reinforcement Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ReinforcementLearning(HierNode):
    def __init__(self):
        super().__init__("Reinforcement Learning")
        self.add(Content())

# eof
