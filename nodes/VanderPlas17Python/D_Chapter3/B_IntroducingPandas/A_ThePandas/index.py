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
# The Pandas Series Object
# A Pandas Series is a one-dimensional array of indexed data. It can be created from a
# list or array as follows:
#     In[2]: data = pd.Series([0.25, 0.5, 0.75, 1.0])
#            data
#     Out[2]: 0    0.25
#             1    0.50
#             2    0.75
#             3    1.00
#             dtype: float64
# 
# As we see in the preceding output, the Series wraps both a sequence of values and a
# sequence of indices, which we can access with the values and index attributes. The
# values are simply a familiar NumPy array:
#     In[3]: data.values
#     Out[3]: array([ 0.25,    0.5 ,   0.75,   1.   ])
# 
# The index is an array-like object of type pd.Index, which we’ll discuss in more detail
# momentarily:
#     In[4]: data.index
#     Out[4]: RangeIndex(start=0, stop=4, step=1)
# Like with a NumPy array, data can be accessed by the associated index via the familiar
# Python square-bracket notation:
#     In[5]: data[1]
#     Out[5]: 0.5
#     In[6]: data[1:3]
#     Out[6]: 1    0.50
#             2    0.75
#             dtype: float64
# 
# As we will see, though, the Pandas Series is much more general and flexible than the
# one-dimensional NumPy array that it emulates.
# 
# Series as generalized NumPy array
# From what we’ve seen so far, it may look like the Series object is basically inter‐
# changeable with a one-dimensional NumPy array. The essential difference is the pres‐
# ence of the index: while the NumPy array has an implicitly defined integer index used
# to access the values, the Pandas Series has an explicitly defined index associated with
# the values.
# 
# 
# 
# 
#                                                             Introducing Pandas Objects   |   99
# 
# This explicit index definition gives the Series object additional capabilities. For
# example, the index need not be an integer, but can consist of values of any desired
# type. For example, if we wish, we can use strings as an index:
#       In[7]: data = pd.Series([0.25, 0.5, 0.75, 1.0],
#                               index=['a', 'b', 'c', 'd'])
#              data
#       Out[7]: a    0.25
#               b    0.50
#               c    0.75
#               d    1.00
#               dtype: float64
# And the item access works as expected:
#       In[8]: data['b']
#       Out[8]: 0.5
# We can even use noncontiguous or nonsequential indices:
#       In[9]: data = pd.Series([0.25, 0.5, 0.75, 1.0],
#                               index=[2, 5, 3, 7])
#              data
#       Out[9]: 2    0.25
#               5    0.50
#               3    0.75
#               7    1.00
#               dtype: float64
#       In[10]: data[5]
#       Out[10]: 0.5
# 
# Series as specialized dictionary
# In this way, you can think of a Pandas Series a bit like a specialization of a Python
# dictionary. A dictionary is a structure that maps arbitrary keys to a set of arbitrary
# values, and a Series is a structure that maps typed keys to a set of typed values. This
# typing is important: just as the type-specific compiled code behind a NumPy array
# makes it more efficient than a Python list for certain operations, the type information
# of a Pandas Series makes it much more efficient than Python dictionaries for certain
# operations.
# We can make the Series-as-dictionary analogy even more clear by constructing a
# Series object directly from a Python dictionary:
# 
# 
# 
# 
# 100   |   Chapter 3: Data Manipulation with Pandas
# 
#     In[11]: population_dict = {'California': 38332521,
#                                'Texas': 26448193,
#                                'New York': 19651127,
#                                'Florida': 19552860,
#                                'Illinois': 12882135}
#             population = pd.Series(population_dict)
#             population
#     Out[11]: California       38332521
#              Florida          19552860
#              Illinois         12882135
#              New York         19651127
#              Texas            26448193
#              dtype: int64
# 
# By default, a Series will be created where the index is drawn from the sorted keys.
# From here, typical dictionary-style item access can be performed:
#     In[12]: population['California']
#     Out[12]: 38332521
# 
# Unlike a dictionary, though, the Series also supports array-style operations such as
# slicing:
#     In[13]: population['California':'Illinois']
#     Out[13]: California   38332521
#              Florida      19552860
#              Illinois     12882135
#              dtype: int64
# We’ll discuss some of the quirks of Pandas indexing and slicing in “Data Indexing and
# Selection” on page 107.
# 
# Constructing Series objects
# We’ve already seen a few ways of constructing a Pandas Series from scratch; all of
# them are some version of the following:
#     >>> pd.Series(data, index=index)
# 
# where index is an optional argument, and data can be one of many entities.
# For example, data can be a list or NumPy array, in which case index defaults to an
# integer sequence:
#     In[14]: pd.Series([2, 4, 6])
#     Out[14]: 0    2
#              1    4
#              2    6
#              dtype: int64
# 
# 
# 
# 
#                                                           Introducing Pandas Objects   |   101
# 
# data can be a scalar, which is repeated to fill the specified index:
#       In[15]: pd.Series(5, index=[100, 200, 300])
#       Out[15]: 100         5
#                200         5
#                300         5
#                dtype:      int64
# 
# data can be a dictionary, in which index defaults to the sorted dictionary keys:
#       In[16]: pd.Series({2:'a', 1:'b', 3:'c'})
#       Out[16]: 1    b
#                2    a
#                3    c
#                dtype: object
# In each case, the index can be explicitly set if a different result is preferred:
#       In[17]: pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])
#       Out[17]: 3    c
#                2    a
#                dtype: object
# 
# Notice that in this case, the Series is populated only with the explicitly identified
# keys.
# 
# The Pandas DataFrame Object
# The next fundamental structure in Pandas is the DataFrame. Like the Series object
# discussed in the previous section, the DataFrame can be thought of either as a gener‐
# alization of a NumPy array, or as a specialization of a Python dictionary. We’ll now
# take a look at each of these perspectives.
# 
# DataFrame as a generalized NumPy array
# If a Series is an analog of a one-dimensional array with flexible indices, a DataFrame
# is an analog of a two-dimensional array with both flexible row indices and flexible
# column names. Just as you might think of a two-dimensional array as an ordered
# sequence of aligned one-dimensional columns, you can think of a DataFrame as a
# sequence of aligned Series objects. Here, by “aligned” we mean that they share the
# same index.
# To demonstrate this, let’s first construct a new Series listing the area of each of the
# five states discussed in the previous section:
#       In[18]:
#       area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
#                    'Florida': 170312, 'Illinois': 149995}
# 
# 
# 
# 
# 102   |   Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Pandas Series Object",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ThePandas(HierNode):
    def __init__(self):
        super().__init__("The Pandas Series Object")
        self.add(Content())

# eof
