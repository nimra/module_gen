# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Growing a Classification Tree
# Growing a classification tree is very similar to the regression tree setting described in
# Figure 23-2. The difference here is that the error measure to minimize is no longer the
# squared error, but the misclassification error. This is because a classification tree is for
# predicting a qualitative response, where a data point is assigned to a particular region
# based on the modal value or the highest occurring class in that region.
#     Two algorithms for selecting which value to use for splitting the feature space in a
# classification setting are the Gini index and entropy; further discussions on these are
# beyond the scope of this chapter.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Growing a Classification Tree",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Growing a Classification Tree"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Growinga(HierNode):
    def __init__(self):
        super().__init__("Growing a Classification Tree")
        self.add(Content())

# eof
