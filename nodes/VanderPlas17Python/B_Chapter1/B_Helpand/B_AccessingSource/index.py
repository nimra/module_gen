# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#       ....:     return a ** 2
#       ....:
# Note that to create a docstring for our function, we simply placed a string literal in
# the first line. Because docstrings are usually multiple lines, by convention we used
# Python’s triple-quote notation for multiline strings.
# Now we’ll use the ? mark to find this docstring:
#     In [7]: square?
#     Type:        function
#     String form: <function square at 0x103713cb0>
#     Definition: square(a)
#     Docstring:   Return the square of a.
# This quick access to documentation via docstrings is one reason you should get in the
# habit of always adding such inline documentation to the code you write!
# 
# Accessing Source Code with ??
# Because the Python language is so easily readable, you can usually gain another level
# of insight by reading the source code of the object you’re curious about. IPython pro‐
# vides a shortcut to the source code with the double question mark (??):
#     In [8]: square??
#     Type:        function
#     String form: <function square at 0x103713cb0>
#     Definition: square(a)
#     Source:
#     def square(a):
#         "Return the square of a"
#         return a ** 2
# For simple functions like this, the double question mark can give quick insight into
# the under-the-hood details.
# If you play with this much, you’ll notice that sometimes the ?? suffix doesn’t display
# any source code: this is generally because the object in question is not implemented in
# Python, but in C or some other compiled extension language. If this is the case, the ??
# suffix gives the same output as the ? suffix. You’ll find this particularly with many of
# Python’s built-in objects and types, for example len from above:
#     In [9]: len??
#     Type:         builtin_function_or_method
#     String form: <built-in function len>
#     Namespace:    Python builtin
#     Docstring:
#     len(object) -> integer
# 
#     Return the number of items of a sequence or mapping.
# 
# 
# 
# 
#                                                         Help and Documentation in IPython   |   5
# 
# Using ? and/or ?? gives a powerful and quick interface for finding information about
# what any Python function or module does.
# 
# Exploring Modules with Tab Completion
# IPython’s other useful interface is the use of the Tab key for autocompletion and
# exploration of the contents of objects, modules, and namespaces. In the examples that
# follow, we’ll use <TAB> to indicate when the Tab key should be pressed.
# 
# Tab completion of object contents
# Every Python object has various attributes and methods associated with it. Like with
# the help function discussed before, Python has a built-in dir function that returns a
# list of these, but the tab-completion interface is much easier to use in practice. To see
# a list of all available attributes of an object, you can type the name of the object fol‐
# lowed by a period (.) character and the Tab key:
#         In [10]: L.<TAB>
#         L.append   L.copy           L.extend        L.insert   L.remove  L.sort
#         L.clear    L.count          L.index         L.pop      L.reverse
# To narrow down the list, you can type the first character or several characters of the
# name, and the Tab key will find the matching attributes and methods:
#         In [10]: L.c<TAB>
#         L.clear L.copy    L.count
# 
#         In [10]: L.co<TAB>
#         L.copy   L.count
# If there is only a single option, pressing the Tab key will complete the line for you. For
# example, the following will instantly be replaced with L.count:
#         In [10]: L.cou<TAB>
# Though Python has no strictly enforced distinction between public/external
# attributes and private/internal attributes, by convention a preceding underscore is
# used to denote such methods. For clarity, these private methods and special methods
# are omitted from the list by default, but it’s possible to list them by explicitly typing
# the underscore:
#         In [10]: L._<TAB>
#         L.__add__                L.__gt__                  L.__reduce__
#         L.__class__              L.__hash__                L.__reduce_ex__
# For brevity, we’ve only shown the first couple lines of the output. Most of these are
# Python’s special double-underscore methods (often nicknamed “dunder” methods).
# 
# 
# 
# 
# 6   |    Chapter 1: IPython: Beyond Normal Python
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Accessing Source Code with ??",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AccessingSource(HierNode):
    def __init__(self):
        super().__init__("Accessing Source Code with ??")
        self.add(Content())

# eof
