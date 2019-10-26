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
#                       Download from finelybook www.finelybook.com
#      sepal width (cm) 0.0231192882825
#      petal length (cm) 0.441030464364
#      petal width (cm) 0.423357996355
# Similarly, if you train a Random Forest classifier on the MNIST dataset (introduced
# in Chapter 3) and plot each pixel’s importance, you get the image represented in
# Figure 7-6.
# 
# 
# 
# 
# Figure 7-6. MNIST pixel importance (according to a Random Forest classifier)
# 
# Random Forests are very handy to get a quick understanding of what features
# actually matter, in particular if you need to perform feature selection.
# 
# Boosting
# Boosting (originally called hypothesis boosting) refers to any Ensemble method that
# can combine several weak learners into a strong learner. The general idea of most
# boosting methods is to train predictors sequentially, each trying to correct its prede‐
# cessor. There are many boosting methods available, but by far the most popular are
# AdaBoost13 (short for Adaptive Boosting) and Gradient Boosting. Let’s start with Ada‐
# Boost.
# 
# 
# 
# 
# 13 “A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting,” Yoav Freund,
#    Robert E. Schapire (1997).
# 
# 
# 
#                                                                                            Boosting   |     191
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Feature Importance",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FeatureImportance(HierNode):
    def __init__(self):
        super().__init__("Feature Importance")
        self.add(Content(), "content")

# eof
