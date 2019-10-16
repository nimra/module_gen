# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Leave-One-Out Cross-Validation (LOOCV)
# In LOOCV just one example is assigned to the test set, and the model is trained on the
# remainder of the dataset. This process is repeated for all the examples in the dataset.
# This process is repeated until all the examples in the dataset have been used for
# evaluating the model.
# 
# from sklearn.model_selection import LeaveOneOut
# from sklearn.model_selection import cross_val_score
# from sklearn.neighbors import KNeighborsClassifier
# 
# # load dataset
# data = datasets.load_iris()
# 
# # separate features and target
# X = data.data
# y = data.target
# 
# # initialize LOOCV
# loocv = LeaveOneOut()
# 
# # create the model
# knn_clf = KNeighborsClassifier(n_neighbors=3)
# 
# # fit the model using cross validation
# cv_result = cross_val_score(knn_clf, X, y, cv=loocv)
# 
# # evaluate the model performance using accuracy metric
# print("Accuracy: %.3f%% (%.3f%%)" % (cv_result.mean()*100.0, cv_result.
# std()*100.0))
# 'Output':
# Accuracy: 96.000% (19.596%)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Leave-One-Out Cross-Validation (LOOCV)",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Leave-One-Out Cross-Validation (LOOCV)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LeaveOneOutCrossValidation(HierNode):
    def __init__(self):
        super().__init__("Leave-One-Out Cross-Validation (LOOCV)")
        self.add(Content())

# eof
