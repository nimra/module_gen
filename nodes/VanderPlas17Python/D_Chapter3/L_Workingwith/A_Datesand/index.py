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
# Going further with recipes
# Hopefully this example has given you a bit of a flavor (ba-dum!) for the types of data
# cleaning operations that are efficiently enabled by Pandas string methods. Of course,
# building a very robust recipe recommendation system would require a lot more
# work! Extracting full ingredient lists from each recipe would be an important piece of
# the task; unfortunately, the wide variety of formats used makes this a relatively time-
# consuming process. This points to the truism that in data science, cleaning and
# munging of real-world data often comprises the majority of the work, and Pandas
# provides the tools that can help you do this efficiently.
# 
# Working with Time Series
# Pandas was developed in the context of financial modeling, so as you might expect, it
# contains a fairly extensive set of tools for working with dates, times, and time-
# indexed data. Date and time data comes in a few flavors, which we will discuss here:
# 
#   • Time stamps reference particular moments in time (e.g., July 4th, 2015, at 7:00
#     a.m.).
#   • Time intervals and periods reference a length of time between a particular begin‐
#     ning and end point—for example, the year 2015. Periods usually reference a spe‐
#     cial case of time intervals in which each interval is of uniform length and does
#     not overlap (e.g., 24 hour-long periods constituting days).
#   • Time deltas or durations reference an exact length of time (e.g., a duration of
#     22.56 seconds).
# 
# In this section, we will introduce how to work with each of these types of date/time
# data in Pandas. This short section is by no means a complete guide to the time series
# tools available in Python or Pandas, but instead is intended as a broad overview of
# how you as a user should approach working with time series. We will start with a
# brief discussion of tools for dealing with dates and times in Python, before moving
# more specifically to a discussion of the tools provided by Pandas. After listing some
# resources that go into more depth, we will review some short examples of working
# with time series data in Pandas.
# 
# Dates and Times in Python
# The Python world has a number of available representations of dates, times, deltas,
# and timespans. While the time series tools provided by Pandas tend to be the most
# useful for data science applications, it is helpful to see their relationship to other
# packages used in Python.
# 
# 
# 
# 
# 188   |   Chapter 3: Data Manipulation with Pandas
# 
# Native Python dates and times: datetime and dateutil
# Python’s basic objects for working with dates and times reside in the built-in date
# time module. Along with the third-party dateutil module, you can use it to quickly
# perform a host of useful functionalities on dates and times. For example, you can
# manually build a date using the datetime type:
#     In[1]: from datetime import datetime
#            datetime(year=2015, month=7, day=4)
#     Out[1]: datetime.datetime(2015, 7, 4, 0, 0)
# 
# Or, using the dateutil module, you can parse dates from a variety of string formats:
#     In[2]: from dateutil import parser
#            date = parser.parse("4th of July, 2015")
#            date
#     Out[2]: datetime.datetime(2015, 7, 4, 0, 0)
# 
# Once you have a datetime object, you can do things like printing the day of the week:
#     In[3]: date.strftime('%A')
#     Out[3]: 'Saturday'
# In the final line, we’ve used one of the standard string format codes for printing dates
# ("%A"), which you can read about in the strftime section of Python’s datetime docu‐
# mentation. Documentation of other useful date utilities can be found in dateutil’s
# online documentation. A related package to be aware of is pytz, which contains tools
# for working with the most migraine-inducing piece of time series data: time zones.
# The power of datetime and dateutil lies in their flexibility and easy syntax: you can
# use these objects and their built-in methods to easily perform nearly any operation
# you might be interested in. Where they break down is when you wish to work with
# large arrays of dates and times: just as lists of Python numerical variables are subopti‐
# mal compared to NumPy-style typed numerical arrays, lists of Python datetime
# objects are suboptimal compared to typed arrays of encoded dates.
# 
# Typed arrays of times: NumPy’s datetime64
# The weaknesses of Python’s datetime format inspired the NumPy team to add a set of
# native time series data type to NumPy. The datetime64 dtype encodes dates as 64-bit
# integers, and thus allows arrays of dates to be represented very compactly. The date
# time64 requires a very specific input format:
#     In[4]: import numpy as np
#            date = np.array('2015-07-04', dtype=np.datetime64)
#            date
#     Out[4]: array(datetime.date(2015, 7, 4), dtype='datetime64[D]')
# 
# 
# 
# 
#                                                               Working with Time Series   |   189
# 
# Once we have this date formatted, however, we can quickly do vectorized operations
# on it:
#       In[5]: date + np.arange(12)
#       Out[5]:
#       array(['2015-07-04', '2015-07-05', '2015-07-06', '2015-07-07',
#               '2015-07-08', '2015-07-09', '2015-07-10', '2015-07-11',
#               '2015-07-12', '2015-07-13', '2015-07-14', '2015-07-15'],
#               dtype='datetime64[D]')
# 
# Because of the uniform type in NumPy datetime64 arrays, this type of operation can
# be accomplished much more quickly than if we were working directly with Python’s
# datetime objects, especially as arrays get large (we introduced this type of vectoriza‐
# tion in “Computation on NumPy Arrays: Universal Functions” on page 50).
# One detail of the datetime64 and timedelta64 objects is that they are built on a fun‐
# damental time unit. Because the datetime64 object is limited to 64-bit precision, the
# range of encodable times is 264 times this fundamental unit. In other words, date
# time64 imposes a trade-off between time resolution and maximum time span.
# For example, if you want a time resolution of one nanosecond, you only have enough
# information to encode a range of 264 nanoseconds, or just under 600 years. NumPy
# will infer the desired unit from the input; for example, here is a day-based datetime:
#       In[6]: np.datetime64('2015-07-04')
#       Out[6]: numpy.datetime64('2015-07-04')
# Here is a minute-based datetime:
#       In[7]: np.datetime64('2015-07-04 12:00')
#       Out[7]: numpy.datetime64('2015-07-04T12:00')
# Notice that the time zone is automatically set to the local time on the computer exe‐
# cuting the code. You can force any desired fundamental unit using one of many for‐
# mat codes; for example, here we’ll force a nanosecond-based time:
#       In[8]: np.datetime64('2015-07-04 12:59:59.50', 'ns')
#       Out[8]: numpy.datetime64('2015-07-04T12:59:59.500000000')
# Table 3-6, drawn from the NumPy datetime64 documentation, lists the available for‐
# mat codes along with the relative and absolute timespans that they can encode.
# 
# Table 3-6. Description of date and time codes
# Code Meaning           Time span (relative) Time span (absolute)
# Y    Year              ± 9.2e18 years       [9.2e18 BC, 9.2e18 AD]
# M         Month        ± 7.6e17 years       [7.6e17 BC, 7.6e17 AD]
# W         Week         ± 1.7e17 years       [1.7e17 BC, 1.7e17 AD]
# 
# 
# 190   |    Chapter 3: Data Manipulation with Pandas
# 
# Code Meaning        Time span (relative) Time span (absolute)
# D    Day            ± 2.5e16 years       [2.5e16 BC, 2.5e16 AD]
# h     Hour          ± 1.0e15 years       [1.0e15 BC, 1.0e15 AD]
# m     Minute        ± 1.7e13 years       [1.7e13 BC, 1.7e13 AD]
# s     Second        ± 2.9e12 years       [ 2.9e9 BC, 2.9e9 AD]
# ms    Millisecond   ± 2.9e9 years        [ 2.9e6 BC, 2.9e6 AD]
# us    Microsecond   ± 2.9e6 years        [290301 BC, 294241 AD]
# ns    Nanosecond    ± 292 years          [ 1678 AD, 2262 AD]
# ps    Picosecond    ± 106 days           [ 1969 AD, 1970 AD]
# fs    Femtosecond ± 2.6 hours            [ 1969 AD, 1970 AD]
# as    Attosecond    ± 9.2 seconds        [ 1969 AD, 1970 AD]
# 
# 
# For the types of data we see in the real world, a useful default is datetime64[ns], as it
# can encode a useful range of modern dates with a suitably fine precision.
# Finally, we will note that while the datetime64 data type addresses some of the defi‐
# ciencies of the built-in Python datetime type, it lacks many of the convenient meth‐
# ods and functions provided by datetime and especially dateutil. More information
# can be found in NumPy’s datetime64 documentation.
# 
# Dates and times in Pandas: Best of both worlds
# Pandas builds upon all the tools just discussed to provide a Timestamp object, which
# combines the ease of use of datetime and dateutil with the efficient storage and
# vectorized interface of numpy.datetime64. From a group of these Timestamp objects,
# Pandas can construct a DatetimeIndex that can be used to index data in a Series or
# DataFrame; we’ll see many examples of this below.
# For example, we can use Pandas tools to repeat the demonstration from above. We
# can parse a flexibly formatted string date, and use format codes to output the day of
# the week:
#      In[9]: import pandas as pd
#             date = pd.to_datetime("4th of July, 2015")
#             date
#      Out[9]: Timestamp('2015-07-04 00:00:00')
#      In[10]: date.strftime('%A')
#      Out[10]: 'Saturday'
# Additionally, we can do NumPy-style vectorized operations directly on this same
# object:
#      In[11]: date + pd.to_timedelta(np.arange(12), 'D')
# 
# 
# 
#                                                                   Working with Time Series   |   191
# 
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
            "Dates and Times in Python",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Datesand(HierNode):
    def __init__(self):
        super().__init__("Dates and Times in Python")
        self.add(Content())

# eof
