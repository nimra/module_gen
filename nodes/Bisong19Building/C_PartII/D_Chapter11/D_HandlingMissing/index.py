# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_IdentifyingMissing.index import IdentifyingMissing as A_IdentifyingMissing
from .B_RemovingMissing.index import RemovingMissing as B_RemovingMissing
from .C_ImputingValues.index import ImputingValues as C_ImputingValues

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Handling Missing Data
# Dealing with missing data is an integral part of the data cleaning/data analysis process.
# Moreover, some machine learning algorithms will not work in the presence of missing
# data. Let’s see some simple Pandas methods for identifying and removing missing data,
# as well as imputing values into missing data.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Handling Missing Data",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Handling Missing Data"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HandlingMissing(HierNode):
    def __init__(self):
        super().__init__("Handling Missing Data")
        self.add(Content())
        self.add(A_IdentifyingMissing())
        self.add(B_RemovingMissing())
        self.add(C_ImputingValues())

# eof
