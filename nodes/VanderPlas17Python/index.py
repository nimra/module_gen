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

from .A_Preface.index import Preface as A_Preface
from .B_Chapter1.index import Chapter1 as B_Chapter1
from .C_Chapter2.index import Chapter2 as C_Chapter2
from .D_Chapter3.index import Chapter3 as D_Chapter3
from .E_Chapter4.index import Chapter4 as E_Chapter4
from .F_Chapter5.index import Chapter5 as F_Chapter5
# from .G_Index.index import Index as G_Index

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "VanderPlas17Python",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class VanderPlas17Python(HierNode):
    def __init__(self):
        super().__init__("VanderPlas17Python")
        self.add(Content())
        # self.add(A_Preface()) # Preface
        # self.add(B_Chapter1()) # IPython: Beyond Normal Python
        # self.add(C_Chapter2()) # Introduction to NumPy
        # self.add(D_Chapter3()) # Data Manipulation with Pandas
        # self.add(E_Chapter4()) # Visualization with Matplotlib
        self.add(F_Chapter5()) # Machine Learning
        # self.add(G_Index()) # Index

# eof