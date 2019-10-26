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
# Another useful attribute is the dtype, the data type of the array (which we discussed
# previously in “Understanding Data Types in Python” on page 34):
#     In[3]: print("dtype:", x3.dtype)
#     dtype: int64
# 
# Other attributes include itemsize, which lists the size (in bytes) of each array ele‐
# ment, and nbytes, which lists the total size (in bytes) of the array:
#     In[4]: print("itemsize:", x3.itemsize, "bytes")
#            print("nbytes:", x3.nbytes, "bytes")
#     itemsize: 8 bytes
#     nbytes: 480 bytes
# 
# In general, we expect that nbytes is equal to itemsize times size.
# 
# Array Indexing: Accessing Single Elements
# If you are familiar with Python’s standard list indexing, indexing in NumPy will feel
# quite familiar. In a one-dimensional array, you can access the ith value (counting from
# zero) by specifying the desired index in square brackets, just as with Python lists:
#     In[5]: x1
#     Out[5]: array([5, 0, 3, 3, 7, 9])
#     In[6]: x1[0]
#     Out[6]: 5
#     In[7]: x1[4]
#     Out[7]: 7
# To index from the end of the array, you can use negative indices:
#     In[8]: x1[-1]
#     Out[8]: 9
#     In[9]: x1[-2]
#     Out[9]: 7
# In a multidimensional array, you access items using a comma-separated tuple of
# indices:
#     In[10]: x2
#     Out[10]: array([[3, 5, 2, 4],
#                     [7, 6, 8, 8],
#                     [1, 6, 7, 7]])
#     In[11]: x2[0, 0]
#     Out[11]: 3
# 
# 
# 
#                                                             The Basics of NumPy Arrays   |   43
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "NumPy Array Attributes",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NumPyArray(HierNode):
    def __init__(self):
        super().__init__("NumPy Array Attributes")
        self.add(Content())

# eof
