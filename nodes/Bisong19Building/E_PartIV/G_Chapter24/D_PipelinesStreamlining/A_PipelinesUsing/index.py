# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Pipelines Using make_pipeline
# Another method for building machine learning pipelines is by using the make_pipeline
# method. For the next example, we use PCA to select the best six features and reduce the
# dimensionality of the dataset, and then we’ll fit the model using Random forests for
# regression.
# 
# from   sklearn.pipeline import make_pipeline
# from   sklearn.svm import SVR
# from   sklearn import datasets
# from   sklearn.model_selection import KFold
# from   sklearn.model_selection import cross_val_score
# from   sklearn.decomposition import PCA
# from   sklearn.pipeline import Pipeline
# from   sklearn.ensemble import RandomForestRegressor
# 
# # load dataset
# data = datasets.load_boston()
# 
# # separate features and target
# X = data.data
# y = data.target
# 
# # build the pipeline model
# pipe = make_pipeline(
#     PCA(n_components=9),
#     RandomForestRegressor()
# )
# 
# # run the pipeline
# kfold = KFold(n_splits=4, shuffle=True)
# cv_result = cross_val_score(pipe, X, y, cv=kfold)
# 
# # evaluate the model performance
# print("Accuracy: %.3f%% (%.3f%%)" % (cv_result.mean()*100.0, cv_result.
# std()*100.0))
# 'Output':
# Accuracy: 73.750% (2.489%)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Pipelines Using make_pipeline",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Pipelines Using make_pipeline"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PipelinesUsing(HierNode):
    def __init__(self):
        super().__init__("Pipelines Using make_pipeline")
        self.add(Content())

# eof
