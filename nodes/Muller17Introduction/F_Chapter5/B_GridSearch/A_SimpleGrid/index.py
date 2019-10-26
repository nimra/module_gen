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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Simple Grid Search",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SimpleGrid(HierNode):
    def __init__(self):
        super().__init__("Simple Grid Search")
        self.add(Content(), "content")

# eof
