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
# There is one clear disadvantage of this approach: if your category has many possible
# values, this can greatly increase the size of your dataset. However, because the enco‐
# ded data contains mostly zeros, a sparse output can be a very efficient solution:
#     In[5]: vec = DictVectorizer(sparse=True, dtype=int)
#            vec.fit_transform(data)
#     Out[5]: <4x5 sparse matrix of type '<class 'numpy.int64'>'
#                 with 12 stored elements in Compressed Sparse Row format>
# Many (though not yet all) of the Scikit-Learn estimators accept such sparse inputs
# when fitting and evaluating models. sklearn.preprocessing.OneHotEncoder and
# sklearn.feature_extraction.FeatureHasher are two additional tools that Scikit-
# Learn includes to support this type of encoding.
# 
# Text Features
# Another common need in feature engineering is to convert text to a set of representa‐
# tive numerical values. For example, most automatic mining of social media data relies
# on some form of encoding the text as numbers. One of the simplest methods of
# encoding data is by word counts: you take each snippet of text, count the occurrences
# of each word within it, and put the results in a table.
# For example, consider the following set of three phrases:
#     In[6]: sample = ['problem of evil',
#                      'evil queen',
#                      'horizon problem']
# For a vectorization of this data based on word count, we could construct a column
# representing the word “problem,” the word “evil,” the word “horizon,” and so on.
# While doing this by hand would be possible, we can avoid the tedium by using Scikit-
# Learn’s CountVectorizer:
#     In[7]: from sklearn.feature_extraction.text import CountVectorizer
# 
#            vec = CountVectorizer()
#            X = vec.fit_transform(sample)
#            X
#     Out[7]: <3x5 sparse matrix of type '<class 'numpy.int64'>'
#                 with 7 stored elements in Compressed Sparse Row format>
# The result is a sparse matrix recording the number of times each word appears; it is
# easier to inspect if we convert this to a DataFrame with labeled columns:
#     In[8]: import pandas as pd
#            pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
# 
# 
# 
# 
#                                                                 Feature Engineering   |   377
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Categorical Features",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CategoricalFeatures(HierNode):
    def __init__(self):
        super().__init__("Categorical Features")
        self.add(Content())

# eof
