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
            "Trade-Offs in Missing Data Conventions",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TradeOffsin(HierNode):
    def __init__(self):
        super().__init__("Trade-Offs in Missing Data Conventions")
        self.add(Content())

# eof
