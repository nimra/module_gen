# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The for Loop
# The for loop repeats the statements within its code block until a terminating condition
# is reached. It is different from the while loop in that it knows exactly how many times
# the iteration should occur. The for loop is controlled by an iterable expression (i.e.,
# expressions in which elements can be accessed sequentially). The for statement is
# visualized by the flowchart in Figure 9-4.
# 
# 
# 
# 
# Figure 9-4. Flowchart of the for loop
# 
#      The syntax for the for loop is as follows:
# 
# for item in iterable:
#     statement
# 
#     Note that in the for loop syntax is not the same as the membership logical operator
# earlier discussed.
#     Here is a program example:
# 
# a = [2, 4, 6, 8, 10]
# for elem in a:
#     print(elem**2)
# 
# 'Output': 4
#     16
#     36
#     64
#     100
# 
#      To loop for a specific number of time, use the range() function.
# 
# for idx in range(5):
#     print('The index is', idx)
# 
# 'Output': The index is 0
#      The index is 1
#      The index is 2
#      The index is 3
#      The index is 4

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The for Loop",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# The for Loop"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Thefor(HierNode):
    def __init__(self):
        super().__init__("The for Loop")
        self.add(Content())

# eof
