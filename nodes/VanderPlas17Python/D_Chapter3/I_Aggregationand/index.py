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

from .A_PlanetsData.index import PlanetsData as A_PlanetsData
from .B_SimpleAggregation.index import SimpleAggregation as B_SimpleAggregation
from .C_GroupBySplit.index import GroupBySplit as C_GroupBySplit

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                 101                AZ   total       2010    6408790.0      Arizona   114006.0
#                 189                AR   total       2010    2922280.0     Arkansas    53182.0
#                 197                CA   total       2010   37333601.0   California   163707.0
# Now let’s compute the population density and display it in order. We’ll start by rein‐
# dexing our data on the state, and then compute the result:
#       In[31]: data2010.set_index('state', inplace=True)
#               density = data2010['population'] / data2010['area (sq. mi)']
#       In[32]: density.sort_values(ascending=False, inplace=True)
#               density.head()
#       Out[32]: state
#                District of Columbia                8898.897059
#                Puerto Rico                         1058.665149
#                New Jersey                          1009.253268
#                Rhode Island                         681.339159
#                Connecticut                          645.600649
#                dtype: float64
# The result is a ranking of US states plus Washington, DC, and Puerto Rico in order of
# their 2010 population density, in residents per square mile. We can see that by far the
# densest region in this dataset is Washington, DC (i.e., the District of Columbia);
# among states, the densest is New Jersey.
# We can also check the end of the list:
#       In[33]: density.tail()
#       Out[33]: state
#                South Dakota   10.583512
#                North Dakota    9.537565
#                Montana         6.736171
#                Wyoming         5.768079
#                Alaska          1.087509
#                dtype: float64
# We see that the least dense state, by far, is Alaska, averaging slightly over one resident
# per square mile.
# This type of messy data merging is a common task when one is trying to answer
# questions using real-world data sources. I hope that this example has given you an
# idea of the ways you can combine tools we’ve covered in order to gain insight from
# your data!
# 
# Aggregation and Grouping
# An essential piece of analysis of large data is efficient summarization: computing
# aggregations like sum(), mean(), median(), min(), and max(), in which a single num‐
# ber gives insight into the nature of a potentially large dataset. In this section, we’ll
# 
# 
# 
# 158   | Chapter 3: Data Manipulation with Pandas
# 
# explore aggregations in Pandas, from simple operations akin to what we’ve seen on
# NumPy arrays, to more sophisticated operations based on the concept of a groupby.
# 
# Planets Data
# Here we will use the Planets dataset, available via the Seaborn package (see “Visuali‐
# zation with Seaborn” on page 311). It gives information on planets that astronomers
# have discovered around other stars (known as extrasolar planets or exoplanets for
# short). It can be downloaded with a simple Seaborn command:
#     In[2]: import seaborn as sns
#            planets = sns.load_dataset('planets')
#            planets.shape
#     Out[2]: (1035, 6)
#     In[3]: planets.head()
#     Out[3]:       method              number   orbital_period   mass  distance      year
#               0   Radial   Velocity   1        269.300          7.10  77.40         2006
#               1   Radial   Velocity   1        874.774          2.21  56.95         2008
#               2   Radial   Velocity   1        763.000          2.60  19.84         2011
#               3   Radial   Velocity   1        326.030          19.40 110.62        2007
#               4   Radial   Velocity   1        516.220          10.50 119.47        2009
# This has some details on the 1,000+ exoplanets discovered up to 2014.
# 
# Simple Aggregation in Pandas
# Earlier we explored some of the data aggregations available for NumPy arrays
# (“Aggregations: Min, Max, and Everything in Between” on page 58). As with a one-
# dimensional NumPy array, for a Pandas Series the aggregates return a single value:
#     In[4]: rng = np.random.RandomState(42)
#            ser = pd.Series(rng.rand(5))
#            ser
#     Out[4]: 0    0.374540
#             1    0.950714
#             2    0.731994
#             3    0.598658
#             4    0.156019
#             dtype: float64
#     In[5]: ser.sum()
#     Out[5]: 2.8119254917081569
#     In[6]: ser.mean()
#     Out[6]: 0.56238509834163142
# 
# For a DataFrame, by default the aggregates return results within each column:
# 
# 
# 
#                                                                   Aggregation and Grouping   |   159
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Aggregation and Grouping",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Aggregationand(HierNode):
    def __init__(self):
        super().__init__("Aggregation and Grouping")
        self.add(Content())
        self.add(A_PlanetsData())
        self.add(B_SimpleAggregation())
        self.add(C_GroupBySplit())

# eof
