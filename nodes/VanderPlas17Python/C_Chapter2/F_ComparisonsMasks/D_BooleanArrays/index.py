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
# Note that the parentheses here are important—because of operator precedence rules,
# with parentheses removed this expression would be evaluated as follows, which
# results in an error:
#     inches > (0.5 & inches) < 1
# Using the equivalence of A AND B and NOT (A OR B) (which you may remember if
# you’ve taken an introductory logic course), we can compute the same result in a dif‐
# ferent manner:
#     In[24]: np.sum(~( (inches <= 0.5) | (inches >= 1) ))
#     Out[24]: 29
# Combining comparison operators and Boolean operators on arrays can lead to a wide
# range of efficient logical operations.
# The following table summarizes the bitwise Boolean operators and their equivalent
# ufuncs:
# 
# Operator Equivalent ufunc
# &         np.bitwise_and
# |         np.bitwise_or
# ^         np.bitwise_xor
# ~         np.bitwise_not
# 
# 
# Using these tools, we might start to answer the types of questions we have about our
# weather data. Here are some examples of results we can compute when combining
# masking with aggregations:
#     In[25]: print("Number days without rain:      ",   np.sum(inches == 0))
#             print("Number days with rain:         ",   np.sum(inches != 0))
#             print("Days with more than 0.5 inches:",   np.sum(inches > 0.5))
#             print("Rainy days with < 0.1 inches :",    np.sum((inches > 0) &
#                                                               (inches < 0.2)))
#     Number days without rain:         215
#     Number days with rain:            150
#     Days with more than 0.5 inches:   37
#     Rainy days with < 0.1 inches :    75
# 
# 
# Boolean Arrays as Masks
# In the preceding section, we looked at aggregates computed directly on Boolean
# arrays. A more powerful pattern is to use Boolean arrays as masks, to select particular
# subsets of the data themselves. Returning to our x array from before, suppose we
# want an array of all values in the array that are less than, say, 5:
# 
# 
# 
# 
#                                                     Comparisons, Masks, and Boolean Logic   |   75
# 
#      In[26]: x
#      Out[26]: array([[5, 0, 3, 3],
#                      [7, 9, 3, 5],
#                      [2, 4, 7, 6]])
# We can obtain a Boolean array for this condition easily, as we’ve already seen:
#      In[27]: x < 5
#      Out[27]: array([[False, True, True, True],
#                      [False, False, True, False],
#                      [ True, True, False, False]], dtype=bool)
# Now to select these values from the array, we can simply index on this Boolean array;
# this is known as a masking operation:
#      In[28]: x[x < 5]
#      Out[28]: array([0, 3, 3, 3, 2, 4])
# What is returned is a one-dimensional array filled with all the values that meet this
# condition; in other words, all the values in positions at which the mask array is True.
# We are then free to operate on these values as we wish. For example, we can compute
# some relevant statistics on our Seattle rain data:
#      In[29]:
#      # construct a mask of all rainy days
#      rainy = (inches > 0)
# 
#      # construct a mask of all summer days (June 21st is the 172nd day)
#      summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)
# 
#      print("Median precip on rainy days in 2014 (inches):   ",
#            np.median(inches[rainy]))
#      print("Median precip on summer days in 2014 (inches): ",
#            np.median(inches[summer]))
#      print("Maximum precip on summer days in 2014 (inches): ",
#            np.max(inches[summer]))
#      print("Median precip on non-summer rainy days (inches):",
#            np.median(inches[rainy & ~summer]))
#      Median precip on rainy days in 2014 (inches):      0.194881889764
#      Median precip on summer days in 2014 (inches):     0.0
#      Maximum precip on summer days in 2014 (inches):    0.850393700787
#      Median precip on non-summer rainy days (inches):   0.200787401575
# By combining Boolean operations, masking operations, and aggregates, we can very
# quickly answer these sorts of questions for our dataset.
# 
# 
# 
# 
# 76   |   Chapter 2: Introduction to NumPy
# 
#            Using the Keywords and/or Versus the Operators &/|
# One common point of confusion is the difference between the keywords and and or
# on one hand, and the operators & and | on the other hand. When would you use one
# versus the other?
# The difference is this: and and or gauge the truth or falsehood of entire object, while &
# and | refer to bits within each object.
# When you use and or or, it’s equivalent to asking Python to treat the object as a single
# Boolean entity. In Python, all nonzero integers will evaluate as True. Thus:
#     In[30]: bool(42), bool(0)
#     Out[30]: (True, False)
#     In[31]: bool(42 and 0)
#     Out[31]: False
#     In[32]: bool(42 or 0)
#     Out[32]: True
# 
# When you use & and | on integers, the expression operates on the bits of the element,
# applying the and or the or to the individual bits making up the number:
#     In[33]: bin(42)
#     Out[33]: '0b101010'
#     In[34]: bin(59)
#     Out[34]: '0b111011'
#     In[35]: bin(42 & 59)
#     Out[35]: '0b101010'
#     In[36]: bin(42 | 59)
#     Out[36]: '0b111011'
# Notice that the corresponding bits of the binary representation are compared in order
# to yield the result.
# When you have an array of Boolean values in NumPy, this can be thought of as a
# string of bits where 1 = True and 0 = False, and the result of & and | operates in a
# similar manner as before:
#     In[37]: A = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
#             B = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
#             A | B
#     Out[37]: array([ True,    True,   True, False,   True,    True], dtype=bool)
# 
# 
# 
# 
#                                                      Comparisons, Masks, and Boolean Logic   |   77
# 
#      Using or on these arrays will try to evaluate the truth or falsehood of the entire array
#      object, which is not a well-defined value:
#            In[38]: A or B
#            ---------------------------------------------------------------------------
# 
#            ValueError                                   Traceback (most recent call last)
# 
#            <ipython-input-38-5d8e4f2e21c0> in <module>()
#            ----> 1 A or B
# 
# 
#            ValueError: The truth value of an array with more than one element is...
# 
#      Similarly, when doing a Boolean expression on a given array, you should use | or &
#      rather than or or and:
#            In[39]: x = np.arange(10)
#                    (x > 4) & (x < 8)
#            Out[39]: array([False, False, ...,   True,    True, False, False], dtype=bool)
#      Trying to evaluate the truth or falsehood of the entire array will give the same
#      ValueError we saw previously:
#            In[40]: (x > 4) and (x < 8)
#            ---------------------------------------------------------------------------
# 
#            ValueError                                   Traceback (most recent call last)
# 
#            <ipython-input-40-3d24f1ffd63d> in <module>()
#            ----> 1 (x > 4) and (x < 8)
# 
# 
#            ValueError: The truth value of an array with more than one element is...
# 
#      So remember this: and and or perform a single Boolean evaluation on an entire
#      object, while & and | perform multiple Boolean evaluations on the content (the indi‐
#      vidual bits or bytes) of an object. For Boolean NumPy arrays, the latter is nearly
#      always the desired operation.
# 
# 
# 
# Fancy Indexing
# In the previous sections, we saw how to access and modify portions of arrays using
# simple indices (e.g., arr[0]), slices (e.g., arr[:5]), and Boolean masks (e.g., arr[arr
# > 0]). In this section, we’ll look at another style of array indexing, known as fancy
# indexing. Fancy indexing is like the simple indexing we’ve already seen, but we pass
# arrays of indices in place of single scalars. This allows us to very quickly access and
# modify complicated subsets of an array’s values.
# 
# 78     |   Chapter 2: Introduction to NumPy
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Boolean Arrays as Masks",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BooleanArrays(HierNode):
    def __init__(self):
        super().__init__("Boolean Arrays as Masks")
        self.add(Content())

# eof