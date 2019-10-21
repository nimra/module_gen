# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Rolling Windows
# Pandas provides a function called rolling() to find the rolling or moving statistics of
# values in a column over a specified window. The window is the “number of observations
# used in calculating the statistic.” So we can find the rolling sums or rolling means of a
# variable. These statistics are vital when working with timeseries datasets. Let’s see some
# examples.
#     Let’s find the rolling means for the closing variable over a 30-day window.
# 
# # find the rolling means for Bitcoin cash
# rolling_means = data_subset_BCH['close'].rolling(window=30).mean()
# 
#     The first few values of the rolling_means variable contain NaNs because the method
# computes the rolling statistic from the earliest time to the latest time in the dataset. Let’s
# print out the first five values using the head method.
# 
# rolling_means.head()
# Out[75]:
# date
# 2017-07-23   NaN
# 2017-07-24   NaN
# 2017-07-25   NaN
# 2017-07-26   NaN
# 2017-07-27   NaN
# 
#    Now let’s observe the last five values using the tail method.
# 
# rolling_means.tail()
# 'Output':
# date
# 2018-01-06    2403.932000
# 2018-01-07    2448.023667
# 2018-01-08    2481.737333
# 2018-01-09    2517.353667
# 2018-01-10    2566.420333
# Name: close, dtype: float64
# 
#    Let’s do a quick plot of the rolling means using the Pandas plotting function. The
# output of the plot is shown in Figure 11-2.
# 
# # plot the rolling means for Bitcoin cash
# data_subset_BCH['close'].rolling(window=30).mean().plot(label='Rolling
# Average over 30 days')
# 
# 
# 
# 
# 
# Figure 11-2. Rolling average closing price over 30 days for Bitcoin Cash
# 
#       More on plotting in the next chapter.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Rolling Windows",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Rolling Windows"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RollingWindows(HierNode):
    def __init__(self):
        super().__init__("Rolling Windows")
        self.add(Content())

# eof
