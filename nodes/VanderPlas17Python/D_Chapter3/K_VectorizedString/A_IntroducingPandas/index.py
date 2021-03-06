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
# In particular, the striking feature of this graph is the dip in birthrate on US holidays
# (e.g., Independence Day, Labor Day, Thanksgiving, Christmas, New Year’s Day)
# although this likely reflects trends in scheduled/induced births rather than some deep
# psychosomatic effect on natural births. For more discussion on this trend, see the
# analysis and links in Andrew Gelman’s blog post on the subject. We’ll return to this
# figure in “Example: Effect of Holidays on US Births” on page 269, where we will use
# Matplotlib’s tools to annotate this plot.
# Looking at this short example, you can see that many of the Python and Pandas tools
# we’ve seen to this point can be combined and used to gain insight from a variety of
# datasets. We will see some more sophisticated applications of these data manipula‐
# tions in future sections!
# 
# Vectorized String Operations
# One strength of Python is its relative ease in handling and manipulating string data.
# Pandas builds on this and provides a comprehensive set of vectorized string operations
# that become an essential piece of the type of munging required when one is working
# with (read: cleaning up) real-world data. In this section, we’ll walk through some of
# the Pandas string operations, and then take a look at using them to partially clean up
# a very messy dataset of recipes collected from the Internet.
# 
# Introducing Pandas String Operations
# We saw in previous sections how tools like NumPy and Pandas generalize arithmetic
# operations so that we can easily and quickly perform the same operation on many
# array elements. For example:
#       In[1]: import numpy as np
#              x = np.array([2, 3, 5, 7, 11, 13])
#              x * 2
#       Out[1]: array([ 4,        6, 10, 14, 22, 26])
# This vectorization of operations simplifies the syntax of operating on arrays of data:
# we no longer have to worry about the size or shape of the array, but just about what
# operation we want done. For arrays of strings, NumPy does not provide such simple
# access, and thus you’re stuck using a more verbose loop syntax:
#       In[2]: data = ['peter', 'Paul', 'MARY', 'gUIDO']
#              [s.capitalize() for s in data]
#       Out[2]: ['Peter', 'Paul', 'Mary', 'Guido']
# This is perhaps sufficient to work with some data, but it will break if there are any
# missing values. For example:
#       In[3]: data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
#              [s.capitalize() for s in data]
# 
# 
# 178   |   Chapter 3: Data Manipulation with Pandas
# 
#     ---------------------------------------------------------------------------
#     ---------------------------------------------------------------------------
# 
#     AttributeError                            Traceback (most recent call last)
# 
#     <ipython-input-3-fc1d891ab539> in <module>()
#           1 data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
#     ----> 2 [s.capitalize() for s in data]
# 
# 
#     <ipython-input-3-fc1d891ab539> in <listcomp>(.0)
#           1 data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
#     ----> 2 [s.capitalize() for s in data]
# 
# 
#     AttributeError: 'NoneType' object has no attribute 'capitalize'
#     ---------------------------------------------------------------------------
# Pandas includes features to address both this need for vectorized string operations
# and for correctly handling missing data via the str attribute of Pandas Series and
# Index objects containing strings. So, for example, suppose we create a Pandas Series
# with this data:
#     In[4]: import pandas as pd
#            names = pd.Series(data)
#            names
#     Out[4]: 0    peter
#             1     Paul
#             2     None
#             3     MARY
#             4    gUIDO
#             dtype: object
# We can now call a single method that will capitalize all the entries, while skipping
# over any missing values:
#     In[5]: names.str.capitalize()
#     Out[5]: 0    Peter
#             1     Paul
#             2     None
#             3     Mary
#             4    Guido
#             dtype: object
# 
# Using tab completion on this str attribute will list all the vectorized string methods
# available to Pandas.
# 
# 
# 
# 
#                                                           Vectorized String Operations   |   179
# 
# Tables of Pandas String Methods
# If you have a good understanding of string manipulation in Python, most of Pandas’
# string syntax is intuitive enough that it’s probably sufficient to just list a table of avail‐
# able methods; we will start with that here, before diving deeper into a few of the sub‐
# tleties. The examples in this section use the following series of names:
#       In[6]: monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam',
#                                 'Eric Idle', 'Terry Jones', 'Michael Palin'])
# 
# Methods similar to Python string methods
# Nearly all Python’s built-in string methods are mirrored by a Pandas vectorized string
# method. Here is a list of Pandas str methods that mirror Python string methods:
# 
# len()         lower()            translate()         islower()
# ljust()       upper()            startswith() isupper()
# rjust()       find()             endswith()          isnumeric()
# center() rfind()                 isalnum()           isdecimal()
# zfill()       index()            isalpha()           split()
# strip()       rindex()           isdigit()           rsplit()
# rstrip() capitalize() isspace()                      partition()
# lstrip() swapcase()              istitle()           rpartition()
# 
# 
# Notice that these have various return values. Some, like lower(), return a series of
# strings:
#       In[7]: monte.str.lower()
#       Out[7]: 0    graham chapman
#               1       john cleese
#               2     terry gilliam
#               3         eric idle
#               4       terry jones
#               5     michael palin
#               dtype: object
# But some others return numbers:
#       In[8]: monte.str.len()
#       Out[8]: 0    14
#               1    11
#               2    13
#               3     9
#               4    11
#               5    13
#               dtype: int64
# 
# 
# 
# 180   |   Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Introducing Pandas String Operations",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IntroducingPandas(HierNode):
    def __init__(self):
        super().__init__("Introducing Pandas String Operations")
        self.add(Content())

# eof
