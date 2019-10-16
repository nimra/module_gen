# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creating 3-D Arrays
# Let’s construct a basic 3-D array.
# 
# # construct a 3-D array
# my_3D = np.array([[
#                      [2,4,6],
#                      [8,10,12]
#                     ],[
#                      [1,2,3],
#                      [7,9,11]
#                     ]])
# my_3D
# 'Output':
# array([[[ 2,  4,  6],
#         [ 8, 10, 12]],
# 
#        [[ 1,  2,  3],
#         [ 7,  9, 11]]])
# 
# # check the number of dimensions
# my_3D.ndim
# 'Output': 3
# # get the shape of the 3-D array - this example has 2 pages, 2 rows and 3
# columns: (p, r, c)
# my_3D.shape
# 'Output': (2, 2, 3)
# 
#     We can also create 3-D arrays with methods such as ones, zeros, full, and empty
# by passing the configuration for [page, row, columns] into the shape parameter of the
# methods. For example:
# 
# # create a 2-page, 3x3 array of ones
# np.ones([2,3,3])
# 'Output':
# array([[[ 1.,  1.,  1.],
#         [ 1.,  1.,  1.],
#         [ 1.,  1.,  1.]],
# 
#        [[ 1.,  1.,  1.],
#         [ 1.,  1.,  1.],
#         [ 1.,  1.,  1.]]])
# # create a 2-page, 3x3 array of zeros
# np.zeros([2,3,3])
# 'Output':
# array([[[ 0.,  0.,  0.],
#         [ 0.,  0.,  0.],
#         [ 0.,  0.,  0.]],
# 
#        [[ 0.,  0.,  0.],
#         [ 0.,  0.,  0.],
#         [ 0.,  0.,  0.]]])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Creating 3-D Arrays",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Creating 3-D Arrays"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Creating3D(HierNode):
    def __init__(self):
        super().__init__("Creating 3-D Arrays")
        self.add(Content())

# eof
