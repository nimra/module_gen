# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Chapter18.index import Chapter18 as A_Chapter18
from .B_Chapter19.index import Chapter19 as B_Chapter19
from .C_Chapter20.index import Chapter20 as C_Chapter20
from .D_Chapter21.index import Chapter21 as D_Chapter21
from .E_Chapter22.index import Chapter22 as E_Chapter22
from .F_Chapter23.index import Chapter23 as F_Chapter23
from .G_Chapter24.index import Chapter24 as G_Chapter24
from .H_Chapter25.index import Chapter25 as H_Chapter25
from .I_Chapter26.index import Chapter26 as I_Chapter26

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PART IV
# 
# Machine Learning
# in Practice

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Part IV: Machine Learning in Practice",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Part IV: Machine Learning in Practice"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PartIV(HierNode):
    def __init__(self):
        super().__init__("Part IV: Machine Learning in Practice")
        self.add(Content())
        self.add(A_Chapter18())
        self.add(B_Chapter19())
        self.add(C_Chapter20())
        self.add(D_Chapter21())
        self.add(E_Chapter22())
        self.add(F_Chapter23())
        self.add(G_Chapter24())
        self.add(H_Chapter25())
        self.add(I_Chapter26())

# eof
