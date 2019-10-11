# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                                      Chapter 9   Python
# 
# import numpy as np
# 
# np.abs(-10)   # the absolute value of -10
# 'Output': 10
# 
# 
# from Statement
# The from statement allows you to import a specific feature from a module into your
# source file. The syntax is as follows:
# 
# from module_name import module_feature [as user_defined_name][,...]
# 
#    Let’s see an example:
# 
# from numpy import mean
# 
# mean([2,4,6,8])
# 'Output': 5.0
# 
#    This chapter provides the fundamentals for programming with Python.
# Programming is a very active endeavor, and competency is gained by experience and
# repetition. What is presented in this chapter provides just enough to be dangerous.
#    In the next chapter, we’ll introduce NumPy, a Python package for numerical
# computing.
# 
# 
# 
# 
#                                                                                       89
# 
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
# 
# 
# 
# NumPy 1-D Array
# Let’s create a simple 1-D NumPy array:
# 
# my_array = np.array([2,4,6,8,10])
# my_array
# 'Output': array([ 2,  4,  6,  8, 10])
# # the data-type of a NumPy array is the ndarray
# type(my_array)
# 'Output': numpy.ndarray
# 
# 
#                                                                                           91
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_10
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("from Statement")
        self.add(MarkdownBlock("# from Statement"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class fromStatement(HierNode):
    def __init__(self):
        super().__init__("from Statement")
        self.add(Content())

# eof
