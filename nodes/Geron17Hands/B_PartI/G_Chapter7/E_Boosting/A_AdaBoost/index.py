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
#                         Download from finelybook www.finelybook.com
# AdaBoost
# One way for a new predictor to correct its predecessor is to pay a bit more attention
# to the training instances that the predecessor underfitted. This results in new predic‐
# tors focusing more and more on the hard cases. This is the technique used by Ada‐
# Boost.
# For example, to build an AdaBoost classifier, a first base classifier (such as a Decision
# Tree) is trained and used to make predictions on the training set. The relative weight
# of misclassified training instances is then increased. A second classifier is trained
# using the updated weights and again it makes predictions on the training set, weights
# are updated, and so on (see Figure 7-7).
# 
# 
# 
# 
# Figure 7-7. AdaBoost sequential training with instance weight updates
# 
# Figure 7-8 shows the decision boundaries of five consecutive predictors on the
# moons dataset (in this example, each predictor is a highly regularized SVM classifier
# with an RBF kernel14). The first classifier gets many instances wrong, so their weights
# get boosted. The second classifier therefore does a better job on these instances, and
# so on. The plot on the right represents the same sequence of predictors except that
# the learning rate is halved (i.e., the misclassified instance weights are boosted half as
# much at every iteration). As you can see, this sequential learning technique has some
# similarities with Gradient Descent, except that instead of tweaking a single predictor’s
# 
# 
# 14 This is just for illustrative purposes. SVMs are generally not good base predictors for AdaBoost, because they
#    are slow and tend to be unstable with AdaBoost.
# 
# 
# 
# 192    |   Chapter 7: Ensemble Learning and Random Forests
# 
#                 Download from finelybook www.finelybook.com
# parameters to minimize a cost function, AdaBoost adds predictors to the ensemble,
# gradually making it better.
# 
# 
# 
# 
# Figure 7-8. Decision boundaries of consecutive predictors
# 
# Once all predictors are trained, the ensemble makes predictions very much like bag‐
# ging or pasting, except that predictors have different weights depending on their
# overall accuracy on the weighted training set.
# 
#                    There is one important drawback to this sequential learning techni‐
#                    que: it cannot be parallelized (or only partially), since each predic‐
#                    tor can only be trained after the previous predictor has been
#                    trained and evaluated. As a result, it does not scale as well as bag‐
#                    ging or pasting.
# 
# Let’s take a closer look at the AdaBoost algorithm. Each instance weight w(i) is initially
#         1
# set to m . A first predictor is trained and its weighted error rate r1 is computed on the
# training set; see Equation 7-1.
# 
#    Equation 7-1. Weighted error rate of the jth predictor
#               m
#              ∑
#             i=1
#                        wi
#           y ji ≠ y i
#    rj =       m
#                             where y ji is the jth predictor’s prediction for the ith instance.
#               ∑
#             i=1
#                   wi
# 
# 
# 
# 
#                                                                                    Boosting   |   193
# 
#                   Download from finelybook www.finelybook.com
# The predictor’s weight αj is then computed using Equation 7-2, where η is the learn‐
# ing rate hyperparameter (defaults to 1).15 The more accurate the predictor is, the
# higher its weight will be. If it is just guessing randomly, then its weight will be close to
# zero. However, if it is most often wrong (i.e., less accurate than random guessing),
# then its weight will be negative.
# 
#       Equation 7-2. Predictor weight
#                     1 − rj
#       α j = η log
#                       rj
# 
# Next the instance weights are updated using Equation 7-3: the misclassified instances
# are boosted.
# 
#       Equation 7-3. Weight update rule
#            for i = 1, 2, ⋯, m
#                   wi                 if y j i = y i
#             i
#        w
#                   w i exp α j if y j i ≠ y i
# 
# 
# Then all the instance weights are normalized (i.e., divided by ∑m      i
#                                                                 i = 1 w ).
# 
# Finally, a new predictor is trained using the updated weights, and the whole process is
# repeated (the new predictor’s weight is computed, the instance weights are updated,
# then another predictor is trained, and so on). The algorithm stops when the desired
# number of predictors is reached, or when a perfect predictor is found.
# To make predictions, AdaBoost simply computes the predictions of all the predictors
# and weighs them using the predictor weights αj. The predicted class is the one that
# receives the majority of weighted votes (see Equation 7-4).
# 
#       Equation 7-4. AdaBoost predictions
#                                 N
#       y � = argmax              ∑
#                                j=1
#                                         αj   where N is the number of predictors.
#                      k
#                              yj � = k
# 
# 
# 
# 
# 15 The original AdaBoost algorithm does not use a learning rate hyperparameter.
# 
# 
# 
# 194    |    Chapter 7: Ensemble Learning and Random Forests
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "AdaBoost",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AdaBoost(HierNode):
    def __init__(self):
        super().__init__("AdaBoost")
        self.add(Content(), "content")

# eof
