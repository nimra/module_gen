# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_OnevsOneOVO.index import OnevsOneOVO as A_OnevsOneOVO
from .B_OnevsAllOVA.index import OnevsAllOVA as B_OnevsAllOVA

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Multi-class Classification
# Previously, we have used the SVC to build a discriminant classifier for binary classes.
# What happens when we have more than two classes of outputs in the dataset, which is
# often the case in practice? The SVM can be extended for classifying k classes within a
# dataset, where k > 2. This extension is, however, not trivial with the SVM. There exist two
# standard approaches for addressing this problem. The first is the one-vs.-one (OVO)
# multi-class classification, while the other is the one-vs.-all (OVA) or one-vs.rest (OVR)
# multi-class classification technique.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Multi-class Classification",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Multi-class Classification"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MulticlassClassification(HierNode):
    def __init__(self):
        super().__init__("Multi-class Classification")
        self.add(Content())
        self.add(A_OnevsOneOVO())
        self.add(B_OnevsAllOVA())

# eof
