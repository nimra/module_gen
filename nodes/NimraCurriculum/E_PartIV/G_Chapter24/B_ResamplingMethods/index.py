# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_kFoldCrossValidation.index import kFoldCrossValidation as A_kFoldCrossValidation
from .B_LeaveOneOutCrossValidation.index import LeaveOneOutCrossValidation as B_LeaveOneOutCrossValidation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Chapter 24   More Supervised Machine Learning Techniques with Scikit-learn
# 
# 'Output':
# AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
#           learning_rate=1.0, n_estimators=50, random_state=None)
# 
# # print the feature importances
# ada_boost_classifier.feature_importances_
# 'Output': array([0.  , 0.  , 0.58, 0.42])
# 
# # create a subset of data based on the relevant features
# model = SelectFromModel(ada_boost_classifier, prefit=True)
# new_data = model.transform(X)
# 
# # the irrelevant features have been removed
# new_data.shape
# 'Output': (150, 2)
# 
# 
# 
# Resampling Methods
# Resampling methods are a set of techniques that involve selecting a subset of the
# available dataset, training on that data subset, and using the remainder of the data to
# evaluate the trained model. Let’s review the techniques for resampling using Scikit-­
# learn. This section covers
# 
#       •   k-Fold cross-validation
# 
#       •   Leave-one-out cross-validation
# 
# 
# k-Fold Cross-Validation
# In k-fold cross validation, the dataset is divided into k-parts or folds. The model is
# trained using k − 1 folds and evaluated on the remaining kth fold. This process is
# repeated k-times so that each fold can serve as a test set. At the end of the process,
# k-fold averages the result and reports a mean score with a standard deviation. Scikit-
# learn implements K-fold CV in the module KFold. The module cross_val_score
# is used to evaluate the cross-validation score using the splitting strategy, which is
# KFold in this case.
# 
# 
# 
# 
#                                                                                           291
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Resampling Methods")
        self.add(MarkdownBlock("# Resampling Methods"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ResamplingMethods(HierNode):
    def __init__(self):
        super().__init__("Resampling Methods")
        self.add(Content())
        self.add(A_kFoldCrossValidation())
        self.add(B_LeaveOneOutCrossValidation())

# eof
