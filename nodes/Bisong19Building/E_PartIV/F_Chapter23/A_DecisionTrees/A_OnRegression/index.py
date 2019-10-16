# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# On Regression and Classification with CART
# A classification or regression tree is built by randomly splitting the set of attributes of the
# given dataset into distinct regions. The data points that fall within a particular region are
# used to form the predictor from the means of the targets in the regression case and the
# highest occurring class in the classification setting.
#     Thus, if an unseen observation or test data falls within a region, the mean or
# modal class is used to predict the output for regression and classification problems,
# respectively. In regression trees, the output variable is continuous, whereas in
# classification trees, the output variable is categorical. The terminal node of a regression
# tree takes the average of the samples in that region, while the terminal node of a
# classification tree is the highest occurring class in that area.
#     The process of splitting the features of the dataset into regions is by a greedy
# algorithm called recursive binary splitting. This strategy works by continuously
# dividing the feature space into two new branches or regions until a stopping
# criterion is reached.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "On Regression and Classification with CART",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# On Regression and Classification with CART"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OnRegression(HierNode):
    def __init__(self):
        super().__init__("On Regression and Classification with CART")
        self.add(Content())

# eof
