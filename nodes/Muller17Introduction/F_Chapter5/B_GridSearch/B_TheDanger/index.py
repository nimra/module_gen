# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#               C = 0.001                 C = 0.01                 … C = 10
# gamma=0.001   SVC(C=0.001, gamma=0.001) SVC(C=0.01, gamma=0.001) … SVC(C=10, gamma=0.001)
# gamma=0.01    SVC(C=0.001, gamma=0.01)   SVC(C=0.01, gamma=0.01)   … SVC(C=10, gamma=0.01)
# …             …                          …                         … …
# gamma=100     SVC(C=0.001, gamma=100)    SVC(C=0.01, gamma=100)    … SVC(C=10, gamma=100)
# 
# 
# Simple Grid Search
# We can implement a simple grid search just as for loops over the two parameters,
# training and evaluating a classifier for each combination:
# In[18]:
#     # naive grid search implementation
#     from sklearn.svm import SVC
#     X_train, X_test, y_train, y_test = train_test_split(
#         iris.data, iris.target, random_state=0)
#     print("Size of training set: {}    size of test set: {}".format(
#           X_train.shape[0], X_test.shape[0]))
# 
#     best_score = 0
# 
#     for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
#         for C in [0.001, 0.01, 0.1, 1, 10, 100]:
#             # for each combination of parameters, train an SVC
#             svm = SVC(gamma=gamma, C=C)
#             svm.fit(X_train, y_train)
#             # evaluate the SVC on the test set
#             score = svm.score(X_test, y_test)
#             # if we got a better score, store the score and parameters
#             if score > best_score:
#                 best_score = score
#                 best_parameters = {'C': C, 'gamma': gamma}
# 
#     print("Best score: {:.2f}".format(best_score))
#     print("Best parameters: {}".format(best_parameters))
# 
# Out[18]:
#     Size of training set: 112   size of test set: 38
#     Best score: 0.97
#     Best parameters: {'C': 100, 'gamma': 0.001}
# 
# 
# The Danger of Overfitting the Parameters and the Validation Set
# Given this result, we might be tempted to report that we found a model that performs
# with 97% accuracy on our dataset. However, this claim could be overly optimistic (or
# just wrong), for the following reason: we tried many different parameters and
# 
# 
#                                                                                 Grid Search   |   261
# 
# selected the one with best accuracy on the test set, but this accuracy won’t necessarily
# carry over to new data. Because we used the test data to adjust the parameters, we can
# no longer use it to assess how good the model is. This is the same reason we needed
# to split the data into training and test sets in the first place; we need an independent
# dataset to evaluate, one that was not used to create the model.
# One way to resolve this problem is to split the data again, so we have three sets: the
# training set to build the model, the validation (or development) set to select the
# parameters of the model, and the test set to evaluate the performance of the selected
# parameters. Figure 5-5 shows what this looks like:
# In[19]:
#       mglearn.plots.plot_threefold_split()
# 
# 
# 
# 
# Figure 5-5. A threefold split of data into training set, validation set, and test set
# 
# After selecting the best parameters using the validation set, we can rebuild a model
# using the parameter settings we found, but now training on both the training data
# and the validation data. This way, we can use as much data as possible to build our
# model. This leads to the following implementation:
# In[20]:
#       from sklearn.svm import SVC
#       # split data into train+validation set and test set
#       X_trainval, X_test, y_trainval, y_test = train_test_split(
#           iris.data, iris.target, random_state=0)
#       # split train+validation set into training and validation sets
#       X_train, X_valid, y_train, y_valid = train_test_split(
#           X_trainval, y_trainval, random_state=1)
#       print("Size of training set: {}   size of validation set: {}   size of test set:"
#             " {}\n".format(X_train.shape[0], X_valid.shape[0], X_test.shape[0]))
# 
#       best_score = 0
# 
#       for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
#           for C in [0.001, 0.01, 0.1, 1, 10, 100]:
#               # for each combination of parameters, train an SVC
#               svm = SVC(gamma=gamma, C=C)
#               svm.fit(X_train, y_train)
#               # evaluate the SVC on the test set
#               score = svm.score(X_valid, y_valid)
#               # if we got a better score, store the score and parameters
#               if score > best_score:
#                   best_score = score
#                   best_parameters = {'C': C, 'gamma': gamma}
# 
# 
# 262   | Chapter 5: Model Evaluation and Improvement
# 
#     # rebuild a model on the combined training and validation set,
#     # and evaluate it on the test set
#     svm = SVC(**best_parameters)
#     svm.fit(X_trainval, y_trainval)
#     test_score = svm.score(X_test, y_test)
#     print("Best score on validation set: {:.2f}".format(best_score))
#     print("Best parameters: ", best_parameters)
#     print("Test set score with best parameters: {:.2f}".format(test_score))
# Out[20]:
#     Size of training set: 84    size of validation set: 28     size of test set: 38
# 
#     Best score on validation set: 0.96
#     Best parameters: {'C': 10, 'gamma': 0.001}
#     Test set score with best parameters: 0.92
# The best score on the validation set is 96%: slightly lower than before, probably
# because we used less data to train the model (X_train is smaller now because we split
# our dataset twice). However, the score on the test set—the score that actually tells us
# how well we generalize—is even lower, at 92%. So we can only claim to classify new
# data 92% correctly, not 97% correctly as we thought before!
# The distinction between the training set, validation set, and test set is fundamentally
# important to applying machine learning methods in practice. Any choices made
# based on the test set accuracy “leak” information from the test set into the model.
# Therefore, it is important to keep a separate test set, which is only used for the final
# evaluation. It is good practice to do all exploratory analysis and model selection using
# the combination of a training and a validation set, and reserve the test set for a final
# evaluation—this is even true for exploratory visualization. Strictly speaking, evaluat‐
# ing more than one model on the test set and choosing the better of the two will result
# in an overly optimistic estimate of how accurate the model is.
# 
# Grid Search with Cross-Validation
# While the method of splitting the data into a training, a validation, and a test set that
# we just saw is workable, and relatively commonly used, it is quite sensitive to how
# exactly the data is split. From the output of the previous code snippet we can see that
# GridSearchCV selects 'C': 10, 'gamma': 0.001 as the best parameters, while the
# output of the code in the previous section selects 'C': 100, 'gamma': 0.001 as the
# best parameters. For a better estimate of the generalization performance, instead of
# using a single split into a training and a validation set, we can use cross-validation to
# evaluate the performance of each parameter combination. This method can be coded
# up as follows:
# 
# 
# 
# 
#                                                                          Grid Search   |   263
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Danger of Overfitting the Parameters and the Validation Set",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheDanger(HierNode):
    def __init__(self):
        super().__init__("The Danger of Overfitting the Parameters and the Validation Set")
        self.add(Content(), "content")

# eof
