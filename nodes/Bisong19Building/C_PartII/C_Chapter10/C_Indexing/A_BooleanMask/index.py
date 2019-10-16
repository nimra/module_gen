# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Boolean Mask
# Let’s index all the even integers in the array using a boolean mask.
# 
# # create 10 random integers between 1 and 20
# my_array = np.random.randint(1, 20, 10)
# my_array
# 'Output': array([14,  9,  3, 19, 16,  1, 16,  5, 13,  3])
# # index all even integers in the array using a boolean mask
# my_array[my_array % 2 == 0]
# 'Output': array([14, 16, 16])
# 
#      Observe that the code my_array % 2 == 0 outputs an array of booleans.
# 
# my_array % 2 == 0
# 'Output': array([ True, False, False, False,  True, False,  True, False,
# False, False], dtype=bool)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Boolean Mask",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Boolean Mask"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BooleanMask(HierNode):
    def __init__(self):
        super().__init__("Boolean Mask")
        self.add(Content())

# eof
