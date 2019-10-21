# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_TheRole.index import TheRole as A_TheRole
from .B_TheCost.index import TheCost as B_TheCost

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 13
# 
# 
# 
# What Is Machine
# Learning?
# Machine learning as a field grew out of the need to get computers to solve problems that
# are difficult to program as a sequence of instructions. Take, for example, that we want
# a computer to perform the task of recognizing faces in an image. One will realize that it
# is incredibly complicated, if not impossible to develop a precise instruction set that will
# satisfactorily perform this task. However, by drawing from the observation that humans
# improve on performing complex functions from past experiences, we can then attempt
# to develop algorithms and methods that enable the computer to establish a system for
# solving complex tasks based off prior experiences without being explicitly programmed.
# The set of methods and algorithms for discovering patterns in data is what is known as
# machine learning.
#      Two classical definitions of machine learning are that of Arthur Samuel in 1956
# who described machine learning as “the ability for computers to learn without being
# explicitly programmed” and Tom Mitchell in 1997 who defined machine learning as "the
# process of teaching a computer to perform a particular task by improving its measure of
# performance with experience.”
#      Machine learning is an interdisciplinary field of study that brings together
# techniques from the fields of computer science, statistics, mathematics, and the
# cognitive sciences which include biology, psychology, and linguistics, to mention just a
# few. While the idea of learning from data has been around the academic community for
# several decades, its entry into the mainstream technology industry began in the early
# 2000s. This growth coincided with the rise of humongous data as a result of the web
# explosion as people started sharing data over the Internet.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 13: What Is Machine Learning?",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 13: What Is Machine Learning?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter13(HierNode):
    def __init__(self):
        super().__init__("Chapter 13: What Is Machine Learning?")
        self.add(Content())
        self.add(A_TheRole())
        self.add(B_TheCost())

# eof
