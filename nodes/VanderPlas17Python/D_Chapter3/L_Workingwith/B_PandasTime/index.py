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
#       Out[11]: DatetimeIndex(['2015-07-04', '2015-07-05', '2015-07-06', '2015-07-07',
#                               '2015-07-08', '2015-07-09', '2015-07-10', '2015-07-11',
#                               '2015-07-12', '2015-07-13', '2015-07-14', '2015-07-15'],
#                              dtype='datetime64[ns]', freq=None)
# In the next section, we will take a closer look at manipulating time series data with
# the tools provided by Pandas.
# 
# Pandas Time Series: Indexing by Time
# Where the Pandas time series tools really become useful is when you begin to index
# data by timestamps. For example, we can construct a Series object that has time-
# indexed data:
#       In[12]: index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
#                                         '2015-07-04', '2015-08-04'])
#               data = pd.Series([0, 1, 2, 3], index=index)
#               data
#       Out[12]: 2014-07-04           0
#                2014-08-04           1
#                2015-07-04           2
#                2015-08-04           3
#                dtype: int64
# 
# Now that we have this data in a Series, we can make use of any of the Series index‐
# ing patterns we discussed in previous sections, passing values that can be coerced into
# dates:
#       In[13]: data['2014-07-04':'2015-07-04']
#       Out[13]: 2014-07-04   0
#                2014-08-04   1
#                2015-07-04   2
#                dtype: int64
# There are additional special date-only indexing operations, such as passing a year to
# obtain a slice of all data from that year:
#       In[14]: data['2015']
#       Out[14]: 2015-07-04           2
#                2015-08-04           3
#                dtype: int64
# Later, we will see additional examples of the convenience of dates-as-indices. But first,
# let’s take a closer look at the available time series data structures.
# 
# Pandas Time Series Data Structures
# This section will introduce the fundamental Pandas data structures for working with
# time series data:
# 
# 
# 192   |   Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Pandas Time Series: Indexing by Time",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PandasTime(HierNode):
    def __init__(self):
        super().__init__("Pandas Time Series: Indexing by Time")
        self.add(Content())

# eof
