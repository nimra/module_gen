# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_XGBoostwith.index import XGBoostwith as A_XGBoostwith

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 23   Ensemble Methods
# 
# 
# XGBoost (Extreme Gradient Boosting)
# XGBoost which is short for Extreme Gradient Boosting makes a couple of computational
# and algorithmic modifications to the stochastic gradient boosting algorithm. This
# enhanced algorithm is a favorite in machine learning practice due to its speed and has
# been the winning algorithm in many machine learning competitions. Let’s go through
# some of the modifications made by the XGBoost algorithm.
# 
#       1. Parallel training: XGBoost supports parallel training over multiple
#          cores. This has made XGBoost extremely fast compared to other
#          machine learning algorithms.
# 
#       2. Out of core computation: XGBoost facilitates training from data
#          not loaded into memory. This feature is a huge advantage when
#          you’re dealing with large datasets that may not necessarily fit into
#          the RAM of the computer.
# 
#       3. Sparse data optimization: XGBoost is optimized to handle and
#          speed up computation with sparse matrices. Sparse matrices
#          contain lots of zeros in its cells.
# 
# 
# XGBoost with Scikit-learn
# This section will implement XGBoost with Scikit-learn for both regression and
# classification use cases.
# 
# XGBoost for Classification
# In this code example, we will build a XGBoost classification model to predict the species
# of flowers from the Iris dataset.
# 
# # import packages
# from xgboost import XGBClassifier
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# 
# # load dataset
# data = datasets.load_iris()
# 
# 284
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("XGBoost (Extreme Gradient Boosting)")
        self.add(MarkdownBlock("# XGBoost (Extreme Gradient Boosting)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class XGBoostExtreme(HierNode):
    def __init__(self):
        super().__init__("XGBoost (Extreme Gradient Boosting)")
        self.add(Content())
        self.add(A_XGBoostwith())

# eof
