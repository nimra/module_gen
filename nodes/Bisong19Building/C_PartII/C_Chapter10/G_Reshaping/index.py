# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Reshapevs.index import Reshapevs as A_Reshapevs
from .B_StackingArrays.index import StackingArrays as B_StackingArrays

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reshaping
# A NumPy array can be restructured to take on a different shape. Let’s convert a 1-D array
# to a m × n matrix.
# 
# # make 20 elements evenly spaced between 0 and 5
# a = np.linspace(0,5,20)
# a
# 'Output':
# array([ 0.        ,  0.26315789,  0.52631579,  0.78947368,  1.05263158,
#         1.31578947,  1.57894737,  1.84210526,  2.10526316,  2.36842105,
#         2.63157895,  2.89473684,  3.15789474,  3.42105263,  3.68421053,
#         3.94736842,  4.21052632,  4.47368421,  4.73684211,  5.        ])
# # observe that a is a 1-D array
# a.shape
# 'Output': (20,)
# # reshape into a 5 x 4 matrix
# A = a.reshape(5, 4)
# A
# 'Output':
# array([[ 0.        ,  0.26315789,  0.52631579,  0.78947368],
#        [ 1.05263158,  1.31578947,  1.57894737,  1.84210526],
#        [ 2.10526316,  2.36842105,  2.63157895,  2.89473684],
#        [ 3.15789474,  3.42105263,  3.68421053,  3.94736842],
#        [ 4.21052632,  4.47368421,  4.73684211,  5.        ]])
# # The vector a has been reshaped into a 5 by 4 matrix A
# A.shape
# 'Output': (5, 4)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Reshaping",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Reshaping"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Reshaping(HierNode):
    def __init__(self):
        super().__init__("Reshaping")
        self.add(Content())
        self.add(A_Reshapevs())
        self.add(B_StackingArrays())

# eof
