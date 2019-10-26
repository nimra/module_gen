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

from .A_JupyterNotebook.index import JupyterNotebook as A_JupyterNotebook
from .B_NumPy.index import NumPy as B_NumPy
from .C_SciPy.index import SciPy as C_SciPy
from .D_matplotlib.index import matplotlib as D_matplotlib
from .E_pandas.index import pandas as E_pandas
from .F_mglearn.index import mglearn as F_mglearn

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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Essential Libraries and Tools",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class EssentialLibraries(HierNode):
    def __init__(self):
        super().__init__("Essential Libraries and Tools")
        self.add(Content(), "content")
        self.add(A_JupyterNotebook())
        self.add(B_NumPy())
        self.add(C_SciPy())
        self.add(D_matplotlib())
        self.add(E_pandas())
        self.add(F_mglearn())

# eof
