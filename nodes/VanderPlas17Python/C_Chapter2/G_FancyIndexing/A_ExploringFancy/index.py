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
# Exploring Fancy Indexing
# Fancy indexing is conceptually simple: it means passing an array of indices to access
# multiple array elements at once. For example, consider the following array:
#     In[1]: import numpy as np
#            rand = np.random.RandomState(42)
# 
#            x = rand.randint(100, size=10)
#            print(x)
#     [51 92 14 71 60 20 82 86 74 74]
# Suppose we want to access three different elements. We could do it like this:
#     In[2]: [x[3], x[7], x[2]]
#     Out[2]: [71, 86, 14]
# Alternatively, we can pass a single list or array of indices to obtain the same result:
#     In[3]: ind = [3, 7, 4]
#            x[ind]
#     Out[3]: array([71, 86, 60])
# With fancy indexing, the shape of the result reflects the shape of the index arrays
# rather than the shape of the array being indexed:
#     In[4]: ind = np.array([[3, 7],
#                            [4, 5]])
#            x[ind]
#     Out[4]: array([[71, 86],
#                    [60, 20]])
# Fancy indexing also works in multiple dimensions. Consider the following array:
#     In[5]: X = np.arange(12).reshape((3, 4))
#            X
#     Out[5]: array([[ 0,    1, 2, 3],
#                    [ 4,    5, 6, 7],
#                    [ 8,    9, 10, 11]])
# Like with standard indexing, the first index refers to the row, and the second to the
# column:
#     In[6]: row = np.array([0, 1, 2])
#            col = np.array([2, 1, 3])
#            X[row, col]
#     Out[6]: array([ 2,    5, 11])
# 
# Notice that the first value in the result is X[0, 2], the second is X[1, 1], and the
# third is X[2, 3]. The pairing of indices in fancy indexing follows all the broadcasting
# rules that were mentioned in “Computation on Arrays: Broadcasting” on page 63. So,
# 
# 
#                                                                          Fancy Indexing   |   79
# 
# for example, if we combine a column vector and a row vector within the indices, we
# get a two-dimensional result:
#      In[7]: X[row[:, np.newaxis], col]
#      Out[7]: array([[ 2,          1, 3],
#                     [ 6,          5, 7],
#                     [10,          9, 11]])
# Here, each row value is matched with each column vector, exactly as we saw in broad‐
# casting of arithmetic operations. For example:
#      In[8]: row[:, np.newaxis] * col
#      Out[8]: array([[0, 0, 0],
#                     [2, 1, 3],
#                     [4, 2, 6]])
# It is always important to remember with fancy indexing that the return value reflects
# the broadcasted shape of the indices, rather than the shape of the array being indexed.
# 
# Combined Indexing
# For even more powerful operations, fancy indexing can be combined with the other
# indexing schemes we’ve seen:
#      In[9]: print(X)
#      [[ 0    1 2 3]
#       [ 4    5 6 7]
#       [ 8    9 10 11]]
# We can combine fancy and simple indices:
#      In[10]: X[2, [2, 0, 1]]
#      Out[10]: array([10,          8,    9])
# We can also combine fancy indexing with slicing:
#      In[11]: X[1:, [2, 0, 1]]
#      Out[11]: array([[ 6,          4,       5],
#                      [10,          8,       9]])
# And we can combine fancy indexing with masking:
#      In[12]: mask = np.array([1, 0, 1, 0], dtype=bool)
#              X[row[:, np.newaxis], mask]
#      Out[12]: array([[ 0, 2],
#                      [ 4, 6],
#                      [ 8, 10]])
# All of these indexing options combined lead to a very flexible set of operations for
# accessing and modifying array values.
# 
# 
# 80   |   Chapter 2: Introduction to NumPy
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Exploring Fancy Indexing",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ExploringFancy(HierNode):
    def __init__(self):
        super().__init__("Exploring Fancy Indexing")
        self.add(Content())

# eof
