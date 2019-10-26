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
#      In[41]: # column vector via reshape
#              x.reshape((3, 1))
#      Out[41]: array([[1],
#                      [2],
#                      [3]])
#      In[42]: # column vector via newaxis
#              x[:, np.newaxis]
#      Out[42]: array([[1],
#                      [2],
#                      [3]])
# We will see this type of transformation often throughout the remainder of the book.
# 
# Array Concatenation and Splitting
# All of the preceding routines worked on single arrays. It’s also possible to combine
# multiple arrays into one, and to conversely split a single array into multiple arrays.
# We’ll take a look at those operations here.
# 
# Concatenation of arrays
# Concatenation, or joining of two arrays in NumPy, is primarily accomplished
# through the routines np.concatenate, np.vstack, and np.hstack. np.concatenate
# takes a tuple or list of arrays as its first argument, as we can see here:
#      In[43]: x = np.array([1, 2, 3])
#              y = np.array([3, 2, 1])
#              np.concatenate([x, y])
#      Out[43]: array([1, 2, 3, 3, 2, 1])
# You can also concatenate more than two arrays at once:
#      In[44]: z = [99, 99, 99]
#              print(np.concatenate([x, y, z]))
#      [ 1   2   3   3   2   1 99 99 99]
# 
# np.concatenate can also be used for two-dimensional arrays:
#      In[45]: grid = np.array([[1, 2, 3],
#                               [4, 5, 6]])
#      In[46]: # concatenate along the first axis
#              np.concatenate([grid, grid])
#      Out[46]: array([[1,       2,   3],
#                      [4,       5,   6],
#                      [1,       2,   3],
#                      [4,       5,   6]])
#      In[47]: # concatenate along the second axis (zero-indexed)
#              np.concatenate([grid, grid], axis=1)
# 
# 
# 48   | Chapter 2: Introduction to NumPy
# 
#     Out[47]: array([[1, 2, 3, 1, 2, 3],
#                     [4, 5, 6, 4, 5, 6]])
# 
# For working with arrays of mixed dimensions, it can be clearer to use the np.vstack
# (vertical stack) and np.hstack (horizontal stack) functions:
#     In[48]: x = np.array([1, 2, 3])
#             grid = np.array([[9, 8, 7],
#                              [6, 5, 4]])
# 
#               # vertically stack the arrays
#               np.vstack([x, grid])
#     Out[48]: array([[1, 2, 3],
#                     [9, 8, 7],
#                     [6, 5, 4]])
#     In[49]: # horizontally stack the arrays
#             y = np.array([[99],
#                           [99]])
#             np.hstack([grid, y])
#     Out[49]: array([[ 9,    8,   7, 99],
#                     [ 6,    5,   4, 99]])
# 
# Similarly, np.dstack will stack arrays along the third axis.
# 
# Splitting of arrays
# The opposite of concatenation is splitting, which is implemented by the functions
# np.split, np.hsplit, and np.vsplit. For each of these, we can pass a list of indices
# giving the split points:
#     In[50]: x = [1, 2, 3, 99, 99, 3, 2, 1]
#             x1, x2, x3 = np.split(x, [3, 5])
#             print(x1, x2, x3)
#     [1 2 3] [99 99] [3 2 1]
# 
# Notice that N split points lead to N + 1 subarrays. The related functions np.hsplit
# and np.vsplit are similar:
#     In[51]: grid = np.arange(16).reshape((4, 4))
#             grid
#     Out[51]: array([[ 0, 1, 2, 3],
#                     [ 4, 5, 6, 7],
#                     [ 8, 9, 10, 11],
#                     [12, 13, 14, 15]])
#     In[52]: upper, lower = np.vsplit(grid, [2])
#             print(upper)
#             print(lower)
#     [[0 1 2 3]
#      [4 5 6 7]]
# 
# 
#                                                                The Basics of NumPy Arrays   |   49
# 
#      [[ 8 9 10 11]
#       [12 13 14 15]]
#      In[53]: left, right = np.hsplit(grid, [2])
#              print(left)
#              print(right)
#      [[ 0 1]
#       [ 4 5]
#       [ 8 9]
#       [12 13]]
#      [[ 2 3]
#       [ 6 7]
#       [10 11]
#       [14 15]]
# 
# Similarly, np.dsplit will split arrays along the third axis.
# 
# Computation on NumPy Arrays: Universal Functions
# Up until now, we have been discussing some of the basic nuts and bolts of NumPy; in
# the next few sections, we will dive into the reasons that NumPy is so important in the
# Python data science world. Namely, it provides an easy and flexible interface to opti‐
# mized computation with arrays of data.
# Computation on NumPy arrays can be very fast, or it can be very slow. The key to
# making it fast is to use vectorized operations, generally implemented through Num‐
# Py’s universal functions (ufuncs). This section motivates the need for NumPy’s ufuncs,
# which can be used to make repeated calculations on array elements much more effi‐
# cient. It then introduces many of the most common and useful arithmetic ufuncs
# available in the NumPy package.
# 
# The Slowness of Loops
# Python’s default implementation (known as CPython) does some operations very
# slowly. This is in part due to the dynamic, interpreted nature of the language: the fact
# that types are flexible, so that sequences of operations cannot be compiled down to
# efficient machine code as in languages like C and Fortran. Recently there have been
# various attempts to address this weakness: well-known examples are the PyPy project,
# a just-in-time compiled implementation of Python; the Cython project, which con‐
# verts Python code to compilable C code; and the Numba project, which converts
# snippets of Python code to fast LLVM bytecode. Each of these has its strengths and
# weaknesses, but it is safe to say that none of the three approaches has yet surpassed
# the reach and popularity of the standard CPython engine.
# The relative sluggishness of Python generally manifests itself in situations where
# many small operations are being repeated—for instance, looping over arrays to oper‐
# 
# 
# 
# 50   |   Chapter 2: Introduction to NumPy
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Array Concatenation and Splitting",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ArrayConcatenation(HierNode):
    def __init__(self):
        super().__init__("Array Concatenation and Splitting")
        self.add(Content())

# eof