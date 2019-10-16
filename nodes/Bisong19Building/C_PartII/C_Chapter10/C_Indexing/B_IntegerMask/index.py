# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Integer Mask
# Let’s select all elements with even indices in the array.
# 
# # create 10 random integers between 1 and 20
# my_array = np.random.randint(1, 20, 10)
# my_array
# 'Output': array([ 1, 18,  8, 12, 10,  2, 17,  4, 17, 17])
# my_array[np.arange(1,10,2)]
# 'Output': array([18, 12,  2,  4, 17])
# 
#    Remember that array indices are indexed from 0. So the second element, 18, is in
# index 1.
# 
# np.arange(1,10,2)
# 'Output': array([1, 3, 5, 7, 9])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Integer Mask",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Integer Mask"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IntegerMask(HierNode):
    def __init__(self):
        super().__init__("Integer Mask")
        self.add(Content())

# eof
