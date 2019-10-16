# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_OnRegression.index import OnRegression as A_OnRegression
from .B_Growinga.index import Growinga as B_Growinga
from .C_Growinga.index import Growinga as C_Growinga
from .D_TreePruning.index import TreePruning as D_TreePruning
from .E_Strengthsand.index import Strengthsand as E_Strengthsand
from .F_CARTwith.index import CARTwith as F_CARTwith

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Decision Trees
# Decision trees, more popularly known as classification and regression trees (CART),
# can be visualized as a graph or flowchart of decisions. A branch connects the nodes in
# the graph, the last node of the graph is called a terminal node, and the topmost node is
# called the root. As seen in Figure 23-1, when constructing a decision tree, the root is at
# the top, while the branches connect nodes at lower layers until the terminal node.
# 
# 
# 
# 
# Figure 23-1. Illustration of a decision tree

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Decision Trees",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Decision Trees"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DecisionTrees(HierNode):
    def __init__(self):
        super().__init__("Decision Trees")
        self.add(Content())
        self.add(A_OnRegression())
        self.add(B_Growinga())
        self.add(C_Growinga())
        self.add(D_TreePruning())
        self.add(E_Strengthsand())
        self.add(F_CARTwith())

# eof
