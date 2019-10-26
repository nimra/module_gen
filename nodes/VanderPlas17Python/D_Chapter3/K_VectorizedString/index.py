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

from .A_IntroducingPandas.index import IntroducingPandas as A_IntroducingPandas
from .B_Tablesof.index import Tablesof as B_Tablesof
from .C_ExampleRecipe.index import ExampleRecipe as C_ExampleRecipe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# In particular, the striking feature of this graph is the dip in birthrate on US holidays
# (e.g., Independence Day, Labor Day, Thanksgiving, Christmas, New Year’s Day)
# although this likely reflects trends in scheduled/induced births rather than some deep
# psychosomatic effect on natural births. For more discussion on this trend, see the
# analysis and links in Andrew Gelman’s blog post on the subject. We’ll return to this
# figure in “Example: Effect of Holidays on US Births” on page 269, where we will use
# Matplotlib’s tools to annotate this plot.
# Looking at this short example, you can see that many of the Python and Pandas tools
# we’ve seen to this point can be combined and used to gain insight from a variety of
# datasets. We will see some more sophisticated applications of these data manipula‐
# tions in future sections!
# 
# Vectorized String Operations
# One strength of Python is its relative ease in handling and manipulating string data.
# Pandas builds on this and provides a comprehensive set of vectorized string operations
# that become an essential piece of the type of munging required when one is working
# with (read: cleaning up) real-world data. In this section, we’ll walk through some of
# the Pandas string operations, and then take a look at using them to partially clean up
# a very messy dataset of recipes collected from the Internet.
# 
# Introducing Pandas String Operations
# We saw in previous sections how tools like NumPy and Pandas generalize arithmetic
# operations so that we can easily and quickly perform the same operation on many
# array elements. For example:
#       In[1]: import numpy as np
#              x = np.array([2, 3, 5, 7, 11, 13])
#              x * 2
#       Out[1]: array([ 4,        6, 10, 14, 22, 26])
# This vectorization of operations simplifies the syntax of operating on arrays of data:
# we no longer have to worry about the size or shape of the array, but just about what
# operation we want done. For arrays of strings, NumPy does not provide such simple
# access, and thus you’re stuck using a more verbose loop syntax:
#       In[2]: data = ['peter', 'Paul', 'MARY', 'gUIDO']
#              [s.capitalize() for s in data]
#       Out[2]: ['Peter', 'Paul', 'Mary', 'Guido']
# This is perhaps sufficient to work with some data, but it will break if there are any
# missing values. For example:
#       In[3]: data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
#              [s.capitalize() for s in data]
# 
# 
# 178   |   Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Vectorized String Operations",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class VectorizedString(HierNode):
    def __init__(self):
        super().__init__("Vectorized String Operations")
        self.add(Content())
        self.add(A_IntroducingPandas())
        self.add(B_Tablesof())
        self.add(C_ExampleRecipe())

# eof
