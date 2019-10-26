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

from .A_NumPyArray.index import NumPyArray as A_NumPyArray
from .B_ArrayIndexing.index import ArrayIndexing as B_ArrayIndexing
from .C_ArraySlicing.index import ArraySlicing as C_ArraySlicing
from .D_Reshapingof.index import Reshapingof as D_Reshapingof
from .E_ArrayConcatenation.index import ArrayConcatenation as E_ArrayConcatenation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# The Basics of NumPy Arrays
# Data manipulation in Python is nearly synonymous with NumPy array manipulation:
# even newer tools like Pandas (Chapter 3) are built around the NumPy array. This sec‐
# tion will present several examples using NumPy array manipulation to access data
# and subarrays, and to split, reshape, and join the arrays. While the types of operations
# shown here may seem a bit dry and pedantic, they comprise the building blocks of
# many other examples used throughout the book. Get to know them well!
# We’ll cover a few categories of basic array manipulations here:
# Attributes of arrays
#     Determining the size, shape, memory consumption, and data types of arrays
# Indexing of arrays
#     Getting and setting the value of individual array elements
# Slicing of arrays
#      Getting and setting smaller subarrays within a larger array
# Reshaping of arrays
#     Changing the shape of a given array
# Joining and splitting of arrays
#      Combining multiple arrays into one, and splitting one array into many
# 
# NumPy Array Attributes
# First let’s discuss some useful array attributes. We’ll start by defining three random
# arrays: a one-dimensional, two-dimensional, and three-dimensional array. We’ll use
# NumPy’s random number generator, which we will seed with a set value in order to
# ensure that the same random arrays are generated each time this code is run:
#      In[1]: import numpy as np
#             np.random.seed(0) # seed for reproducibility
# 
#               x1 = np.random.randint(10, size=6) # One-dimensional array
#               x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
#               x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array
# 
# Each array has attributes ndim (the number of dimensions), shape (the size of each
# dimension), and size (the total size of the array):
#      In[2]: print("x3 ndim: ", x3.ndim)
#             print("x3 shape:", x3.shape)
#             print("x3 size: ", x3.size)
#      x3 ndim: 3
#      x3 shape: (3, 4, 5)
#      x3 size: 60
# 
# 
# 42   | Chapter 2: Introduction to NumPy
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Basics of NumPy Arrays",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheBasics(HierNode):
    def __init__(self):
        super().__init__("The Basics of NumPy Arrays")
        self.add(Content())
        self.add(A_NumPyArray())
        self.add(B_ArrayIndexing())
        self.add(C_ArraySlicing())
        self.add(D_Reshapingof())
        self.add(E_ArrayConcatenation())

# eof
