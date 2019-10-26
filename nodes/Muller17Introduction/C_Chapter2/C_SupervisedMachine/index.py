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

from .A_SomeSample.index import SomeSample as A_SomeSample
from .B_kNearestNeighbors.index import kNearestNeighbors as B_kNearestNeighbors
from .C_LinearModels.index import LinearModels as C_LinearModels
from .D_NaiveBayes.index import NaiveBayes as D_NaiveBayes
from .E_DecisionTrees.index import DecisionTrees as E_DecisionTrees
from .F_Ensemblesof.index import Ensemblesof as F_Ensemblesof
from .G_KernelizedSupport.index import KernelizedSupport as G_KernelizedSupport
from .H_NeuralNetworks.index import NeuralNetworks as H_NeuralNetworks

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# Figure 2-1. Trade-off of model complexity against training and test accuracy
# 
# Relation of Model Complexity to Dataset Size
# It’s important to note that model complexity is intimately tied to the variation of
# inputs contained in your training dataset: the larger variety of data points your data‐
# set contains, the more complex a model you can use without overfitting. Usually, col‐
# lecting more data points will yield more variety, so larger datasets allow building
# more complex models. However, simply duplicating the same data points or collect‐
# ing very similar data will not help.
# Going back to the boat selling example, if we saw 10,000 more rows of customer data,
# and all of them complied with the rule “If the customer is older than 45, and has less
# than 3 children or is not divorced, then they want to buy a boat,” we would be much
# more likely to believe this to be a good rule than when it was developed using only
# the 12 rows in Table 2-1.
# Having more data and building appropriately more complex models can often work
# wonders for supervised learning tasks. In this book, we will focus on working with
# datasets of fixed sizes. In the real world, you often have the ability to decide how
# much data to collect, which might be more beneficial than tweaking and tuning your
# model. Never underestimate the power of more data.
# 
# Supervised Machine Learning Algorithms
# We will now review the most popular machine learning algorithms and explain how
# they learn from data and how they make predictions. We will also discuss how the
# concept of model complexity plays out for each of these models, and provide an over‐
# 
# 
#                                                     Supervised Machine Learning Algorithms   |   29
# 
# view of how each algorithm builds a model. We will examine the strengths and weak‐
# nesses of each algorithm, and what kind of data they can best be applied to. We will
# also explain the meaning of the most important parameters and options.4 Many algo‐
# rithms have a classification and a regression variant, and we will describe both.
# It is not necessary to read through the descriptions of each algorithm in detail, but
# understanding the models will give you a better feeling for the different ways
# machine learning algorithms can work. This chapter can also be used as a reference
# guide, and you can come back to it when you are unsure about the workings of any of
# the algorithms.
# 
# Some Sample Datasets
# We will use several datasets to illustrate the different algorithms. Some of the datasets
# will be small and synthetic (meaning made-up), designed to highlight particular
# aspects of the algorithms. Other datasets will be large, real-world examples.
# An example of a synthetic two-class classification dataset is the forge dataset, which
# has two features. The following code creates a scatter plot (Figure 2-2) visualizing all
# of the data points in this dataset. The plot has the first feature on the x-axis and the
# second feature on the y-axis. As is always the case in scatter plots, each data point is
# represented as one dot. The color and shape of the dot indicates its class:
# In[2]:
#        # generate dataset
#        X, y = mglearn.datasets.make_forge()
#        # plot dataset
#        mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
#        plt.legend(["Class 0", "Class 1"], loc=4)
#        plt.xlabel("First feature")
#        plt.ylabel("Second feature")
#        print("X.shape: {}".format(X.shape))
# 
# Out[2]:
#        X.shape: (26, 2)
# 
# 
# 
# 
# 4 Discussing all of them is beyond the scope of the book, and we refer you to the scikit-learn documentation
#      for more details.
# 
# 
# 
# 30     |   Chapter 2: Supervised Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Supervised Machine Learning Algorithms",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SupervisedMachine(HierNode):
    def __init__(self):
        super().__init__("Supervised Machine Learning Algorithms")
        self.add(Content(), "content")
        self.add(A_SomeSample())
        self.add(B_kNearestNeighbors())
        self.add(C_LinearModels())
        self.add(D_NaiveBayes())
        self.add(E_DecisionTrees())
        self.add(F_Ensemblesof())
        self.add(G_KernelizedSupport())
        self.add(H_NeuralNetworks())

# eof
