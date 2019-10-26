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

from .A_RelationalAlgebra.index import RelationalAlgebra as A_RelationalAlgebra
from .B_Categoriesof.index import Categoriesof as B_Categoriesof
from .C_Specificationof.index import Specificationof as C_Specificationof
from .D_SpecifyingSet.index import SpecifyingSet as D_SpecifyingSet
from .E_OverlappingColumn.index import OverlappingColumn as E_OverlappingColumn
from .F_ExampleUS.index import ExampleUS as F_ExampleUS

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                                                        3 NaN B3 C3
#                                                        4 NaN B4 C4
# 
# The combination of options of the pd.concat function allows a wide range of possi‐
# ble behaviors when you are joining two datasets; keep these in mind as you use these
# tools for your own data.
# 
# The append() method
# Because direct array concatenation is so common, Series and DataFrame objects
# have an append method that can accomplish the same thing in fewer keystrokes. For
# example, rather than calling pd.concat([df1, df2]), you can simply call
# df1.append(df2):
#       In[16]: print(df1); print(df2); print(df1.append(df2))
#       df1                    df2                df1.append(df2)
#              A     B              A    B             A   B
#        1    A1    B1         3   A3   B3        1   A1 B1
#        2    A2    B2         4   A4   B4        2   A2 B2
#                                                 3   A3 B3
#                                                 4   A4 B4
# 
# Keep in mind that unlike the append() and extend() methods of Python lists, the
# append() method in Pandas does not modify the original object—instead, it creates a
# new object with the combined data. It also is not a very efficient method, because it
# involves creation of a new index and data buffer. Thus, if you plan to do multiple
# append operations, it is generally better to build a list of DataFrames and pass them all
# at once to the concat() function.
# In the next section, we’ll look at another more powerful approach to combining data
# from multiple sources, the database-style merges/joins implemented in pd.merge. For
# more information on concat(), append(), and related functionality, see the “Merge,
# Join, and Concatenate” section of the Pandas documentation.
# 
# Combining Datasets: Merge and Join
# One essential feature offered by Pandas is its high-performance, in-memory join and
# merge operations. If you have ever worked with databases, you should be familiar
# with this type of data interaction. The main interface for this is the pd.merge func‐
# tion, and we’ll see a few examples of how this can work in practice.
# 
# Relational Algebra
# The behavior implemented in pd.merge() is a subset of what is known as relational
# algebra, which is a formal set of rules for manipulating relational data, and forms the
# conceptual foundation of operations available in most databases. The strength of the
# 
# 
# 146   |     Chapter 3: Data Manipulation with Pandas
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Combining Datasets: Merge and Join",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CombiningDatasets(HierNode):
    def __init__(self):
        super().__init__("Combining Datasets: Merge and Join")
        self.add(Content())
        self.add(A_RelationalAlgebra())
        self.add(B_Categoriesof())
        self.add(C_Specificationof())
        self.add(D_SpecifyingSet())
        self.add(E_OverlappingColumn())
        self.add(F_ExampleUS())

# eof
