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
#      In[29]: np.multiply.accumulate(x)
#      Out[29]: array([         1,     2,     6,    24, 120])
# Note that for these particular cases, there are dedicated NumPy functions to compute
# the results (np.sum, np.prod, np.cumsum, np.cumprod), which we’ll explore in “Aggre‐
# gations: Min, Max, and Everything in Between” on page 58.
# 
# Outer products
# Finally, any ufunc can compute the output of all pairs of two different inputs using
# the outer method. This allows you, in one line, to do things like create a multiplica‐
# tion table:
#      In[30]: x = np.arange(1, 6)
#              np.multiply.outer(x, x)
#      Out[30]: array([[        1,    2,     3,    4,    5],
#                      [        2,    4,     6,    8,   10],
#                      [        3,    6,     9,   12,   15],
#                      [        4,    8,    12,   16,   20],
#                      [        5,   10,    15,   20,   25]])
# 
# The ufunc.at and ufunc.reduceat methods, which we’ll explore in “Fancy Index‐
# ing” on page 78, are very helpful as well.
# Another extremely useful feature of ufuncs is the ability to operate between arrays of
# different sizes and shapes, a set of operations known as broadcasting. This subject is
# important enough that we will devote a whole section to it (see “Computation on
# Arrays: Broadcasting” on page 63).
# 
# Ufuncs: Learning More
# More information on universal functions (including the full list of available func‐
# tions) can be found on the NumPy and SciPy documentation websites.
# Recall that you can also access information directly from within IPython by import‐
# ing the packages and using IPython’s tab-completion and help (?) functionality, as
# described in “Help and Documentation in IPython” on page 3.
# 
# Aggregations: Min, Max, and Everything in Between
# Often when you are faced with a large amount of data, a first step is to compute sum‐
# mary statistics for the data in question. Perhaps the most common summary statistics
# are the mean and standard deviation, which allow you to summarize the “typical” val‐
# ues in a dataset, but other aggregates are useful as well (the sum, product, median,
# minimum and maximum, quantiles, etc.).
# 
# 
# 
# 
# 58   |   Chapter 2: Introduction to NumPy
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Ufuncs: Learning More",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UfuncsLearning(HierNode):
    def __init__(self):
        super().__init__("Ufuncs: Learning More")
        self.add(Content())

# eof