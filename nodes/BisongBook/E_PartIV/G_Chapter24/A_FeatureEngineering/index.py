# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_StatisticalTests.index import StatisticalTests as A_StatisticalTests
from .B_RecursiveFeature.index import RecursiveFeature as B_RecursiveFeature
from .C_FeatureImportances.index import FeatureImportances as C_FeatureImportances

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Feature Engineering
# Feature engineering is the process of systematically choosing the set of features in the
# dataset that are useful and relevant to the learning problem. It is often the case that
# irrelevant features negatively affect the performance of the model. This section will
# review some techniques implemented in Scikit-learn for selecting relevant features from
# a dataset. The techniques surveyed include
# 
#        •    Statistical tests to select the best k features using the
#             SelectKBest module
# 
#        •    Recursive feature elimination (RFE) to recursively remove irrelevant
#             features from the dataset
# 
#         •   Principal component analysis to select the components that account
#             for the variation in the dataset
# 
#         •   Feature importances using ensembled or tree classifiers

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Feature Engineering",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Feature Engineering"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FeatureEngineering(HierNode):
    def __init__(self):
        super().__init__("Feature Engineering")
        self.add(Content())
        self.add(A_StatisticalTests())
        self.add(B_RecursiveFeature())
        self.add(C_FeatureImportances())

# eof
