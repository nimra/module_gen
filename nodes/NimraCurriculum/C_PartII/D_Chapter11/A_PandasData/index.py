# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Series.index import Series as A_Series
from .B_DataFrames.index import DataFrames as B_DataFrames

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 11
# 
# 
# 
# Pandas
# Pandas is a specialized Python library for data analysis, especially on humongous
# datasets. It boasts easy-to-use functionality for reading and writing data, dealing with
# missing data, reshaping the dataset, and massaging the data by slicing, indexing,
# inserting, and deleting data variables and records. Pandas also has an important
# groupBy functionality for aggregating data for defined conditions – useful for plotting
# and computing data summaries for exploration.
#      Another key strength of Pandas is in re-ordering and cleaning time series data
# for time series analysis. In short, Pandas is the go-to tool for data cleaning and data
# exploration.
#      To use Pandas, first import the Pandas module:
# 
# import pandas as pd
# 
# 
# 
# Pandas Data Structures
# Just like NumPy, Pandas can store and manipulate a multi-dimensional array of data. To
# handle this, Pandas has the Series and DataFrame data structures.
# 
# 
# S
#  eries
# The Series data structure is for storing a 1-D array (or vector) of data elements. A series
# data structure also provides labels to the data items in the form of an index. The user
# can specify this label via the index parameter in the Series function, but if the index
# parameter is left unspecified, a default label of 0 to one minus the size of the data
# elements is assigned.
# 
# 
# 
# 
#                                                                                           115
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_11
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Pandas Data Structures")
        self.add(MarkdownBlock("# Pandas Data Structures"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PandasData(HierNode):
    def __init__(self):
        super().__init__("Pandas Data Structures")
        self.add(Content())
        self.add(A_Series())
        self.add(B_DataFrames())

# eof
