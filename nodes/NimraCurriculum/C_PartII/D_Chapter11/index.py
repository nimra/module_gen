# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_PandasData.index import PandasData as A_PandasData
from .B_DataIndexing.index import DataIndexing as B_DataIndexing
from .C_DataFrameManipulation.index import DataFrameManipulation as C_DataFrameManipulation
from .D_HandlingMissing.index import HandlingMissing as D_HandlingMissing
from .E_DataAggregation.index import DataAggregation as E_DataAggregation
from .F_StatisticalSummaries.index import StatisticalSummaries as F_StatisticalSummaries
from .G_ImportingData.index import ImportingData as G_ImportingData
from .H_Timeserieswith.index import Timeserieswith as H_Timeserieswith

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
        super().__init__("Chapter 11: Pandas")
        self.add(MarkdownBlock("# Chapter 11: Pandas"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter11(HierNode):
    def __init__(self):
        super().__init__("Chapter 11: Pandas")
        self.add(Content())
        self.add(A_PandasData())
        self.add(B_DataIndexing())
        self.add(C_DataFrameManipulation())
        self.add(D_HandlingMissing())
        self.add(E_DataAggregation())
        self.add(F_StatisticalSummaries())
        self.add(G_ImportingData())
        self.add(H_Timeserieswith())

# eof
