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
#                  Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 2-13. California housing prices
# 
# This image tells you that the housing prices are very much related to the location
# (e.g., close to the ocean) and to the population density, as you probably knew already.
# It will probably be useful to use a clustering algorithm to detect the main clusters, and
# add new features that measure the proximity to the cluster centers. The ocean prox‐
# imity attribute may be useful as well, although in Northern California the housing
# prices in coastal districts are not too high, so it is not a simple rule.
# 
# Looking for Correlations
# Since the dataset is not too large, you can easily compute the standard correlation
# coefficient (also called Pearson’s r) between every pair of attributes using the corr()
# method:
#     corr_matrix = housing.corr()
# Now let’s look at how much each attribute correlates with the median house value:
#     >>> corr_matrix["median_house_value"].sort_values(ascending=False)
#     median_house_value    1.000000
#     median_income         0.687170
#     total_rooms           0.135231
#     housing_median_age    0.114220
#     households            0.064702
# 
# 
# 
#                                                Discover and Visualize the Data to Gain Insights   |   55
# 
#                        Download from finelybook www.finelybook.com
#      total_bedrooms        0.047865
#      population           -0.026699
#      longitude            -0.047279
#      latitude             -0.142826
#      Name: median_house_value, dtype: float64
# The correlation coefficient ranges from –1 to 1. When it is close to 1, it means that
# there is a strong positive correlation; for example, the median house value tends to go
# up when the median income goes up. When the coefficient is close to –1, it means
# that there is a strong negative correlation; you can see a small negative correlation
# between the latitude and the median house value (i.e., prices have a slight tendency to
# go down when you go north). Finally, coefficients close to zero mean that there is no
# linear correlation. Figure 2-14 shows various plots along with the correlation coeffi‐
# cient between their horizontal and vertical axes.
# 
# 
# 
# 
# Figure 2-14. Standard correlation coefficient of various datasets (source: Wikipedia;
# public domain image)
# 
#                      The correlation coefficient only measures linear correlations (“if x
#                      goes up, then y generally goes up/down”). It may completely miss
#                      out on nonlinear relationships (e.g., “if x is close to zero then y gen‐
#                      erally goes up”). Note how all the plots of the bottom row have a
#                      correlation coefficient equal to zero despite the fact that their axes
#                      are clearly not independent: these are examples of nonlinear rela‐
#                      tionships. Also, the second row shows examples where the correla‐
#                      tion coefficient is equal to 1 or –1; notice that this has nothing to
#                      do with the slope. For example, your height in inches has a correla‐
#                      tion coefficient of 1 with your height in feet or in nanometers.
# 
# Another way to check for correlation between attributes is to use Pandas’
# scatter_matrix function, which plots every numerical attribute against every other
# numerical attribute. Since there are now 11 numerical attributes, you would get 112 =
# 
# 56   |   Chapter 2: End-to-End Machine Learning Project
# 
#                    Download from finelybook www.finelybook.com
# 121 plots, which would not fit on a page, so let’s just focus on a few promising
# attributes that seem most correlated with the median housing value (Figure 2-15):
#     from pandas.tools.plotting import scatter_matrix
# 
#     attributes = ["median_house_value", "median_income", "total_rooms",
#                   "housing_median_age"]
#     scatter_matrix(housing[attributes], figsize=(12, 8))
# 
# 
# 
# 
# Figure 2-15. Scatter matrix
# 
# The main diagonal (top left to bottom right) would be full of straight lines if Pandas
# plotted each variable against itself, which would not be very useful. So instead Pandas
# displays a histogram of each attribute (other options are available; see Pandas’ docu‐
# mentation for more details).
# The most promising attribute to predict the median house value is the median
# income, so let’s zoom in on their correlation scatterplot (Figure 2-16):
#     housing.plot(kind="scatter", x="median_income", y="median_house_value",
#                  alpha=0.1)
# 
# 
# 
# 
#                                               Discover and Visualize the Data to Gain Insights   |   57
# 
#                        Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 2-16. Median income versus median house value
# 
# This plot reveals a few things. First, the correlation is indeed very strong; you can
# clearly see the upward trend and the points are not too dispersed. Second, the price
# cap that we noticed earlier is clearly visible as a horizontal line at $500,000. But this
# plot reveals other less obvious straight lines: a horizontal line around $450,000,
# another around $350,000, perhaps one around $280,000, and a few more below that.
# You may want to try removing the corresponding districts to prevent your algorithms
# from learning to reproduce these data quirks.
# 
# Experimenting with Attribute Combinations
# Hopefully the previous sections gave you an idea of a few ways you can explore the
# data and gain insights. You identified a few data quirks that you may want to clean up
# before feeding the data to a Machine Learning algorithm, and you found interesting
# correlations between attributes, in particular with the target attribute. You also
# noticed that some attributes have a tail-heavy distribution, so you may want to trans‐
# form them (e.g., by computing their logarithm). Of course, your mileage will vary
# considerably with each project, but the general ideas are similar.
# One last thing you may want to do before actually preparing the data for Machine
# Learning algorithms is to try out various attribute combinations. For example, the
# total number of rooms in a district is not very useful if you don’t know how many
# households there are. What you really want is the number of rooms per household.
# Similarly, the total number of bedrooms by itself is not very useful: you probably
# want to compare it to the number of rooms. And the population per household also
# 
# 
# 
# 58   |   Chapter 2: End-to-End Machine Learning Project
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Looking for Correlations",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Lookingfor(HierNode):
    def __init__(self):
        super().__init__("Looking for Correlations")
        self.add(Content(), "content")

# eof
