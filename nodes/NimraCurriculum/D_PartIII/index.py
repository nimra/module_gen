# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Chapter13.index import Chapter13 as A_Chapter13
from .B_Chapter14.index import Chapter14 as B_Chapter14
from .C_Chapter15.index import Chapter15 as C_Chapter15
from .D_Chapter16.index import Chapter16 as D_Chapter16
from .E_Chapter17.index import Chapter17 as E_Chapter17

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PART III
# 
# Introducing Machine
# Learning
# 
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
# 
# 
# 
# 
#                                                                                           169
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_13
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Part III: Introducing Machine Learning")
        self.add(MarkdownBlock("# Part III: Introducing Machine Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PartIII(HierNode):
    def __init__(self):
        super().__init__("Part III: Introducing Machine Learning")
        self.add(Content())
        self.add(A_Chapter13())
        self.add(B_Chapter14())
        self.add(C_Chapter15())
        self.add(D_Chapter16())
        self.add(E_Chapter17())

# eof
