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
# For more information on %prun, as well as its available options, use the IPython help
# functionality (i.e., type %prun? at the IPython prompt).
# 
# Line-by-Line Profiling with %lprun
# The function-by-function profiling of %prun is useful, but sometimes it’s more conve‐
# nient to have a line-by-line profile report. This is not built into Python or IPython,
# but there is a line_profiler package available for installation that can do this. Start
# by using Python’s packaging tool, pip, to install the line_profiler package:
#      $ pip install line_profiler
# 
# Next, you can use IPython to load the line_profiler IPython extension, offered as
# part of this package:
#      In[9]: %load_ext line_profiler
# 
# Now the %lprun command will do a line-by-line profiling of any function—in this
# case, we need to tell it explicitly which functions we’re interested in profiling:
#      In[10]: %lprun -f sum_of_lists sum_of_lists(5000)
# As before, the notebook sends the result to the pager, but it looks something like this:
#      Timer unit: 1e-06 s
# 
#      Total time: 0.009382 s
#      File: <ipython-input-19-fa2be176cc3e>
#      Function: sum_of_lists at line 1
# 
#      Line #      Hits         Time Per Hit % Time Line Contents
#      ==============================================================
#           1                                           def sum_of_lists(N):
#           2         1            2      2.0      0.0      total = 0
#           3         6            8      1.3      0.1      for i in range(5):
#           4         5         9001   1800.2     95.9          L = [j ^ (j >> i) ...
#           5         5          371     74.2      4.0          total += sum(L)
#           6         1            0      0.0      0.0      return total
# The information at the top gives us the key to reading the results: the time is reported
# in microseconds and we can see where the program is spending the most time. At this
# point, we may be able to use this information to modify aspects of the script and
# make it perform better for our desired use case.
# For more information on %lprun, as well as its available options, use the IPython help
# functionality (i.e., type %lprun? at the IPython prompt).
# 
# 
# 
# 
# 28   |   Chapter 1: IPython: Beyond Normal Python
# 
# Profiling Memory Use: %memit and %mprun
# Another aspect of profiling is the amount of memory an operation uses. This can be
# evaluated with another IPython extension, the memory_profiler. As with the
# line_profiler, we start by pip-installing the extension:
#     $ pip install memory_profiler
# Then we can use IPython to load the extension:
#     In[12]: %load_ext memory_profiler
# 
# The memory profiler extension contains two useful magic functions: the %memit
# magic (which offers a memory-measuring equivalent of %timeit) and the %mprun
# function (which offers a memory-measuring equivalent of %lprun). The %memit func‐
# tion can be used rather simply:
#     In[13]: %memit sum_of_lists(1000000)
#     peak memory: 100.08 MiB, increment: 61.36 MiB
# We see that this function uses about 100 MB of memory.
# For a line-by-line description of memory use, we can use the %mprun magic. Unfortu‐
# nately, this magic works only for functions defined in separate modules rather than
# the notebook itself, so we’ll start by using the %%file magic to create a simple module
# called mprun_demo.py, which contains our sum_of_lists function, with one addition
# that will make our memory profiling results more clear:
#     In[14]: %%file mprun_demo.py
#             def sum_of_lists(N):
#                 total = 0
#                 for i in range(5):
#                     L = [j ^ (j >> i) for j in range(N)]
#                     total += sum(L)
#                     del L # remove reference to L
#                 return total
#     Overwriting mprun_demo.py
# We can now import the new version of this function and run the memory line
# profiler:
#     In[15]: from mprun_demo import sum_of_lists
#             %mprun -f sum_of_lists sum_of_lists(1000000)
# The result, printed to the pager, gives us a summary of the memory use of the func‐
# tion, and looks something like this:
# 
# 
# 
# 
#                                                              Profiling and Timing Code   |   29
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Line-by-Line Profiling with %lprun",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LinebyLineProfiling(HierNode):
    def __init__(self):
        super().__init__("Line-by-Line Profiling with %lprun")
        self.add(Content())

# eof
