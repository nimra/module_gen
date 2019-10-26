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
# Figure 2-3. Histogram of presidential heights
# 
# These aggregates are some of the fundamental pieces of exploratory data analysis that
# we’ll explore in more depth in later chapters of the book.
# 
# Computation on Arrays: Broadcasting
# We saw in the previous section how NumPy’s universal functions can be used to vec‐
# torize operations and thereby remove slow Python loops. Another means of vectoriz‐
# ing operations is to use NumPy’s broadcasting functionality. Broadcasting is simply a
# set of rules for applying binary ufuncs (addition, subtraction, multiplication, etc.) on
# arrays of different sizes.
# 
# Introducing Broadcasting
# Recall that for arrays of the same size, binary operations are performed on an
# element-by-element basis:
#     In[1]: import numpy as np
#     In[2]: a = np.array([0, 1, 2])
#            b = np.array([5, 5, 5])
#            a + b
#     Out[2]: array([5, 6, 7])
# Broadcasting allows these types of binary operations to be performed on arrays of dif‐
# ferent sizes—for example, we can just as easily add a scalar (think of it as a zero-
# dimensional array) to an array:
# 
# 
# 
# 
#                                                       Computation on Arrays: Broadcasting   |   63
# 
#      In[3]: a + 5
#      Out[3]: array([5, 6, 7])
# 
# We can think of this as an operation that stretches or duplicates the value 5 into the
# array [5, 5, 5], and adds the results. The advantage of NumPy’s broadcasting is that
# this duplication of values does not actually take place, but it is a useful mental model
# as we think about broadcasting.
# We can similarly extend this to arrays of higher dimension. Observe the result when
# we add a one-dimensional array to a two-dimensional array:
#      In[4]: M = np.ones((3, 3))
#             M
#      Out[4]: array([[ 1., 1., 1.],
#                     [ 1., 1., 1.],
#                     [ 1., 1., 1.]])
#      In[5]: M + a
#      Out[5]: array([[ 1.,         2.,     3.],
#                     [ 1.,         2.,     3.],
#                     [ 1.,         2.,     3.]])
# 
# Here the one-dimensional array a is stretched, or broadcast, across the second
# dimension in order to match the shape of M.
# While these examples are relatively easy to understand, more complicated cases can
# involve broadcasting of both arrays. Consider the following example:
#      In[6]: a = np.arange(3)
#             b = np.arange(3)[:, np.newaxis]
# 
#               print(a)
#               print(b)
#      [0 1 2]
#      [[0]
#       [1]
#       [2]]
#      In[7]: a + b
#      Out[7]: array([[0, 1, 2],
#                     [1, 2, 3],
#                     [2, 3, 4]])
# 
# 
# 
# 
# 64   | Chapter 2: Introduction to NumPy
# 
# Just as before we stretched or broadcasted one value to match the shape of the other,
# here we’ve stretched both a and b to match a common shape, and the result is a two-
# dimensional array! The geometry of these examples is visualized in Figure 2-4.1
# 
# 
# 
# 
# Figure 2-4. Visualization of NumPy broadcasting
# 
# The light boxes represent the broadcasted values: again, this extra memory is not
# actually allocated in the course of the operation, but it can be useful conceptually to
# imagine that it is.
# 
# Rules of Broadcasting
# Broadcasting in NumPy follows a strict set of rules to determine the interaction
# between the two arrays:
# 
#   • Rule 1: If the two arrays differ in their number of dimensions, the shape of the
#     one with fewer dimensions is padded with ones on its leading (left) side.
#   • Rule 2: If the shape of the two arrays does not match in any dimension, the array
#     with shape equal to 1 in that dimension is stretched to match the other shape.
#   • Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is
#     raised.
# 
# 
# 
# 
# 1 Code to produce this plot can be found in the online appendix, and is adapted from source published in the
#   astroML documentation. Used with permission.
# 
# 
# 
#                                                                     Computation on Arrays: Broadcasting   |    65
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Introducing Broadcasting",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IntroducingBroadcasting(HierNode):
    def __init__(self):
        super().__init__("Introducing Broadcasting")
        self.add(Content())

# eof