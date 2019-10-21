# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The break and continue Statements
# The break statement terminates the execution of the nearest enclosing loop (for, while
# loops) in which it appears.
# 
# for val in range(0,10):
#     print("The variable val is:", val)
#     if val > 5:
#         print("Break out of for loop")
#         break
# 
# 'Output': The variable val is: 0
#      The variable val is: 1
#      The variable val is: 2
#      The variable val is: 3
#      The variable val is: 4
#      The variable val is: 5
#      The variable val is: 6
#      Break out of for loop
# 
#     The continue statement skips the next iteration of the loop to which it belongs,
# ignoring any code after it.
# 
# a = 6
# while a > 0:
#     if a != 3:
#         print("The variable a is:", a)
#     # decrement a
#     a = a - 1
#     if a == 3:
#         print("Skip the iteration when a is", a)
#         continue
# 
# 'Output': The variable a is: 6
#      The variable a is: 5
#      The variable a is: 4
#      Skip the iteration when a is 3
#      The variable a is: 2
#      The variable a is: 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The break and continue Statements",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# The break and continue Statements"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Thebreak(HierNode):
    def __init__(self):
        super().__init__("The break and continue Statements")
        self.add(Content())

# eof
