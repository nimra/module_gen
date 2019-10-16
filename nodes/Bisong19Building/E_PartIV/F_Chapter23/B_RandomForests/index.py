# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_MakingPredictions.index import MakingPredictions as A_MakingPredictions
from .B_RandomForests.index import RandomForests as B_RandomForests

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Random Forests
# Random forest is a robust machine learning algorithm and is often the algorithm of
# choice for many classification and regression problems. It is a popular algorithm in
# machine learning competitions.
#     Random forest builds an ensemble classifier from a combination of several decision
# tree classifiers. This does an excellent job of reducing the variance that may be found in a
# single decision tree classifier.
# 
#     Random forest is an improvement on the bagging ensemble algorithm (also known
# as bootstrap aggregation) which involves creating a large number of fully grown decision
# trees by repeatedly selecting random samples from the training dataset (also called
# bootstrapping). The result of these trees is then averaged to smoothen out the variance.
#     Random forest improves this bagging procedure by using only a subset of the
# features or attributes in the training dataset on each tree split. In doing this, Random
# forest creates trees whose average is more robust and less prone to high variances.
#     Observe that the principal distinction between bagging and Random forests is the
# choice of features when splitting the feature space or when building the tree. Bagging
# makes use of the entire features in the dataset, whereas Random forest imposes a
# constraint on the number of features and uses only a subset of features on each tree split
# to reduce the correlation of each sub-tree. Empirically, the size of features for each tree
# split using Random forests is the square root of the original number of predictors.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Random Forests",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Random Forests"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RandomForests(HierNode):
    def __init__(self):
        super().__init__("Random Forests")
        self.add(Content())
        self.add(A_MakingPredictions())
        self.add(B_RandomForests())

# eof
