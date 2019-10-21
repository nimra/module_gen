# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Resampling Datetime Objects
# A Pandas DataFrame with an index of DatetimeIndex, PeriodIndex, or TimedeltaIndex
# can be resampled to any of the date time frequencies from seconds, to minutes, to
# months. Let’s see some examples.
#    Let’s get the average monthly closing values for Litecoin.
# 
# data.loc[data.slug == 'bitcoin', 'close'].resample('M').mean().head()
# 'Output':
# date
# 2013-04-30    139.250000
# 2013-05-31    119.993226
# 2013-06-30    107.761333
# 2013-07-31     90.512258
# 2013-08-31    113.905161
# Freq: M, Name: close, dtype: float64
# 
#       Get the average weekly market value of Bitcoin Cash.
# 
# data.loc[data.symbol == 'BCH', 'market'].resample('W').mean().head()
# 'Output':
# date
# 2017-07-23    0.000000e+00
# 2017-07-30    0.000000e+00
# 2017-08-06    3.852961e+09
# 2017-08-13    4.982661e+09
# 2017-08-20    7.355117e+09
# Freq: W-SUN, Name: market, dtype: float64

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Resampling Datetime Objects",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Resampling Datetime Objects"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ResamplingDatetime(HierNode):
    def __init__(self):
        super().__init__("Resampling Datetime Objects")
        self.add(Content())

# eof
