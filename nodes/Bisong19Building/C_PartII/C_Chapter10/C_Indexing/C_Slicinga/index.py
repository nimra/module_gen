# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Slicing a 1-D Array
# Slicing a NumPy array is also similar to slicing a Python list.
# 
# my_array = np.array([14,  9,  3, 19, 16,  1, 16,  5, 13,  3])
# my_array
# 'Output': array([14,  9,  3, 19, 16,  1, 16,  5, 13,  3])
# # slice the first 2 elements
# my_array[:2]
# 'Output': array([14,  9])
# # slice the last 3 elements
# my_array[-3:]
# 'Output': array([ 5, 13,  3])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Slicing a 1-D Array",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Slicing a 1-D Array"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Slicinga(HierNode):
    def __init__(self):
        super().__init__("Slicing a 1-D Array")
        self.add(Content())

# eof
