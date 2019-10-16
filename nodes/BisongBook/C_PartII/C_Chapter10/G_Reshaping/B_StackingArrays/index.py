# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Stacking Arrays
# NumPy has methods for concatenating arrays – also called stacking. The methods
# hstack and vstack are used to stack several arrays along the horizontal and vertical axis,
# respectively.
# 
# #   create a 2x2 matrix of random integers in the range of 1 to 20
# A   = np.random.randint(1, 50, size=[3,3])
# B   = np.random.randint(1, 50, size=[3,3])
# #   print out the arrays
# A
# 'Output':
# array([[19, 40, 31],
#        [ 5, 16, 38],
#        [22, 49,  9]])
# 
# B
# 'Output':
# array([[15, 22, 16],
#        [49, 26,  9],
#        [42, 13, 39]])
# 
#     Let’s stack A and B horizontally using hstack. To use hstack, the arrays must have
# the same number of rows. Also, the arrays to be stacked are passed as a tuple to the
# hstack method.
# 
# # arrays are passed    as tuple to hstack
# np.hstack((A,B))
# 'Output':
# array([[19, 40, 31,    15, 22, 16],
#        [ 5, 16, 38,    49, 26,  9],
#        [22, 49,  9,    42, 13, 39]])
# 
#     To stack A and B vertically using vstack, the arrays must have the same number of
# columns. The arrays to be stacked are also passed as a tuple to the vstack method.
# 
# # arrays are passed as tuple to hstack
# np.vstack((A,B))
# 'Output':
# array([[19, 40, 31],
#        [ 5, 16, 38],
#        [22, 49,  9],
#        [15, 22, 16],
#        [49, 26,  9],
#        [42, 13, 39]])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Stacking Arrays",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Stacking Arrays"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class StackingArrays(HierNode):
    def __init__(self):
        super().__init__("Stacking Arrays")
        self.add(Content())

# eof
