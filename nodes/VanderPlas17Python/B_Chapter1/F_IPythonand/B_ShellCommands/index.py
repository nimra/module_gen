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
# Shell Commands in IPython
# You can use any command that works at the command line in IPython by prefixing it
# with the ! character. For example, the ls, pwd, and echo commands can be run as
# follows:
#      In [1]: !ls
#      myproject.txt
# 
#      In [2]: !pwd
#      /home/jake/projects/myproject
# 
#      In [3]: !echo "printing from the shell"
#      printing from the shell
# 
# 
# Passing Values to and from the Shell
# Shell commands can not only be called from IPython, but can also be made to inter‐
# act with the IPython namespace. For example, you can save the output of any shell
# command to a Python list using the assignment operator:
#      In [4]: contents = !ls
# 
#      In [5]: print(contents)
#      ['myproject.txt']
# 
#      In [6]: directory = !pwd
# 
#      In [7]: print(directory)
#      ['/Users/jakevdp/notebooks/tmp/myproject']
# Note that these results are not returned as lists, but as a special shell return type
# defined in IPython:
#      In [8]: type(directory)
#      IPython.utils.text.SList
# This looks and acts a lot like a Python list, but has additional functionality, such as
# the grep and fields methods and the s, n, and p properties that allow you to search,
# filter, and display the results in convenient ways. For more information on these, you
# can use IPython’s built-in help features.
# Communication in the other direction—passing Python variables into the shell—is
# possible through the {varname} syntax:
#      In [9]: message = "hello from Python"
# 
#      In [10]: !echo {message}
#      hello from Python
# 
# 
# 
# 
# 18   |   Chapter 1: IPython: Beyond Normal Python
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Shell Commands in IPython",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ShellCommands(HierNode):
    def __init__(self):
        super().__init__("Shell Commands in IPython")
        self.add(Content())

# eof
