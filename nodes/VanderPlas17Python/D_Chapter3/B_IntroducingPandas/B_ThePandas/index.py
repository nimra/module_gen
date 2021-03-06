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
#     area = pd.Series(area_dict)
#     area
#     Out[18]: California   423967
#              Florida      170312
#              Illinois     149995
#              New York     141297
#              Texas        695662
#              dtype: int64
# 
# Now that we have this along with the population Series from before, we can use a
# dictionary to construct a single two-dimensional object containing this information:
#     In[19]: states = pd.DataFrame({'population': population,
#                                    'area': area})
#             states
#     Out[19]:                area       population
#                California   423967     38332521
#                Florida      170312     19552860
#                Illinois     149995     12882135
#                New York     141297     19651127
#                Texas        695662     26448193
# 
# Like the Series object, the DataFrame has an index attribute that gives access to the
# index labels:
#     In[20]: states.index
#     Out[20]:
#     Index(['California', 'Florida', 'Illinois', 'New York', 'Texas'], dtype='object')
# 
# Additionally, the DataFrame has a columns attribute, which is an Index object holding
# the column labels:
#     In[21]: states.columns
#     Out[21]: Index(['area', 'population'], dtype='object')
# 
# Thus the DataFrame can be thought of as a generalization of a two-dimensional
# NumPy array, where both the rows and columns have a generalized index for access‐
# ing the data.
# 
# DataFrame as specialized dictionary
# Similarly, we can also think of a DataFrame as a specialization of a dictionary. Where
# a dictionary maps a key to a value, a DataFrame maps a column name to a Series of
# column data. For example, asking for the 'area' attribute returns the Series object
# containing the areas we saw earlier:
#     In[22]: states['area']
#     Out[22]: California       423967
#              Florida          170312
# 
# 
# 
#                                                              Introducing Pandas Objects   |   103
# 
#                  Illinois      149995
#                  New York      141297
#                  Texas         695662
#                  Name: area, dtype: int64
# Notice the potential point of confusion here: in a two-dimensional NumPy array,
# data[0] will return the first row. For a DataFrame, data['col0'] will return the first
# column. Because of this, it is probably better to think about DataFrames as generalized
# dictionaries rather than generalized arrays, though both ways of looking at the situa‐
# tion can be useful. We’ll explore more flexible means of indexing DataFrames in “Data
# Indexing and Selection” on page 107.
# 
# Constructing DataFrame objects
# A Pandas DataFrame can be constructed in a variety of ways. Here we’ll give several
# examples.
# 
# From a single Series object. A DataFrame is a collection of Series objects, and a single-
# column DataFrame can be constructed from a single Series:
#       In[23]: pd.DataFrame(population, columns=['population'])
#       Out[23]:                           population
#                  California              38332521
#                  Florida                 19552860
#                  Illinois                12882135
#                  New York                19651127
#                  Texas                   26448193
# 
# From a list of dicts. Any list of dictionaries can be made into a DataFrame. We’ll use a
# simple list comprehension to create some data:
#       In[24]: data = [{'a': i, 'b': 2 * i}
#                       for i in range(3)]
#               pd.DataFrame(data)
#       Out[24]:       a     b
#                  0   0     0
#                  1   1     2
#                  2   2     4
# 
# Even if some keys in the dictionary are missing, Pandas will fill them in with NaN (i.e.,
# “not a number”) values:
#       In[25]: pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])
#       Out[25]:       a         b   c
#                  0   1.0       2   NaN
#                  1   NaN       3   4.0
# 
# 
# 
# 
# 104   |   Chapter 3: Data Manipulation with Pandas
# 
# From a dictionary of Series objects. As we saw before, a DataFrame can be constructed
# from a dictionary of Series objects as well:
#     In[26]: pd.DataFrame({'population': population,
#                           'area': area})
#     Out[26]:                  area        population
#                California     423967      38332521
#                Florida        170312      19552860
#                Illinois       149995      12882135
#                New York       141297      19651127
#                Texas          695662      26448193
# 
# From a two-dimensional NumPy array. Given a two-dimensional array of data, we can
# create a DataFrame with any specified column and index names. If omitted, an integer
# index will be used for each:
#     In[27]: pd.DataFrame(np.random.rand(3, 2),
#                          columns=['foo', 'bar'],
#                          index=['a', 'b', 'c'])
#     Out[27]:       foo         bar
#                a   0.865257    0.213169
#                b   0.442759    0.108267
#                c   0.047110    0.905718
# 
# From a NumPy structured array. We covered structured arrays in “Structured Data:
# NumPy’s Structured Arrays” on page 92. A Pandas DataFrame operates much like a
# structured array, and can be created directly from one:
#     In[28]: A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
#             A
#     Out[28]: array([(0, 0.0), (0, 0.0), (0, 0.0)],
#                    dtype=[('A', '<i8'), ('B', '<f8')])
#     In[29]: pd.DataFrame(A)
#     Out[29]:       A   B
#                0   0   0.0
#                1   0   0.0
#                2   0   0.0
# 
# 
# The Pandas Index Object
# We have seen here that both the Series and DataFrame objects contain an explicit
# index that lets you reference and modify data. This Index object is an interesting
# structure in itself, and it can be thought of either as an immutable array or as an
# ordered set (technically a multiset, as Index objects may contain repeated values).
# Those views have some interesting consequences in the operations available on Index
# objects. As a simple example, let’s construct an Index from a list of integers:
# 
# 
#                                                           Introducing Pandas Objects   |   105
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Pandas DataFrame Object",
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
        super().__init__("The Pandas DataFrame Object")
        self.add(Content())

# eof
