# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Matrix Multiplication (Dot Product)
# First let’s create random integers using the method np.random.randint(low,
# high=None, size=None,) which returns random integers from low (inclusive) to high
# (exclusive).
# 
# # create a 3x3 matrix of random integers in the range of 1 to 50
# A = np.random.randint(1, 50, size=[3,3])
# B = np.random.randint(1, 50, size=[3,3])
# # print the arrays
# A
# 'Output':
# array([[15, 29, 24],
#        [ 5, 23, 26],
#        [30, 14, 44]])
# B
# 'Output':
# array([[38, 32, 22],
#        [32, 30, 46],
#        [33, 47, 24]])
# 
#    We can use the following routines for matrix multiplication, np.matmul(a,b) or
# a @ b if using Python 3.6. Using a @ b is preferred. Remember that when multiplying
# matrices, the inner matrix dimensions must agree. For example, if A is an m × n matrix
# and B is an n × p matrix, the product of the matrices will be an m × p matrix with the
# inner dimensions of the respective matrices n agreeing (see Figure 10-1).
# 
# 
# 
# 
# Figure 10-1. Matrix multiplication
# 
# # multiply the two matrices A and B (dot product)
# A @ B    # or np.matmul(A,B)
# 
# 'Output':
# array([[2290, 2478, 2240],
#        [1784, 2072, 1792],
#        [3040, 3448, 2360]])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Matrix Multiplication (Dot Product)",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Matrix Multiplication (Dot Product)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MatrixMultiplication(HierNode):
    def __init__(self):
        super().__init__("Matrix Multiplication (Dot Product)")
        self.add(Content())

# eof
