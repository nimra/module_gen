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
# Example: Birthrate Data
# As a more interesting example, let’s take a look at the freely available data on births in
# the United States, provided by the Centers for Disease Control (CDC). This data can
# be found at https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/
# births.csv (this dataset has been analyzed rather extensively by Andrew Gelman and
# his group; see, for example, this blog post):
#       In[10]:
#       # shell command to download the data:
#       # !curl -O https://raw.githubusercontent.com/jakevdp/data-CDCbirths/
#       # master/births.csv
#       In[11]: births = pd.read_csv('births.csv')
# Taking a look at the data, we see that it’s relatively simple—it contains the number of
# births grouped by date and gender:
#       In[12]: births.head()
#       Out[12]:       year month day gender births
#                  0    1969     1   1      F   4046
#                  1    1969     1   1      M   4440
#                  2    1969     1   2      F   4454
#                  3    1969     1   2      M   4548
#                  4    1969     1   3      F   4548
# We can start to understand this data a bit more by using a pivot table. Let’s add a dec‐
# ade column, and take a look at male and female births as a function of decade:
#       In[13]:
#       births['decade'] = 10 * (births['year'] // 10)
#       births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')
#       Out[13]: gender                 F              M
#                decade
#                1960          1753634       1846572
#                1970         16263075      17121550
#                1980         18310351      19243452
#                1990         19479454      20420553
#                2000         18229309      19106428
# We immediately see that male births outnumber female births in every decade. To see
# this trend a bit more clearly, we can use the built-in plotting tools in Pandas to visual‐
# ize the total number of births by year (Figure 3-2; see Chapter 4 for a discussion of
# plotting with Matplotlib):
#       In[14]:
#       %matplotlib inline
#       import matplotlib.pyplot as plt
#       sns.set() # use Seaborn styles
#       births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()
#       plt.ylabel('total births per year');
# 
# 
# 
# 174   |   Chapter 3: Data Manipulation with Pandas
# 
# Figure 3-2. Total number of US births by year and gender
# 
# With a simple pivot table and plot() method, we can immediately see the annual
# trend in births by gender. By eye, it appears that over the past 50 years male births
# have outnumbered female births by around 5%.
# 
# Further data exploration
# Though this doesn’t necessarily relate to the pivot table, there are a few more interest‐
# ing features we can pull out of this dataset using the Pandas tools covered up to this
# point. We must start by cleaning the data a bit, removing outliers caused by mistyped
# dates (e.g., June 31st) or missing values (e.g., June 99th). One easy way to remove
# these all at once is to cut outliers; we’ll do this via a robust sigma-clipping operation:1
#     In[15]: quartiles = np.percentile(births['births'], [25, 50, 75])
#             mu = quartiles[1]
#             sig = 0.74 * (quartiles[2] - quartiles[0])
# This final line is a robust estimate of the sample mean, where the 0.74 comes from the
# interquartile range of a Gaussian distribution. With this we can use the query()
# method (discussed further in “High-Performance Pandas: eval() and query()” on
# page 208) to filter out rows with births outside these values:
#     In[16]:
#     births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
# 
# 
# 
# 
# 1 You can learn more about sigma-clipping operations in a book I coauthored with Željko Ivezić, Andrew J.
#   Connolly, and Alexander Gray: Statistics, Data Mining, and Machine Learning in Astronomy: A Practical
#   Python Guide for the Analysis of Survey Data (Princeton University Press, 2014).
# 
# 
# 
#                                                                                          Pivot Tables     |   175
# 
# Next we set the day column to integers; previously it had been a string because some
# columns in the dataset contained the value 'null':
#       In[17]: # set 'day' column to integer; it originally was a string due to nulls
#               births['day'] = births['day'].astype(int)
# Finally, we can combine the day, month, and year to create a Date index (see “Work‐
# ing with Time Series” on page 188). This allows us to quickly compute the weekday
# corresponding to each row:
#       In[18]: # create a datetime index from the year, month, day
#               births.index = pd.to_datetime(10000 * births.year +
#                                             100 * births.month +
#                                             births.day, format='%Y%m%d')
# 
#                 births['dayofweek'] = births.index.dayofweek
# Using this we can plot births by weekday for several decades (Figure 3-3):
#       In[19]:
#       import matplotlib.pyplot as plt
#       import matplotlib as mpl
# 
#       births.pivot_table('births', index='dayofweek',
#                           columns='decade', aggfunc='mean').plot()
#       plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
#       plt.ylabel('mean births by day');
# 
# 
# 
# 
# Figure 3-3. Average daily births by day of week and decade
# 
# Apparently births are slightly less common on weekends than on weekdays! Note that
# the 1990s and 2000s are missing because the CDC data contains only the month of
# birth starting in 1989.
# 
# 
# 
# 176   |   Chapter 3: Data Manipulation with Pandas
# 
# Another interesting view is to plot the mean number of births by the day of the year.
# Let’s first group the data by month and day separately:
#     In[20]:
#     births_by_date = births.pivot_table('births',
#                                         [births.index.month, births.index.day])
#     births_by_date.head()
#     Out[20]: 1  1    4009.225
#                 2    4247.400
#                 3    4500.900
#                 4    4571.350
#                 5    4603.625
#              Name: births, dtype: float64
# The result is a multi-index over months and days. To make this easily plottable, let’s
# turn these months and days into a date by associating them with a dummy year vari‐
# able (making sure to choose a leap year so February 29th is correctly handled!)
#     In[21]: births_by_date.index = [pd.datetime(2012, month, day)
#                                     for (month, day) in births_by_date.index]
#             births_by_date.head()
#     Out[21]: 2012-01-01      4009.225
#              2012-01-02      4247.400
#              2012-01-03      4500.900
#              2012-01-04      4571.350
#              2012-01-05      4603.625
#              Name: births,   dtype: float64
# Focusing on the month and day only, we now have a time series reflecting the average
# number of births by date of the year. From this, we can use the plot method to plot
# the data (Figure 3-4). It reveals some interesting trends:
#     In[22]: # Plot the results
#             fig, ax = plt.subplots(figsize=(12, 4))
#             births_by_date.plot(ax=ax);
# 
# 
# 
# 
# Figure 3-4. Average daily births by date
# 
# 
#                                                                       Pivot Tables   |   177
# 
# In particular, the striking feature of this graph is the dip in birthrate on US holidays
# (e.g., Independence Day, Labor Day, Thanksgiving, Christmas, New Year’s Day)
# although this likely reflects trends in scheduled/induced births rather than some deep
# psychosomatic effect on natural births. For more discussion on this trend, see the
# analysis and links in Andrew Gelman’s blog post on the subject. We’ll return to this
# figure in “Example: Effect of Holidays on US Births” on page 269, where we will use
# Matplotlib’s tools to annotate this plot.
# Looking at this short example, you can see that many of the Python and Pandas tools
# we’ve seen to this point can be combined and used to gain insight from a variety of
# datasets. We will see some more sophisticated applications of these data manipula‐
# tions in future sections!
# 
# Vectorized String Operations
# One strength of Python is its relative ease in handling and manipulating string data.
# Pandas builds on this and provides a comprehensive set of vectorized string operations
# that become an essential piece of the type of munging required when one is working
# with (read: cleaning up) real-world data. In this section, we’ll walk through some of
# the Pandas string operations, and then take a look at using them to partially clean up
# a very messy dataset of recipes collected from the Internet.
# 
# Introducing Pandas String Operations
# We saw in previous sections how tools like NumPy and Pandas generalize arithmetic
# operations so that we can easily and quickly perform the same operation on many
# array elements. For example:
#       In[1]: import numpy as np
#              x = np.array([2, 3, 5, 7, 11, 13])
#              x * 2
#       Out[1]: array([ 4,        6, 10, 14, 22, 26])
# This vectorization of operations simplifies the syntax of operating on arrays of data:
# we no longer have to worry about the size or shape of the array, but just about what
# operation we want done. For arrays of strings, NumPy does not provide such simple
# access, and thus you’re stuck using a more verbose loop syntax:
#       In[2]: data = ['peter', 'Paul', 'MARY', 'gUIDO']
#              [s.capitalize() for s in data]
#       Out[2]: ['Peter', 'Paul', 'Mary', 'Guido']
# This is perhaps sufficient to work with some data, but it will break if there are any
# missing values. For example:
#       In[3]: data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
#              [s.capitalize() for s in data]
# 
# 
# 178   |   Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Example: Birthrate Data",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ExampleBirthrate(HierNode):
    def __init__(self):
        super().__init__("Example: Birthrate Data")
        self.add(Content())

# eof
