# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Introduction.index import Introduction as A_Introduction
from .B_PartI.index import PartI as B_PartI
from .C_PartII.index import PartII as C_PartII
from .D_PartIII.index import PartIII as D_PartIII
from .E_PartIV.index import PartIV as E_PartIV
from .F_PartV.index import PartV as F_PartV
from .G_PartVI.index import PartVI as G_PartVI
from .H_PartVII.index import PartVII as H_PartVII
from .I_PartVIII.index import PartVIII as I_PartVIII
# from .J_Index.index import Index as J_Index

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Bisong Book",
            Stage.REMOVE_EXTRANEOUS,
            Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Bisong Book"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BisongBook(HierNode):
    def __init__(self):
        super().__init__("Bisong Book")
        self.add(Content())
        # self.add(A_Introduction())
        # self.add(B_PartI())
        # self.add(C_PartII())
        # self.add(D_PartIII())
        self.add(E_PartIV())
        # self.add(F_PartV())
        # self.add(G_PartVI())
        # self.add(H_PartVII())
        # self.add(I_PartVIII())
        # self.add(J_Index())

# eof
