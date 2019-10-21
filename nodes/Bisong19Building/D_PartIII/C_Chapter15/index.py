# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_BatchLearning.index import BatchLearning as A_BatchLearning
from .B_OnlineLearning.index import OnlineLearning as B_OnlineLearning

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 15
# 
# 
# 
# Batch vs. Online Learning
# Data is a vital component for building learning models. There are two design choices for
# how data is used in the modeling pipeline. The first is to build your learning model with
# data at rest (batch learning), and the other is when the data is flowing in streams into
# the learning algorithm (online learning). This flow can be as individual sample points in
# your dataset, or it can be in small batch sizes. Let’s briefly discuss these concepts.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 15: Batch vs. Online Learning",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 15: Batch vs. Online Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter15(HierNode):
    def __init__(self):
        super().__init__("Chapter 15: Batch vs. Online Learning")
        self.add(Content())
        self.add(A_BatchLearning())
        self.add(B_OnlineLearning())

# eof
