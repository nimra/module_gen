# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_SupervisedLearning.index import SupervisedLearning as A_SupervisedLearning
from .B_UnsupervisedLearning.index import UnsupervisedLearning as B_UnsupervisedLearning
from .C_ReinforcementLearning.index import ReinforcementLearning as C_ReinforcementLearning

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 14
# 
# 
# 
# Principles of Learning
# Machine learning is, for the most part, sub-divided into three components based on the
# approach to the learning problem. The three predominant categories of learning are the
# supervised, unsupervised, and reinforcement learning schemes. In this chapter, we will
# go over supervised learning schemes in detail and also touch upon unsupervised and
# reinforcement learning schemes to a lesser extent.
#     The focus on supervised learning is for a variety of reasons. Firstly, they are the
# predominant techniques used for building machine learning products in industry;
# secondly, as you will soon learn, they are easy to ground truth and assess their
# performances before being deployed as part of a large-scale production pipeline. Let’s
# examine each of the three schemes.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 14: Principles of Learning",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Chapter 14: Principles of Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter14(HierNode):
    def __init__(self):
        super().__init__("Chapter 14: Principles of Learning")
        self.add(Content())
        self.add(A_SupervisedLearning())
        self.add(B_UnsupervisedLearning())
        self.add(C_ReinforcementLearning())

# eof
