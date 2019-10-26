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

from .A_ExtraTrees.index import ExtraTrees as A_ExtraTrees
from .B_FeatureImportance.index import FeatureImportance as B_FeatureImportance

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                   Download from finelybook www.finelybook.com
# Sampling features results in even more predictor diversity, trading a bit more bias for
# a lower variance.
# 
# Random Forests
# As we have discussed, a Random Forest9 is an ensemble of Decision Trees, generally
# trained via the bagging method (or sometimes pasting), typically with max_samples
# set to the size of the training set. Instead of building a BaggingClassifier and pass‐
# ing it a DecisionTreeClassifier, you can instead use the RandomForestClassifier
# class, which is more convenient and optimized for Decision Trees10 (similarly, there is
# a RandomForestRegressor class for regression tasks). The following code trains a
# Random Forest classifier with 500 trees (each limited to maximum 16 nodes), using
# all available CPU cores:
#       from sklearn.ensemble import RandomForestClassifier
# 
#       rnd_clf = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, n_jobs=-1)
#       rnd_clf.fit(X_train, y_train)
# 
#       y_pred_rf = rnd_clf.predict(X_test)
# 
# With a few exceptions, a RandomForestClassifier has all the hyperparameters of a
# DecisionTreeClassifier (to control how trees are grown), plus all the hyperpara‐
# meters of a BaggingClassifier to control the ensemble itself.11
# The Random Forest algorithm introduces extra randomness when growing trees;
# instead of searching for the very best feature when splitting a node (see Chapter 6), it
# searches for the best feature among a random subset of features. This results in a
# greater tree diversity, which (once again) trades a higher bias for a lower variance,
# generally yielding an overall better model. The following BaggingClassifier is
# roughly equivalent to the previous RandomForestClassifier:
#       bag_clf = BaggingClassifier(
#               DecisionTreeClassifier(splitter="random", max_leaf_nodes=16),
#               n_estimators=500, max_samples=1.0, bootstrap=True, n_jobs=-1
#           )
# 
# 
# 
# 
#  9 “Random Decision Forests,” T. Ho (1995).
# 10 The BaggingClassifier class remains useful if you want a bag of something other than Decision Trees.
# 11 There are a few notable exceptions: splitter is absent (forced to "random"), presort is absent (forced to
#    False), max_samples is absent (forced to 1.0), and base_estimator is absent (forced to DecisionTreeClassi
#    fier with the provided hyperparameters).
# 
# 
# 
#                                                                                         Random Forests    |    189
# 
#                        Download from finelybook www.finelybook.com
# Extra-Trees
# When you are growing a tree in a Random Forest, at each node only a random subset
# of the features is considered for splitting (as discussed earlier). It is possible to make
# trees even more random by also using random thresholds for each feature rather than
# searching for the best possible thresholds (like regular Decision Trees do).
# A forest of such extremely random trees is simply called an Extremely Randomized
# Trees ensemble12 (or Extra-Trees for short). Once again, this trades more bias for a
# lower variance. It also makes Extra-Trees much faster to train than regular Random
# Forests since finding the best possible threshold for each feature at every node is one
# of the most time-consuming tasks of growing a tree.
# You can create an Extra-Trees classifier using Scikit-Learn’s ExtraTreesClassifier
# class. Its API is identical to the RandomForestClassifier class. Similarly, the Extra
# TreesRegressor class has the same API as the RandomForestRegressor class.
# 
#                     It is hard to tell in advance whether a RandomForestClassifier
#                     will perform better or worse than an ExtraTreesClassifier. Gen‐
#                     erally, the only way to know is to try both and compare them using
#                     cross-validation (and tuning the hyperparameters using grid
#                     search).
# 
# 
# Feature Importance
# Lastly, if you look at a single Decision Tree, important features are likely to appear
# closer to the root of the tree, while unimportant features will often appear closer to
# the leaves (or not at all). It is therefore possible to get an estimate of a feature’s impor‐
# tance by computing the average depth at which it appears across all trees in the forest.
# Scikit-Learn computes this automatically for every feature after training. You can
# access the result using the feature_importances_ variable. For example, the follow‐
# ing code trains a RandomForestClassifier on the iris dataset (introduced in Chap‐
# ter 4) and outputs each feature’s importance. It seems that the most important
# features are the petal length (44%) and width (42%), while sepal length and width are
# rather unimportant in comparison (11% and 2%, respectively):
#       >>> from sklearn.datasets import load_iris
#       >>> iris = load_iris()
#       >>> rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=-1)
#       >>> rnd_clf.fit(iris["data"], iris["target"])
#       >>> for name, score in zip(iris["feature_names"], rnd_clf.feature_importances_):
#       >>>     print(name, score)
#       sepal length (cm) 0.112492250999
# 
# 
# 
# 12 “Extremely randomized trees,” P. Geurts, D. Ernst, L. Wehenkel (2005).
# 
# 
# 
# 190   |   Chapter 7: Ensemble Learning and Random Forests
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Random Forests",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RandomForests(HierNode):
    def __init__(self):
        super().__init__("Random Forests")
        self.add(Content(), "content")
        self.add(A_ExtraTrees())
        self.add(B_FeatureImportance())

# eof
