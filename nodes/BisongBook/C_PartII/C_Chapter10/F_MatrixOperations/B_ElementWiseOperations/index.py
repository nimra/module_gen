# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Element-Wise Operations
# Element-wise matrix operations involve matrices operating on themselves in an
# element-wise fashion. The action can be an addition, subtraction, division, or
# multiplication (which is commonly called the Hadamard product). The matrices must be
# of the same shape. Please note that while a matrix is of shape n × n, a vector is of shape
# n × 1. These concepts easily apply to vectors as well. See Figure 10-2.
# 
# 
# 
# 
# Figure 10-2. Element-wise matrix operations
#       Let’s have some examples.
# 
# # Hadamard multiplication of A and B
# A * B
# 'Output':
# array([[ 570,  928,  528],
#        [ 160,  690, 1196],
#        [ 990,  658, 1056]])
# # add A and B
# A + B
# 'Output':
# array([[53, 61, 46],
#        [37, 53, 72],
#        [63, 61, 68]])
# # subtract A from B
# B - A
# 'Output':
# array([[ 23,   3,  -2],
#        [ 27,   7,  20],
#        [  3,  33, -20]])
# # divide A with B
# A / B
# 'Output':
# array([[ 0.39473684,  0.90625   ,  1.09090909],
#        [ 0.15625   ,  0.76666667,  0.56521739],
#        [ 0.90909091,  0.29787234,  1.83333333]])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Element-Wise Operations",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Element-Wise Operations"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ElementWiseOperations(HierNode):
    def __init__(self):
        super().__init__("Element-Wise Operations")
        self.add(Content())

# eof
