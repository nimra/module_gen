# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Removinga.index import Removinga as A_Removinga
from .B_Addinga.index import Addinga as B_Addinga
from .C_DataAlignment.index import DataAlignment as C_DataAlignment
from .D_CombiningDatasets.index import CombiningDatasets as D_CombiningDatasets

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DataFrame Manipulation
# Let’s go through some common tasks for manipulating a DataFrame.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "DataFrame Manipulation",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# DataFrame Manipulation"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataFrameManipulation(HierNode):
    def __init__(self):
        super().__init__("DataFrame Manipulation")
        self.add(Content())
        self.add(A_Removinga())
        self.add(B_Addinga())
        self.add(C_DataAlignment())
        self.add(D_CombiningDatasets())

# eof
