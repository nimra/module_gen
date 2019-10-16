# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Selection Using DatetimeIndex
# The DatetimeIndex can be used to select the observations of the dataset in various
# interesting ways. For example, we can select the observation of an exact day or the
# observations belonging to a particular month or year. The selected observation can be
# subsetted by columns and grouped to give more insight in understanding the dataset.
#     Let’s see some examples.
# 
# Select a Particular Date
# Let’s select a particular date from a DataFrame.
# 
# # select a particular date
# data['2018-01-05'].head()
# 'Output':
#                     slug symbol         name  ranknow      open   high  \
# date
# 2018-01-05       bitcoin    BTC       Bitcoin        1  15477.20  17705.20
# 2018-01-05      ethereum    ETH      Ethereum       2    975.75   1075.39
# 2018-01-05        ripple    XRP        Ripple        3     3.30     3.56
# 2018-01-05  bitcoin-cash    BCH  Bitcoin Cash        4   2400.74   2648.32
# 2018-01-05       cardano    ADA       Cardano        5     1.17     1.25
# 
#                      low         close       volume     market  \
# date
# 2018-01-05  15202.800000  17429.500000  23840900000  259748000000
# 2018-01-05    956.330000    997.720000   6683150000   94423900000
# 2018-01-05      2.830000      3.050000   6288500000  127870000000
# 2018-01-05   2370.590000   2584.480000   2115710000   40557600000
# 2018-01-05      0.903503      0.999559    508100000   30364400000
# 
#             close_ratio   spread
# date
# 2018-01-05       0.8898  2502.40
# 2018-01-05       0.3476   119.06
# 2018-01-05       0.3014     0.73
# 2018-01-05       0.7701   277.73
# 2018-01-05       0.2772     0.35
# 
# # select a range of dates
# data['2018-01-05':'2018-01-06'].head()
# 'Output':
#                 slug symbol     name  ranknow      open      high    low  \
# date
# 2018-01-05  bitcoin    BTC   Bitcoin        1  15477.20  17705.20  15202.80
# 2018-01-06  bitcoin    BTC   Bitcoin        1  17462.10  17712.40  16764.60
# 2018-01-05  ethereum   ETH  Ethereum        2    975.75   1075.39    956.33
# 2018-01-06  ethereum   ETH  Ethereum        2    995.15   1060.71    994.62
# 2018-01-05  ripple     XRP    Ripple        3     3.30     3.56     2.83
# 
#                close       volume        market  close_ratio   spread
# date
# 2018-01-05  17429.50  23840900000  259748000000       0.8898  2502.40
# 2018-01-06  17527.00  18314600000  293091000000       0.8044   947.80
# 2018-01-05    997.72   6683150000   94423900000       0.3476   119.06
# 2018-01-06   1041.68   4662220000   96326500000       0.7121    66.09
# 2018-01-05      3.05   6288500000  127870000000       0.3014     0.73
# 
# Select a Month
# Let’s select a particular month from a DataFrame.
# 
# # select a particular month
# data['2018-01'].head()
# 'Output':
#                slug    symbol     name  ranknow     open     high     low \
# date
# 2018-01-01  bitcoin      BTC   Bitcoin        1  14112.2  14112.2   13154.7
# 2018-01-02  bitcoin      BTC   Bitcoin        1  13625.0  15444.6   13163.6
# 2018-01-03  bitcoin      BTC   Bitcoin        1  14978.2  15572.8   14844.5
# 2018-01-04  bitcoin      BTC   Bitcoin        1  15270.7  15739.7   14522.2
# 2018-01-05  bitcoin      BTC   Bitcoin        1  15477.2  17705.2   15202.8
# 
#               close       volume        market  close_ratio  spread
# date
# 2018-01-01  13657.2  10291200000  236725000000       0.5248   957.5
# 2018-01-02  14982.1  16846600000  228579000000       0.7972  2281.0
# 2018-01-03  15201.0  16871900000  251312000000       0.4895   728.3
# 2018-01-04  15599.2  21783200000  256250000000       0.8846  1217.5
# 2018-01-05  17429.5  23840900000  259748000000       0.8898  2502.4
# 
# Select a Year
# Let’s select a particular year from a DataFrame.
# 
# # select a particular year
# data['2018'].head()
# 'Output':
#                slug symbol     name  ranknow     open     high low  \
# date
# 2018-01-01  bitcoin    BTC  Bitcoin        1  14112.2  14112.2  13154.7
# 2018-01-02  bitcoin    BTC  Bitcoin        1  13625.0  15444.6  13163.6
# 2018-01-03  bitcoin    BTC  Bitcoin        1  14978.2  15572.8  14844.5
# 2018-01-04  bitcoin    BTC  Bitcoin        1  15270.7  15739.7  14522.2
# 2018-01-05  bitcoin    BTC  Bitcoin        1  15477.2  17705.2  15202.8
# 
#               close       volume        market  close_ratio  spread
# date
# 2018-01-01  13657.2  10291200000  236725000000       0.5248   957.5
# 2018-01-02  14982.1  16846600000  228579000000       0.7972  2281.0
# 2018-01-03  15201.0  16871900000  251312000000       0.4895   728.3
# 2018-01-04  15599.2  21783200000  256250000000       0.8846  1217.5
# 2018-01-05  17429.5  23840900000  259748000000       0.8898  2502.4

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Selection Using DatetimeIndex",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Selection Using DatetimeIndex"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SelectionUsing(HierNode):
    def __init__(self):
        super().__init__("Selection Using DatetimeIndex")
        self.add(Content())

# eof
