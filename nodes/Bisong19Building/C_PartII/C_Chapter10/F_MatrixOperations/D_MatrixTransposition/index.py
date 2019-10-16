# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Matrix Transposition
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Matrix Transposition",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Matrix Transposition"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MatrixTransposition(HierNode):
    def __init__(self):
        super().__init__("Matrix Transposition")
        self.add(Content())

# eof
