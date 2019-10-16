# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_TheChallenge.index import TheChallenge as A_TheChallenge
from .B_TheData.index import TheData as B_TheData
from .C_TheData.index import TheData as C_TheData

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 8
# 
# 
# 
# What Is Data Science?
# Data science encompasses the tools and techniques for extracting information from
# data. Data science techniques draw extensively from the field of mathematics, statistics,
# and computation. However, data science is now encapsulated into software packages
# and libraries, thus making them easily accessible and consumable by the software
# development and engineering communities. This is a major factor to the rise of
# intelligence capabilities now integrated as a major staple in software products across all
# sorts of domains.
#      This chapter will discuss broadly on the opportunities for data science and big
# data analytics integration as part of the transformation portfolio of businesses and
# institutions and give an overview on the data science process as a reusable template for
# fulfilling data science projects.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 8: What Is Data Science?",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Chapter 8: What Is Data Science?"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter8(HierNode):
    def __init__(self):
        super().__init__("Chapter 8: What Is Data Science?")
        self.add(Content())
        self.add(A_TheChallenge())
        self.add(B_TheData())
        self.add(C_TheData())

# eof
