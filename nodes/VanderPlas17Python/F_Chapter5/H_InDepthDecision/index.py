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

from .A_MotivatingRandom.index import MotivatingRandom as A_MotivatingRandom
from .B_Ensemblesof.index import Ensemblesof as B_Ensemblesof
from .C_RandomForest.index import RandomForest as C_RandomForest
from .D_ExampleRandom.index import ExampleRandom as D_ExampleRandom
from .E_Summaryof.index import Summaryof as E_Summaryof

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# In-Depth: Decision Trees and Random Forests
# Previously we have looked in depth at a simple generative classifier (naive Bayes; see
# “In Depth: Naive Bayes Classification” on page 382) and a powerful discriminative
# classifier (support vector machines; see “In-Depth: Support Vector Machines” on
# page 405). Here we’ll take a look at motivating another powerful algorithm—a non‐
# parametric algorithm called random forests. Random forests are an example of an
# ensemble method, a method that relies on aggregating the results of an ensemble of
# simpler estimators. The somewhat surprising result with such ensemble methods is
# that the sum can be greater than the parts; that is, a majority vote among a number of
# estimators can end up being better than any of the individual estimators doing the
# voting! We will see examples of this in the following sections. We begin with the stan‐
# dard imports:
#     In[1]: %matplotlib inline
#            import numpy as np
#            import matplotlib.pyplot as plt
#            import seaborn as sns; sns.set()
# 
# 
# Motivating Random Forests: Decision Trees
# Random forests are an example of an ensemble learner built on decision trees. For this
# reason we’ll start by discussing decision trees themselves.
# Decision trees are extremely intuitive ways to classify or label objects: you simply ask
# a series of questions designed to zero in on the classification. For example, if you
# wanted to build a decision tree to classify an animal you come across while on a hike,
# you might construct the one shown in Figure 5-67.
# 
# 
# 
# 
# Figure 5-67. An example of a binary decision tree
# 
# 
# 
# 
#                                                In-Depth: Decision Trees and Random Forests   |   421
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "In-Depth: Decision Trees and Random Forests",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class InDepthDecision(HierNode):
    def __init__(self):
        super().__init__("In-Depth: Decision Trees and Random Forests")
        self.add(Content())
        self.add(A_MotivatingRandom())
        self.add(B_Ensemblesof())
        self.add(C_RandomForest())
        self.add(D_ExampleRandom())
        self.add(E_Summaryof())

# eof
