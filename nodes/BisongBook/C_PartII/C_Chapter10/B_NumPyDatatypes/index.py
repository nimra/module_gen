# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NumPy Datatypes
# NumPy boasts a broad range of numerical datatypes in comparison with vanilla Python.
# This extended datatype support is useful for dealing with different kinds of signed
# and unsigned integer and floating-point numbers as well as booleans and complex
# numbers for scientific computation. NumPy datatypes include the bool_, int(8,16,32,64),
# uint(8,16,32,64), float(16,32,64), complex(64,128) as well as the int_, float_, and
# complex_, to mention just a few.
#     The datatypes with a _ appended are base Python datatypes converted to NumPy
# datatypes. The parameter dtype is used to assign a datatype to a NumPy function. The
# default NumPy type is float_. Also, NumPy infers contiguous arrays of the same type.
#     Let’s explore a bit with NumPy datatypes:
# 
# # ints
# my_ints = np.array([3, 7, 9, 11])
# my_ints.dtype
# 'Output': dtype('int64')
# 
# # floats
# my_floats = np.array([3., 7., 9., 11.])
# my_floats.dtype
# 'Output': dtype('float64')
# 
# # non-contiguous types - default: float
# my_array = np.array([3., 7., 9, 11])
# my_array.dtype
# 'Output': dtype('float64')
# 
# # manually assigning datatypes
# my_array = np.array([3, 7, 9, 11], dtype="float64")
# my_array.dtype
# 'Output': dtype('float64')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "NumPy Datatypes",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# NumPy Datatypes"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NumPyDatatypes(HierNode):
    def __init__(self):
        super().__init__("NumPy Datatypes")
        self.add(Content())

# eof
