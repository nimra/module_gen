# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Theifelif.index import Theifelif as A_Theifelif
from .B_Thewhile.index import Thewhile as B_Thewhile
from .C_Thefor.index import Thefor as C_Thefor
from .D_ListComprehensions.index import ListComprehensions as D_ListComprehensions
from .E_Thebreak.index import Thebreak as E_Thebreak

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Control Structures
# Programs need to make decisions which result in executing a particular set of
# instructions or a specific block of code repeatedly. With control structures, we would
# have the ability to write programs that can make logical decisions and execute an
# instruction set until a terminating condition occurs.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Control Structures",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Control Structures"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ControlStructures(HierNode):
    def __init__(self):
        super().__init__("Control Structures")
        self.add(Content())
        self.add(A_Theifelif())
        self.add(B_Thewhile())
        self.add(C_Thefor())
        self.add(D_ListComprehensions())
        self.add(E_Thebreak())

# eof
