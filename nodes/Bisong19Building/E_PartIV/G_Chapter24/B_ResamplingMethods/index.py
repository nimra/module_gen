# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_kFoldCrossValidation.index import kFoldCrossValidation as A_kFoldCrossValidation
from .B_LeaveOneOutCrossValidation.index import LeaveOneOutCrossValidation as B_LeaveOneOutCrossValidation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Resampling Methods
# Resampling methods are a set of techniques that involve selecting a subset of the
# available dataset, training on that data subset, and using the remainder of the data to
# evaluate the trained model. Let’s review the techniques for resampling using Scikit-­
# learn. This section covers
# 
#       •   k-Fold cross-validation
# 
#       •   Leave-one-out cross-validation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Resampling Methods",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Resampling Methods"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ResamplingMethods(HierNode):
    def __init__(self):
        super().__init__("Resampling Methods")
        self.add(Content())
        self.add(A_kFoldCrossValidation())
        self.add(B_LeaveOneOutCrossValidation())

# eof
