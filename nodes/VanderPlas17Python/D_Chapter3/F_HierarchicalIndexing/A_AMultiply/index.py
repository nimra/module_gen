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
# Hierarchical Indexing
# Up to this point we’ve been focused primarily on one-dimensional and two-
# dimensional data, stored in Pandas Series and DataFrame objects, respectively. Often
# it is useful to go beyond this and store higher-dimensional data—that is, data indexed
# by more than one or two keys. While Pandas does provide Panel and Panel4D objects
# that natively handle three-dimensional and four-dimensional data (see “Panel Data”
# on page 141), a far more common pattern in practice is to make use of hierarchical
# indexing (also known as multi-indexing) to incorporate multiple index levels within a
# single index. In this way, higher-dimensional data can be compactly represented
# within the familiar one-dimensional Series and two-dimensional DataFrame objects.
# In this section, we’ll explore the direct creation of MultiIndex objects; considerations
# around indexing, slicing, and computing statistics across multiply indexed data; and
# useful routines for converting between simple and hierarchically indexed representa‐
# tions of your data.
# We begin with the standard imports:
#       In[1]: import pandas as pd
#              import numpy as np
# 
# 
# A Multiply Indexed Series
# Let’s start by considering how we might represent two-dimensional data within a
# one-dimensional Series. For concreteness, we will consider a series of data where
# each point has a character and numerical key.
# 
# The bad way
# Suppose you would like to track data about states from two different years. Using the
# Pandas tools we’ve already covered, you might be tempted to simply use Python
# tuples as keys:
#       In[2]: index = [('California', 2000), ('California', 2010),
#                       ('New York', 2000), ('New York', 2010),
#                       ('Texas', 2000), ('Texas', 2010)]
#              populations = [33871648, 37253956,
#                             18976457, 19378102,
#                             20851820, 25145561]
#              pop = pd.Series(populations, index=index)
#              pop
#       Out[2]: (California, 2000)              33871648
#               (California, 2010)              37253956
#               (New York, 2000)                18976457
#               (New York, 2010)                19378102
#               (Texas, 2000)                   20851820
# 
# 
# 
# 128   |   Chapter 3: Data Manipulation with Pandas
# 
#             (Texas, 2010)             25145561
#             dtype: int64
# With this indexing scheme, you can straightforwardly index or slice the series based
# on this multiple index:
#     In[3]: pop[('California', 2010):('Texas', 2000)]
#     Out[3]: (California, 2010)        37253956
#             (New York, 2000)          18976457
#             (New York, 2010)          19378102
#             (Texas, 2000)             20851820
#             dtype: int64
# But the convenience ends there. For example, if you need to select all values from
# 2010, you’ll need to do some messy (and potentially slow) munging to make it
# happen:
#     In[4]: pop[[i for i in pop.index if i[1] == 2010]]
#     Out[4]: (California, 2010)        37253956
#             (New York, 2010)          19378102
#             (Texas, 2010)             25145561
#             dtype: int64
# This produces the desired result, but is not as clean (or as efficient for large datasets)
# as the slicing syntax we’ve grown to love in Pandas.
# 
# The better way: Pandas MultiIndex
# Fortunately, Pandas provides a better way. Our tuple-based indexing is essentially a
# rudimentary multi-index, and the Pandas MultiIndex type gives us the type of opera‐
# tions we wish to have. We can create a multi-index from the tuples as follows:
#     In[5]: index = pd.MultiIndex.from_tuples(index)
#            index
#     Out[5]: MultiIndex(levels=[['California', 'New York', 'Texas'], [2000, 2010]],
#                        labels=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]])
# 
# Notice that the MultiIndex contains multiple levels of indexing—in this case, the state
# names and the years, as well as multiple labels for each data point which encode these
# levels.
# If we reindex our series with this MultiIndex, we see the hierarchical representation
# of the data:
#     In[6]: pop = pop.reindex(index)
#            pop
#     Out[6]: California   2000       33871648
#                          2010       37253956
#             New York     2000       18976457
#                          2010       19378102
# 
# 
#                                                                   Hierarchical Indexing   |   129
# 
#                 Texas          2000       20851820
#                                2010       25145561
#                 dtype: int64
# 
# Here the first two columns of the Series representation show the multiple index val‐
# ues, while the third column shows the data. Notice that some entries are missing in
# the first column: in this multi-index representation, any blank entry indicates the
# same value as the line above it.
# Now to access all data for which the second index is 2010, we can simply use the Pan‐
# das slicing notation:
#       In[7]: pop[:, 2010]
#       Out[7]: California         37253956
#               New York           19378102
#               Texas              25145561
#               dtype: int64
# The result is a singly indexed array with just the keys we’re interested in. This syntax
# is much more convenient (and the operation is much more efficient!) than the home-
# spun tuple-based multi-indexing solution that we started with. We’ll now further dis‐
# cuss this sort of indexing operation on hierarchically indexed data.
# 
# MultiIndex as extra dimension
# You might notice something else here: we could easily have stored the same data
# using a simple DataFrame with index and column labels. In fact, Pandas is built with
# this equivalence in mind. The unstack() method will quickly convert a multiply-
# indexed Series into a conventionally indexed DataFrame:
#       In[8]: pop_df = pop.unstack()
#              pop_df
#       Out[8]:                      2000         2010
#                 California     33871648     37253956
#                 New York       18976457     19378102
#                 Texas          20851820     25145561
# 
# Naturally, the stack() method provides the opposite operation:
#       In[9]: pop_df.stack()
#       Out[9]:    California     2000       33871648
#                                 2010       37253956
#                  New York       2000       18976457
#                                 2010       19378102
#                  Texas          2000       20851820
#                                 2010       25145561
#                  dtype: int64
# Seeing this, you might wonder why would we would bother with hierarchical index‐
# ing at all. The reason is simple: just as we were able to use multi-indexing to represent
# 
# 130   | Chapter 3: Data Manipulation with Pandas
# 
# two-dimensional data within a one-dimensional Series, we can also use it to repre‐
# sent data of three or more dimensions in a Series or DataFrame. Each extra level in a
# multi-index represents an extra dimension of data; taking advantage of this property
# gives us much more flexibility in the types of data we can represent. Concretely, we
# might want to add another column of demographic data for each state at each year
# (say, population under 18); with a MultiIndex this is as easy as adding another col‐
# umn to the DataFrame:
#     In[10]: pop_df = pd.DataFrame({'total': pop,
#                                    'under18': [9267089, 9284094,
#                                                4687374, 4318033,
#                                                5906301, 6879014]})
#             pop_df
#     Out[10]:                         total   under18
#                California 2000    33871648   9267089
#                           2010    37253956   9284094
#                New York   2000    18976457   4687374
#                           2010    19378102   4318033
#                Texas      2000    20851820   5906301
#                           2010    25145561   6879014
# In addition, all the ufuncs and other functionality discussed in “Operating on Data in
# Pandas” on page 115 work with hierarchical indices as well. Here we compute the
# fraction of people under 18 by year, given the above data:
#     In[11]: f_u18 = pop_df['under18'] / pop_df['total']
#             f_u18.unstack()
#     Out[11]:                    2000       2010
#                California   0.273594   0.249211
#                New York     0.247010   0.222831
#                Texas        0.283251   0.273568
# This allows us to easily and quickly manipulate and explore even high-dimensional
# data.
# 
# Methods of MultiIndex Creation
# The most straightforward way to construct a multiply indexed Series or DataFrame
# is to simply pass a list of two or more index arrays to the constructor. For example:
#     In[12]: df = pd.DataFrame(np.random.rand(4, 2),
#                               index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
#                               columns=['data1', 'data2'])
#             df
#     Out[12]:            data1       data2
#                a 1   0.554233    0.356072
#                  2   0.925244    0.219474
#                b 1   0.441759    0.610054
#                  2   0.171495    0.886688
# 
# 
#                                                                Hierarchical Indexing   |   131
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "A Multiply Indexed Series",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AMultiply(HierNode):
    def __init__(self):
        super().__init__("A Multiply Indexed Series")
        self.add(Content())

# eof
