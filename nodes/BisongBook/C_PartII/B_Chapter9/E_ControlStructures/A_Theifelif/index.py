# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The if/elif (else-if) Statements
# The if/elif (else-if ) statement executes a set of instructions if the tested condition
# evaluates to true. The else statement specifies the code that should execute if none of the
# previous conditions evaluate to true. It can be visualized by the flowchart in Figure 9-2.
# 
# 
# 
# 
# 
# Figure 9-2. Flowchart of the if statement
# 
#    The syntax for the if/elif statement is given as follows:
# 
# if expressionA:
#     statementA
# elif expressionB:
#     statementB
# ...
# ...
# else:
#     statementC
# 
#    Here is a program example:
# 
# a = 8
# if type(a) is int:
#     print('Number is an integer')
# elif a > 0:
#     print('Number is positive')
# else:
#     print('The number is negative and not an integer')
# 
# 'Output': Number is an integer

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The if/elif (else-if) Statements",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# The if/elif (else-if) Statements"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Theifelif(HierNode):
    def __init__(self):
        super().__init__("The if/elif (else-if) Statements")
        self.add(Content())

# eof
