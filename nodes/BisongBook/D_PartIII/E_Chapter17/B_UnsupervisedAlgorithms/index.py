# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Unsupervised Algorithms
# Examples of unsupervised learning include
# 
#       •   Clustering
# 
#       •   Principal component analysis
# 
#      In the later chapters, we will survey the preceding unsupervised learning algorithms
# for learning from non-labeled datasets. Clustering is an algorithm for grouping
# homogeneous samples into partitions called clusters. Principal component analysis
# is a method for finding low-dimensional feature sub-spaces that capture as much
# information as possible from the original higher-dimensional features of the dataset.
#      This chapter provides an overview of the machine learning algorithms that we’ll
# discuss together with code examples in Part 4 of this book.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Unsupervised Algorithms",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Unsupervised Algorithms"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UnsupervisedAlgorithms(HierNode):
    def __init__(self):
        super().__init__("Unsupervised Algorithms")
        self.add(Content())

# eof
