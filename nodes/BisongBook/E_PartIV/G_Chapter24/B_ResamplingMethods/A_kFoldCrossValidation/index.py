# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# k-Fold Cross-Validation
# In k-fold cross validation, the dataset is divided into k-parts or folds. The model is
# trained using k − 1 folds and evaluated on the remaining kth fold. This process is
# repeated k-times so that each fold can serve as a test set. At the end of the process,
# k-fold averages the result and reports a mean score with a standard deviation. Scikit-
# learn implements K-fold CV in the module KFold. The module cross_val_score
# is used to evaluate the cross-validation score using the splitting strategy, which is
# KFold in this case.
# 
#     Let’s see an example of this using the k-nearest neighbors (kNN) classification
# algorithm. When initializing KFold, it is standard practice to shuffle the data before
# splitting.
# 
# from sklearn.model_selection import KFold
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
# # initialize KFold - with shuffle = True, shuffle the data before splitting
# kfold = KFold(n_splits=3, shuffle=True)
# 
# # create the model
# knn_clf = KNeighborsClassifier(n_neighbors=3)
# 
# # fit the model using cross validation
# cv_result = cross_val_score(knn_clf, X, y, cv=kfold)
# 
# # evaluate the model performance using accuracy metric
# print("Accuracy: %.3f%% (%.3f%%)" % (cv_result.mean()*100.0, cv_result.
# std()*100.0))
# 'Output':
# Accuracy: 93.333% (2.494%)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "k-Fold Cross-Validation",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# k-Fold Cross-Validation"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class kFoldCrossValidation(HierNode):
    def __init__(self):
        super().__init__("k-Fold Cross-Validation")
        self.add(Content())

# eof
