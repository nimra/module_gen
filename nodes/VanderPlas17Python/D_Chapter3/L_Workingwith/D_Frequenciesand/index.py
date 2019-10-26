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
# Frequencies and Offsets
# Fundamental to these Pandas time series tools is the concept of a frequency or date
# offset. Just as we saw the D (day) and H (hour) codes previously, we can use such codes
# to specify any desired frequency spacing. Table 3-7 summarizes the main codes
# available.
# 
# Table 3-7. Listing of Pandas frequency codes
# Code Description Code Description
# D    Calendar day B   Business day
# W     Weekly
# M     Month end       BM       Business month end
# Q     Quarter end     BQ       Business quarter end
# A     Year end        BA       Business year end
# H     Hours           BH       Business hours
# T     Minutes
# S     Seconds
# L     Milliseonds
# U     Microseconds
# N     Nanoseconds
# 
# The monthly, quarterly, and annual frequencies are all marked at the end of the speci‐
# fied period. Adding an S suffix to any of these marks it instead at the beginning
# (Table 3-8).
# 
# Table 3-8. Listing of start-indexed frequency codes
# Code Description
# MS   Month start
# BMS   Business month start
# QS    Quarter start
# BQS   Business quarter start
# AS    Year start
# BAS   Business year start
# 
# 
# 
# 
#                                                              Working with Time Series   |   195
# 
# Additionally, you can change the month used to mark any quarterly or annual code
# by adding a three-letter month code as a suffix:
# 
#   • Q-JAN, BQ-FEB, QS-MAR, BQS-APR, etc.
#   • A-JAN, BA-FEB, AS-MAR, BAS-APR, etc.
# 
# In the same way, you can modify the split-point of the weekly frequency by adding a
# three-letter weekday code:
# 
#   • W-SUN, W-MON, W-TUE, W-WED, etc.
# 
# On top of this, codes can be combined with numbers to specify other frequencies. For
# example, for a frequency of 2 hours 30 minutes, we can combine the hour (H) and
# minute (T) codes as follows:
#       In[23]: pd.timedelta_range(0, periods=9, freq="2H30T")
#       Out[23]:
#       TimedeltaIndex(['00:00:00', '02:30:00', '05:00:00', '07:30:00', '10:00:00',
#                       '12:30:00', '15:00:00', '17:30:00', '20:00:00'],
#                      dtype='timedelta64[ns]', freq='150T')
# All of these short codes refer to specific instances of Pandas time series offsets, which
# can be found in the pd.tseries.offsets module. For example, we can create a busi‐
# ness day offset directly as follows:
#       In[24]: from pandas.tseries.offsets import BDay
#               pd.date_range('2015-07-01', periods=5, freq=BDay())
#       Out[24]: DatetimeIndex(['2015-07-01', '2015-07-02', '2015-07-03', '2015-07-06',
#                               '2015-07-07'],
#                              dtype='datetime64[ns]', freq='B')
# For more discussion of the use of frequencies and offsets, see the “DateOffset objects”
# section of the Pandas online documentation.
# 
# Resampling, Shifting, and Windowing
# The ability to use dates and times as indices to intuitively organize and access data is
# an important piece of the Pandas time series tools. The benefits of indexed data in
# general (automatic alignment during operations, intuitive data slicing and access,
# etc.) still apply, and Pandas provides several additional time series–specific
# operations.
# We will take a look at a few of those here, using some stock price data as an example.
# Because Pandas was developed largely in a finance context, it includes some very spe‐
# cific tools for financial data. For example, the accompanying pandas-datareader
# package (installable via conda install pandas-datareader) knows how to import
# 
# 
# 196   |   Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Frequencies and Offsets",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Frequenciesand(HierNode):
    def __init__(self):
        super().__init__("Frequencies and Offsets")
        self.add(Content())

# eof
