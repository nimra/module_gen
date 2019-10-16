# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_UserDefinedFunctions.index import UserDefinedFunctions as A_UserDefinedFunctions
from .B_LambdaExpressions.index import LambdaExpressions as B_LambdaExpressions

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions
# A function is a code block that carries out a particular action (Figure 9-5). Functions are
# called by the programmer when needed by making a function call. Python comes pre-­
# packaged with lots of useful functions to simplify programming. The programmer can
# also write custom functions.
# 
# 
# 
# 
# Figure 9-5. Functions
# 
#     A function receives data into its parameter list during a function call. The inputed
# data is used to complete the function execution. At the end of its execution, a function
# always returns a result – this result could be ‘None’ or a specific data value.
#     Functions are treated as first-class objects in Python. That means a function can be
# passed as data into another function, the result of a function execution can also be a
# function, and a function can also be stored as a variable.
#     Functions are visualized as a black box that receives a set of objects as input,
# executes some code, and returns another set of objects as output.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Functions",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Functions"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Functions(HierNode):
    def __init__(self):
        super().__init__("Functions")
        self.add(Content())
        self.add(A_UserDefinedFunctions())
        self.add(B_LambdaExpressions())

# eof
