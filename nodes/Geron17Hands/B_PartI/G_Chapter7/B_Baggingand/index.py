# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Baggingand.index import Baggingand as A_Baggingand
from .B_OutofBagEvaluation.index import OutofBagEvaluation as B_OutofBagEvaluation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                        Download from finelybook www.finelybook.com
# Bagging and Pasting
# One way to get a diverse set of classifiers is to use very different training algorithms,
# as just discussed. Another approach is to use the same training algorithm for every
# predictor, but to train them on different random subsets of the training set. When
# sampling is performed with replacement, this method is called bagging1 (short for
# bootstrap aggregating2). When sampling is performed without replacement, it is called
# pasting.3
# In other words, both bagging and pasting allow training instances to be sampled sev‐
# eral times across multiple predictors, but only bagging allows training instances to be
# sampled several times for the same predictor. This sampling and training process is
# represented in Figure 7-4.
# 
# 
# 
# 
# Figure 7-4. Pasting/bagging training set sampling and training
# 
# Once all predictors are trained, the ensemble can make a prediction for a new
# instance by simply aggregating the predictions of all predictors. The aggregation
# function is typically the statistical mode (i.e., the most frequent prediction, just like a
# hard voting classifier) for classification, or the average for regression. Each individual
# predictor has a higher bias than if it were trained on the original training set, but
# aggregation reduces both bias and variance.4 Generally, the net result is that the
# 
# 
# 
# 1 “Bagging Predictors,” L. Breiman (1996).
# 2 In statistics, resampling with replacement is called bootstrapping.
# 3 “Pasting small votes for classification in large databases and on-line,” L. Breiman (1999).
# 4 Bias and variance were introduced in Chapter 4.
# 
# 
# 
#                                                                                       Bagging and Pasting   |   185
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Bagging and Pasting",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Bagging and Pasting"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Baggingand(HierNode):
    def __init__(self):
        super().__init__("Bagging and Pasting")
        self.add(Content())
        self.add(A_Baggingand())
        self.add(B_OutofBagEvaluation())

# eof
