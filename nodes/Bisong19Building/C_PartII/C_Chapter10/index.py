# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_NumPy1D.index import NumPy1D as A_NumPy1D
from .B_NumPyDatatypes.index import NumPyDatatypes as B_NumPyDatatypes
from .C_Indexing.index import Indexing as C_Indexing
from .D_BasicMath.index import BasicMath as D_BasicMath
from .E_HigherDimensionalArrays.index import HigherDimensionalArrays as E_HigherDimensionalArrays
from .F_MatrixOperations.index import MatrixOperations as F_MatrixOperations
from .G_Reshaping.index import Reshaping as G_Reshaping
from .H_Broadcasting.index import Broadcasting as H_Broadcasting
from .I_LoadingData.index import LoadingData as I_LoadingData

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 10
# 
# 
# 
# NumPy
# NumPy is a Python library optimized for numerical computing. It bears close semblance
# with MATLAB and is equally as powerful when used in conjunction with other packages
# such as SciPy for various scientific functions, Matplotlib for visualization, and Pandas for
# data analysis. NumPy is short for numerical python.
#     NumPy’s core strength lies in its ability to create and manipulate n-dimensional
# arrays. This is particularly critical for building machine learning and deep learning
# models. Data is often represented in a matrix-like grid of rows and columns, where each
# row represents an observation and each column a variable or feature. Hence, NumPy’s
# 2-D array is a natural fit for storing and manipulating datasets.
#     This tutorial will cover the basics of NumPy to get you very comfortable working with
# the package and also get you to appreciate the thinking behind how NumPy works. This
# understanding forms a foundation from which one can extend and seek solutions from
# the NumPy reference documentation when a specific functionality is needed.
#     To begin using NumPy, we’ll start by importing the NumPy module:
# 
# import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 10: NumPy",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 10: NumPy"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter10(HierNode):
    def __init__(self):
        super().__init__("Chapter 10: NumPy")
        self.add(Content())
        self.add(A_NumPy1D())
        self.add(B_NumPyDatatypes())
        self.add(C_Indexing())
        self.add(D_BasicMath())
        self.add(E_HigherDimensionalArrays())
        self.add(F_MatrixOperations())
        self.add(G_Reshaping())
        self.add(H_Broadcasting())
        self.add(I_LoadingData())

# eof
