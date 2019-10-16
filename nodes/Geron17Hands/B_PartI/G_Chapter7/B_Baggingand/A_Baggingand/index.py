# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                   Download from finelybook www.finelybook.com
# ensemble has a similar bias but a lower variance than a single predictor trained on the
# original training set.
# As you can see in Figure 7-4, predictors can all be trained in parallel, via different
# CPU cores or even different servers. Similarly, predictions can be made in parallel.
# This is one of the reasons why bagging and pasting are such popular methods: they
# scale very well.
# 
# Bagging and Pasting in Scikit-Learn
# Scikit-Learn offers a simple API for both bagging and pasting with the BaggingClas
# sifier class (or BaggingRegressor for regression). The following code trains an
# ensemble of 500 Decision Tree classifiers,5 each trained on 100 training instances ran‐
# domly sampled from the training set with replacement (this is an example of bagging,
# but if you want to use pasting instead, just set bootstrap=False). The n_jobs param‐
# eter tells Scikit-Learn the number of CPU cores to use for training and predictions
# (–1 tells Scikit-Learn to use all available cores):
#       from sklearn.ensemble import BaggingClassifier
#       from sklearn.tree import DecisionTreeClassifier
# 
#       bag_clf = BaggingClassifier(
#               DecisionTreeClassifier(), n_estimators=500,
#               max_samples=100, bootstrap=True, n_jobs=-1
#           )
#       bag_clf.fit(X_train, y_train)
#       y_pred = bag_clf.predict(X_test)
# 
# 
#                     The BaggingClassifier automatically performs soft voting
#                     instead of hard voting if the base classifier can estimate class proba‐
#                     bilities (i.e., if it has a predict_proba() method), which is the case
#                     with Decision Trees classifiers.
# 
# 
# Figure 7-5 compares the decision boundary of a single Decision Tree with the deci‐
# sion boundary of a bagging ensemble of 500 trees (from the preceding code), both
# trained on the moons dataset. As you can see, the ensemble’s predictions will likely
# generalize much better than the single Decision Tree’s predictions: the ensemble has a
# comparable bias but a smaller variance (it makes roughly the same number of errors
# on the training set, but the decision boundary is less irregular).
# 
# 
# 
# 
# 5 max_samples can alternatively be set to a float between 0.0 and 1.0, in which case the max number of instances
#   to sample is equal to the size of the training set times max_samples.
# 
# 
# 
# 186   |   Chapter 7: Ensemble Learning and Random Forests
# 
#                      Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 7-5. A single Decision Tree versus a bagging ensemble of 500 trees
# 
# Bootstrapping introduces a bit more diversity in the subsets that each predictor is
# trained on, so bagging ends up with a slightly higher bias than pasting, but this also
# means that predictors end up being less correlated so the ensemble’s variance is
# reduced. Overall, bagging often results in better models, which explains why it is gen‐
# erally preferred. However, if you have spare time and CPU power you can use cross-
# validation to evaluate both bagging and pasting and select the one that works best.
# 
# Out-of-Bag Evaluation
# With bagging, some instances may be sampled several times for any given predictor,
# while others may not be sampled at all. By default a BaggingClassifier samples m
# training instances with replacement (bootstrap=True), where m is the size of the
# training set. This means that only about 63% of the training instances are sampled on
# average for each predictor.6 The remaining 37% of the training instances that are not
# sampled are called out-of-bag (oob) instances. Note that they are not the same 37%
# for all predictors.
# Since a predictor never sees the oob instances during training, it can be evaluated on
# these instances, without the need for a separate validation set or cross-validation. You
# can evaluate the ensemble itself by averaging out the oob evaluations of each predic‐
# tor.
# In Scikit-Learn, you can set oob_score=True when creating a BaggingClassifier to
# request an automatic oob evaluation after training. The following code demonstrates
# this. The resulting evaluation score is available through the oob_score_ variable:
#     >>> bag_clf = BaggingClassifier(
#     >>>         DecisionTreeClassifier(), n_estimators=500,
#     >>>         bootstrap=True, n_jobs=-1, oob_score=True)
# 
# 
# 
# 6 As m grows, this ratio approaches 1 – exp(–1) ≈ 63.212%.
# 
# 
# 
#                                                                   Bagging and Pasting   |   187
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Bagging and Pasting in Scikit-Learn",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Bagging and Pasting in Scikit-Learn"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Baggingand(HierNode):
    def __init__(self):
        super().__init__("Bagging and Pasting in Scikit-Learn")
        self.add(Content())

# eof
