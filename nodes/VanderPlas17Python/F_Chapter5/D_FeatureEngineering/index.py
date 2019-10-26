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

from .A_CategoricalFeatures.index import CategoricalFeatures as A_CategoricalFeatures
from .B_TextFeatures.index import TextFeatures as B_TextFeatures
from .C_ImageFeatures.index import ImageFeatures as C_ImageFeatures
from .D_DerivedFeatures.index import DerivedFeatures as D_DerivedFeatures
from .E_Imputationof.index import Imputationof as E_Imputationof
from .F_FeaturePipelines.index import FeaturePipelines as F_FeaturePipelines

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# Figure 5-34. The best-fit model determined via an automatic grid-search
# 
# Summary
# In this section, we have begun to explore the concept of model validation and hyper‐
# parameter optimization, focusing on intuitive aspects of the bias–variance trade-off
# and how it comes into play when fitting models to data. In particular, we found that
# the use of a validation set or cross-validation approach is vital when tuning parame‐
# ters in order to avoid overfitting for more complex/flexible models.
# In later sections, we will discuss the details of particularly useful models, and
# throughout will talk about what tuning is available for these models and how these
# free parameters affect model complexity. Keep the lessons of this section in mind as
# you read on and learn about these machine learning approaches!
# 
# Feature Engineering
# The previous sections outline the fundamental ideas of machine learning, but all of
# the examples assume that you have numerical data in a tidy, [n_samples, n_fea
# tures] format. In the real world, data rarely comes in such a form. With this in mind,
# one of the more important steps in using machine learning in practice is feature engi‐
# neering—that is, taking whatever information you have about your problem and
# turning it into numbers that you can use to build your feature matrix.
# In this section, we will cover a few common examples of feature engineering tasks:
# features for representing categorical data, features for representing text, and features
# for representing images. Additionally, we will discuss derived features for increasing
# model complexity and imputation of missing data. Often this process is known as vec‐
# torization, as it involves converting arbitrary data into well-behaved vectors.
# 
# 
# 
#                                                                  Feature Engineering   |   375
# 
# Categorical Features
# One common type of non-numerical data is categorical data. For example, imagine
# you are exploring some data on housing prices, and along with numerical features
# like “price” and “rooms,” you also have “neighborhood” information. For example,
# your data might look something like this:
#       In[1]: data = [
#                  {'price':      850000,   'rooms':   4,   'neighborhood':   'Queen Anne'},
#                  {'price':      700000,   'rooms':   3,   'neighborhood':   'Fremont'},
#                  {'price':      650000,   'rooms':   3,   'neighborhood':   'Wallingford'},
#                  {'price':      600000,   'rooms':   2,   'neighborhood':   'Fremont'}
#              ]
# You might be tempted to encode this data with a straightforward numerical mapping:
#       In[2]: {'Queen Anne': 1, 'Fremont': 2, 'Wallingford': 3};
# It turns out that this is not generally a useful approach in Scikit-Learn: the package’s
# models make the fundamental assumption that numerical features reflect algebraic
# quantities. Thus such a mapping would imply, for example, that Queen Anne < Fre‐
# mont < Wallingford, or even that Wallingford - Queen Anne = Fremont, which (niche
# demographic jokes aside) does not make much sense.
# In this case, one proven technique is to use one-hot encoding, which effectively creates
# extra columns indicating the presence or absence of a category with a value of 1 or 0,
# respectively. When your data comes as a list of dictionaries, Scikit-Learn’s DictVector
# izer will do this for you:
#       In[3]: from sklearn.feature_extraction import DictVectorizer
#              vec = DictVectorizer(sparse=False, dtype=int)
#              vec.fit_transform(data)
#       Out[3]: array([[          0,        1,         0,   850000,     4],
#                      [          1,        0,         0,   700000,     3],
#                      [          0,        0,         1,   650000,     3],
#                      [          1,        0,         0,   600000,     2]], dtype=int64)
# Notice that the neighborhood column has been expanded into three separate columns,
# representing the three neighborhood labels, and that each row has a 1 in the column
# associated with its neighborhood. With these categorical features thus encoded, you
# can proceed as normal with fitting a Scikit-Learn model.
# To see the meaning of each column, you can inspect the feature names:
#       In[4]: vec.get_feature_names()
#       Out[4]: ['neighborhood=Fremont',
#                'neighborhood=Queen Anne',
#                'neighborhood=Wallingford',
#                'price',
#                'rooms']
# 
# 
# 
# 376   | Chapter 5: Machine Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Feature Engineering",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FeatureEngineering(HierNode):
    def __init__(self):
        super().__init__("Feature Engineering")
        self.add(Content())
        self.add(A_CategoricalFeatures())
        self.add(B_TextFeatures())
        self.add(C_ImageFeatures())
        self.add(D_DerivedFeatures())
        self.add(E_Imputationof())
        self.add(F_FeaturePipelines())

# eof
