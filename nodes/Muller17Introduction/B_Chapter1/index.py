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

from .A_WhyMachine.index import WhyMachine as A_WhyMachine
from .B_WhyPython.index import WhyPython as B_WhyPython
from .C_scikitlearn.index import scikitlearn as C_scikitlearn
from .D_EssentialLibraries.index import EssentialLibraries as D_EssentialLibraries
from .E_Python2.index import Python2 as E_Python2
from .F_VersionsUsed.index import VersionsUsed as F_VersionsUsed
from .G_AFirst.index import AFirst as G_AFirst
from .H_Summaryand.index import Summaryand as H_Summaryand

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                                                                            CHAPTER 1
#                                                                Introduction
# 
# 
# 
# 
# Machine learning is about extracting knowledge from data. It is a research field at the
# intersection of statistics, artificial intelligence, and computer science and is also
# known as predictive analytics or statistical learning. The application of machine
# learning methods has in recent years become ubiquitous in everyday life. From auto‐
# matic recommendations of which movies to watch, to what food to order or which
# products to buy, to personalized online radio and recognizing your friends in your
# photos, many modern websites and devices have machine learning algorithms at their
# core. When you look at a complex website like Facebook, Amazon, or Netflix, it is
# very likely that every part of the site contains multiple machine learning models.
# Outside of commercial applications, machine learning has had a tremendous influ‐
# ence on the way data-driven research is done today. The tools introduced in this book
# have been applied to diverse scientific problems such as understanding stars, finding
# distant planets, discovering new particles, analyzing DNA sequences, and providing
# personalized cancer treatments.
# Your application doesn’t need to be as large-scale or world-changing as these exam‐
# ples in order to benefit from machine learning, though. In this chapter, we will
# explain why machine learning has become so popular and discuss what kinds of
# problems can be solved using machine learning. Then, we will show you how to build
# your first machine learning model, introducing important concepts along the way.
# 
# Why Machine Learning?
# In the early days of “intelligent” applications, many systems used handcoded rules of
# “if ” and “else” decisions to process data or adjust to user input. Think of a spam filter
# whose job is to move the appropriate incoming email messages to a spam folder. You
# could make up a blacklist of words that would result in an email being marked as
# 
# 
#                                                                                          1
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 1. Introduction",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter1(HierNode):
    def __init__(self):
        super().__init__("Chapter 1. Introduction")
        self.add(Content(), "content")
        self.add(A_WhyMachine())
        self.add(B_WhyPython())
        self.add(C_scikitlearn())
        self.add(D_EssentialLibraries())
        self.add(E_Python2())
        self.add(F_VersionsUsed())
        self.add(G_AFirst())
        self.add(H_Summaryand())

# eof
