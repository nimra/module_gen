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
# As you saw in the previous examples, binning, polynomials, and interactions can
# have a huge influence on how models perform on a given dataset. This is particularly
# true for less complex models like linear models and naive Bayes models. Tree-based
# models, on the other hand, are often able to discover important interactions them‐
# selves, and don’t require transforming the data explicitly most of the time. Other
# models, like SVMs, nearest neighbors, and neural networks, might sometimes benefit
# from using binning, interactions, or polynomials, but the implications there are usu‐
# ally much less clear than in the case of linear models.
# 
# Automatic Feature Selection
# With so many ways to create new features, you might get tempted to increase the
# dimensionality of the data way beyond the number of original features. However,
# adding more features makes all models more complex, and so increases the chance of
# overfitting. When adding new features, or with high-dimensional datasets in general,
# it can be a good idea to reduce the number of features to only the most useful ones,
# and discard the rest. This can lead to simpler models that generalize better. But how
# can you know how good each feature is? There are three basic strategies: univariate
# statistics, model-based selection, and iterative selection. We will discuss all three of
# them in detail. All of these methods are supervised methods, meaning they need the
# target for fitting the model. This means we need to split the data into training and test
# sets, and fit the feature selection only on the training part of the data.
# 
# Univariate Statistics
# In univariate statistics, we compute whether there is a statistically significant relation‐
# ship between each feature and the target. Then the features that are related with the
# highest confidence are selected. In the case of classification, this is also known as
# analysis of variance (ANOVA). A key property of these tests is that they are univari‐
# ate, meaning that they only consider each feature individually. Consequently, a fea‐
# ture will be discarded if it is only informative when combined with another feature.
# Univariate tests are often very fast to compute, and don’t require building a model.
# On the other hand, they are completely independent of the model that you might
# want to apply after the feature selection.
# To use univariate feature selection in scikit-learn, you need to choose a test, usu‐
# ally either f_classif (the default) for classification or f_regression for regression,
# and a method to discard features based on the p-values determined in the test. All
# methods for discarding parameters use a threshold to discard all features with too
# high a p-value (which means they are unlikely to be related to the target). The meth‐
# ods differ in how they compute this threshold, with the simplest ones being SelectKB
# est, which selects a fixed number k of features, and SelectPercentile, which selects
# a fixed percentage of features. Let’s apply the feature selection for classification on the
# 
# 
# 236   |   Chapter 4: Representing Data and Engineering Features
# 
# cancer dataset. To make the task a bit harder, we’ll add some noninformative noise
# features to the data. We expect the feature selection to be able to identify the features
# that are noninformative and remove them:
# In[39]:
#     from sklearn.datasets import load_breast_cancer
#     from sklearn.feature_selection import SelectPercentile
#     from sklearn.model_selection import train_test_split
# 
#     cancer = load_breast_cancer()
# 
#     # get deterministic random numbers
#     rng = np.random.RandomState(42)
#     noise = rng.normal(size=(len(cancer.data), 50))
#     # add noise features to the data
#     # the first 30 features are from the dataset, the next 50 are noise
#     X_w_noise = np.hstack([cancer.data, noise])
# 
#     X_train, X_test, y_train, y_test = train_test_split(
#         X_w_noise, cancer.target, random_state=0, test_size=.5)
#     # use f_classif (the default) and SelectPercentile to select 50% of features
#     select = SelectPercentile(percentile=50)
#     select.fit(X_train, y_train)
#     # transform training set
#     X_train_selected = select.transform(X_train)
# 
#     print("X_train.shape: {}".format(X_train.shape))
#     print("X_train_selected.shape: {}".format(X_train_selected.shape))
# 
# Out[39]:
#     X_train.shape: (284, 80)
#     X_train_selected.shape: (284, 40)
# As you can see, the number of features was reduced from 80 to 40 (50 percent of the
# original number of features). We can find out which features have been selected using
# the get_support method, which returns a Boolean mask of the selected features
# (visualized in Figure 4-9):
# In[40]:
#     mask = select.get_support()
#     print(mask)
#     # visualize the mask -- black is True, white is False
#     plt.matshow(mask.reshape(1, -1), cmap='gray_r')
#     plt.xlabel("Sample index")
# 
# Out[40]:
#     [ True True True True True True True True True False True False
#       True True True True True True False False True True True True
#       True True True True True True False False False True False True
# 
# 
# 
#                                                             Automatic Feature Selection   |   237
# 
#        False False True False False False False True False False True False
#        False True False True False False False False False False True False
#         True False False False False True False True False False False False
#         True True False True False False False False]
# 
# 
# 
# 
# Figure 4-9. Features selected by SelectPercentile
# 
# As you can see from the visualization of the mask, most of the selected features are
# the original features, and most of the noise features were removed. However, the
# recovery of the original features is not perfect. Let’s compare the performance of
# logistic regression on all features against the performance using only the selected
# features:
# In[41]:
#       from sklearn.linear_model import LogisticRegression
# 
#       # transform test data
#       X_test_selected = select.transform(X_test)
# 
#       lr = LogisticRegression()
#       lr.fit(X_train, y_train)
#       print("Score with all features: {:.3f}".format(lr.score(X_test, y_test)))
#       lr.fit(X_train_selected, y_train)
#       print("Score with only selected features: {:.3f}".format(
#           lr.score(X_test_selected, y_test)))
# 
# Out[41]:
#       Score with all features: 0.930
#       Score with only selected features: 0.940
# In this case, removing the noise features improved performance, even though some
# of the original features were lost. This was a very simple synthetic example, and out‐
# comes on real data are usually mixed. Univariate feature selection can still be very
# helpful, though, if there is such a large number of features that building a model on
# them is infeasible, or if you suspect that many features are completely uninformative.
# 
# Model-Based Feature Selection
# Model-based feature selection uses a supervised machine learning model to judge the
# importance of each feature, and keeps only the most important ones. The supervised
# model that is used for feature selection doesn’t need to be the same model that is used
# for the final supervised modeling. The feature selection model needs to provide some
# measure of importance for each feature, so that they can be ranked by this measure.
# Decision trees and decision tree–based models provide a feature_importances_
# 
# 
# 238   |   Chapter 4: Representing Data and Engineering Features
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Univariate Statistics",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UnivariateStatistics(HierNode):
    def __init__(self):
        super().__init__("Univariate Statistics")
        self.add(Content(), "content")

# eof
