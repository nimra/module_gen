# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Boolean Operations
# Boolean operations evaluate to True or False. Boolean operators include the comparison
# and logical operators. The comparison operators include less than or equal to <=, less
# than <, greater than or equal to >=, greater than >, not equal to !=, and equal to ==.
# 
# 2 < 5
# 'Output': True
# 2 <= 5
# 'Output': True
# 2 > 5
# 'Output':   False
# 2 >= 5
# 'Output':   False
# 2 != 5
# 'Output':   True
# 2 == 5
# 'Output':   False
# 
#    The logical operators include Boolean NOT (not), Boolean AND (and), and Boolean
# OR (or). We can also carry out identity and membership tests using
# 
#       •   is, is not (identity)
# 
#       •   in, not in (membership)
# 
# a = [1, 2, 3]
# 2 in a
# 'Output': True
# 2 not in a
# 'Output': False
# 2 is a
# 'Output': False
# 2 is not a
# 'Output': True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Boolean Operations",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Boolean Operations"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BooleanOperations(HierNode):
    def __init__(self):
        super().__init__("Boolean Operations")
        self.add(Content())

# eof
