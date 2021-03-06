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
# General Machine Learning
# Of course, machine learning is much broader than just the Python world. There are
# many good resources to take your knowledge further, and here I highlight a few that I
# have found useful:
# Machine Learning
#    Taught by Andrew Ng (Coursera), this is a very clearly taught, free online course
#    covering the basics of machine learning from an algorithmic perspective. It
#    assumes undergraduate-level understanding of mathematics and programming,
#    and steps through detailed considerations of some of the most important
#    machine learning algorithms. Homework assignments, which are algorithmically
#    graded, have you actually implement some of these models yourself.
# Pattern Recognition and Machine Learning
#     Written by Christopher Bishop, this classic technical text covers the concepts of
#     machine learning discussed in this chapter in detail. If you plan to go further in
#     this subject, you should have this book on your shelf.
# Machine Learning: A Probabilistic Perspective
#    Written by Kevin Murphy, this is an excellent graduate-level text that explores
#    nearly all important machine learning algorithms from a ground-up, unified
#    probabilistic perspective.
# These resources are more technical than the material presented in this book, but to
# really understand the fundamentals of these methods requires a deep dive into the
# mathematics behind them. If you’re up for the challenge and ready to bring your data
# science to the next level, don’t hesitate to dive in!
# 
# 
# 
# 
#                                                     Further Machine Learning Resources   |   515
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Machine Learning in Python",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MachineLearning(HierNode):
    def __init__(self):
        super().__init__("Machine Learning in Python")
        self.add(Content())

# eof
