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
#                  Download from finelybook www.finelybook.com
# Scikit-Learn actually uses a multiclass version of AdaBoost called SAMME16 (which
# stands for Stagewise Additive Modeling using a Multiclass Exponential loss function).
# When there are just two classes, SAMME is equivalent to AdaBoost. Moreover, if the
# predictors can estimate class probabilities (i.e., if they have a predict_proba()
# method), Scikit-Learn can use a variant of SAMME called SAMME.R (the R stands
# for “Real”), which relies on class probabilities rather than predictions and generally
# performs better.
# The following code trains an AdaBoost classifier based on 200 Decision Stumps using
# Scikit-Learn’s AdaBoostClassifier class (as you might expect, there is also an Ada
# BoostRegressor class). A Decision Stump is a Decision Tree with max_depth=1—in
# other words, a tree composed of a single decision node plus two leaf nodes. This is
# the default base estimator for the AdaBoostClassifier class:
#       from sklearn.ensemble import AdaBoostClassifier
# 
#       ada_clf = AdaBoostClassifier(
#               DecisionTreeClassifier(max_depth=1), n_estimators=200,
#               algorithm="SAMME.R", learning_rate=0.5
#           )
#       ada_clf.fit(X_train, y_train)
# 
#                      If your AdaBoost ensemble is overfitting the training set, you can
#                      try reducing the number of estimators or more strongly regulariz‐
#                      ing the base estimator.
# 
# 
# 
# Gradient Boosting
# Another very popular Boosting algorithm is Gradient Boosting.17 Just like AdaBoost,
# Gradient Boosting works by sequentially adding predictors to an ensemble, each one
# correcting its predecessor. However, instead of tweaking the instance weights at every
# iteration like AdaBoost does, this method tries to fit the new predictor to the residual
# errors made by the previous predictor.
# Let’s go through a simple regression example using Decision Trees as the base predic‐
# tors (of course Gradient Boosting also works great with regression tasks). This is
# called Gradient Tree Boosting, or Gradient Boosted Regression Trees (GBRT). First, let’s
# fit a DecisionTreeRegressor to the training set (for example, a noisy quadratic train‐
# ing set):
# 
# 
# 
# 
# 16 For more details, see “Multi-Class AdaBoost,” J. Zhu et al. (2006).
# 17 First introduced in “Arcing the Edge,” L. Breiman (1997).
# 
# 
# 
#                                                                                  Boosting   |   195
# 
#                        Download from finelybook www.finelybook.com
#       from sklearn.tree import DecisionTreeRegressor
# 
#       tree_reg1 = DecisionTreeRegressor(max_depth=2)
#       tree_reg1.fit(X, y)
# 
# Now train a second DecisionTreeRegressor on the residual errors made by the first
# predictor:
#       y2 = y - tree_reg1.predict(X)
#       tree_reg2 = DecisionTreeRegressor(max_depth=2)
#       tree_reg2.fit(X, y2)
# Then we train a third regressor on the residual errors made by the second predictor:
#       y3 = y2 - tree_reg2.predict(X)
#       tree_reg3 = DecisionTreeRegressor(max_depth=2)
#       tree_reg3.fit(X, y3)
# Now we have an ensemble containing three trees. It can make predictions on a new
# instance simply by adding up the predictions of all the trees:
#       y_pred = sum(tree.predict(X_new) for tree in (tree_reg1, tree_reg2, tree_reg3))
# Figure 7-9 represents the predictions of these three trees in the left column, and the
# ensemble’s predictions in the right column. In the first row, the ensemble has just one
# tree, so its predictions are exactly the same as the first tree’s predictions. In the second
# row, a new tree is trained on the residual errors of the first tree. On the right you can
# see that the ensemble’s predictions are equal to the sum of the predictions of the first
# two trees. Similarly, in the third row another tree is trained on the residual errors of
# the second tree. You can see that the ensemble’s predictions gradually get better as
# trees are added to the ensemble.
# A simpler way to train GBRT ensembles is to use Scikit-Learn’s GradientBoostingRe
# gressor class. Much like the RandomForestRegressor class, it has hyperparameters to
# control the growth of Decision Trees (e.g., max_depth, min_samples_leaf, and so on),
# as well as hyperparameters to control the ensemble training, such as the number of
# trees (n_estimators). The following code creates the same ensemble as the previous
# one:
#       from sklearn.ensemble import GradientBoostingRegressor
# 
#       gbrt = GradientBoostingRegressor(max_depth=2, n_estimators=3, learning_rate=1.0)
#       gbrt.fit(X, y)
# 
# 
# 
# 
# 196   |   Chapter 7: Ensemble Learning and Random Forests
# 
#                   Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 7-9. Gradient Boosting
# 
# The learning_rate hyperparameter scales the contribution of each tree. If you set it
# to a low value, such as 0.1, you will need more trees in the ensemble to fit the train‐
# ing set, but the predictions will usually generalize better. This is a regularization tech‐
# nique called shrinkage. Figure 7-10 shows two GBRT ensembles trained with a low
# learning rate: the one on the left does not have enough trees to fit the training set,
# while the one on the right has too many trees and overfits the training set.
# 
# 
# 
# 
#                                                                             Boosting   |   197
# 
#                        Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 7-10. GBRT ensembles with not enough predictors (left) and too many (right)
# 
# In order to find the optimal number of trees, you can use early stopping (see Chap‐
# ter 4). A simple way to implement this is to use the staged_predict() method: it
# returns an iterator over the predictions made by the ensemble at each stage of train‐
# ing (with one tree, two trees, etc.). The following code trains a GBRT ensemble with
# 120 trees, then measures the validation error at each stage of training to find the opti‐
# mal number of trees, and finally trains another GBRT ensemble using the optimal
# number of trees:
#       import numpy as np
#       from sklearn.model_selection import train_test_split
#       from sklearn.metrics import mean_squared_error
# 
#       X_train, X_val, y_train, y_val = train_test_split(X, y)
# 
#       gbrt = GradientBoostingRegressor(max_depth=2, n_estimators=120)
#       gbrt.fit(X_train, y_train)
# 
#       errors = [mean_squared_error(y_val, y_pred)
#                 for y_pred in gbrt.staged_predict(X_val)]
#       bst_n_estimators = np.argmin(errors)
# 
#       gbrt_best = GradientBoostingRegressor(max_depth=2,n_estimators=bst_n_estimators)
#       gbrt_best.fit(X_train, y_train)
# The validation errors are represented on the left of Figure 7-11, and the best model’s
# predictions are represented on the right.
# 
# 
# 
# 
# 198   |   Chapter 7: Ensemble Learning and Random Forests
# 
#                  Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 7-11. Tuning the number of trees using early stopping
# 
# It is also possible to implement early stopping by actually stopping training early
# (instead of training a large number of trees first and then looking back to find the
# optimal number). You can do so by setting warm_start=True, which makes Scikit-
# Learn keep existing trees when the fit() method is called, allowing incremental
# training. The following code stops training when the validation error does not
# improve for five iterations in a row:
#     gbrt = GradientBoostingRegressor(max_depth=2, warm_start=True)
# 
#     min_val_error = float("inf")
#     error_going_up = 0
#     for n_estimators in range(1, 120):
#         gbrt.n_estimators = n_estimators
#         gbrt.fit(X_train, y_train)
#         y_pred = gbrt.predict(X_val)
#         val_error = mean_squared_error(y_val, y_pred)
#         if val_error < min_val_error:
#             min_val_error = val_error
#             error_going_up = 0
#         else:
#             error_going_up += 1
#             if error_going_up == 5:
#                 break # early stopping
# 
# The GradientBoostingRegressor class also supports a subsample hyperparameter,
# which specifies the fraction of training instances to be used for training each tree. For
# example, if subsample=0.25, then each tree is trained on 25% of the training instan‐
# ces, selected randomly. As you can probably guess by now, this trades a higher bias
# for a lower variance. It also speeds up training considerably. This technique is called
# Stochastic Gradient Boosting.
# 
# 
# 
# 
#                                                                           Boosting   |   199
# 
#                          Download from finelybook www.finelybook.com
#                       It is possible to use Gradient Boosting with other cost functions.
#                       This is controlled by the loss hyperparameter (see Scikit-Learn’s
#                       documentation for more details).
# 
# 
# 
# Stacking
# The last Ensemble method we will discuss in this chapter is called stacking (short for
# stacked generalization).18 It is based on a simple idea: instead of using trivial functions
# (such as hard voting) to aggregate the predictions of all predictors in an ensemble,
# why don’t we train a model to perform this aggregation? Figure 7-12 shows such an
# ensemble performing a regression task on a new instance. Each of the bottom three
# predictors predicts a different value (3.1, 2.7, and 2.9), and then the final predictor
# (called a blender, or a meta learner) takes these predictions as inputs and makes the
# final prediction (3.0).
# 
# 
# 
# 
# Figure 7-12. Aggregating predictions using a blending predictor
# 
# To train the blender, a common approach is to use a hold-out set.19 Let’s see how it
# works. First, the training set is split in two subsets. The first subset is used to train the
# predictors in the first layer (see Figure 7-13).
# 
# 
# 
# 18 “Stacked Generalization,” D. Wolpert (1992).
# 19 Alternatively, it is possible to use out-of-fold predictions. In some contexts this is called stacking, while using a
#    hold-out set is called blending. However, for many people these terms are synonymous.
# 
# 
# 
# 200    |   Chapter 7: Ensemble Learning and Random Forests
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Gradient Boosting",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GradientBoosting(HierNode):
    def __init__(self):
        super().__init__("Gradient Boosting")
        self.add(Content(), "content")

# eof
