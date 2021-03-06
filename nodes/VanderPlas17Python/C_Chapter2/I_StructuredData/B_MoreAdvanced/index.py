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
#       Out[13]: dtype([('f0', 'S10'), ('f1', '<i4'), ('f2', '<f8')])
# The shortened string format codes may seem confusing, but they are built on simple
# principles. The first (optional) character is < or >, which means “little endian” or “big
# endian,” respectively, and specifies the ordering convention for significant bits. The
# next character specifies the type of data: characters, bytes, ints, floating points, and so
# on (see Table 2-4). The last character or characters represents the size of the object in
# bytes.
# 
# Table 2-4. NumPy data types
# Character Description         Example
# 'b'       Byte                np.dtype('b')
# 'i'        Signed integer     np.dtype('i4') == np.int32
# 'u'        Unsigned integer   np.dtype('u1') == np.uint8
# 'f'        Floating point     np.dtype('f8') == np.int64
# 'c'        Complex floating point np.dtype('c16') == np.complex128
# 'S', 'a' string               np.dtype('S5')
# 'U'        Unicode string     np.dtype('U') == np.str_
# 'V'        Raw data (void)    np.dtype('V') == np.void
# 
# 
# More Advanced Compound Types
# It is possible to define even more advanced compound types. For example, you can
# create a type where each element contains an array or matrix of values. Here, we’ll
# create a data type with a mat component consisting of a 3×3 floating-point matrix:
#       In[14]: tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
#               X = np.zeros(1, dtype=tp)
#               print(X[0])
#               print(X['mat'][0])
#       (0, [[0.0,   0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
#       [[ 0. 0.     0.]
#        [ 0. 0.     0.]
#        [ 0. 0.     0.]]
# 
# Now each element in the X array consists of an id and a 3×3 matrix. Why would you
# use this rather than a simple multidimensional array, or perhaps a Python dictionary?
# The reason is that this NumPy dtype directly maps onto a C structure definition, so
# the buffer containing the array content can be accessed directly within an appropri‐
# ately written C program. If you find yourself writing a Python interface to a legacy C
# or Fortran library that manipulates structured data, you’ll probably find structured
# arrays quite useful!
# 
# 
# 
# 
#                                                       Structured Data: NumPy’s Structured Arrays   |   95
# 
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
            "More Advanced Compound Types",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MoreAdvanced(HierNode):
    def __init__(self):
        super().__init__("More Advanced Compound Types")
        self.add(Content())

# eof
