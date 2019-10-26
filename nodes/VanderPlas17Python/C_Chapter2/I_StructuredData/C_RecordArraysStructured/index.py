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
# RecordArrays: Structured Arrays with a Twist
# NumPy also provides the np.recarray class, which is almost identical to the struc‐
# tured arrays just described, but with one additional feature: fields can be accessed as
# attributes rather than as dictionary keys. Recall that we previously accessed the ages
# by writing:
#      In[15]: data['age']
#      Out[15]: array([25, 45, 37, 19], dtype=int32)
# If we view our data as a record array instead, we can access this with slightly fewer
# keystrokes:
#      In[16]: data_rec = data.view(np.recarray)
#              data_rec.age
#      Out[16]: array([25, 45, 37, 19], dtype=int32)
# The downside is that for record arrays, there is some extra overhead involved in
# accessing the fields, even when using the same syntax. We can see this here:
#      In[17]: %timeit data['age']
#              %timeit data_rec['age']
#              %timeit data_rec.age
#      1000000 loops, best of 3: 241 ns per loop
#      100000 loops, best of 3: 4.61 µs per loop
#      100000 loops, best of 3: 7.27 µs per loop
# Whether the more convenient notation is worth the additional overhead will depend
# on your own application.
# 
# On to Pandas
# This section on structured and record arrays is purposely at the end of this chapter,
# because it leads so well into the next package we will cover: Pandas. Structured arrays
# like the ones discussed here are good to know about for certain situations, especially
# in case you’re using NumPy arrays to map onto binary data formats in C, Fortran, or
# another language. For day-to-day use of structured data, the Pandas package is a
# much better choice, and we’ll dive into a full discussion of it in the next chapter.
# 
# 
# 
# 
# 96   |   Chapter 2: Introduction to NumPy
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "RecordArrays: Structured Arrays with a Twist",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RecordArraysStructured(HierNode):
    def __init__(self):
        super().__init__("RecordArrays: Structured Arrays with a Twist")
        self.add(Content())

# eof
