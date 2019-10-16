# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Chapter1.index import Chapter1 as A_Chapter1
from .B_Chapter2.index import Chapter2 as B_Chapter2
from .C_Chapter3.index import Chapter3 as C_Chapter3
from .D_Chapter4.index import Chapter4 as D_Chapter4
from .E_Chapter5.index import Chapter5 as E_Chapter5
from .F_Chapter6.index import Chapter6 as F_Chapter6
from .G_Chapter7.index import Chapter7 as G_Chapter7
from .H_Chapter8.index import Chapter8 as H_Chapter8

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Download from finelybook www.finelybook.com
# 
# 
# 
#                                               PART I
#                   The Fundamentals of
#                      Machine Learning
# 
# Download from finelybook www.finelybook.com
# 
#                   Download from finelybook www.finelybook.com
# 
# 
#                                                                            CHAPTER 1
#                      The Machine Learning Landscape
# 
# 
# 
# 
# When most people hear “Machine Learning,” they picture a robot: a dependable but‐
# ler or a deadly Terminator depending on who you ask. But Machine Learning is not
# just a futuristic fantasy, it’s already here. In fact, it has been around for decades in
# some specialized applications, such as Optical Character Recognition (OCR). But the
# first ML application that really became mainstream, improving the lives of hundreds
# of millions of people, took over the world back in the 1990s: it was the spam filter.
# Not exactly a self-aware Skynet, but it does technically qualify as Machine Learning
# (it has actually learned so well that you seldom need to flag an email as spam any‐
# more). It was followed by hundreds of ML applications that now quietly power hun‐
# dreds of products and features that you use regularly, from better recommendations
# to voice search.
# Where does Machine Learning start and where does it end? What exactly does it
# mean for a machine to learn something? If I download a copy of Wikipedia, has my
# computer really “learned” something? Is it suddenly smarter? In this chapter we will
# start by clarifying what Machine Learning is and why you may want to use it.
# Then, before we set out to explore the Machine Learning continent, we will take a
# look at the map and learn about the main regions and the most notable landmarks:
# supervised versus unsupervised learning, online versus batch learning, instance-
# based versus model-based learning. Then we will look at the workflow of a typical ML
# project, discuss the main challenges you may face, and cover how to evaluate and
# fine-tune a Machine Learning system.
# This chapter introduces a lot of fundamental concepts (and jargon) that every data
# scientist should know by heart. It will be a high-level overview (the only chapter
# without much code), all rather simple, but you should make sure everything is
# crystal-clear to you before continuing to the rest of the book. So grab a coffee and let’s
# get started!
# 
# 
#                                                                                          3
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Part I. The Fundamentals of Machine Learning",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Part I. The Fundamentals of Machine Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PartI(HierNode):
    def __init__(self):
        super().__init__("Part I. The Fundamentals of Machine Learning")
        self.add(Content())
        self.add(A_Chapter1())
        self.add(B_Chapter2())
        self.add(C_Chapter3())
        self.add(D_Chapter4())
        self.add(E_Chapter5())
        self.add(F_Chapter6())
        self.add(G_Chapter7())
        self.add(H_Chapter8())

# eof
