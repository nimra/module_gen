# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Recursive Feature Elimination (RFE)
# RFE is used together with a learning model to recursively select the desired number of
# top performing features.
#     Let’s use RFE with LinearRegression.
# 
# # import packages
# from sklearn.feature_selection import RFE
# from sklearn.linear_model import LinearRegression
# from sklearn import datasets
# 
# # load dataset
# data = datasets.load_boston()
# 
# # separate features and target
# X = data.data
# y = data.target
# 
# # feature engineering
# linear_reg = LinearRegression()
# rfe = RFE(estimator=linear_reg, n_features_to_select=6)
# rfe_fit = rfe.fit(X, y)
# 
# # print the feature ranking
# rfe_fit.ranking_
# 'Output': array([3, 5, 4, 1, 1, 1, 8, 1, 2, 6, 1, 7, 1])
# 
#     From the result, the 4th, 5th, 6th, 8th, 11th, and 13th features are the top 6 features in
# the Boston dataset.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Recursive Feature Elimination (RFE)",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Recursive Feature Elimination (RFE)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RecursiveFeature(HierNode):
    def __init__(self):
        super().__init__("Recursive Feature Elimination (RFE)")
        self.add(Content())

# eof
