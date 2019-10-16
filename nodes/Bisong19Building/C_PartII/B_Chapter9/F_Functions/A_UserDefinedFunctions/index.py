# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# User-Defined Functions
# A function is defined using the def keyword. The syntax for creating a function is as follows:
# 
# def function-name(parameters):
#     statement(s)
# 
#     Let’s create a simple function:
# 
# def squares(number):
#     return number**2
# 
# squares(2)
# 'Output': 4
# 
#     Here’s another function example:
# 
# def _mean_(*number):
#     avg = sum(number)/len(number)
#     return avg
# 
# _mean_(1,2,3,4,5,6,7,8,9)
# 'Output': 5.0
# 
#    The * before the parameter number indicates that the variable can receive any
# number of values, which is implicitly bound to a tuple.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "User-Defined Functions",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# User-Defined Functions"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UserDefinedFunctions(HierNode):
    def __init__(self):
        super().__init__("User-Defined Functions")
        self.add(Content())

# eof
