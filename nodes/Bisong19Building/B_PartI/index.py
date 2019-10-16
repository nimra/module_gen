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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PART I
# 
# Getting Started with
# Google Cloud Platform

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Part I: Getting Started with Google Cloud Platform",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Part I: Getting Started with Google Cloud Platform"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PartI(HierNode):
    def __init__(self):
        super().__init__("Part I: Getting Started with Google Cloud Platform")
        self.add(Content())
        self.add(A_Chapter1())
        self.add(B_Chapter2())
        self.add(C_Chapter3())
        self.add(D_Chapter4())
        self.add(E_Chapter5())
        self.add(F_Chapter6())
        self.add(G_Chapter7())

# eof
