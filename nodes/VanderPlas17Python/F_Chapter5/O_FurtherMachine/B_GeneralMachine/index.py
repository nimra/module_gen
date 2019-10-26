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
# 
#                                                                           Index
# 
# 
# 
# 
# Symbols                                     multidimensional aggregates, 60
# %automagic, 19                              presidents average height example, 61
# %cpaste, 11                                 summing the values in an array, 59
# %debug, 22                                  various functions, 61
# %history, 16                            aggregation (Pandas), 158-170
# %lprun, 28                                  groupby() operation, 161-170
# %lsmagic, 13                                MultiIndex, 140
# %magic, 13                                  Planets dataset for, 159
# %matplotlib, 219                            simple aggregation, 159-161
# %memit, 29                              Akaike information criterion (AIC), 487, 489
# %mode, 20-22                            Albers equal-area projection, 303
# %mprun, 29                              algorithmic efficiency
# %paste, 11                                  big-O notation, 92
# %prun, 27                                   dataset size and, 85
# %run, 12                                ampersand (&), 77
# %time, 25-27                            Anaconda, xiv
# %timeit, 12, 25-27                      and keyword, 77
# & (ampersand), 77                       annotation of plots, 268-275
# * (asterisk), 7                             arrows, 272-275
# : (colon), 44                               holidays/US births example, 269
# ? (question mark), 3                        transforms and text position, 270-272
# ?? (double question mark), 5            APIs (see Estimator API)
# _ (underscore) shortcut, 15             append() method, Pandas vs. Python, 146
# | (operator), 77                        apply() method, 167
#                                         arithmetic operators, 52
#                                         arrays
# A                                           accessing single rows/columns, 45
# absolute value function, 54
#                                             arithmetic operators, 52
# aggregate() method, 166
#                                             attributes, 42
# aggregates
#                                             basics, 42
#    computed directly from object, 57
#                                             Boolean, 73-75
#    multidimensional, 60
#                                             broadcasting, 63-69
#    summarizing set of values with, 61
#                                             centering, 68
# aggregation (NumPy), 58-63
#                                             computation on, 50-58
#    minimum and maximum, 59
# 
# 
#                                                                                    517
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "General Machine Learning",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GeneralMachine(HierNode):
    def __init__(self):
        super().__init__("General Machine Learning")
        self.add(Content())

# eof