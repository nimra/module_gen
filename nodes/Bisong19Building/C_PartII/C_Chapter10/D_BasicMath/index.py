# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Basic Math Operations on Arrays: Universal Functions
#
# The core power of NumPy is in its highly optimized vectorized functions for various
# mathematical, arithmetic, and string operations. In NumPy these functions are called
# universal functions. We’ll explore a couple of basic arithmetic with NumPy 1-D arrays.
# 
# # create an array of even numbers between 2 and 10
# my_array = np.arange(2,11,2)
# 'Output': array([ 2,  4,  6,  8, 10])
# # sum of array elements
# np.sum(my_array) # or my_array.sum()
# 'Output': 30
# # square root
# np.sqrt(my_array)
# 'Output': array([ 1.41421356,  2.        ,  2.44948974,  2.82842712,
#                    3.16227766])
# # log
# np.log(my_array)
# 'Output': array([ 0.69314718,  1.38629436,  1.79175947,  2.07944154,
#                    2.30258509])
# # exponent
# np.exp(my_array)
# 'Output': array([  7.38905610e+00,   5.45981500e+01,   4.03428793e+02,
#                    2.98095799e+03,   2.20264658e+04])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Basic Math Operations on Arrays: Universal Functions",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Basic Math Operations on Arrays: Universal Functions"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BasicMath(HierNode):
    def __init__(self):
        super().__init__("Basic Math Operations on Arrays: Universal Functions")
        self.add(Content())

# eof
