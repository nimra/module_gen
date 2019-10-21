# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Indexing/Slicing of Matrices
# Let’s see some examples of indexing and slicing 2-D arrays. The concept extends nicely
# from doing the same with 1-D arrays.
# 
# # create a 3x3 array contain random normal numbers
# my_3D = np.random.randn(3,3)
# 'Output':
# array([[ 0.99709882, -0.41960273,  0.12544161],
#        [-0.21474247,  0.99555079,  0.62395035],
#        [-0.32453132,  0.3119651 , -0.35781825]])
# # select a particular cell (or element) from a 2-D array.
# my_3D[1,1]    # In this case, the cell at the 2nd row and column
# 'Output': 0.99555079000000002
# # slice the last 3 columns
# my_3D[:,1:3]
# 'Output':
# array([[-0.41960273,  0.12544161],
#        [ 0.99555079,  0.62395035],
#        [ 0.3119651 , -0.35781825]])
# # slice the first 2 rows and columns
# my_3D[0:2, 0:2]
# 'Output':
# array([[ 0.99709882, -0.41960273],
#        [-0.21474247,  0.99555079]])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Indexing/Slicing of Matrices",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Indexing/Slicing of Matrices"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IndexingSlicingof(HierNode):
    def __init__(self):
        super().__init__("Indexing/Slicing of Matrices")
        self.add(Content())

# eof
