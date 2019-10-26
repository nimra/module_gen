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
# Evidently, even this very simple classifier can successfully separate space talk from
# computer talk, but it gets confused between talk about religion and talk about Chris‐
# tianity. This is perhaps an expected area of confusion!
# The very cool thing here is that we now have the tools to determine the category for
# any string, using the predict() method of this pipeline. Here’s a quick utility func‐
# tion that will return the prediction for a single string:
#     In[13]: def predict_category(s, train=train, model=model):
#                 pred = model.predict([s])
#                 return train.target_names[pred[0]]
# Let’s try it out:
#     In[14]: predict_category('sending a payload to the ISS')
#     Out[14]: 'sci.space'
#     In[15]: predict_category('discussing islam vs atheism')
#     Out[15]: 'soc.religion.christian'
#     In[16]: predict_category('determining the screen resolution')
#     Out[16]: 'comp.graphics'
# Remember that this is nothing more sophisticated than a simple probability model
# for the (weighted) frequency of each word in the string; nevertheless, the result is
# striking. Even a very naive algorithm, when used carefully and trained on a large set
# of high-dimensional data, can be surprisingly effective.
# 
# When to Use Naive Bayes
# Because naive Bayesian classifiers make such stringent assumptions about data, they
# will generally not perform as well as a more complicated model. That said, they have
# several advantages:
# 
#   • They are extremely fast for both training and prediction
#   • They provide straightforward probabilistic prediction
#   • They are often very easily interpretable
#   • They have very few (if any) tunable parameters
# 
# These advantages mean a naive Bayesian classifier is often a good choice as an initial
# baseline classification. If it performs suitably, then congratulations: you have a very
# fast, very interpretable classifier for your problem. If it does not perform well, then
# you can begin exploring more sophisticated models, with some baseline knowledge of
# how well they should perform.
# Naive Bayes classifiers tend to perform especially well in one of the following
# situations:
# 
#                                                       In Depth: Naive Bayes Classification |   389
# 
#   • When the naive assumptions actually match the data (very rare in practice)
#   • For very well-separated categories, when model complexity is less important
#   • For very high-dimensional data, when model complexity is less important
# 
# The last two points seem distinct, but they actually are related: as the dimension of a
# dataset grows, it is much less likely for any two points to be found close together
# (after all, they must be close in every single dimension to be close overall). This means
# that clusters in high dimensions tend to be more separated, on average, than clusters
# in low dimensions, assuming the new dimensions actually add information. For this
# reason, simplistic classifiers like naive Bayes tend to work as well or better than more
# complicated classifiers as the dimensionality grows: once you have enough data, even
# a simple model can be very powerful.
# 
# In Depth: Linear Regression
# Just as naive Bayes (discussed earlier in “In Depth: Naive Bayes Classification” on
# page 382) is a good starting point for classification tasks, linear regression models are
# a good starting point for regression tasks. Such models are popular because they can
# be fit very quickly, and are very interpretable. You are probably familiar with the sim‐
# plest form of a linear regression model (i.e., fitting a straight line to data), but such
# models can be extended to model more complicated data behavior.
# In this section we will start with a quick intuitive walk-through of the mathematics
# behind this well-known problem, before moving on to see how linear models can be
# generalized to account for more complicated patterns in data. We begin with the stan‐
# dard imports:
#       In[1]: %matplotlib inline
#              import matplotlib.pyplot as plt
#              import seaborn as sns; sns.set()
#              import numpy as np
# 
# 
# Simple Linear Regression
# We will start with the most familiar linear regression, a straight-line fit to data. A
# straight-line fit is a model of the form y = ax + b where a is commonly known as the
# slope, and b is commonly known as the intercept.
# Consider the following data, which is scattered about a line with a slope of 2 and an
# intercept of –5 (Figure 5-42):
#       In[2]: rng = np.random.RandomState(1)
#              x = 10 * rng.rand(50)
#              y = 2 * x - 5 + rng.randn(50)
#              plt.scatter(x, y);
# 
# 
# 
# 390   |   Chapter 5: Machine Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "When to Use Naive Bayes",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Whento(HierNode):
    def __init__(self):
        super().__init__("When to Use Naive Bayes")
        self.add(Content())

# eof
