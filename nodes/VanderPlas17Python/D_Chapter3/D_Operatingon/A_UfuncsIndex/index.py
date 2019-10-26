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
# Operating on Data in Pandas
# One of the essential pieces of NumPy is the ability to perform quick element-wise
# operations, both with basic arithmetic (addition, subtraction, multiplication, etc.) and
# with more sophisticated operations (trigonometric functions, exponential and loga‐
# rithmic functions, etc.). Pandas inherits much of this functionality from NumPy, and
# the ufuncs that we introduced in “Computation on NumPy Arrays: Universal Func‐
# tions” on page 50 are key to this.
# Pandas includes a couple useful twists, however: for unary operations like negation
# and trigonometric functions, these ufuncs will preserve index and column labels in the
# output, and for binary operations such as addition and multiplication, Pandas will
# automatically align indices when passing the objects to the ufunc. This means that
# keeping the context of data and combining data from different sources—both poten‐
# tially error-prone tasks with raw NumPy arrays—become essentially foolproof ones
# with Pandas. We will additionally see that there are well-defined operations between
# one-dimensional Series structures and two-dimensional DataFrame structures.
# 
# Ufuncs: Index Preservation
# Because Pandas is designed to work with NumPy, any NumPy ufunc will work on
# Pandas Series and DataFrame objects. Let’s start by defining a simple Series and
# DataFrame on which to demonstrate this:
#     In[1]: import pandas as pd
#            import numpy as np
#     In[2]: rng = np.random.RandomState(42)
#            ser = pd.Series(rng.randint(0, 10, 4))
#            ser
#     Out[2]: 0    6
#             1    3
#             2    7
#             3    4
#             dtype: int64
#     In[3]: df = pd.DataFrame(rng.randint(0, 10, (3, 4)),
#                              columns=['A', 'B', 'C', 'D'])
#            df
#     Out[3]:       A   B   C   D
#               0   6   9   2   6
#               1   7   4   3   7
#               2   7   2   5   4
# If we apply a NumPy ufunc on either of these objects, the result will be another Pan‐
# das object with the indices preserved:
#     In[4]: np.exp(ser)
# 
# 
# 
#                                                            Operating on Data in Pandas   |   115
# 
#       Out[4]: 0     403.428793
#               1      20.085537
#               2    1096.633158
#               3      54.598150
#               dtype: float64
# Or, for a slightly more complex calculation:
#       In[5]: np.sin(df * np.pi / 4)
#       Out[5]:             A                  B         C            D
#                 0 -1.000000       7.071068e-01 1.000000 -1.000000e+00
#                 1 -0.707107       1.224647e-16 0.707107 -7.071068e-01
#                 2 -0.707107       1.000000e+00 -0.707107 1.224647e-16
# Any of the ufuncs discussed in “Computation on NumPy Arrays: Universal Func‐
# tions” on page 50 can be used in a similar manner.
# 
# UFuncs: Index Alignment
# For binary operations on two Series or DataFrame objects, Pandas will align indices
# in the process of performing the operation. This is very convenient when you are
# working with incomplete data, as we’ll see in some of the examples that follow.
# 
# Index alignment in Series
# As an example, suppose we are combining two different data sources, and find only
# the top three US states by area and the top three US states by population:
#       In[6]: area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
#                                'California': 423967}, name='area')
#              population = pd.Series({'California': 38332521, 'Texas': 26448193,
#                                      'New York': 19651127}, name='population')
# Let’s see what happens when we divide these to compute the population density:
#       In[7]: population / area
#       Out[7]: Alaska               NaN
#               California     90.413926
#               New York             NaN
#               Texas          38.018740
#               dtype: float64
# The resulting array contains the union of indices of the two input arrays, which we
# could determine using standard Python set arithmetic on these indices:
#       In[8]: area.index | population.index
#       Out[8]: Index(['Alaska', 'California', 'New York', 'Texas'], dtype='object')
# 
# Any item for which one or the other does not have an entry is marked with NaN, or
# “Not a Number,” which is how Pandas marks missing data (see further discussion of
# missing data in “Handling Missing Data” on page 119). This index matching is imple‐
# 
# 
# 116   |   Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Ufuncs: Index Preservation",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UfuncsIndex(HierNode):
    def __init__(self):
        super().__init__("Ufuncs: Index Preservation")
        self.add(Content())

# eof
