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

from .A_TradeOffsin.index import TradeOffsin as A_TradeOffsin
from .B_MissingData.index import MissingData as B_MissingData
from .C_Operatingon.index import Operatingon as C_Operatingon

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# According to NumPy’s broadcasting rules (see “Computation on Arrays: Broadcast‐
# ing” on page 63), subtraction between a two-dimensional array and one of its rows is
# applied row-wise.
# In Pandas, the convention similarly operates row-wise by default:
#     In[17]: df = pd.DataFrame(A, columns=list('QRST'))
#             df - df.iloc[0]
#     Out[17]:      Q R S T
#                0 0 0 0 0
#                1 -1 -2 2 4
#                2 3 -7 1 4
# If you would instead like to operate column-wise, you can use the object methods
# mentioned earlier, while specifying the axis keyword:
#     In[18]: df.subtract(df['R'], axis=0)
#     Out[18]:      Q R S T
#                0 -5 0 -6 -4
#                1 -4 0 -2 2
#                2 5 0 2 7
# 
# Note that these DataFrame/Series operations, like the operations discussed before,
# will automatically align indices between the two elements:
#     In[19]: halfrow = df.iloc[0, ::2]
#             halfrow
#     Out[19]: Q    3
#              S    2
#              Name: 0, dtype: int64
#     In[20]: df - halfrow
#     Out[20]:        Q   R     S   T
#                0 0.0 NaN    0.0 NaN
#                1 -1.0 NaN   2.0 NaN
#                2 3.0 NaN    1.0 NaN
# This preservation and alignment of indices and columns means that operations on
# data in Pandas will always maintain the data context, which prevents the types of silly
# errors that might come up when you are working with heterogeneous and/or mis‐
# aligned data in raw NumPy arrays.
# 
# Handling Missing Data
# The difference between data found in many tutorials and data in the real world is that
# real-world data is rarely clean and homogeneous. In particular, many interesting
# datasets will have some amount of data missing. To make matters even more compli‐
# cated, different data sources may indicate missing data in different ways.
# 
# 
# 
#                                                                Handling Missing Data   |   119
# 
# In this section, we will discuss some general considerations for missing data, discuss
# how Pandas chooses to represent it, and demonstrate some built-in Pandas tools for
# handling missing data in Python. Here and throughout the book, we’ll refer to miss‐
# ing data in general as null, NaN, or NA values.
# 
# Trade-Offs in Missing Data Conventions
# A number of schemes have been developed to indicate the presence of missing data in
# a table or DataFrame. Generally, they revolve around one of two strategies: using a
# mask that globally indicates missing values, or choosing a sentinel value that indicates
# a missing entry.
# In the masking approach, the mask might be an entirely separate Boolean array, or it
# may involve appropriation of one bit in the data representation to locally indicate the
# null status of a value.
# In the sentinel approach, the sentinel value could be some data-specific convention,
# such as indicating a missing integer value with –9999 or some rare bit pattern, or it
# could be a more global convention, such as indicating a missing floating-point value
# with NaN (Not a Number), a special value which is part of the IEEE floating-point
# specification.
# None of these approaches is without trade-offs: use of a separate mask array requires
# allocation of an additional Boolean array, which adds overhead in both storage and
# computation. A sentinel value reduces the range of valid values that can be repre‐
# sented, and may require extra (often non-optimized) logic in CPU and GPU arith‐
# metic. Common special values like NaN are not available for all data types.
# As in most cases where no universally optimal choice exists, different languages and
# systems use different conventions. For example, the R language uses reserved bit pat‐
# terns within each data type as sentinel values indicating missing data, while the SciDB
# system uses an extra byte attached to every cell to indicate a NA state.
# 
# Missing Data in Pandas
# The way in which Pandas handles missing values is constrained by its reliance on the
# NumPy package, which does not have a built-in notion of NA values for non-
# floating-point data types.
# Pandas could have followed R’s lead in specifying bit patterns for each individual data
# type to indicate nullness, but this approach turns out to be rather unwieldy. While R
# contains four basic data types, NumPy supports far more than this: for example,
# while R has a single integer type, NumPy supports fourteen basic integer types once
# you account for available precisions, signedness, and endianness of the encoding.
# Reserving a specific bit pattern in all available NumPy types would lead to an
# unwieldy amount of overhead in special-casing various operations for various types,
# 
# 120   |   Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Handling Missing Data",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HandlingMissing(HierNode):
    def __init__(self):
        super().__init__("Handling Missing Data")
        self.add(Content())
        self.add(A_TradeOffsin())
        self.add(B_MissingData())
        self.add(C_Operatingon())

# eof
