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
#       In[42]: pop_flat.set_index(['state', 'year'])
#       Out[42]:                             population
#                  state      year
#                  California 2000             33871648
#                             2010             37253956
#                  New York   2000             18976457
#                             2010             19378102
#                  Texas      2000             20851820
#                             2010             25145561
# In practice, I find this type of reindexing to be one of the more useful patterns when I
# encounter real-world datasets.
# 
# Data Aggregations on Multi-Indices
# We’ve previously seen that Pandas has built-in data aggregation methods, such as
# mean(), sum(), and max(). For hierarchically indexed data, these can be passed a
# level parameter that controls which subset of the data the aggregate is computed on.
# For example, let’s return to our health data:
#       In[43]: health_data
#       Out[43]:     subject           Bob             Guido            Sue
#                    type               HR    Temp        HR   Temp      HR    Temp
#                    year visit
#                    2013 1          31.0 38.7 32.0 36.7 35.0 37.2
#                         2          44.0 37.7 50.0 35.0 29.0 36.7
#                    2014 1          30.0 37.4 39.0 37.8 61.0 36.9
#                         2          47.0 37.8 48.0 37.3 51.0 36.5
# Perhaps we’d like to average out the measurements in the two visits each year. We can
# do this by naming the index level we’d like to explore, in this case the year:
#       In[44]: data_mean = health_data.mean(level='year')
#               data_mean
#       Out[44]: subject         Bob           Guido                  Sue
#                type             HR    Temp      HR       Temp        HR     Temp
#                year
#                2013          37.5     38.2    41.0      35.85   32.0      36.95
#                2014          38.5     37.6    43.5      37.55   56.0      36.70
# 
# By further making use of the axis keyword, we can take the mean among levels on
# the columns as well:
#       In[45]: data_mean.mean(axis=1, level='type')
#       Out[45]: type        HR      Temp
#                year
#                2013 36.833333 37.000000
#                2014 46.000000 37.283333
# 
# 
# 
# 
# 140   |   Chapter 3: Data Manipulation with Pandas
# 
# Thus in two lines, we’ve been able to find the average heart rate and temperature
# measured among all subjects in all visits each year. This syntax is actually a shortcut
# to the GroupBy functionality, which we will discuss in “Aggregation and Grouping” on
# page 158. While this is a toy example, many real-world datasets have similar hierarch‐
# ical structure.
# 
# 
#                                       Panel Data
#  Pandas has a few other fundamental data structures that we have not yet discussed,
#  namely the pd.Panel and pd.Panel4D objects. These can be thought of, respectively,
#  as three-dimensional and four-dimensional generalizations of the (one-dimensional)
#  Series and (two-dimensional) DataFrame structures. Once you are familiar with
#  indexing and manipulation of data in a Series and DataFrame, Panel and Panel4D
#  are relatively straightforward to use. In particular, the ix, loc, and iloc indexers dis‐
#  cussed in “Data Indexing and Selection” on page 107 extend readily to these higher-
#  dimensional structures.
#  We won’t cover these panel structures further in this text, as I’ve found in the majority
#  of cases that multi-indexing is a more useful and conceptually simpler representation
#  for higher-dimensional data. Additionally, panel data is fundamentally a dense data
#  representation, while multi-indexing is fundamentally a sparse data representation.
#  As the number of dimensions increases, the dense representation can become very
#  inefficient for the majority of real-world datasets. For the occasional specialized appli‐
#  cation, however, these structures can be useful. If you’d like to read more about the
#  Panel and Panel4D structures, see the references listed in “Further Resources” on
#  page 215.
# 
# 
# 
# Combining Datasets: Concat and Append
# Some of the most interesting studies of data come from combining different data
# sources. These operations can involve anything from very straightforward concatena‐
# tion of two different datasets, to more complicated database-style joins and merges
# that correctly handle any overlaps between the datasets. Series and DataFrames are
# built with this type of operation in mind, and Pandas includes functions and methods
# that make this sort of data wrangling fast and straightforward.
# Here we’ll take a look at simple concatenation of Series and DataFrames with the
# pd.concat function; later we’ll dive into more sophisticated in-memory merges and
# joins implemented in Pandas.
# We begin with the standard imports:
#     In[1]: import pandas as pd
#            import numpy as np
# 
# 
# 
#                                                      Combining Datasets: Concat and Append   |   141
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Data Aggregations on Multi-Indices",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataAggregations(HierNode):
    def __init__(self):
        super().__init__("Data Aggregations on Multi-Indices")
        self.add(Content())

# eof
