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

from .A_Classificationand.index import Classificationand as A_Classificationand
from .B_GeneralizationOverfitting.index import GeneralizationOverfitting as B_GeneralizationOverfitting
from .C_SupervisedMachine.index import SupervisedMachine as C_SupervisedMachine
from .D_UncertaintyEstimates.index import UncertaintyEstimates as D_UncertaintyEstimates
from .E_Summaryand.index import Summaryand as E_Summaryand

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                                                                             CHAPTER 2
#                                                 Supervised Learning
# 
# 
# 
# 
# As we mentioned earlier, supervised machine learning is one of the most commonly
# used and successful types of machine learning. In this chapter, we will describe super‐
# vised learning in more detail and explain several popular supervised learning algo‐
# rithms. We already saw an application of supervised machine learning in Chapter 1:
# classifying iris flowers into several species using physical measurements of the
# flowers.
# Remember that supervised learning is used whenever we want to predict a certain
# outcome from a given input, and we have examples of input/output pairs. We build a
# machine learning model from these input/output pairs, which comprise our training
# set. Our goal is to make accurate predictions for new, never-before-seen data. Super‐
# vised learning often requires human effort to build the training set, but afterward
# automates and often speeds up an otherwise laborious or infeasible task.
# 
# Classification and Regression
# There are two major types of supervised machine learning problems, called classifica‐
# tion and regression.
# In classification, the goal is to predict a class label, which is a choice from a predefined
# list of possibilities. In Chapter 1 we used the example of classifying irises into one of
# three possible species. Classification is sometimes separated into binary classification,
# which is the special case of distinguishing between exactly two classes, and multiclass
# classification, which is classification between more than two classes. You can think of
# binary classification as trying to answer a yes/no question. Classifying emails as
# either spam or not spam is an example of a binary classification problem. In this
# binary classification task, the yes/no question being asked would be “Is this email
# spam?”
# 
# 
#                                                                                           25
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 2. Supervised Learning",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter2(HierNode):
    def __init__(self):
        super().__init__("Chapter 2. Supervised Learning")
        self.add(Content(), "content")
        self.add(A_Classificationand())
        self.add(B_GeneralizationOverfitting())
        self.add(C_SupervisedMachine())
        self.add(D_UncertaintyEstimates())
        self.add(E_Summaryand())

# eof
