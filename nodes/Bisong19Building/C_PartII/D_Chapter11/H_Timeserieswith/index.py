# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Importinga.index import Importinga as A_Importinga
from .B_SelectionUsing.index import SelectionUsing as B_SelectionUsing
from .C_SubsetData.index import SubsetData as C_SubsetData
from .D_ResamplingDatetime.index import ResamplingDatetime as D_ResamplingDatetime
from .E_Convertto.index import Convertto as E_Convertto
from .F_Theshift.index import Theshift as F_Theshift
from .G_RollingWindows.index import RollingWindows as G_RollingWindows

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Timeseries with Pandas
# One of the core strengths of Pandas is its powerful set of functions for manipulating
# timeseries datasets. A couple of these functions are covered in this material.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Timeseries with Pandas",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Timeseries with Pandas"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Timeserieswith(HierNode):
    def __init__(self):
        super().__init__("Timeseries with Pandas")
        self.add(Content())
        self.add(A_Importinga())
        self.add(B_SelectionUsing())
        self.add(C_SubsetData())
        self.add(D_ResamplingDatetime())
        self.add(E_Convertto())
        self.add(F_Theshift())
        self.add(G_RollingWindows())

# eof
