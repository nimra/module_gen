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
#                 Download from finelybook www.finelybook.com
# seems like an interesting attribute combination to look at. Let’s create these new
# attributes:
#     housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
#     housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
#     housing["population_per_household"]=housing["population"]/housing["households"]
# And now let’s look at the correlation matrix again:
#     >>> corr_matrix = housing.corr()
#     >>> corr_matrix["median_house_value"].sort_values(ascending=False)
#     median_house_value          1.000000
#     median_income               0.687170
#     rooms_per_household         0.199343
#     total_rooms                 0.135231
#     housing_median_age          0.114220
#     households                  0.064702
#     total_bedrooms              0.047865
#     population_per_household   -0.021984
#     population                 -0.026699
#     longitude                  -0.047279
#     latitude                   -0.142826
#     bedrooms_per_room          -0.260070
#     Name: median_house_value, dtype: float64
# 
# Hey, not bad! The new bedrooms_per_room attribute is much more correlated with
# the median house value than the total number of rooms or bedrooms. Apparently
# houses with a lower bedroom/room ratio tend to be more expensive. The number of
# rooms per household is also more informative than the total number of rooms in a
# district—obviously the larger the houses, the more expensive they are.
# This round of exploration does not have to be absolutely thorough; the point is to
# start off on the right foot and quickly gain insights that will help you get a first rea‐
# sonably good prototype. But this is an iterative process: once you get a prototype up
# and running, you can analyze its output to gain more insights and come back to this
# exploration step.
# 
# Prepare the Data for Machine Learning Algorithms
# It’s time to prepare the data for your Machine Learning algorithms. Instead of just
# doing this manually, you should write functions to do that, for several good reasons:
# 
#   • This will allow you to reproduce these transformations easily on any dataset (e.g.,
#     the next time you get a fresh dataset).
#   • You will gradually build a library of transformation functions that you can reuse
#     in future projects.
#   • You can use these functions in your live system to transform the new data before
#     feeding it to your algorithms.
# 
# 
#                                              Prepare the Data for Machine Learning Algorithms   |   59
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Experimenting with Attribute Combinations",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Experimentingwith(HierNode):
    def __init__(self):
        super().__init__("Experimenting with Attribute Combinations")
        self.add(Content(), "content")

# eof
