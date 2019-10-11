# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_WhyLogistic.index import WhyLogistic as A_WhyLogistic
from .B_Introducingthe.index import Introducingthe as B_Introducingthe
from .C_Trainingthe.index import Trainingthe as C_Trainingthe
from .D_MulticlassClassificationMultinomial.index import MulticlassClassificationMultinomial as D_MulticlassClassificationMultinomial
from .E_LogisticRegression.index import LogisticRegression as E_LogisticRegression
from .F_Optimizingthe.index import Optimizingthe as F_Optimizingthe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 20
# 
# 
# 
# Logistic Regression
# Logistic regression is a supervised machine learning algorithm developed for learning
# classification problems. A classification learning problem is when the target variable is
# categorical. The goal of logistic regression is to map a function from the features of the
# dataset to the targets to predict the probability that a new example belongs to one of the
# target classes. Figure 20-1 is an example of a dataset with categorical targets.
# 
# 
# 
# 
# Figure 20-1. Dataset with qualitative variables as output
# 
# 
# Why Logistic Regression?
# To develop our understanding of classification with logistic regression and why linear
# regression is unsuitable for learning categorical outputs, let us consider a binary or
# two-­class classification problem. The dataset illustrated in Figure 20-2 has the output y
# (i.e., eye disease) = {disease, no-disease} is an example of dataset with binary targets.
# 
# 
# 
#                                                                                           243
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_20
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Chapter 20: Logistic Regression")
        self.add(MarkdownBlock("# Chapter 20: Logistic Regression"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter20(HierNode):
    def __init__(self):
        super().__init__("Chapter 20: Logistic Regression")
        self.add(Content())
        self.add(A_WhyLogistic())
        self.add(B_Introducingthe())
        self.add(C_Trainingthe())
        self.add(D_MulticlassClassificationMultinomial())
        self.add(E_LogisticRegression())
        self.add(F_Optimizingthe())

# eof
