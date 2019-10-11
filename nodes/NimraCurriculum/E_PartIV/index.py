# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Chapter18.index import Chapter18 as A_Chapter18
from .B_Chapter19.index import Chapter19 as B_Chapter19
from .C_Chapter20.index import Chapter20 as C_Chapter20
from .D_Chapter21.index import Chapter21 as D_Chapter21
from .E_Chapter22.index import Chapter22 as E_Chapter22
from .F_Chapter23.index import Chapter23 as F_Chapter23
from .G_Chapter24.index import Chapter24 as G_Chapter24
from .H_Chapter25.index import Chapter25 as H_Chapter25
from .I_Chapter26.index import Chapter26 as I_Chapter26

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PART IV
# 
# Machine Learning
# in Practice
# 
# CHAPTER 18
# 
# 
# 
# Introduction to
# Scikit-learn
# Scikit-learn is a Python library that provides a standard interface for implementing
# machine learning algorithms. It includes other ancillary functions that are integral
# to the machine learning pipeline such as data preprocessing steps, data resampling
# techniques, evaluation parameters, and search interfaces for tuning/optimizing an
# algorithm’s performance.
#     This section will go through the functions for implementing a typical machine
# learning pipeline with Scikit-learn. Since, Scikit-learn has a variety of packages and
# modules that are called depending on the use case, we’ll import a module directly from
# a package if and when needed using the from keyword. Again the goal of this material is
# to provide the foundation to be able to comb through the exhaustive Scikit-learn library
# and be able to use the right tool or function to get the job done.
# 
# 
# 
# Loading Sample Datasets from Scikit-learn
# Scikit-learn comes with a set of small standard datasets for quickly testing and
# prototyping machine learning models. These datasets are ideal for learning purposes
# when starting off working with machine learning or even trying out the performance of
# some new model. They save a bit of the time required to identify, download, and clean
# up a dataset obtained from the wild. However, these datasets are small and well curated,
# they do not represent real-world scenarios.
#     Five popular sample datasets are
#        •    Boston house-prices dataset
# 
#        •    Diabetes dataset
# 
#                                                                                           215
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_18
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Part IV: Machine Learning in Practice")
        self.add(MarkdownBlock("# Part IV: Machine Learning in Practice"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PartIV(HierNode):
    def __init__(self):
        super().__init__("Part IV: Machine Learning in Practice")
        self.add(Content())
        self.add(A_Chapter18())
        self.add(B_Chapter19())
        self.add(C_Chapter20())
        self.add(D_Chapter21())
        self.add(E_Chapter22())
        self.add(F_Chapter23())
        self.add(G_Chapter24())
        self.add(H_Chapter25())
        self.add(I_Chapter26())

# eof
