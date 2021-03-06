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
# If you already have a Python installation set up, you can use pip to install all of these
# packages:
#     $ pip install numpy scipy matplotlib ipython scikit-learn pandas
# 
# 
# Essential Libraries and Tools
# Understanding what scikit-learn is and how to use it is important, but there are a
# few other libraries that will enhance your experience. scikit-learn is built on top of
# the NumPy and SciPy scientific Python libraries. In addition to NumPy and SciPy, we
# will be using pandas and matplotlib. We will also introduce the Jupyter Notebook,
# which is a browser-based interactive programming environment. Briefly, here is what
# you should know about these tools in order to get the most out of scikit-learn.1
# 
# Jupyter Notebook
# The Jupyter Notebook is an interactive environment for running code in the browser.
# It is a great tool for exploratory data analysis and is widely used by data scientists.
# While the Jupyter Notebook supports many programming languages, we only need
# the Python support. The Jupyter Notebook makes it easy to incorporate code, text,
# and images, and all of this book was in fact written as a Jupyter Notebook. All of the
# code examples we include can be downloaded from GitHub.
# 
# NumPy
# NumPy is one of the fundamental packages for scientific computing in Python. It
# contains functionality for multidimensional arrays, high-level mathematical func‐
# tions such as linear algebra operations and the Fourier transform, and pseudorandom
# number generators.
# In scikit-learn, the NumPy array is the fundamental data structure. scikit-learn
# takes in data in the form of NumPy arrays. Any data you’re using will have to be con‐
# verted to a NumPy array. The core functionality of NumPy is the ndarray class, a
# multidimensional (n-dimensional) array. All elements of the array must be of the
# same type. A NumPy array looks like this:
# In[2]:
#     import numpy as np
# 
#     x = np.array([[1, 2, 3], [4, 5, 6]])
#     print("x:\n{}".format(x))
# 
# 
# 
# 1 If you are unfamiliar with NumPy or matplotlib, we recommend reading the first chapter of the SciPy Lec‐
#   ture Notes.
# 
# 
# 
#                                                                             Essential Libraries and Tools   |   7
# 
# Out[2]:
#         x:
#         [[1 2 3]
#          [4 5 6]]
# We will be using NumPy a lot in this book, and we will refer to objects of the NumPy
# ndarray class as “NumPy arrays” or just “arrays.”
# 
# SciPy
# SciPy is a collection of functions for scientific computing in Python. It provides,
# among other functionality, advanced linear algebra routines, mathematical function
# optimization, signal processing, special mathematical functions, and statistical distri‐
# butions. scikit-learn draws from SciPy’s collection of functions for implementing
# its algorithms. The most important part of SciPy for us is scipy.sparse: this provides
# sparse matrices, which are another representation that is used for data in scikit-
# learn. Sparse matrices are used whenever we want to store a 2D array that contains
# mostly zeros:
# In[3]:
#         from scipy import sparse
# 
#         # Create a 2D NumPy array with a diagonal of ones, and zeros everywhere else
#         eye = np.eye(4)
#         print("NumPy array:\n{}".format(eye))
# 
# Out[3]:
#         NumPy array:
#         [[ 1. 0. 0.         0.]
#          [ 0. 1. 0.         0.]
#          [ 0. 0. 1.         0.]
#          [ 0. 0. 0.         1.]]
# 
# In[4]:
#         # Convert the NumPy array to a SciPy sparse matrix in CSR format
#         # Only the nonzero entries are stored
#         sparse_matrix = sparse.csr_matrix(eye)
#         print("\nSciPy sparse CSR matrix:\n{}".format(sparse_matrix))
# 
# Out[4]:
#         SciPy   sparse CSR matrix:
#           (0,   0)    1.0
#           (1,   1)    1.0
#           (2,   2)    1.0
#           (3,   3)    1.0
# 
# 
# 
# 
# 8   |    Chapter 1: Introduction
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "NumPy",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NumPy(HierNode):
    def __init__(self):
        super().__init__("NumPy")
        self.add(Content(), "content")

# eof
