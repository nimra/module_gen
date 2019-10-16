# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Scalar Operation
# A matrix can be acted upon by a scalar (i.e., a single numeric entity) in the same way
# element-wise fashion. This time the scalar operates upon each element of the matrix or
# vector. See Figure 10-3.
# 
# 
# 
# 
# 
# Figure 10-3. Scalar operations
# 
#       Let’s look at some examples.
# 
# # Hadamard multiplication of A and a scalar, 0.5
# A * 0.5
# 'Output':
# array([[  7.5,  14.5,  12. ],
#        [  2.5,  11.5,  13. ],
#        [ 15. ,   7. ,  22. ]])
# # add A and a scalar, 0.5
# A + 0.5
# 'Output':
# array([[ 15.5,  29.5,  24.5],
#        [  5.5,  23.5,  26.5],
#        [ 30.5,  14.5,  44.5]])
# # subtract a scalar 0.5 from B
# B - 0.5
# 'Output':
# array([[ 37.5,  31.5,  21.5],
#        [ 31.5,  29.5,  45.5],
#        [ 32.5,  46.5,  23.5]])
# # divide A and a scalar, 0.5
# A / 0.5
# 'Output':
# array([[ 30.,  58.,  48.],
#        [ 10.,  46.,  52.],
#        [ 60.,  28.,  88.]])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Scalar Operation",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Scalar Operation"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ScalarOperation(HierNode):
    def __init__(self):
        super().__init__("Scalar Operation")
        self.add(Content())

# eof
