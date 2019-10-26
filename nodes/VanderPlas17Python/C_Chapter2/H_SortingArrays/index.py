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

from .A_FastSorting.index import FastSorting as A_FastSorting
from .B_PartialSorts.index import PartialSorts as B_PartialSorts
from .C_ExamplekNearest.index import ExamplekNearest as C_ExamplekNearest

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#             print("Custom routine:")
#             %timeit np.add.at(counts, np.searchsorted(bins, x), 1)
#     NumPy routine:
#     10000 loops, best of 3: 97.6 µs per loop
#     Custom routine:
#     10000 loops, best of 3: 19.5 µs per loop
# Our own one-line algorithm is several times faster than the optimized algorithm in
# NumPy! How can this be? If you dig into the np.histogram source code (you can do
# this in IPython by typing np.histogram??), you’ll see that it’s quite a bit more
# involved than the simple search-and-count that we’ve done; this is because NumPy’s
# algorithm is more flexible, and particularly is designed for better performance when
# the number of data points becomes large:
#     In[26]: x = np.random.randn(1000000)
#             print("NumPy routine:")
#             %timeit counts, edges = np.histogram(x, bins)
# 
#             print("Custom routine:")
#             %timeit np.add.at(counts, np.searchsorted(bins, x), 1)
#     NumPy routine:
#     10 loops, best of 3: 68.7 ms per loop
#     Custom routine:
#     10 loops, best of 3: 135 ms per loop
# What this comparison shows is that algorithmic efficiency is almost never a simple
# question. An algorithm efficient for large datasets will not always be the best choice
# for small datasets, and vice versa (see “Big-O Notation” on page 92). But the advan‐
# tage of coding this algorithm yourself is that with an understanding of these basic
# methods, you could use these building blocks to extend this to do some very interest‐
# ing custom behaviors. The key to efficiently using Python in data-intensive applica‐
# tions is knowing about general convenience routines like np.histogram and when
# they’re appropriate, but also knowing how to make use of lower-level functionality
# when you need more pointed behavior.
# 
# Sorting Arrays
# Up to this point we have been concerned mainly with tools to access and operate on
# array data with NumPy. This section covers algorithms related to sorting values in
# NumPy arrays. These algorithms are a favorite topic in introductory computer sci‐
# ence courses: if you’ve ever taken one, you probably have had dreams (or, depending
# on your temperament, nightmares) about insertion sorts, selection sorts, merge sorts,
# quick sorts, bubble sorts, and many, many more. All are means of accomplishing a
# similar task: sorting the values in a list or array.
# 
# 
# 
# 
#                                                                      Sorting Arrays   |   85
# 
# For example, a simple selection sort repeatedly finds the minimum value from a list,
# and makes swaps until the list is sorted. We can code this in just a few lines of Python:
#      In[1]: import numpy as np
# 
#                def selection_sort(x):
#                    for i in range(len(x)):
#                        swap = i + np.argmin(x[i:])
#                        (x[i], x[swap]) = (x[swap], x[i])
#                    return x
#      In[2]: x = np.array([2, 1, 4, 3, 5])
#             selection_sort(x)
#      Out[2]: array([1, 2, 3, 4, 5])
# As any first-year computer science major will tell you, the selection sort is useful for
# its simplicity, but is much too slow to be useful for larger arrays. For a list of N values,
# it requires N loops, each of which does on the order of ~ N comparisons to find the
# swap value. In terms of the “big-O” notation often used to characterize these algo‐
# rithms (see “Big-O Notation” on page 92), selection sort averages � N 2 : if you dou‐
# ble the number of items in the list, the execution time will go up by about a factor of
# four.
# Even selection sort, though, is much better than my all-time favorite sorting algo‐
# rithms, the bogosort:
#      In[3]: def bogosort(x):
#                 while np.any(x[:-1] > x[1:]):
#                     np.random.shuffle(x)
#                 return x
#      In[4]: x = np.array([2, 1, 4, 3, 5])
#             bogosort(x)
#      Out[4]: array([1, 2, 3, 4, 5])
# This silly sorting method relies on pure chance: it repeatedly applies a random shuf‐
# fling of the array until the result happens to be sorted. With an average scaling of
# � N × N ! (that’s N times N factorial), this should—quite obviously—never be used
# for any real computation.
# Fortunately, Python contains built-in sorting algorithms that are much more efficient
# than either of the simplistic algorithms just shown. We’ll start by looking at the
# Python built-ins, and then take a look at the routines included in NumPy and opti‐
# mized for NumPy arrays.
# 
# Fast Sorting in NumPy: np.sort and np.argsort
# Although Python has built-in sort and sorted functions to work with lists, we won’t
# discuss them here because NumPy’s np.sort function turns out to be much more
# 
# 
# 86   |   Chapter 2: Introduction to NumPy
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Sorting Arrays",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SortingArrays(HierNode):
    def __init__(self):
        super().__init__("Sorting Arrays")
        self.add(Content())
        self.add(A_FastSorting())
        self.add(B_PartialSorts())
        self.add(C_ExamplekNearest())

# eof
