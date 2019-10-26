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
# the conventions used by Python’s built-in set data structure, so that unions, intersec‐
# tions, differences, and other combinations can be computed in a familiar way:
#     In[35]: indA = pd.Index([1, 3, 5, 7, 9])
#             indB = pd.Index([2, 3, 5, 7, 11])
#     In[36]: indA & indB   # intersection
#     Out[36]: Int64Index([3, 5, 7], dtype='int64')
#     In[37]: indA | indB   # union
#     Out[37]: Int64Index([1, 2, 3, 5, 7, 9, 11], dtype='int64')
#     In[38]: indA ^ indB   # symmetric difference
#     Out[38]: Int64Index([1, 2, 9, 11], dtype='int64')
# 
# These operations may also be accessed via object methods—for example, indA.inter
# section(indB).
# 
# 
# Data Indexing and Selection
# In Chapter 2, we looked in detail at methods and tools to access, set, and modify val‐
# ues in NumPy arrays. These included indexing (e.g., arr[2, 1]), slicing (e.g., arr[:,
# 1:5]), masking (e.g., arr[arr > 0]), fancy indexing (e.g., arr[0, [1, 5]]), and
# combinations thereof (e.g., arr[:, [1, 5]]). Here we’ll look at similar means of
# accessing and modifying values in Pandas Series and DataFrame objects. If you have
# used the NumPy patterns, the corresponding patterns in Pandas will feel very famil‐
# iar, though there are a few quirks to be aware of.
# We’ll start with the simple case of the one-dimensional Series object, and then move
# on to the more complicated two-dimensional DataFrame object.
# 
# Data Selection in Series
# As we saw in the previous section, a Series object acts in many ways like a one-
# dimensional NumPy array, and in many ways like a standard Python dictionary. If we
# keep these two overlapping analogies in mind, it will help us to understand the pat‐
# terns of data indexing and selection in these arrays.
# 
# Series as dictionary
# Like a dictionary, the Series object provides a mapping from a collection of keys to a
# collection of values:
#     In[1]: import pandas as pd
#            data = pd.Series([0.25, 0.5, 0.75, 1.0],
#                             index=['a', 'b', 'c', 'd'])
#            data
# 
# 
# 
#                                                            Data Indexing and Selection   |   107
# 
#       Out[1]: a    0.25
#               b    0.50
#               c    0.75
#               d    1.00
#               dtype: float64
#       In[2]: data['b']
#       Out[2]: 0.5
# We can also use dictionary-like Python expressions and methods to examine the
# keys/indices and values:
#       In[3]: 'a' in data
#       Out[3]: True
#       In[4]: data.keys()
#       Out[4]: Index(['a', 'b', 'c', 'd'], dtype='object')
#       In[5]: list(data.items())
#       Out[5]: [('a', 0.25), ('b', 0.5), ('c', 0.75), ('d', 1.0)]
# 
# Series objects can even be modified with a dictionary-like syntax. Just as you can
# extend a dictionary by assigning to a new key, you can extend a Series by assigning
# to a new index value:
#       In[6]: data['e'] = 1.25
#              data
#       Out[6]: a    0.25
#               b    0.50
#               c    0.75
#               d    1.00
#               e    1.25
#               dtype: float64
# This easy mutability of the objects is a convenient feature: under the hood, Pandas is
# making decisions about memory layout and data copying that might need to take
# place; the user generally does not need to worry about these issues.
# 
# Series as one-dimensional array
# A Series builds on this dictionary-like interface and provides array-style item selec‐
# tion via the same basic mechanisms as NumPy arrays—that is, slices, masking, and
# fancy indexing. Examples of these are as follows:
#       In[7]: # slicing by explicit index
#              data['a':'c']
#       Out[7]: a    0.25
#               b    0.50
#               c    0.75
#               dtype: float64
# 
# 
# 108   | Chapter 3: Data Manipulation with Pandas
# 
#     In[8]: # slicing by implicit integer index
#            data[0:2]
#     Out[8]: a    0.25
#             b    0.50
#             dtype: float64
#     In[9]: # masking
#            data[(data > 0.3) & (data < 0.8)]
#     Out[9]: b    0.50
#             c    0.75
#             dtype: float64
#     In[10]: # fancy indexing
#             data[['a', 'e']]
#     Out[10]: a    0.25
#              e    1.25
#              dtype: float64
# Among these, slicing may be the source of the most confusion. Notice that when you
# are slicing with an explicit index (i.e., data['a':'c']), the final index is included in
# the slice, while when you’re slicing with an implicit index (i.e., data[0:2]), the final
# index is excluded from the slice.
# 
# Indexers: loc, iloc, and ix
# These slicing and indexing conventions can be a source of confusion. For example, if
# your Series has an explicit integer index, an indexing operation such as data[1] will
# use the explicit indices, while a slicing operation like data[1:3] will use the implicit
# Python-style index.
#     In[11]: data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
#             data
#     Out[11]: 1    a
#              3    b
#              5    c
#              dtype: object
#     In[12]: # explicit index when indexing
#             data[1]
#     Out[12]: 'a'
#     In[13]: # implicit index when slicing
#             data[1:3]
#     Out[13]: 3    b
#              5    c
#              dtype: object
# Because of this potential confusion in the case of integer indexes, Pandas provides
# some special indexer attributes that explicitly expose certain indexing schemes. These
# 
# 
#                                                             Data Indexing and Selection   |   109
# 
# are not functional methods, but attributes that expose a particular slicing interface to
# the data in the Series.
# First, the loc attribute allows indexing and slicing that always references the explicit
# index:
#       In[14]: data.loc[1]
#       Out[14]: 'a'
#       In[15]: data.loc[1:3]
#       Out[15]: 1    a
#                3    b
#                dtype: object
# 
# The iloc attribute allows indexing and slicing that always references the implicit
# Python-style index:
#       In[16]: data.iloc[1]
#       Out[16]: 'b'
#       In[17]: data.iloc[1:3]
#       Out[17]: 3    b
#                5    c
#                dtype: object
# 
# A third indexing attribute, ix, is a hybrid of the two, and for Series objects is equiva‐
# lent to standard []-based indexing. The purpose of the ix indexer will become more
# apparent in the context of DataFrame objects, which we will discuss in a moment.
# One guiding principle of Python code is that “explicit is better than implicit.” The
# explicit nature of loc and iloc make them very useful in maintaining clean and read‐
# able code; especially in the case of integer indexes, I recommend using these both to
# make code easier to read and understand, and to prevent subtle bugs due to the
# mixed indexing/slicing convention.
# 
# Data Selection in DataFrame
# Recall that a DataFrame acts in many ways like a two-dimensional or structured array,
# and in other ways like a dictionary of Series structures sharing the same index.
# These analogies can be helpful to keep in mind as we explore data selection within
# this structure.
# 
# DataFrame as a dictionary
# The first analogy we will consider is the DataFrame as a dictionary of related Series
# objects. Let’s return to our example of areas and populations of states:
# 
# 
# 
# 
# 110   |   Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Data Selection in Series",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataSelection(HierNode):
    def __init__(self):
        super().__init__("Data Selection in Series")
        self.add(Content())

# eof
