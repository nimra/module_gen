# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tree Pruning
# Tree pruning is a technique for dealing with model overfitting when growing trees.
# Fully grown trees have a high tendency to overfit with high variances when applied to
# unseen samples.
#     Pruning involves growing a large tree and then pruning or clipping it to create
# a sub-tree. By doing so, we can have a full picture of the tree performance and then
# select a sub-tree that results in a minimized error measure on the test dataset. The
# technique for selecting the best sub-tree is called the cost complexity pruning or the
# weakest link pruning.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Tree Pruning",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Tree Pruning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TreePruning(HierNode):
    def __init__(self):
        super().__init__("Tree Pruning")
        self.add(Content())

# eof
