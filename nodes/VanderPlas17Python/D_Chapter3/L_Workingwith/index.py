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

from .A_Datesand.index import Datesand as A_Datesand
from .B_PandasTime.index import PandasTime as B_PandasTime
from .C_PandasTime.index import PandasTime as C_PandasTime
from .D_Frequenciesand.index import Frequenciesand as D_Frequenciesand
from .E_ResamplingShifting.index import ResamplingShifting as E_ResamplingShifting
from .F_Whereto.index import Whereto as F_Whereto
from .G_ExampleVisualizing.index import ExampleVisualizing as G_ExampleVisualizing

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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Working with Time Series",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Workingwith(HierNode):
    def __init__(self):
        super().__init__("Working with Time Series")
        self.add(Content())
        self.add(A_Datesand())
        self.add(B_PandasTime())
        self.add(C_PandasTime())
        self.add(D_Frequenciesand())
        self.add(E_ResamplingShifting())
        self.add(F_Whereto())
        self.add(G_ExampleVisualizing())

# eof
