# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Unsupervised Learning
# In unsupervised learning, the goal is to build a model that captures the underlying
# distribution of the dataset. The dataset has no given targets for the input features (see
# Figure 14-17). So, it is not possible to learn a function that maps a relationship between
# the input features and the targets as we do in supervised learning.
# 
# 
# 
# 
# Figure 14-17. Unsupervised dataset
# 
#     Rather, unsupervised learning algorithms attempt to determine the unknown
# structure of the dataset by grouping similar samples together.
#     Assume we have a dataset of patients with heart diseases; using unsupervised
# machine learning algorithms, we can find some hidden sub-groups of patients to help
# understand more about the disease patterns. This is known as clustering.
#     Also, we can use algorithms like principal component analysis (PCA) to compress
# a large number of features into principal components (that summarizes all the other
# features) for easy visualization. We will talk more about clustering and principal
# component analysis in later chapters.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Unsupervised Learning",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Unsupervised Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UnsupervisedLearning(HierNode):
    def __init__(self):
        super().__init__("Unsupervised Learning")
        self.add(Content())

# eof
