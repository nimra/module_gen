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

from .A_ParameterSelection.index import ParameterSelection as A_ParameterSelection
from .B_BuildingPipelines.index import BuildingPipelines as B_BuildingPipelines
from .C_UsingPipelines.index import UsingPipelines as C_UsingPipelines
from .D_TheGeneral.index import TheGeneral as D_TheGeneral
from .E_GridSearchingPreprocessing.index import GridSearchingPreprocessing as E_GridSearchingPreprocessing
from .F_GridSearchingWhich.index import GridSearchingWhich as F_GridSearchingWhich
from .G_Summaryand.index import Summaryand as G_Summaryand

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                                                                        CHAPTER 6
#                          Algorithm Chains and Pipelines
# 
# 
# 
# 
# For many machine learning algorithms, the particular representation of the data that
# you provide is very important, as we discussed in Chapter 4. This starts with scaling
# the data and combining features by hand and goes all the way to learning features
# using unsupervised machine learning, as we saw in Chapter 3. Consequently, most
# machine learning applications require not only the application of a single algorithm,
# but the chaining together of many different processing steps and machine learning
# models. In this chapter, we will cover how to use the Pipeline class to simplify the
# process of building chains of transformations and models. In particular, we will see
# how we can combine Pipeline and GridSearchCV to search over parameters for all
# processing steps at once.
# As an example of the importance of chaining models, we noticed that we can greatly
# improve the performance of a kernel SVM on the cancer dataset by using the Min
# MaxScaler for preprocessing. Here’s code for splitting the data, computing the mini‐
# mum and maximum, scaling the data, and training the SVM:
# In[1]:
#     from   sklearn.svm import SVC
#     from   sklearn.datasets import load_breast_cancer
#     from   sklearn.model_selection import train_test_split
#     from   sklearn.preprocessing import MinMaxScaler
# 
#     # load and split the data
#     cancer = load_breast_cancer()
#     X_train, X_test, y_train, y_test = train_test_split(
#         cancer.data, cancer.target, random_state=0)
# 
#     # compute minimum and maximum on the training data
#     scaler = MinMaxScaler().fit(X_train)
# 
# 
# 
# 
#                                                                                   305
# 
# In[2]:
#       # rescale the training data
#       X_train_scaled = scaler.transform(X_train)
# 
#       svm = SVC()
#       # learn an SVM on the scaled training data
#       svm.fit(X_train_scaled, y_train)
#       # scale the test data and score the scaled data
#       X_test_scaled = scaler.transform(X_test)
#       print("Test score: {:.2f}".format(svm.score(X_test_scaled, y_test)))
# 
# Out[2]:
#       Test score: 0.95
# 
# 
# Parameter Selection with Preprocessing
# Now let’s say we want to find better parameters for SVC using GridSearchCV, as dis‐
# cussed in Chapter 5. How should we go about doing this? A naive approach might
# look like this:
# In[3]:
#       from sklearn.model_selection import GridSearchCV
#       # for illustration purposes only, don't use this code!
#       param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100],
#                     'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}
#       grid = GridSearchCV(SVC(), param_grid=param_grid, cv=5)
#       grid.fit(X_train_scaled, y_train)
#       print("Best cross-validation accuracy: {:.2f}".format(grid.best_score_))
#       print("Best set score: {:.2f}".format(grid.score(X_test_scaled, y_test)))
#       print("Best parameters: ", grid.best_params_)
# 
# Out[3]:
#       Best cross-validation accuracy: 0.98
#       Best set score: 0.97
#       Best parameters: {'gamma': 1, 'C': 1}
# 
# Here, we ran the grid search over the parameters of SVC using the scaled data. How‐
# ever, there is a subtle catch in what we just did. When scaling the data, we used all the
# data in the training set to find out how to train it. We then use the scaled training data
# to run our grid search using cross-validation. For each split in the cross-validation,
# some part of the original training set will be declared the training part of the split,
# and some the test part of the split. The test part is used to measure what new data will
# look like to a model trained on the training part. However, we already used the infor‐
# mation contained in the test part of the split, when scaling the data. Remember that
# the test part in each split in the cross-validation is part of the training set, and we
# used the information from the entire training set to find the right scaling of the data.
# 
# 
# 306   |   Chapter 6: Algorithm Chains and Pipelines
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 6. Algorithm Chains and Pipelines",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter6(HierNode):
    def __init__(self):
        super().__init__("Chapter 6. Algorithm Chains and Pipelines")
        self.add(Content(), "content")
        self.add(A_ParameterSelection())
        self.add(B_BuildingPipelines())
        self.add(C_UsingPipelines())
        self.add(D_TheGeneral())
        self.add(E_GridSearchingPreprocessing())
        self.add(F_GridSearchingWhich())
        self.add(G_Summaryand())

# eof
