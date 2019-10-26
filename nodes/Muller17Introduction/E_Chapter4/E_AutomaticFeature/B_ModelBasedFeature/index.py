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
# attribute, which directly encodes the importance of each feature. Linear models have
# coefficients, which can also be used to capture feature importances by considering the
# absolute values. As we saw in Chapter 2, linear models with L1 penalty learn sparse
# coefficients, which only use a small subset of features. This can be viewed as a form of
# feature selection for the model itself, but can also be used as a preprocessing step to
# select features for another model. In contrast to univariate selection, model-based
# selection considers all features at once, and so can capture interactions (if the model
# can capture them). To use model-based feature selection, we need to use the
# SelectFromModel transformer:
# In[42]:
#     from sklearn.feature_selection import SelectFromModel
#     from sklearn.ensemble import RandomForestClassifier
#     select = SelectFromModel(
#         RandomForestClassifier(n_estimators=100, random_state=42),
#         threshold="median")
# 
# The SelectFromModel class selects all features that have an importance measure of
# the feature (as provided by the supervised model) greater than the provided thresh‐
# old. To get a comparable result to what we got with univariate feature selection, we
# used the median as a threshold, so that half of the features will be selected. We use a
# random forest classifier with 100 trees to compute the feature importances. This is a
# quite complex model and much more powerful than using univariate tests. Now let’s
# actually fit the model:
# In[43]:
#     select.fit(X_train, y_train)
#     X_train_l1 = select.transform(X_train)
#     print("X_train.shape: {}".format(X_train.shape))
#     print("X_train_l1.shape: {}".format(X_train_l1.shape))
# 
# Out[43]:
#     X_train.shape: (284, 80)
#     X_train_l1.shape: (284, 40)
# Again, we can have a look at the features that were selected (Figure 4-10):
# In[44]:
#     mask = select.get_support()
#     # visualize the mask -- black is True, white is False
#     plt.matshow(mask.reshape(1, -1), cmap='gray_r')
#     plt.xlabel("Sample index")
# 
# 
# 
# 
# Figure 4-10. Features selected by SelectFromModel using the RandomForestClassifier
# 
# 
#                                                             Automatic Feature Selection   |   239
# 
# This time, all but two of the original features were selected. Because we specified to
# select 40 features, some of the noise features are also selected. Let’s take a look at the
# performance:
# In[45]:
#       X_test_l1 = select.transform(X_test)
#       score = LogisticRegression().fit(X_train_l1, y_train).score(X_test_l1, y_test)
#       print("Test score: {:.3f}".format(score))
# 
# Out[45]:
#       Test score: 0.951
# With the better feature selection, we also gained some improvements here.
# 
# Iterative Feature Selection
# In univariate testing we used no model, while in model-based selection we used a sin‐
# gle model to select features. In iterative feature selection, a series of models are built,
# with varying numbers of features. There are two basic methods: starting with no fea‐
# tures and adding features one by one until some stopping criterion is reached, or
# starting with all features and removing features one by one until some stopping crite‐
# rion is reached. Because a series of models are built, these methods are much more
# computationally expensive than the methods we discussed previously. One particular
# method of this kind is recursive feature elimination (RFE), which starts with all fea‐
# tures, builds a model, and discards the least important feature according to the
# model. Then a new model is built using all but the discarded feature, and so on until
# only a prespecified number of features are left. For this to work, the model used for
# selection needs to provide some way to determine feature importance, as was the case
# for the model-based selection. Here, we use the same random forest model that we
# used earlier, and get the results shown in Figure 4-11:
# In[46]:
#       from sklearn.feature_selection import RFE
#       select = RFE(RandomForestClassifier(n_estimators=100, random_state=42),
#                    n_features_to_select=40)
# 
#       select.fit(X_train, y_train)
#       # visualize the selected features:
#       mask = select.get_support()
#       plt.matshow(mask.reshape(1, -1), cmap='gray_r')
#       plt.xlabel("Sample index")
# 
# 
# 
# 
# 240   |   Chapter 4: Representing Data and Engineering Features
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Model-Based Feature Selection",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ModelBasedFeature(HierNode):
    def __init__(self):
        super().__init__("Model-Based Feature Selection")
        self.add(Content(), "content")

# eof