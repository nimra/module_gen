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

from .A_MachineLearning.index import MachineLearning as A_MachineLearning
from .B_GeneralMachine.index import GeneralMachine as B_GeneralMachine

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#       TensorFlow have recently made deep learning approaches much more accessible
#       than they once were. As of the writing of this book, deep learning in Python is
#       still relatively young, and so I can’t yet point to any definitive resource. That said,
#       the list of references in the following section should provide a useful place to
#       start.
# 
# Further Machine Learning Resources
# This chapter has been a quick tour of machine learning in Python, primarily using
# the tools within the Scikit-Learn library. As long as the chapter is, it is still too short
# to cover many interesting and important algorithms, approaches, and discussions.
# Here I want to suggest some resources for those who would like to learn more about
# machine learning.
# 
# Machine Learning in Python
# To learn more about machine learning in Python, I’d suggest some of the following
# resources:
# The Scikit-Learn website
#     The Scikit-Learn website has an impressive breadth of documentation and exam‐
#     ples covering some of the models discussed here, and much, much more. If you
#     want a brief survey of the most important and often used machine learning algo‐
#     rithms, this website is a good place to start.
# SciPy, PyCon, and PyData tutorial videos
#     Scikit-Learn and other machine learning topics are perennial favorites in the
#     tutorial tracks of many Python-focused conference series, in particular the
#     PyCon, SciPy, and PyData conferences. You can find the most recent ones via a
#     simple web search.
# Introduction to Machine Learning with Python
#      Written by Andreas C. Mueller and Sarah Guido, this book includes a fuller treat‐
#      ment of the topics in this chapter. If you’re interested in reviewing the fundamen‐
#      tals of machine learning and pushing the Scikit-Learn toolkit to its limits, this is a
#      great resource, written by one of the most prolific developers on the Scikit-Learn
#      team.
# Python Machine Learning
#     Sebastian Raschka’s book focuses less on Scikit-Learn itself, and more on the
#     breadth of machine learning tools available in Python. In particular, there is
#     some very useful discussion on how to scale Python-based machine learning
#     approaches to large and complex datasets.
# 
# 
# 
# 
# 514   |   Chapter 5: Machine Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Further Machine Learning Resources",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FurtherMachine(HierNode):
    def __init__(self):
        super().__init__("Further Machine Learning Resources")
        self.add(Content())
        self.add(A_MachineLearning())
        self.add(B_GeneralMachine())

# eof
