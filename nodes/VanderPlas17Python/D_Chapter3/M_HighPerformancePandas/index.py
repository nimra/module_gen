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

from .A_Motivatingquery.index import Motivatingquery as A_Motivatingquery
from .B_pandasevalfor.index import pandasevalfor as B_pandasevalfor
from .C_DataFrameevalfor.index import DataFrameevalfor as C_DataFrameevalfor
from .D_DataFramequeryMethod.index import DataFramequeryMethod as D_DataFramequeryMethod
from .E_PerformanceWhen.index import PerformanceWhen as E_PerformanceWhen

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# With this in mind, let’s do a compound groupby and look at the hourly trend on
# weekdays versus weekends. We’ll start by grouping by both a flag marking the week‐
# end, and the time of day:
#       In[45]: weekend = np.where(data.index.weekday < 5, 'Weekday', 'Weekend')
#               by_time = data.groupby([weekend, data.index.time]).mean()
# Now we’ll use some of the Matplotlib tools described in “Multiple Subplots” on page
# 262 to plot two panels side by side (Figure 3-17):
#       In[46]: import matplotlib.pyplot as plt
#               fig, ax = plt.subplots(1, 2, figsize=(14, 5))
#               by_time.ix['Weekday'].plot(ax=ax[0], title='Weekdays',
#                                          xticks=hourly_ticks, style=[':', '--', '-'])
#               by_time.ix['Weekend'].plot(ax=ax[1], title='Weekends',
#                                          xticks=hourly_ticks, style=[':', '--', '-']);
# 
# 
# 
# 
# Figure 3-17. Average hourly bicycle counts by weekday and weekend
# 
# The result is very interesting: we see a bimodal commute pattern during the work
# week, and a unimodal recreational pattern during the weekends. It would be interest‐
# ing to dig through this data in more detail, and examine the effect of weather, temper‐
# ature, time of year, and other factors on people’s commuting patterns; for further
# discussion, see my blog post “Is Seattle Really Seeing an Uptick In Cycling?”, which
# uses a subset of this data. We will also revisit this dataset in the context of modeling in
# “In Depth: Linear Regression” on page 390.
# 
# High-Performance Pandas: eval() and query()
# As we’ve already seen in previous chapters, the power of the PyData stack is built
# upon the ability of NumPy and Pandas to push basic operations into C via an intu‐
# itive syntax: examples are vectorized/broadcasted operations in NumPy, and
# grouping-type operations in Pandas. While these abstractions are efficient and effec‐
# 
# 
# 208   |   Chapter 3: Data Manipulation with Pandas
# 
# tive for many common use cases, they often rely on the creation of temporary inter‐
# mediate objects, which can cause undue overhead in computational time and
# memory use.
# As of version 0.13 (released January 2014), Pandas includes some experimental tools
# that allow you to directly access C-speed operations without costly allocation of inter‐
# mediate arrays. These are the eval() and query() functions, which rely on the
# Numexpr package. In this notebook we will walk through their use and give some
# rules of thumb about when you might think about using them.
# 
# Motivating query() and eval(): Compound Expressions
# We’ve seen previously that NumPy and Pandas support fast vectorized operations; for
# example, when you are adding the elements of two arrays:
#     In[1]: import numpy as np
#            rng = np.random.RandomState(42)
#            x = rng.rand(1E6)
#            y = rng.rand(1E6)
#            %timeit x + y
#     100 loops, best of 3: 3.39 ms per loop
# As discussed in “Computation on NumPy Arrays: Universal Functions” on page 50,
# this is much faster than doing the addition via a Python loop or comprehension:
#     In[2]:
#     %timeit np.fromiter((xi + yi for xi, yi in zip(x, y)),
#                          dtype=x.dtype, count=len(x))
#     1 loop, best of 3: 266 ms per loop
# But this abstraction can become less efficient when you are computing compound
# expressions. For example, consider the following expression:
#     In[3]: mask = (x > 0.5) & (y < 0.5)
# Because NumPy evaluates each subexpression, this is roughly equivalent to the
# following:
#     In[4]: tmp1 = (x > 0.5)
#            tmp2 = (y < 0.5)
#            mask = tmp1 & tmp2
# 
# In other words, every intermediate step is explicitly allocated in memory. If the x and y
# arrays are very large, this can lead to significant memory and computational over‐
# head. The Numexpr library gives you the ability to compute this type of compound
# expression element by element, without the need to allocate full intermediate arrays.
# The Numexpr documentation has more details, but for the time being it is sufficient
# to say that the library accepts a string giving the NumPy-style expression you’d like to
# compute:
# 
# 
#                                                 High-Performance Pandas: eval() and query()   |   209
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "High-Performance Pandas: eval() and query()",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HighPerformancePandas(HierNode):
    def __init__(self):
        super().__init__("High-Performance Pandas: eval() and query()")
        self.add(Content())
        self.add(A_Motivatingquery())
        self.add(B_pandasevalfor())
        self.add(C_DataFrameevalfor())
        self.add(D_DataFramequeryMethod())
        self.add(E_PerformanceWhen())

# eof
