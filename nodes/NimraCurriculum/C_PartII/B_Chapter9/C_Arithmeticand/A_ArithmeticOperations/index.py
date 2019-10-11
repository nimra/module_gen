# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 9   Python
# 
# a + b + c
# 'Output': 'ILoveYou'
# 
# # let's add some space
# a + ' ' + b +  ' ' + c
# 
# 
# 
# Arithmetic and Boolean Operations
# This section introduces operators for programming arithmetic and logical constructs.
# 
# 
# Arithmetic Operations
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
# 
# 
# Boolean Operations
# Boolean operations evaluate to True or False. Boolean operators include the comparison
# and logical operators. The comparison operators include less than or equal to <=, less
# than <, greater than or equal to >=, greater than >, not equal to !=, and equal to ==.
# 
# 2 < 5
# 'Output': True
# 2 <= 5
# 'Output': True
# 
# 
# 78
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Arithmetic Operations")
        self.add(MarkdownBlock("# Arithmetic Operations"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ArithmeticOperations(HierNode):
    def __init__(self):
        super().__init__("Arithmetic Operations")
        self.add(Content())

# eof
