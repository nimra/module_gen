# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Chapter8.index import Chapter8 as A_Chapter8
from .B_Chapter9.index import Chapter9 as B_Chapter9
from .C_Chapter10.index import Chapter10 as C_Chapter10
from .D_Chapter11.index import Chapter11 as D_Chapter11
from .E_Chapter12.index import Chapter12 as E_Chapter12

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PART II
# 
# Programming
# Foundations for Data
# Science

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Part II: Programming Foundations for Data Science",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Part II: Programming Foundations for Data Science"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PartII(HierNode):
    def __init__(self):
        super().__init__("Part II: Programming Foundations for Data Science")
        self.add(Content())
        self.add(A_Chapter8())
        self.add(B_Chapter9())
        self.add(C_Chapter10())
        self.add(D_Chapter11())
        self.add(E_Chapter12())

# eof
