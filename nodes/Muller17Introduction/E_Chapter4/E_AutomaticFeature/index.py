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

from .A_UnivariateStatistics.index import UnivariateStatistics as A_UnivariateStatistics
from .B_ModelBasedFeature.index import ModelBasedFeature as B_ModelBasedFeature
from .C_IterativeFeature.index import IterativeFeature as C_IterativeFeature

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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Automatic Feature Selection",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AutomaticFeature(HierNode):
    def __init__(self):
        super().__init__("Automatic Feature Selection")
        self.add(Content(), "content")
        self.add(A_UnivariateStatistics())
        self.add(B_ModelBasedFeature())
        self.add(C_IterativeFeature())

# eof
