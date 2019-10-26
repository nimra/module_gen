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

from .A_Categoriesof.index import Categoriesof as A_Categoriesof
from .B_QualitativeExamples.index import QualitativeExamples as B_QualitativeExamples
from .C_Summary.index import Summary as C_Summary

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# clarity in the following pages is likely due to the many workshop participants and co-
# instructors who have given me valuable feedback on this material over the years!
# Finally, if you are seeking a more comprehensive or technical treatment of any of
# these subjects, I’ve listed several resources and references in “Further Machine Learn‐
# ing Resources” on page 514.
# 
# What Is Machine Learning?
# Before we take a look at the details of various machine learning methods, let’s start by
# looking at what machine learning is, and what it isn’t. Machine learning is often cate‐
# gorized as a subfield of artificial intelligence, but I find that categorization can often
# be misleading at first brush. The study of machine learning certainly arose from
# research in this context, but in the data science application of machine learning meth‐
# ods, it’s more helpful to think of machine learning as a means of building models of
# data.
# Fundamentally, machine learning involves building mathematical models to help
# understand data. “Learning” enters the fray when we give these models tunable
# parameters that can be adapted to observed data; in this way the program can be con‐
# sidered to be “learning” from the data. Once these models have been fit to previously
# seen data, they can be used to predict and understand aspects of newly observed data.
# I’ll leave to the reader the more philosophical digression regarding the extent to
# which this type of mathematical, model-based “learning” is similar to the “learning”
# exhibited by the human brain.
# Understanding the problem setting in machine learning is essential to using these
# tools effectively, and so we will start with some broad categorizations of the types of
# approaches we’ll discuss here.
# 
# Categories of Machine Learning
# At the most fundamental level, machine learning can be categorized into two main
# types: supervised learning and unsupervised learning.
# Supervised learning involves somehow modeling the relationship between measured
# features of data and some label associated with the data; once this model is deter‐
# mined, it can be used to apply labels to new, unknown data. This is further subdivi‐
# ded into classification tasks and regression tasks: in classification, the labels are
# discrete categories, while in regression, the labels are continuous quantities. We will
# see examples of both types of supervised learning in the following section.
# Unsupervised learning involves modeling the features of a dataset without reference to
# any label, and is often described as “letting the dataset speak for itself.” These models
# include tasks such as clustering and dimensionality reduction. Clustering algorithms
# 
# 
# 332   |   Chapter 5: Machine Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "What Is Machine Learning?",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WhatIs(HierNode):
    def __init__(self):
        super().__init__("What Is Machine Learning?")
        self.add(Content())
        self.add(A_Categoriesof())
        self.add(B_QualitativeExamples())
        self.add(C_Summary())

# eof
