# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_MachineLearning.index import MachineLearning as A_MachineLearning
from .B_DeepLearning.index import DeepLearning as B_DeepLearning
from .C_DeepLearning.index import DeepLearning as C_DeepLearning
from .D_DeepLearning.index import DeepLearning as D_DeepLearning
from .E_Review.index import Review as E_Review

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                                          CHAPTER 1
#                           Introduction to Deep Learning
# 
# 
# 
# 
# Deep learning has revolutionized the technology industry. Modern machine transla‐
# tion, search engines, and computer assistants are all powered by deep learning. This
# trend will only continue as deep learning expands its reach into robotics, pharma‐
# ceuticals, energy, and all other fields of contemporary technology. It is rapidly becom‐
# ing essential for the modern software professional to develop a working knowledge of
# the principles of deep learning.
# In this chapter, we will introduce you to the history of deep learning, and to the
# broader impact deep learning has had on the research and commercial communities.
# We will next cover some of the most famous applications of deep learning. This will
# include both prominent machine learning architectures and fundamental deep learn‐
# ing primitives. We will end by giving a brief perspective of where deep learning is
# heading over the next few years before we dive into TensorFlow in the next few
# chapters.
# 
# Machine Learning Eats Computer Science
# Until recently, software engineers went to school to learn a number of basic algo‐
# rithms (graph search, sorting, database queries, and so on). After school, these engi‐
# neers would go out into the real world to apply these algorithms to systems. Most of
# today’s digital economy is built on intricate chains of basic algorithms laboriously
# glued together by generations of engineers. Most of these systems are not capable of
# adapting. All configurations and reconfigurations have to be performed by highly
# trained engineers, rendering systems brittle.
# Machine learning promises to change the field of software development by enabling
# systems to adapt dynamically. Deployed machine learning systems are capable of
# learning desired behaviors from databases of examples. Furthermore, such systems
# 
# 
#                                                                                        1
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 1. Introduction to Deep Learning",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 1. Introduction to Deep Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter1(HierNode):
    def __init__(self):
        super().__init__("Chapter 1. Introduction to Deep Learning")
        self.add(Content())
        self.add(A_MachineLearning())
        self.add(B_DeepLearning())
        self.add(C_DeepLearning())
        self.add(D_DeepLearning())
        self.add(E_Review())

# eof
