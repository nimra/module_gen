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

from .A_ControllingExceptions.index import ControllingExceptions as A_ControllingExceptions
from .B_DebuggingWhen.index import DebuggingWhen as B_DebuggingWhen

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# Errors and Debugging
# Code development and data analysis always require a bit of trial and error, and
# IPython contains tools to streamline this process. This section will briefly cover some
# options for controlling Python’s exception reporting, followed by exploring tools for
# debugging errors in code.
# 
# Controlling Exceptions: %xmode
# Most of the time when a Python script fails, it will raise an exception. When the inter‐
# preter hits one of these exceptions, information about the cause of the error can be
# found in the traceback, which can be accessed from within Python. With the %xmode
# magic function, IPython allows you to control the amount of information printed
# when the exception is raised. Consider the following code:
#      In[1]: def func1(a, b):
#                 return a / b
# 
#               def func2(x):
#                   a = x
#                   b = x - 1
#                   return func1(a, b)
#      In[2]: func2(1)
#      ---------------------------------------------------------------------------
#      ZeroDivisionError                         Traceback (most recent call last)
# 
#      <ipython-input-2-b2e110f6fc8f^gt; in <module>()
#      ----> 1 func2(1)
# 
# 
#      <ipython-input-1-d849e34d61fb> in func2(x)
#            5     a = x
#            6     b = x - 1
#      ----> 7     return func1(a, b)
# 
# 
#      <ipython-input-1-d849e34d61fb> in func1(a, b)
#            1 def func1(a, b):
#      ----> 2     return a / b
#            3
#            4 def func2(x):
#            5     a = x
# 
# 
#      ZeroDivisionError: division by zero
# 
# Calling func2 results in an error, and reading the printed trace lets us see exactly what
# happened. By default, this trace includes several lines showing the context of each
# 
# 
# 20   | Chapter 1: IPython: Beyond Normal Python
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Errors and Debugging",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Errorsand(HierNode):
    def __init__(self):
        super().__init__("Errors and Debugging")
        self.add(Content())
        self.add(A_ControllingExceptions())
        self.add(B_DebuggingWhen())

# eof
