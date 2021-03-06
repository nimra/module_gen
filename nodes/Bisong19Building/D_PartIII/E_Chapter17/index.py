# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Classesof.index import Classesof as A_Classesof
from .B_UnsupervisedAlgorithms.index import UnsupervisedAlgorithms as B_UnsupervisedAlgorithms

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 17
# 
# 
# 
# Learning Algorithms
# In this section, we introduce a variety of supervised and unsupervised machine learning
# algorithms. The algorithms presented here provide a foundation for understanding other
# machine learning methods (e.g., linear and logistic regression), and others like Random
# forests and Extreme Stochastic Gradient Boosting (XGBoost) are widely used in applied
# machine learning.
#     We will survey the various learning algorithms from a conceptual level. In general,
# the discussion will cut across
# 
#        •    What a particular algorithm is all about and how it works.
# 
#        •    How we interpret the results of the learning algorithm.
# 
#        •    What various ways it can be optimized to improve performance in
#             certain circumstances.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 17: Learning Algorithms",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 17: Learning Algorithms"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter17(HierNode):
    def __init__(self):
        super().__init__("Chapter 17: Learning Algorithms")
        self.add(Content())
        self.add(A_Classesof())
        self.add(B_UnsupervisedAlgorithms())

# eof
