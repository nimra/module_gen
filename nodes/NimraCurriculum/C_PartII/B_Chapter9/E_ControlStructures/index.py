# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Theifelif.index import Theifelif as A_Theifelif
from .B_Thewhile.index import Thewhile as B_Thewhile
from .C_Thefor.index import Thefor as C_Thefor
from .D_ListComprehensions.index import ListComprehensions as D_ListComprehensions
from .E_Thebreak.index import Thebreak as E_Thebreak

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 9   Python
# 
# U
#  sing the Formatter
# Formatters add a placeholder for inputting a data value into a string output using the
# curly brace {}. The format method from the str class is invoked to receive the value as a
# parameter. The number of parameters in the format method should match the number
# of placeholders in the string representation. Other format specifiers can be added with
# the placeholder curly brackets.
# 
# print("{} {} {}".format(a, b, c))
# 'Output': I Love You
# # re-ordering the output
# print("{2} {1} {0}".format(a, b, c))
# 'Output': You Love I
# 
# 
# 
# C
#  ontrol Structures
# Programs need to make decisions which result in executing a particular set of
# instructions or a specific block of code repeatedly. With control structures, we would
# have the ability to write programs that can make logical decisions and execute an
# instruction set until a terminating condition occurs.
# 
# 
# The if/elif (else-if) Statements
# The if/elif (else-if ) statement executes a set of instructions if the tested condition
# evaluates to true. The else statement specifies the code that should execute if none of the
# previous conditions evaluate to true. It can be visualized by the flowchart in Figure 9-2.
# 
# 
# 
# 
# 80
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Control Structures")
        self.add(MarkdownBlock("# Control Structures"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ControlStructures(HierNode):
    def __init__(self):
        super().__init__("Control Structures")
        self.add(Content())
        self.add(A_Theifelif())
        self.add(B_Thewhile())
        self.add(C_Thefor())
        self.add(D_ListComprehensions())
        self.add(E_Thebreak())

# eof
