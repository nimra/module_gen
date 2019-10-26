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

from .A_IntroducingBroadcasting.index import IntroducingBroadcasting as A_IntroducingBroadcasting
from .B_Rulesof.index import Rulesof as B_Rulesof
from .C_Broadcastingin.index import Broadcastingin as C_Broadcastingin

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# Figure 2-3. Histogram of presidential heights
# 
# These aggregates are some of the fundamental pieces of exploratory data analysis that
# we’ll explore in more depth in later chapters of the book.
# 
# Computation on Arrays: Broadcasting
# We saw in the previous section how NumPy’s universal functions can be used to vec‐
# torize operations and thereby remove slow Python loops. Another means of vectoriz‐
# ing operations is to use NumPy’s broadcasting functionality. Broadcasting is simply a
# set of rules for applying binary ufuncs (addition, subtraction, multiplication, etc.) on
# arrays of different sizes.
# 
# Introducing Broadcasting
# Recall that for arrays of the same size, binary operations are performed on an
# element-by-element basis:
#     In[1]: import numpy as np
#     In[2]: a = np.array([0, 1, 2])
#            b = np.array([5, 5, 5])
#            a + b
#     Out[2]: array([5, 6, 7])
# Broadcasting allows these types of binary operations to be performed on arrays of dif‐
# ferent sizes—for example, we can just as easily add a scalar (think of it as a zero-
# dimensional array) to an array:
# 
# 
# 
# 
#                                                       Computation on Arrays: Broadcasting   |   63
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Computation on Arrays: Broadcasting",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Computationon(HierNode):
    def __init__(self):
        super().__init__("Computation on Arrays: Broadcasting")
        self.add(Content())
        self.add(A_IntroducingBroadcasting())
        self.add(B_Rulesof())
        self.add(C_Broadcastingin())

# eof
