# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The while Loop
# The while loop evaluates a condition, which, if true, repeatedly executes the set of
# instructions within the while block. It does so until the condition evaluates to false. The
# while statement is visualized by the flowchart in Figure 9-3.
# 
# 
# 
# 
# Figure 9-3. Flowchart of the while loop
# 
#      Here is a program example:
# 
# a = 8
# while a > 0:
#     print('Number is', a)
# 
#     # decrement a
#     a -= 1
# 
# 'Output': Number is 8
#      Number is 7
#      Number is 6
#      Number is 5
#      Number is 4
#      Number is 3
#      Number is 2
#      Number is 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The while Loop",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# The while Loop"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Thewhile(HierNode):
    def __init__(self):
        super().__init__("The while Loop")
        self.add(Content())

# eof
