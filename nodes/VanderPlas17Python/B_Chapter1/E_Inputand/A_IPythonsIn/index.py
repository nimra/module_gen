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
# The benefit of %timeit is that for short commands it will automatically perform mul‐
# tiple runs in order to attain more robust results. For multiline statements, adding a
# second % sign will turn this into a cell magic that can handle multiple lines of input.
# For example, here’s the equivalent construction with a for loop:
#     In [9]: %%timeit
#        ...: L = []
#        ...: for n in range(1000):
#        ...:     L.append(n ** 2)
#        ...:
#     1000 loops, best of 3: 373 µs per loop
# We can immediately see that list comprehensions are about 10% faster than the
# equivalent for loop construction in this case. We’ll explore %timeit and other
# approaches to timing and profiling code in “Profiling and Timing Code” on page 25.
# 
# Help on Magic Functions: ?, %magic, and %lsmagic
# Like normal Python functions, IPython magic functions have docstrings, and this
# useful documentation can be accessed in the standard manner. So, for example, to
# read the documentation of the %timeit magic, simply type this:
#     In [10]: %timeit?
# Documentation for other functions can be accessed similarly. To access a general
# description of available magic functions, including some examples, you can type this:
#     In [11]: %magic
# For a quick and simple list of all available magic functions, type this:
#     In [12]: %lsmagic
# Finally, I’ll mention that it is quite straightforward to define your own magic func‐
# tions if you wish. We won’t discuss it here, but if you are interested, see the references
# listed in “More IPython Resources” on page 30.
# 
# Input and Output History
# Previously we saw that the IPython shell allows you to access previous commands
# with the up and down arrow keys, or equivalently the Ctrl-p/Ctrl-n shortcuts. Addi‐
# tionally, in both the shell and the notebook, IPython exposes several ways to obtain
# the output of previous commands, as well as string versions of the commands them‐
# selves. We’ll explore those here.
# 
# IPython’s In and Out Objects
# By now I imagine you’re quite familiar with the In[1]:/Out[1]: style prompts used
# by IPython. But it turns out that these are not just pretty decoration: they give a clue
# 
# 
#                                                                  Input and Output History   |   13
# 
# as to how you can access previous inputs and outputs in your current session. Imag‐
# ine you start a session that looks like this:
#      In [1]: import math
# 
#      In [2]: math.sin(2)
#      Out[2]: 0.9092974268256817
# 
#      In [3]: math.cos(2)
#      Out[3]: -0.4161468365471424
# 
# We’ve imported the built-in math package, then computed the sine and the cosine of
# the number 2. These inputs and outputs are displayed in the shell with In/Out labels,
# but there’s more—IPython actually creates some Python variables called In and Out
# that are automatically updated to reflect this history:
#      In [4]: print(In)
#      ['', 'import math', 'math.sin(2)', 'math.cos(2)', 'print(In)']
# 
#      In [5]: Out
#      Out[5]: {2: 0.9092974268256817, 3: -0.4161468365471424}
# 
# The In object is a list, which keeps track of the commands in order (the first item in
# the list is a placeholder so that In[1] can refer to the first command):
#      In [6]: print(In[1])
#      import math
# 
# The Out object is not a list but a dictionary mapping input numbers to their outputs
# (if any):
#      In [7]: print(Out[2])
#      0.9092974268256817
# 
# Note that not all operations have outputs: for example, import statements and print
# statements don’t affect the output. The latter may be surprising, but makes sense if
# you consider that print is a function that returns None; for brevity, any command
# that returns None is not added to Out.
# Where this can be useful is if you want to interact with past results. For example, let’s
# check the sum of sin(2) ** 2 and cos(2) ** 2 using the previously computed
# results:
#      In [8]: Out[2] ** 2 + Out[3] ** 2
#      Out[8]: 1.0
# 
# The result is 1.0 as we’d expect from the well-known trigonometric identity. In this
# case, using these previous results probably is not necessary, but it can become very
# handy if you execute a very expensive computation and want to reuse the result!
# 
# 
# 
# 
# 14   |   Chapter 1: IPython: Beyond Normal Python
# 
# Underscore Shortcuts and Previous Outputs
# The standard Python shell contains just one simple shortcut for accessing previous
# output; the variable _ (i.e., a single underscore) is kept updated with the previous out‐
# put; this works in IPython as well:
#     In [9]: print(_)
#     1.0
# But IPython takes this a bit further—you can use a double underscore to access the
# second-to-last output, and a triple underscore to access the third-to-last output (skip‐
# ping any commands with no output):
#     In [10]: print(__)
#     -0.4161468365471424
# 
#     In [11]: print(___)
#     0.9092974268256817
# IPython stops there: more than three underscores starts to get a bit hard to count,
# and at that point it’s easier to refer to the output by line number.
# There is one more shortcut we should mention, however—a shorthand for Out[X] is
# _X (i.e., a single underscore followed by the line number):
#     In [12]: Out[2]
#     Out[12]: 0.9092974268256817
# 
#     In [13]: _2
#     Out[13]: 0.9092974268256817
# 
# 
# Suppressing Output
# Sometimes you might wish to suppress the output of a statement (this is perhaps
# most common with the plotting commands that we’ll explore in Chapter 4). Or
# maybe the command you’re executing produces a result that you’d prefer not to store
# in your output history, perhaps so that it can be deallocated when other references are
# removed. The easiest way to suppress the output of a command is to add a semicolon
# to the end of the line:
#     In [14]: math.sin(2) + math.cos(2);
# Note that the result is computed silently, and the output is neither displayed on the
# screen or stored in the Out dictionary:
#     In [15]: 14 in Out
#     Out[15]: False
# 
# 
# 
# 
#                                                                 Input and Output History   |   15
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "IPython’s In and Out Objects",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IPythonsIn(HierNode):
    def __init__(self):
        super().__init__("IPython’s In and Out Objects")
        self.add(Content())

# eof