# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 23   Ensemble Methods
# 
# Tree Pruning
# Tree pruning is a technique for dealing with model overfitting when growing trees.
# Fully grown trees have a high tendency to overfit with high variances when applied to
# unseen samples.
#     Pruning involves growing a large tree and then pruning or clipping it to create
# a sub-tree. By doing so, we can have a full picture of the tree performance and then
# select a sub-tree that results in a minimized error measure on the test dataset. The
# technique for selecting the best sub-tree is called the cost complexity pruning or the
# weakest link pruning.
# 
# 
# Strengths and Weaknesses of CART
# One of the significant advantages of CART models is that they perform well on linear and
# non-linear datasets. Moreover, CART models implicitly take care of feature selection and
# work well with high-dimensional datasets.
#     On the flip side, CART models can very easily overfit the dataset and fail to generalize
# to new examples. This downside is mitigated by aggregating a large number of decision
# trees in techniques like Random forests and boosting ensemble algorithms.
# 
# 
# CART with Scikit-learn
# In this section, we will implement a classification and regression decision tree classifier
# with Scikit-learn.
# 
# Classification Tree with Scikit-learn
# In this code example, we will build a classification decision tree classifier to predict the
# species of flowers from the Iris dataset.
# 
# # import packages
# from sklearn.tree import DecisionTreeClassifier
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# 
# 
# 
# 
# 272
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Strengths and Weaknesses of CART")
        self.add(MarkdownBlock("# Strengths and Weaknesses of CART"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Strengthsand(HierNode):
    def __init__(self):
        super().__init__("Strengths and Weaknesses of CART")
        self.add(Content())

# eof
