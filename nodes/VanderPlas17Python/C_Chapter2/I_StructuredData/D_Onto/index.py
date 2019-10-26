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
# RecordArrays: Structured Arrays with a Twist
# NumPy also provides the np.recarray class, which is almost identical to the struc‐
# tured arrays just described, but with one additional feature: fields can be accessed as
# attributes rather than as dictionary keys. Recall that we previously accessed the ages
# by writing:
#      In[15]: data['age']
#      Out[15]: array([25, 45, 37, 19], dtype=int32)
# If we view our data as a record array instead, we can access this with slightly fewer
# keystrokes:
#      In[16]: data_rec = data.view(np.recarray)
#              data_rec.age
#      Out[16]: array([25, 45, 37, 19], dtype=int32)
# The downside is that for record arrays, there is some extra overhead involved in
# accessing the fields, even when using the same syntax. We can see this here:
#      In[17]: %timeit data['age']
#              %timeit data_rec['age']
#              %timeit data_rec.age
#      1000000 loops, best of 3: 241 ns per loop
#      100000 loops, best of 3: 4.61 µs per loop
#      100000 loops, best of 3: 7.27 µs per loop
# Whether the more convenient notation is worth the additional overhead will depend
# on your own application.
# 
# On to Pandas
# This section on structured and record arrays is purposely at the end of this chapter,
# because it leads so well into the next package we will cover: Pandas. Structured arrays
# like the ones discussed here are good to know about for certain situations, especially
# in case you’re using NumPy arrays to map onto binary data formats in C, Fortran, or
# another language. For day-to-day use of structured data, the Pandas package is a
# much better choice, and we’ll dive into a full discussion of it in the next chapter.
# 
# 
# 
# 
# 96   |   Chapter 2: Introduction to NumPy
# 
#                                                                         CHAPTER 3
#                        Data Manipulation with Pandas
# 
# 
# 
# 
# In the previous chapter, we dove into detail on NumPy and its ndarray object, which
# provides efficient storage and manipulation of dense typed arrays in Python. Here
# we’ll build on this knowledge by looking in detail at the data structures provided by
# the Pandas library. Pandas is a newer package built on top of NumPy, and provides an
# efficient implementation of a DataFrame. DataFrames are essentially multidimen‐
# sional arrays with attached row and column labels, and often with heterogeneous
# types and/or missing data. As well as offering a convenient storage interface for
# labeled data, Pandas implements a number of powerful data operations familiar to
# users of both database frameworks and spreadsheet programs.
# As we saw, NumPy’s ndarray data structure provides essential features for the type of
# clean, well-organized data typically seen in numerical computing tasks. While it
# serves this purpose very well, its limitations become clear when we need more flexi‐
# bility (attaching labels to data, working with missing data, etc.) and when attempting
# operations that do not map well to element-wise broadcasting (groupings, pivots,
# etc.), each of which is an important piece of analyzing the less structured data avail‐
# able in many forms in the world around us. Pandas, and in particular its Series and
# DataFrame objects, builds on the NumPy array structure and provides efficient access
# to these sorts of “data munging” tasks that occupy much of a data scientist’s time.
# In this chapter, we will focus on the mechanics of using Series, DataFrame, and
# related structures effectively. We will use examples drawn from real datasets where
# appropriate, but these examples are not necessarily the focus.
# 
# Installing and Using Pandas
# Installing Pandas on your system requires NumPy to be installed, and if you’re build‐
# ing the library from source, requires the appropriate tools to compile the C and
# 
# 
#                                                                                      97
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "On to Pandas",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Onto(HierNode):
    def __init__(self):
        super().__init__("On to Pandas")
        self.add(Content())

# eof
