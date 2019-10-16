# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Randomized Search
# As opposed to grid search, not all the provided hyper-parameter values are evaluated,
# but rather a determined number of hyper-parameter values are sampled from a random
# uniform distribution. The number of hyper-parameter values that can be evaluated is
# determined by the n_iter attribute of the RandomizedSearchCV module.
#     In this example, we will use the same scenario as in the grid search case.
# 
# from sklearn.model_selection import RandomizedSearchCV
# from sklearn.ensemble import RandomForestRegressor
# from sklearn import datasets
# 
# # load dataset
# data = datasets.load_boston()
# 
# # separate features and target
# X = data.data
# y = data.target
# 
# # construct grid search      parameters in a dictionary
# parameters = {
#     'n_estimators': [2,      4, 6, 8, 10, 12, 14, 16],
#     'max_depth': [2, 4,      6, 8],
#     'min_samples_leaf':      [1,2,3,4,5]
#     }
# 
# # create the model
# rf_model = RandomForestRegressor()
# 
# # run the grid search
# randomized_search = RandomizedSearchCV(estimator=rf_model, param_
# distributions=parameters, n_iter=10)
# # fit the model
# randomized_search.fit(X,y)
# 'Output':
# RandomizedSearchCV(cv=None, error_score='raise',
#           estimator=RandomForestRegressor(bootstrap=True, criterion='mse',
#            max_depth=None,
#            max_features='auto', max_leaf_nodes=None,
#            min_impurity_decrease=0.0, min_impurity_split=None,
#            min_samples_leaf=1, min_samples_split=2,
#            min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
#            oob_score=False, random_state=None, verbose=0, warm_
#             start=False),
#           fit_params=None, iid=True, n_iter=10, n_jobs=1,
#           param_distributions={'n_estimators': [2, 4, 6, 8, 10, 12, 14, 16],
#            'max_depth': [2, 4, 6, 8], 'min_samples_leaf': [1, 2, 3, 4, 5]},
#           pre_dispatch='2*n_jobs', random_state=None, refit=True,
#           return_train_score='warn', scoring=None, verbose=0)
# 
# # evaluate the model performance
# print("Best Accuracy: %.3f%%" %  (randomized_search.best_score_*100.0))
# 'Output':
# Best Accuracy: 57.856%
# 
# # best set of hyper-parameter values
# print("Best n_estimators: %d \nBest max_depth: %d \nBest min_samples_leaf:
# %d " %  \
#             (randomized_search.best_estimator_.n_estimators, \
#             randomized_search.best_estimator_.max_depth, \
#             randomized_search.best_estimator_.min_samples_leaf))
# 
# 'Output':
# Best n_estimators: 12
# Best max_depth: 6
# Best min_samples_leaf: 5
# 
#      This chapter further explored using Scikit-learn to incorporate other machine
#  learning techniques such as feature selection and resampling methods to develop a
#  more robust machine learning method. In the next chapter, we will examine our first
#  unsupervised machine learning method, clustering, and its implementation with
# ­Scikit-­learn.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Randomized Search",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Randomized Search"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RandomizedSearch(HierNode):
    def __init__(self):
        super().__init__("Randomized Search")
        self.add(Content())

# eof
