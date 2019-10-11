# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_DecisionTrees.index import DecisionTrees as A_DecisionTrees
from .B_RandomForests.index import RandomForests as B_RandomForests
from .C_StochasticGradient.index import StochasticGradient as C_StochasticGradient
from .D_XGBoostExtreme.index import XGBoostExtreme as D_XGBoostExtreme

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 23
# 
# 
# 
# Ensemble Methods
# Ensemble learning is a technique that combines the output of multiple classifiers also
# called weak learners to build a more robust prediction model. Ensemble methods work
# by combining a group of classifiers (or models) to get an enhanced prediction accuracy.
# The idea behind an “ensemble” is that the performance from the average of a group
# of classifiers will be better than each classifier on its own. So each classifier is called a
# “weak” learner.
#      Ensemble learners are usually high-performing algorithms for both classification
# and regression tasks and are mostly competition-winning algorithms. Examples of
# ensemble learning algorithms are Random Forest (RF) and Stochastic Gradient Boosting
# (SGB). We will motivate our discussion of ensemble methods by first discussing decision
# trees because ensemble classifiers such as RF and SGB are built by combining several
# decision tree classifiers.
# 
# 
# 
# D
#  ecision Trees
# Decision trees, more popularly known as classification and regression trees (CART),
# can be visualized as a graph or flowchart of decisions. A branch connects the nodes in
# the graph, the last node of the graph is called a terminal node, and the topmost node is
# called the root. As seen in Figure 23-1, when constructing a decision tree, the root is at
# the top, while the branches connect nodes at lower layers until the terminal node.
# 
# 
# 
# 
#                                                                                           269
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_23
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Chapter 23: Ensemble Methods")
        self.add(MarkdownBlock("# Chapter 23: Ensemble Methods"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter23(HierNode):
    def __init__(self):
        super().__init__("Chapter 23: Ensemble Methods")
        self.add(Content())
        self.add(A_DecisionTrees())
        self.add(B_RandomForests())
        self.add(C_StochasticGradient())
        self.add(D_XGBoostExtreme())

# eof
