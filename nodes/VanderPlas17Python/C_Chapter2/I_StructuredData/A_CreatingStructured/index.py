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
#      Out[6]: array(['Alice', 'Bob', 'Cathy', 'Doug'],
#                    dtype='<U10')
#      In[7]: # Get first row of data
#             data[0]
#      Out[7]: ('Alice', 25, 55.0)
#      In[8]: # Get the name from the last row
#             data[-1]['name']
#      Out[8]: 'Doug'
# Using Boolean masking, this even allows you to do some more sophisticated opera‐
# tions such as filtering on age:
#      In[9]: # Get names where age is under 30
#             data[data['age'] < 30]['name']
#      Out[9]: array(['Alice', 'Doug'],
#                    dtype='<U10')
# Note that if you’d like to do any operations that are any more complicated than these,
# you should probably consider the Pandas package, covered in the next chapter. As
# we’ll see, Pandas provides a DataFrame object, which is a structure built on NumPy
# arrays that offers a variety of useful data manipulation functionality similar to what
# we’ve shown here, as well as much, much more.
# 
# Creating Structured Arrays
# Structured array data types can be specified in a number of ways. Earlier, we saw the
# dictionary method:
#      In[10]: np.dtype({'names':('name', 'age', 'weight'),
#                        'formats':('U10', 'i4', 'f8')})
#      Out[10]: dtype([('name', '<U10'), ('age', '<i4'), ('weight', '<f8')])
# 
# For clarity, numerical types can be specified with Python types or NumPy dtypes
# instead:
#      In[11]: np.dtype({'names':('name', 'age', 'weight'),
#                        'formats':((np.str_, 10), int, np.float32)})
#      Out[11]: dtype([('name', '<U10'), ('age', '<i8'), ('weight', '<f4')])
# A compound type can also be specified as a list of tuples:
#      In[12]: np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])
#      Out[12]: dtype([('name', 'S10'), ('age', '<i4'), ('weight', '<f8')])
# If the names of the types do not matter to you, you can specify the types alone in a
# comma-separated string:
#      In[13]: np.dtype('S10,i4,f8')
# 
# 
# 
# 94   |   Chapter 2: Introduction to NumPy
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Creating Structured Arrays",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CreatingStructured(HierNode):
    def __init__(self):
        super().__init__("Creating Structured Arrays")
        self.add(Content())

# eof
