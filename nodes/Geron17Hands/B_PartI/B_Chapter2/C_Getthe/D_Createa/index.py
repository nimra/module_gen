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
#                   Download from finelybook www.finelybook.com
# But both these solutions will break next time you fetch an updated dataset. A com‐
# mon solution is to use each instance’s identifier to decide whether or not it should go
# in the test set (assuming instances have a unique and immutable identifier). For
# example, you could compute a hash of each instance’s identifier, keep only the last
# byte of the hash, and put the instance in the test set if this value is lower or equal to
# 51 (~20% of 256). This ensures that the test set will remain consistent across multiple
# runs, even if you refresh the dataset. The new test set will contain 20% of the new
# instances, but it will not contain any instance that was previously in the training set.
# Here is a possible implementation:
#        import hashlib
# 
#        def test_set_check(identifier, test_ratio, hash):
#            return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio
# 
#        def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
#            ids = data[id_column]
#            in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
#            return data.loc[~in_test_set], data.loc[in_test_set]
# Unfortunately, the housing dataset does not have an identifier column. The simplest
# solution is to use the row index as the ID:
#        housing_with_id = housing.reset_index()   # adds an `index` column
#        train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")
# If you use the row index as a unique identifier, you need to make sure that new data
# gets appended to the end of the dataset, and no row ever gets deleted. If this is not
# possible, then you can try to use the most stable features to build a unique identifier.
# For example, a district’s latitude and longitude are guaranteed to be stable for a few
# million years, so you could combine them into an ID like so:14
#        housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
#        train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")
# Scikit-Learn provides a few functions to split datasets into multiple subsets in various
# ways. The simplest function is train_test_split, which does pretty much the same
# thing as the function split_train_test defined earlier, with a couple of additional
# features. First there is a random_state parameter that allows you to set the random
# generator seed as explained previously, and second you can pass it multiple datasets
# with an identical number of rows, and it will split them on the same indices (this is
# very useful, for example, if you have a separate DataFrame for labels):
# 
# 
# 
# 
# 14 The location information is actually quite coarse, and as a result many districts will have the exact same ID, so
#      they will end up in the same set (test or train). This introduces some unfortunate sampling bias.
# 
# 
# 
# 50     |   Chapter 2: End-to-End Machine Learning Project
# 
#                  Download from finelybook www.finelybook.com
#     from sklearn.model_selection import train_test_split
# 
#     train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
# So far we have considered purely random sampling methods. This is generally fine if
# your dataset is large enough (especially relative to the number of attributes), but if it
# is not, you run the risk of introducing a significant sampling bias. When a survey
# company decides to call 1,000 people to ask them a few questions, they don’t just pick
# 1,000 people randomly in a phone booth. They try to ensure that these 1,000 people
# are representative of the whole population. For example, the US population is com‐
# posed of 51.3% female and 48.7% male, so a well-conducted survey in the US would
# try to maintain this ratio in the sample: 513 female and 487 male. This is called strati‐
# fied sampling: the population is divided into homogeneous subgroups called strata,
# and the right number of instances is sampled from each stratum to guarantee that the
# test set is representative of the overall population. If they used purely random sam‐
# pling, there would be about 12% chance of sampling a skewed test set with either less
# than 49% female or more than 54% female. Either way, the survey results would be
# significantly biased.
# Suppose you chatted with experts who told you that the median income is a very
# important attribute to predict median housing prices. You may want to ensure that
# the test set is representative of the various categories of incomes in the whole dataset.
# Since the median income is a continuous numerical attribute, you first need to create
# an income category attribute. Let’s look at the median income histogram more closely
# (see Figure 2-9):
# 
# 
# 
# 
# Figure 2-9. Histogram of income categories
# 
# Most median income values are clustered around 2–5 (tens of thousands of dollars),
# but some median incomes go far beyond 6. It is important to have a sufficient num‐
# 
# 
#                                                                          Get the Data   |   51
# 
#                    Download from finelybook www.finelybook.com
# ber of instances in your dataset for each stratum, or else the estimate of the stratum’s
# importance may be biased. This means that you should not have too many strata, and
# each stratum should be large enough. The following code creates an income category
# attribute by dividing the median income by 1.5 (to limit the number of income cate‐
# gories), and rounding up using ceil (to have discrete categories), and then merging
# all the categories greater than 5 into category 5:
#      housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
#      housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
# Now you are ready to do stratified sampling based on the income category. For this
# you can use Scikit-Learn’s StratifiedShuffleSplit class:
#      from sklearn.model_selection import StratifiedShuffleSplit
# 
#      split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
#      for train_index, test_index in split.split(housing, housing["income_cat"]):
#          strat_train_set = housing.loc[train_index]
#          strat_test_set = housing.loc[test_index]
# Let’s see if this worked as expected. You can start by looking at the income category
# proportions in the full housing dataset:
#      >>> housing["income_cat"].value_counts() / len(housing)
#      3.0    0.350581
#      2.0    0.318847
#      4.0    0.176308
#      5.0    0.114438
#      1.0    0.039826
#      Name: income_cat, dtype: float64
# With similar code you can measure the income category proportions in the test set.
# Figure 2-10 compares the income category proportions in the overall dataset, in the
# test set generated with stratified sampling, and in a test set generated using purely
# random sampling. As you can see, the test set generated using stratified sampling has
# income category proportions almost identical to those in the full dataset, whereas the
# test set generated using purely random sampling is quite skewed.
# 
# 
# 
# 
# Figure 2-10. Sampling bias comparison of stratified versus purely random sampling
# 
# 
# 52   |   Chapter 2: End-to-End Machine Learning Project
# 
#               Download from finelybook www.finelybook.com
# Now you should remove the income_cat attribute so the data is back to its original
# state:
#     for set in (strat_train_set, strat_test_set):
#         set.drop(["income_cat"], axis=1, inplace=True)
# We spent quite a bit of time on test set generation for a good reason: this is an often
# neglected but critical part of a Machine Learning project. Moreover, many of these
# ideas will be useful later when we discuss cross-validation. Now it’s time to move on
# to the next stage: exploring the data.
# 
# Discover and Visualize the Data to Gain Insights
# So far you have only taken a quick glance at the data to get a general understanding of
# the kind of data you are manipulating. Now the goal is to go a little bit more in depth.
# First, make sure you have put the test set aside and you are only exploring the train‐
# ing set. Also, if the training set is very large, you may want to sample an exploration
# set, to make manipulations easy and fast. In our case, the set is quite small so you can
# just work directly on the full set. Let’s create a copy so you can play with it without
# harming the training set:
#     housing = strat_train_set.copy()
# 
# 
# Visualizing Geographical Data
# Since there is geographical information (latitude and longitude), it is a good idea to
# create a scatterplot of all districts to visualize the data (Figure 2-11):
#     housing.plot(kind="scatter", x="longitude", y="latitude")
# 
# 
# 
# 
# Figure 2-11. A geographical scatterplot of the data
# 
# 
#                                                 Discover and Visualize the Data to Gain Insights   |   53
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Create a Test Set",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Createa(HierNode):
    def __init__(self):
        super().__init__("Create a Test Set")
        self.add(Content(), "content")

# eof
