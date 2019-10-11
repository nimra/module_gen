# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                                        Chapter 10   NumPy
# 
# # divide A and a scalar, 0.5
# A / 0.5
# 'Output':
# array([[ 30.,  58.,  48.],
#        [ 10.,  46.,  52.],
#        [ 60.,  28.,  88.]])
# 
# 
# M
#  atrix Transposition
# Transposition is a vital matrix operation that reverses the rows and columns of a matrix
# by flipping the row and column indices. The transpose of a matrix is denoted as AT.
# Observe that the diagonal elements remain unchanged. See Figure 10-4.
# 
# 
# 
# 
# Figure 10-4. Matrix transpose
# 
#    Let’s see an example.
# 
# A = np.array([[15, 29, 24],
#                 [ 5, 23, 26],
#                 [30, 14, 44]])
# # transpose A
# A.T   # or A.transpose()
# 'Output':
# array([[15,  5, 30],
#        [29, 23, 14],
#        [24, 26, 44]])
# 
# 
# 
# 
#                                                                                       105
# 
# Chapter 10   NumPy
# 
# 
# The Inverse of a Matrix
# A m × m matrix A (also called a square matrix) has an inverse if A times another matrix B
# results in the identity matrix I also of shape m × m. This matrix B is called the inverse of A
# and is denoted as A−1. This relationship is formally written as
# 
#                                        AA-1 = A-1 A = I
# 
#    However, not all matrices have an inverse. A matrix with an inverse is called a
# nonsingular or invertible matrix, while those without an inverse are known as singular or
# degenerate.
# 
# 
#  Note     A square matrix is a matrix that has the same number of rows and columns.
# 
#    Let’s use NumPy to get the inverse of a matrix. Some linear algebra modules are
# found in a sub-module of NumPy called linalg.
# 
# A = np.array([[15, 29, 24],
#                 [ 5, 23, 26],
#                 [30, 14, 44]])
# # find the inverse of A
# np.linalg.inv(A)
# 'Output':
# array([[ 0.05848375, -0.08483755,  0.01823105],
#        [ 0.05054152, -0.00541516, -0.02436823],
#        [-0.05595668,  0.05956679,  0.01805054]])
# 
#     NumPy also implements the Moore-Penrose pseudo inverse, which gives an inverse
# derivation for degenerate matrices. Here, we use the pinv method to find the inverses of
# invertible matrices.
# 
# # using pinv()
# np.linalg.pinv(A)
# 'Output':
# array([[ 0.05848375, -0.08483755,  0.01823105],
#        [ 0.05054152, -0.00541516, -0.02436823],
#        [-0.05595668,  0.05956679,  0.01805054]])
# 
# 106
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Matrix Transposition")
        self.add(MarkdownBlock("# Matrix Transposition"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MatrixTransposition(HierNode):
    def __init__(self):
        super().__init__("Matrix Transposition")
        self.add(Content())

# eof
