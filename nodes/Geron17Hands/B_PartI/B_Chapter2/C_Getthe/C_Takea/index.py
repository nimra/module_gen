# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# This function returns a Pandas DataFrame object containing all the data.
# 
# Take a Quick Look at the Data Structure
# Let’s take a look at the top five rows using the DataFrame’s head() method (see
# Figure 2-5).
# 
# 
# 
# 
# Figure 2-5. Top five rows in the dataset
# 
# Each row represents one district. There are 10 attributes (you can see the first 6 in the
# screenshot): longitude, latitude, housing_median_age, total_rooms, total_bed
# rooms, population, households, median_income, median_house_value, and
# ocean_proximity.
# The info() method is useful to get a quick description of the data, in particular the
# total number of rows, and each attribute’s type and number of non-null values (see
# Figure 2-6).
# 
# 
# 
# 
# Figure 2-6. Housing info
# 
# 
# 
#                                                                          Get the Data   |   45
# 
#                    Download from finelybook www.finelybook.com
# There are 20,640 instances in the dataset, which means that it is fairly small by
# Machine Learning standards, but it’s perfect to get started. Notice that the total_bed
# rooms attribute has only 20,433 non-null values, meaning that 207 districts are miss‐
# ing this feature. We will need to take care of this later.
# All attributes are numerical, except the ocean_proximity field. Its type is object, so it
# could hold any kind of Python object, but since you loaded this data from a CSV file
# you know that it must be a text attribute. When you looked at the top five rows, you
# probably noticed that the values in that column were repetitive, which means that it is
# probably a categorical attribute. You can find out what categories exist and how many
# districts belong to each category by using the value_counts() method:
#      >>> housing["ocean_proximity"].value_counts()
#      <1H OCEAN     9136
#      INLAND        6551
#      NEAR OCEAN    2658
#      NEAR BAY      2290
#      ISLAND           5
#      Name: ocean_proximity, dtype: int64
# 
# Let’s look at the other fields. The describe() method shows a summary of the
# numerical attributes (Figure 2-7).
# 
# 
# 
# 
# Figure 2-7. Summary of each numerical attribute
# 
# The count, mean, min, and max rows are self-explanatory. Note that the null values are
# ignored (so, for example, count of total_bedrooms is 20,433, not 20,640). The std
# row shows the standard deviation (which measures how dispersed the values are).
# The 25%, 50%, and 75% rows show the corresponding percentiles: a percentile indi‐
# cates the value below which a given percentage of observations in a group of observa‐
# tions falls. For example, 25% of the districts have a housing_median_age lower than
# 
# 
# 
# 46   |   Chapter 2: End-to-End Machine Learning Project
# 
#                   Download from finelybook www.finelybook.com
# 18, while 50% are lower than 29 and 75% are lower than 37. These are often called the
# 25th percentile (or 1st quartile), the median, and the 75th percentile (or 3rd quartile).
# Another quick way to get a feel of the type of data you are dealing with is to plot a
# histogram for each numerical attribute. A histogram shows the number of instances
# (on the vertical axis) that have a given value range (on the horizontal axis). You can
# either plot this one attribute at a time, or you can call the hist() method on the
# whole dataset, and it will plot a histogram for each numerical attribute (see
# Figure 2-8). For example, you can see that slightly over 800 districts have a
# median_house_value equal to about $500,000.
#     %matplotlib inline   # only in a Jupyter notebook
#     import matplotlib.pyplot as plt
#     housing.hist(bins=50, figsize=(20,15))
#     plt.show()
# 
# 
# 
# 
# Figure 2-8. A histogram for each numerical attribute
# 
# 
# 
# 
#                                                                          Get the Data   |   47
# 
#                           Download from finelybook www.finelybook.com
#                        The hist() method relies on Matplotlib, which in turn relies on a
#                        user-specified graphical backend to draw on your screen. So before
#                        you can plot anything, you need to specify which backend Matplot‐
#                        lib should use. The simplest option is to use Jupyter’s magic com‐
#                        mand %matplotlib inline. This tells Jupyter to set up Matplotlib
#                        so it uses Jupyter’s own backend. Plots are then rendered within the
#                        notebook itself. Note that calling show() is optional in a Jupyter
#                        notebook, as Jupyter will automatically display plots when a cell is
#                        executed.
# 
# Notice a few things in these histograms:
# 
#  1. First, the median income attribute does not look like it is expressed in US dollars
#     (USD). After checking with the team that collected the data, you are told that the
#     data has been scaled and capped at 15 (actually 15.0001) for higher median
#     incomes, and at 0.5 (actually 0.4999) for lower median incomes. Working with
#     preprocessed attributes is common in Machine Learning, and it is not necessarily
#     a problem, but you should try to understand how the data was computed.
#  2. The housing median age and the median house value were also capped. The lat‐
#     ter may be a serious problem since it is your target attribute (your labels). Your
#     Machine Learning algorithms may learn that prices never go beyond that limit.
#     You need to check with your client team (the team that will use your system’s out‐
#     put) to see if this is a problem or not. If they tell you that they need precise pre‐
#     dictions even beyond $500,000, then you have mainly two options:
#          a. Collect proper labels for the districts whose labels were capped.
#          b. Remove those districts from the training set (and also from the test set, since
#             your system should not be evaluated poorly if it predicts values beyond
#             $500,000).
#  3. These attributes have very different scales. We will discuss this later in this chap‐
#     ter when we explore feature scaling.
#  4. Finally, many histograms are tail heavy: they extend much farther to the right of
#     the median than to the left. This may make it a bit harder for some Machine
#     Learning algorithms to detect patterns. We will try transforming these attributes
#     later on to have more bell-shaped distributions.
# 
# Hopefully you now have a better understanding of the kind of data you are dealing
# with.
# 
# 
# 
# 
# 48   |     Chapter 2: End-to-End Machine Learning Project
# 
#                       Download from finelybook www.finelybook.com
#                     Wait! Before you look at the data any further, you need to create a
#                     test set, put it aside, and never look at it.
# 
# 
# 
# 
# Create a Test Set
# It may sound strange to voluntarily set aside part of the data at this stage. After all,
# you have only taken a quick glance at the data, and surely you should learn a whole
# lot more about it before you decide what algorithms to use, right? This is true, but
# your brain is an amazing pattern detection system, which means that it is highly
# prone to overfitting: if you look at the test set, you may stumble upon some seemingly
# interesting pattern in the test data that leads you to select a particular kind of
# Machine Learning model. When you estimate the generalization error using the test
# set, your estimate will be too optimistic and you will launch a system that will not
# perform as well as expected. This is called data snooping bias.
# Creating a test set is theoretically quite simple: just pick some instances randomly,
# typically 20% of the dataset, and set them aside:
#       import numpy as np
# 
#       def split_train_test(data, test_ratio):
#           shuffled_indices = np.random.permutation(len(data))
#           test_set_size = int(len(data) * test_ratio)
#           test_indices = shuffled_indices[:test_set_size]
#           train_indices = shuffled_indices[test_set_size:]
#           return data.iloc[train_indices], data.iloc[test_indices]
# You can then use this function like this:
#       >>> train_set, test_set = split_train_test(housing, 0.2)
#       >>> print(len(train_set), "train +", len(test_set), "test")
#       16512 train + 4128 test
# Well, this works, but it is not perfect: if you run the program again, it will generate a
# different test set! Over time, you (or your Machine Learning algorithms) will get to
# see the whole dataset, which is what you want to avoid.
# One solution is to save the test set on the first run and then load it in subsequent
# runs. Another option is to set the random number generator’s seed (e.g., np.ran
# dom.seed(42))13 before calling np.random.permutation(), so that it always generates
# the same shuffled indices.
# 
# 
# 
# 13 You will often see people set the random seed to 42. This number has no special property, other than to be
#    The Answer to the Ultimate Question of Life, the Universe, and Everything.
# 
# 
# 
#                                                                                              Get the Data   |   49
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Take a Quick Look at the Data Structure",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Take a Quick Look at the Data Structure"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Takea(HierNode):
    def __init__(self):
        super().__init__("Take a Quick Look at the Data Structure")
        self.add(Content())

# eof
