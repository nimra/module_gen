# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_BooleanMask.index import BooleanMask as A_BooleanMask
from .B_IntegerMask.index import IntegerMask as B_IntegerMask
from .C_Slicinga.index import Slicinga as C_Slicinga

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Indexing + Fancy Indexing (1-D)
# We can index a single element of a NumPy 1-D array similar to how we index a Python list.
# 
# # create a random numpy 1-D array
# my_array = np.random.rand(10)
# my_array
# 'Output': array([ 0.7736445 ,  0.28671796,  0.61980802,  0.42110553,
#                    0.86091567,  0.93953255,  0.300224  ,  0.56579416,
#                    0.58890282,   0.97219289])
# # index the first element
# my_array[0]
# 'Output': 0.77364449999999996
# # index the last element
# my_array[-1]
# 'Output': 0.97219288999999998
# 
#    Fancy indexing in NumPy is an advanced mechanism for indexing array elements
# based on integers or boolean. This technique is also called masking.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Indexing + Fancy Indexing (1-D)",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Indexing + Fancy Indexing (1-D)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Indexing(HierNode):
    def __init__(self):
        super().__init__("Indexing + Fancy Indexing (1-D)")
        self.add(Content())
        self.add(A_BooleanMask())
        self.add(B_IntegerMask())
        self.add(C_Slicinga())

# eof
