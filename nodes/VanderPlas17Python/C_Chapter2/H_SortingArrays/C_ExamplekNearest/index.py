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
#                            [6, 3, 7, 4, 6, 7],
#                            [7, 6, 7, 4, 9, 9]])
#      In[11]: # sort each row of X
#              np.sort(X, axis=1)
#      Out[11]: array([[3,         4,   6,    6,   7,   9],
#                      [2,         3,   4,    6,   7,   7],
#                      [1,         2,   4,    5,   7,   7],
#                      [0,         1,   4,    5,   5,   9]])
# Keep in mind that this treats each row or column as an independent array, and any
# relationships between the row or column values will be lost!
# 
# Partial Sorts: Partitioning
# Sometimes we’re not interested in sorting the entire array, but simply want to find the
# K smallest values in the array. NumPy provides this in the np.partition function.
# np.partition takes an array and a number K; the result is a new array with the small‐
# est K values to the left of the partition, and the remaining values to the right, in arbi‐
# trary order:
#      In[12]: x = np.array([7, 2, 3, 1, 6, 5, 4])
#              np.partition(x, 3)
#      Out[12]: array([2, 1, 3, 4, 6, 5, 7])
# Note that the first three values in the resulting array are the three smallest in the
# array, and the remaining array positions contain the remaining values. Within the
# two partitions, the elements have arbitrary order.
# Similarly to sorting, we can partition along an arbitrary axis of a multidimensional
# array:
#      In[13]: np.partition(X, 2, axis=1)
#      Out[13]: array([[3,         4,   6,    7,   6,   9],
#                      [2,         3,   4,    7,   6,   7],
#                      [1,         2,   4,    5,   7,   7],
#                      [0,         1,   4,    5,   9,   5]])
# The result is an array where the first two slots in each row contain the smallest values
# from that row, with the remaining values filling the remaining slots.
# Finally, just as there is a np.argsort that computes indices of the sort, there is a
# np.argpartition that computes indices of the partition. We’ll see this in action in the
# following section.
# 
# Example: k-Nearest Neighbors
# Let’s quickly see how we might use this argsort function along multiple axes to find
# the nearest neighbors of each point in a set. We’ll start by creating a random set of 10
# 
# 88   |   Chapter 2: Introduction to NumPy
# 
# points on a two-dimensional plane. Using the standard convention, we’ll arrange
# these in a 10×2 array:
#     In[14]: X = rand.rand(10, 2)
# To get an idea of how these points look, let’s quickly scatter plot them (Figure 2-10):
#     In[15]: %matplotlib inline
#             import matplotlib.pyplot as plt
#             import seaborn; seaborn.set() # Plot styling
#             plt.scatter(X[:, 0], X[:, 1], s=100);
# 
# 
# 
# 
# Figure 2-10. Visualization of points in the k-neighbors example
# 
# Now we’ll compute the distance between each pair of points. Recall that the squared-
# distance between two points is the sum of the squared differences in each dimension;
# using the efficient broadcasting (“Computation on Arrays: Broadcasting” on page 63)
# and aggregation (“Aggregations: Min, Max, and Everything in Between” on page 58)
# routines provided by NumPy, we can compute the matrix of square distances in a sin‐
# gle line of code:
#     In[16]: dist_sq = np.sum((X[:,np.newaxis,:] - X[np.newaxis,:,:]) ** 2, axis=-1)
# This operation has a lot packed into it, and it might be a bit confusing if you’re unfa‐
# miliar with NumPy’s broadcasting rules. When you come across code like this, it can
# be useful to break it down into its component steps:
#     In[17]: # for each pair of points, compute differences in their coordinates
#             differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
#             differences.shape
#     Out[17]: (10, 10, 2)
# 
# 
# 
# 
#                                                                         Sorting Arrays   |   89
# 
#      In[18]: # square the coordinate differences
#              sq_differences = differences ** 2
#              sq_differences.shape
#      Out[18]: (10, 10, 2)
#      In[19]: # sum the coordinate differences to get the squared distance
#              dist_sq = sq_differences.sum(-1)
#              dist_sq.shape
#      Out[19]: (10, 10)
# Just to double-check what we are doing, we should see that the diagonal of this matrix
# (i.e., the set of distances between each point and itself) is all zero:
#      In[20]: dist_sq.diagonal()
#      Out[20]: array([ 0.,                    0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.,   0.])
# 
# It checks out! With the pairwise square-distances converted, we can now use np.arg
# sort to sort along each row. The leftmost columns will then give the indices of the
# nearest neighbors:
#      In[21]: nearest = np.argsort(dist_sq, axis=1)
#              print(nearest)
#      [[0   3   9   7   1   4   2   5   6   8]
#       [1   4   7   9   3   6   8   5   0   2]
#       [2   1   4   6   3   0   8   9   7   5]
#       [3   9   7   0   1   4   5   8   6   2]
#       [4   1   8   5   6   7   9   3   0   2]
#       [5   8   6   4   1   7   9   3   2   0]
#       [6   8   5   4   1   7   9   3   2   0]
#       [7   9   3   1   4   0   5   8   6   2]
#       [8   5   6   4   1   7   9   3   2   0]
#       [9   7   3   0   1   4   5   8   6   2]]
# Notice that the first column gives the numbers 0 through 9 in order: this is due to the
# fact that each point’s closest neighbor is itself, as we would expect.
# By using a full sort here, we’ve actually done more work than we need to in this case.
# If we’re simply interested in the nearest k neighbors, all we need is to partition each
# row so that the smallest k + 1 squared distances come first, with larger distances fill‐
# ing the remaining positions of the array. We can do this with the np.argpartition
# function:
#      In[22]: K = 2
#              nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)
# In order to visualize this network of neighbors, let’s quickly plot the points along with
# lines representing the connections from each point to its two nearest neighbors
# (Figure 2-11):
# 
# 
# 
# 
# 90   | Chapter 2: Introduction to NumPy
# 
#     In[23]: plt.scatter(X[:, 0], X[:, 1], s=100)
# 
#             # draw lines from each point to its two nearest neighbors
#             K = 2
# 
#             for i in range(X.shape[0]):
#                 for j in nearest_partition[i, :K+1]:
#                     # plot a line from X[i] to X[j]
#                     # use some zip magic to make it happen:
#                     plt.plot(*zip(X[j], X[i]), color='black')
# 
# 
# 
# 
# Figure 2-11. Visualization of the neighbors of each point
# 
# Each point in the plot has lines drawn to its two nearest neighbors. At first glance, it
# might seem strange that some of the points have more than two lines coming out of
# them: this is due to the fact that if point A is one of the two nearest neighbors of point
# B, this does not necessarily imply that point B is one of the two nearest neighbors of
# point A.
# Although the broadcasting and row-wise sorting of this approach might seem less
# straightforward than writing a loop, it turns out to be a very efficient way of operating
# on this data in Python. You might be tempted to do the same type of operation by
# manually looping through the data and sorting each set of neighbors individually, but
# this would almost certainly lead to a slower algorithm than the vectorized version we
# used. The beauty of this approach is that it’s written in a way that’s agnostic to the size
# of the input data: we could just as easily compute the neighbors among 100 or
# 1,000,000 points in any number of dimensions, and the code would look the same.
# Finally, I’ll note that when doing very large nearest-neighbor searches, there are tree-
# based and/or approximate algorithms that can scale as � N log N or better rather
# 
# 
# 
# 
#                                                                          Sorting Arrays   |   91
# 
# than the � N 2 of the brute-force algorithm. One example of this is the KD-Tree,
# implemented in Scikit-Learn.
# 
# 
#                                             Big-O Notation
#      Big-O notation is a means of describing how the number of operations required for
#      an algorithm scales as the input grows in size. To use it correctly is to dive deeply into
#      the realm of computer science theory, and to carefully distinguish it from the related
#      small-o notation, big-θ notation, big-Ω notation, and probably many mutant hybrids
#      thereof. While these distinctions add precision to statements about algorithmic scal‐
#      ing, outside computer science theory exams and the remarks of pedantic blog com‐
#      menters, you’ll rarely see such distinctions made in practice. Far more common in the
#      data science world is a less rigid use of big-O notation: as a general (if imprecise)
#      description of the scaling of an algorithm. With apologies to theorists and pedants,
#      this is the interpretation we’ll use throughout this book.
#      Big-O notation, in this loose sense, tells you how much time your algorithm will take
#      as you increase the amount of data. If you have an � N (read “order N”) algorithm
#      that takes 1 second to operate on a list of length N=1,000, then you should expect it to
#      take roughly 5 seconds for a list of length N=5,000. If you have an � N 2 (read “order
#      N squared”) algorithm that takes 1 second for N=1,000, then you should expect it to
#      take about 25 seconds for N=5,000.
#      For our purposes, the N will usually indicate some aspect of the size of the dataset (the
#      number of points, the number of dimensions, etc.). When trying to analyze billions or
#      trillions of samples, the difference between � N and � N 2 can be far from trivial!
#      Notice that the big-O notation by itself tells you nothing about the actual wall-clock
#      time of a computation, but only about its scaling as you change N. Generally, for
#      example, an � N algorithm is considered to have better scaling than an � N 2 algo‐
#      rithm, and for good reason. But for small datasets in particular, the algorithm with
#      better scaling might not be faster. For example, in a given problem an � N 2 algo‐
#      rithm might take 0.01 seconds, while a “better” � N algorithm might take 1 second.
#      Scale up N by a factor of 1,000, though, and the � N algorithm will win out.
#      Even this loose version of Big-O notation can be very useful for comparing the per‐
#      formance of algorithms, and we’ll use this notation throughout the book when talking
#      about how algorithms scale.
# 
# 
# 
# Structured Data: NumPy’s Structured Arrays
# While often our data can be well represented by a homogeneous array of values,
# sometimes this is not the case. This section demonstrates the use of NumPy’s struc‐
# tured arrays and record arrays, which provide efficient storage for compound, hetero‐
# 
# 92     | Chapter 2: Introduction to NumPy
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Example: k-Nearest Neighbors",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ExamplekNearest(HierNode):
    def __init__(self):
        super().__init__("Example: k-Nearest Neighbors")
        self.add(Content())

# eof
