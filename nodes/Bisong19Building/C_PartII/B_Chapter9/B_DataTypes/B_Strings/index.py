# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Strings
# Strings in Python are enclosed by a pair of single quotes (‘ … ’). Strings are immutable.
# This means they cannot be altered when assigned or when a string variable is created.
# Strings can be indexed like a list as well as sliced to create new lists.
# 
# my_string = 'Schatz'
# my_string[0]      # get first index of string
# 'Output': 'S'
# my_string[1:4]    # slice the string from the 2nd to the 5th element
#                      (indexed from 0)
# 'Output': 'cha'
# len(my_string)    # get the length of the string
# 'Output': 6
# my_string[-1]     # get last element of the string
# 'Output': 'z'
# 
#     We can operate on string values with the boolean operators.
# 
# 't' in my_string
# 'Output': True
# 't' not in my_string
# 'Output': False
# 't' is my_string
# 'Output': False
# 't' is not my_string
# 'Output': True
# 't' == my_string
# 'Output': False
# 't' != my_string
# 'Output': True
# 
#     We can concatenate two strings to create a new string using the overloaded operator +.
# 
# a = 'I'
# b = 'Love'
# c = 'You'
# 
# a + b + c
# 'Output': 'ILoveYou'
# 
# # let's add some space
# a + ' ' + b +  ' ' + c

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Strings",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Strings"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Strings(HierNode):
    def __init__(self):
        super().__init__("Strings")
        self.add(Content())

# eof
