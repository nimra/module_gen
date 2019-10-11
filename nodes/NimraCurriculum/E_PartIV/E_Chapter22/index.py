# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_WhatIs.index import WhatIs as A_WhatIs
from .B_TheSupport.index import TheSupport as B_TheSupport
from .C_MulticlassClassification.index import MulticlassClassification as C_MulticlassClassification
from .D_TheKernel.index import TheKernel as D_TheKernel

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 22
# 
# 
# 
# Support Vector Machines
# Support vector machine (SVM) is a machine learning algorithm for learning classification
# and regression models. To build intuition, we will consider the case of learning a
# classification model with SVM. Given a dataset with two target classes that are linearly
# separable, it turns out that there exists an infinite number of lines that can discriminate
# between the two classes (see Figure 22-1). The goal of the SVM is to find the best line that
# separates the two classes. In higher dimensions, this line is called a hyperplane.
# 
# 
# 
# 
# Figure 22-1. Infinite set of discriminants
# 
# 
# What Is a Hyperplane?
# A hyperplane is a line or more technically called a discriminant that separates two
# classes in n-dimensional space. When a hyperplane is drawn in 2-D space, it is called a
# line. In 3-D space, it is called a plane, and in dimensions greater than 3, the discriminant
# is called a hyperplane (see Figure 22-2). For any n-dimensional world, we have n-1
# hyperplanes.
#                                                                                          255
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_22
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Chapter 22: Support Vector Machines")
        self.add(MarkdownBlock("# Chapter 22: Support Vector Machines"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter22(HierNode):
    def __init__(self):
        super().__init__("Chapter 22: Support Vector Machines")
        self.add(Content())
        self.add(A_WhatIs())
        self.add(B_TheSupport())
        self.add(C_MulticlassClassification())
        self.add(D_TheKernel())

# eof
