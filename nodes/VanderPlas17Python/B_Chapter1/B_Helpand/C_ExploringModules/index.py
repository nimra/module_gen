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
# Tab completion when importing
# Tab completion is also useful when importing objects from packages. Here we’ll use it
# to find all possible imports in the itertools package that start with co:
#     In [10]: from itertools import co<TAB>
#     combinations                   compress
#     combinations_with_replacement count
# Similarly, you can use tab completion to see which imports are available on your sys‐
# tem (this will change depending on which third-party scripts and modules are visible
# to your Python session):
#     In [10]: import <TAB>
#     Display all 399 possibilities? (y or n)
#     Crypto              dis                 py_compile
#     Cython              distutils           pyclbr
#     ...                 ...                 ...
#     difflib             pwd                 zmq
# 
#     In [10]: import h<TAB>
#     hashlib             hmac                  http
#     heapq               html                  husl
# (Note that for brevity, I did not print here all 399 importable packages and modules
# on my system.)
# 
# Beyond tab completion: Wildcard matching
# Tab completion is useful if you know the first few characters of the object or attribute
# you’re looking for, but is little help if you’d like to match characters at the middle or
# end of the word. For this use case, IPython provides a means of wildcard matching
# for names using the * character.
# For example, we can use this to list every object in the namespace that ends with
# Warning:
#     In [10]: *Warning?
#     BytesWarning                   RuntimeWarning
#     DeprecationWarning             SyntaxWarning
#     FutureWarning                  UnicodeWarning
#     ImportWarning                  UserWarning
#     PendingDeprecationWarning      Warning
#     ResourceWarning
# 
# Notice that the * character matches any string, including the empty string.
# Similarly, suppose we are looking for a string method that contains the word find
# somewhere in its name. We can search for it this way:
# 
# 
# 
# 
#                                                          Help and Documentation in IPython   |   7
# 
#         In [10]: str.*find*?
#         str.find
#         str.rfind
# I find this type of flexible wildcard search can be very useful for finding a particular
# command when I’m getting to know a new package or reacquainting myself with a
# familiar one.
# 
# Keyboard Shortcuts in the IPython Shell
# If you spend any amount of time on the computer, you’ve probably found a use for
# keyboard shortcuts in your workflow. Most familiar perhaps are Cmd-C and Cmd-V
# (or Ctrl-C and Ctrl-V) for copying and pasting in a wide variety of programs and sys‐
# tems. Power users tend to go even further: popular text editors like Emacs, Vim, and
# others provide users an incredible range of operations through intricate combina‐
# tions of keystrokes.
# The IPython shell doesn’t go this far, but does provide a number of keyboard short‐
# cuts for fast navigation while you’re typing commands. These shortcuts are not in fact
# provided by IPython itself, but through its dependency on the GNU Readline library:
# thus, some of the following shortcuts may differ depending on your system configu‐
# ration. Also, while some of these shortcuts do work in the browser-based notebook,
# this section is primarily about shortcuts in the IPython shell.
# Once you get accustomed to these, they can be very useful for quickly performing
# certain commands without moving your hands from the “home” keyboard position.
# If you’re an Emacs user or if you have experience with Linux-style shells, the follow‐
# ing will be very familiar. We’ll group these shortcuts into a few categories: navigation
# shortcuts, text entry shortcuts, command history shortcuts, and miscellaneous shortcuts.
# 
# Navigation Shortcuts
# While the use of the left and right arrow keys to move backward and forward in the
# line is quite obvious, there are other options that don’t require moving your hands
# from the “home” keyboard position:
# 
# Keystroke                        Action
# Ctrl-a                           Move cursor to the beginning of the line
# Ctrl-e                           Move cursor to the end of the line
# Ctrl-b (or the left arrow key)   Move cursor back one character
# Ctrl-f (or the right arrow key) Move cursor forward one character
# 
# 
# 
# 
# 8   |    Chapter 1: IPython: Beyond Normal Python
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Exploring Modules with Tab Completion",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ExploringModules(HierNode):
    def __init__(self):
        super().__init__("Exploring Modules with Tab Completion")
        self.add(Content())

# eof
