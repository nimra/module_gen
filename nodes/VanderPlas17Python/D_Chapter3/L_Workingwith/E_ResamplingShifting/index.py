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
# financial data from a number of available sources, including Yahoo finance, Google
# Finance, and others. Here we will load Google’s closing price history:
#     In[25]: from pandas_datareader import data
# 
#              goog = data.DataReader('GOOG', start='2004', end='2016',
#                                     data_source='google')
#              goog.head()
#     Out[25]:               Open  High   Low Close Volume
#                Date
#                2004-08-19 49.96 51.98 47.93 50.12    NaN
#                2004-08-20 50.69 54.49 50.20 54.10    NaN
#                2004-08-23 55.32 56.68 54.47 54.65    NaN
#                2004-08-24 55.56 55.74 51.73 52.38    NaN
#                2004-08-25 52.43 53.95 51.89 52.95    NaN
# For simplicity, we’ll use just the closing price:
#     In[26]: goog = goog['Close']
# 
# We can visualize this using the plot() method, after the normal Matplotlib setup
# boilerplate (Figure 3-5):
#     In[27]: %matplotlib inline
#             import matplotlib.pyplot as plt
#             import seaborn; seaborn.set()
#     In[28]: goog.plot();
# 
# 
# 
# 
# Figure 3-5. Google’s closing stock price over time
# 
# Resampling and converting frequencies
# One common need for time series data is resampling at a higher or lower frequency.
# You can do this using the resample() method, or the much simpler asfreq()
# 
# 
#                                                             Working with Time Series   |   197
# 
# method. The primary difference between the two is that resample() is fundamentally
# a data aggregation, while asfreq() is fundamentally a data selection.
# Taking a look at the Google closing price, let’s compare what the two return when we
# down-sample the data. Here we will resample the data at the end of business year
# (Figure 3-6):
#       In[29]: goog.plot(alpha=0.5, style='-')
#               goog.resample('BA').mean().plot(style=':')
#               goog.asfreq('BA').plot(style='--');
#               plt.legend(['input', 'resample', 'asfreq'],
#                          loc='upper left');
# 
# 
# 
# 
# Figure 3-6. Resamplings of Google’s stock price
# 
# Notice the difference: at each point, resample reports the average of the previous year,
# while asfreq reports the value at the end of the year.
# For up-sampling, resample() and asfreq() are largely equivalent, though resample
# has many more options available. In this case, the default for both methods is to leave
# the up-sampled points empty—that is, filled with NA values. Just as with the
# pd.fillna() function discussed previously, asfreq() accepts a method argument to
# specify how values are imputed. Here, we will resample the business day data at a
# daily frequency (i.e., including weekends); see Figure 3-7:
#       In[30]: fig, ax = plt.subplots(2, sharex=True)
#               data = goog.iloc[:10]
# 
#                 data.asfreq('D').plot(ax=ax[0], marker='o')
# 
#                 data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
#                 data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
#                 ax[1].legend(["back-fill", "forward-fill"]);
# 
# 
# 
# 198   |   Chapter 3: Data Manipulation with Pandas
# 
# Figure 3-7. Comparison between forward-fill and back-fill interpolation
# 
# The top panel is the default: non-business days are left as NA values and do not
# appear on the plot. The bottom panel shows the differences between two strategies
# for filling the gaps: forward-filling and backward-filling.
# 
# Time-shifts
# Another common time series–specific operation is shifting of data in time. Pandas
# has two closely related methods for computing this: shift() and tshift(). In short,
# the difference between them is that shift() shifts the data, while tshift() shifts the
# index. In both cases, the shift is specified in multiples of the frequency.
# Here we will both shift() and tshift() by 900 days (Figure 3-8):
#     In[31]: fig, ax = plt.subplots(3, sharey=True)
# 
#               # apply a frequency to the data
#               goog = goog.asfreq('D', method='pad')
# 
#               goog.plot(ax=ax[0])
#               goog.shift(900).plot(ax=ax[1])
#               goog.tshift(900).plot(ax=ax[2])
# 
#               # legends and annotations
#               local_max = pd.to_datetime('2007-11-05')
#               offset = pd.Timedelta(900, 'D')
# 
#               ax[0].legend(['input'], loc=2)
#               ax[0].get_xticklabels()[4].set(weight='heavy', color='red')
#               ax[0].axvline(local_max, alpha=0.3, color='red')
# 
# 
# 
#                                                              Working with Time Series   |   199
# 
#                 ax[1].legend(['shift(900)'], loc=2)
#                 ax[1].get_xticklabels()[4].set(weight='heavy', color='red')
#                 ax[1].axvline(local_max + offset, alpha=0.3, color='red')
# 
#                 ax[2].legend(['tshift(900)'], loc=2)
#                 ax[2].get_xticklabels()[1].set(weight='heavy', color='red')
#                 ax[2].axvline(local_max + offset, alpha=0.3, color='red');
# 
# 
# 
# 
# Figure 3-8. Comparison between shift and tshift
# 
# We see here that shift(900) shifts the data by 900 days, pushing some of it off the
# end of the graph (and leaving NA values at the other end), while tshift(900) shifts
# the index values by 900 days.
# A common context for this type of shift is computing differences over time. For
# example, we use shifted values to compute the one-year return on investment for
# Google stock over the course of the dataset (Figure 3-9):
#       In[32]: ROI = 100 * (goog.tshift(-365) / goog - 1)
#               ROI.plot()
#               plt.ylabel('% Return on Investment');
# 
# 
# 
# 
# 200   |   Chapter 3: Data Manipulation with Pandas
# 
# Figure 3-9. Return on investment to present day for Google stock
# 
# This helps us to see the overall trend in Google stock: thus far, the most profitable
# times to invest in Google have been (unsurprisingly, in retrospect) shortly after its
# IPO, and in the middle of the 2009 recession.
# 
# Rolling windows
# Rolling statistics are a third type of time series–specific operation implemented by
# Pandas. These can be accomplished via the rolling() attribute of Series and Data
# Frame objects, which returns a view similar to what we saw with the groupby opera‐
# tion (see “Aggregation and Grouping” on page 158). This rolling view makes available
# a number of aggregation operations by default.
# For example, here is the one-year centered rolling mean and standard deviation of the
# Google stock prices (Figure 3-10):
#     In[33]: rolling = goog.rolling(365, center=True)
# 
#             data = pd.DataFrame({'input': goog,
#                                  'one-year rolling_mean': rolling.mean(),
#                                  'one-year rolling_std': rolling.std()})
#             ax = data.plot(style=['-', '--', ':'])
#             ax.lines[0].set_alpha(0.3)
# 
# 
# 
# 
#                                                               Working with Time Series   |   201
# 
# Figure 3-10. Rolling statistics on Google stock prices
# 
# As with groupby operations, the aggregate() and apply() methods can be used for
# custom rolling computations.
# 
# Where to Learn More
# This section has provided only a brief summary of some of the most essential features
# of time series tools provided by Pandas; for a more complete discussion, you can refer
# to the “Time Series/Date” section of the Pandas online documentation.
# Another excellent resource is the textbook Python for Data Analysis by Wes McKin‐
# ney (O’Reilly, 2012). Although it is now a few years old, it is an invaluable resource on
# the use of Pandas. In particular, this book emphasizes time series tools in the context
# of business and finance, and focuses much more on particular details of business cal‐
# endars, time zones, and related topics.
# As always, you can also use the IPython help functionality to explore and try further
# options available to the functions and methods discussed here. I find this often is the
# best way to learn a new Python tool.
# 
# Example: Visualizing Seattle Bicycle Counts
# As a more involved example of working with some time series data, let’s take a look at
# bicycle counts on Seattle’s Fremont Bridge. This data comes from an automated bicy‐
# cle counter, installed in late 2012, which has inductive sensors on the east and west
# sidewalks of the bridge. The hourly bicycle counts can be downloaded from http://
# data.seattle.gov/; here is the direct link to the dataset.
# As of summer 2016, the CSV can be downloaded as follows:
# 
# 
# 202   |   Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Resampling, Shifting, and Windowing",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ResamplingShifting(HierNode):
    def __init__(self):
        super().__init__("Resampling, Shifting, and Windowing")
        self.add(Content())

# eof
