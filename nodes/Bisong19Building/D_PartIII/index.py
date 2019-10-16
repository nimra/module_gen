# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Part III: Introducing Machine Learning",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
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
