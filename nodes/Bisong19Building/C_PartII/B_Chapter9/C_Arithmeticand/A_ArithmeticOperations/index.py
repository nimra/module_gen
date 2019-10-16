# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Arithmetic Operations
# In Python, we can operate on data using familiar algebra operations such as addition +,
# subtraction -, multiplication *, division /, and exponentiation **.
# 
# 2 + 2     # addition
# 'Output': 4
# 5 - 3     # subtraction
# 'Output': 2
# 4 * 4     # multiplication
# 'Output': 16
# 10 / 2    # division
# 'Output': 5.0
# 2**4 / (5 + 3)    # use brackets to enforce precedence
# 'Output': 2.0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Arithmetic Operations",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Arithmetic Operations"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ArithmeticOperations(HierNode):
    def __init__(self):
        super().__init__("Arithmetic Operations")
        self.add(Content())

# eof
