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

from .A_WebResources.index import WebResources as A_WebResources
from .B_Books.index import Books as B_Books

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#      Filename: ./mprun_demo.py
# 
#      Line #    Mem usage    Increment   Line Contents
#      ================================================
#           4     71.9 MiB      0.0 MiB           L = [j ^ (j >> i) for j in range(N)]
# 
# 
#      Filename: ./mprun_demo.py
# 
#      Line #    Mem usage    Increment   Line Contents
#      ================================================
#           1     39.0 MiB      0.0 MiB   def sum_of_lists(N):
#           2     39.0 MiB      0.0 MiB       total = 0
#           3     46.5 MiB      7.5 MiB       for i in range(5):
#           4     71.9 MiB     25.4 MiB           L = [j ^ (j >> i) for j in range(N)]
#           5     71.9 MiB      0.0 MiB           total += sum(L)
#           6     46.5 MiB    -25.4 MiB           del L # remove reference to L
#           7     39.1 MiB     -7.4 MiB       return total
# 
# Here the Increment column tells us how much each line affects the total memory
# budget: observe that when we create and delete the list L, we are adding about 25 MB
# of memory usage. This is on top of the background memory usage from the Python
# interpreter itself.
# For more information on %memit and %mprun, as well as their available options, use
# the IPython help functionality (i.e., type %memit? at the IPython prompt).
# 
# More IPython Resources
# In this chapter, we’ve just scratched the surface of using IPython to enable data sci‐
# ence tasks. Much more information is available both in print and on the Web, and
# here we’ll list some other resources that you may find helpful.
# 
# Web Resources
# The IPython website
#     The IPython website links to documentation, examples, tutorials, and a variety of
#     other resources.
# The nbviewer website
#     This site shows static renderings of any IPython notebook available on the Inter‐
#     net. The front page features some example notebooks that you can browse to see
#     what other folks are using IPython for!
# 
# 
# 
# 
# 30   | Chapter 1: IPython: Beyond Normal Python
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "More IPython Resources",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MoreIPython(HierNode):
    def __init__(self):
        super().__init__("More IPython Resources")
        self.add(Content())
        self.add(A_WebResources())
        self.add(B_Books())

# eof
