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

from .A_Installingand.index import Installingand as A_Installingand
from .B_IntroducingPandas.index import IntroducingPandas as B_IntroducingPandas
from .C_DataIndexing.index import DataIndexing as C_DataIndexing
from .D_Operatingon.index import Operatingon as D_Operatingon
from .E_HandlingMissing.index import HandlingMissing as E_HandlingMissing
from .F_HierarchicalIndexing.index import HierarchicalIndexing as F_HierarchicalIndexing
from .G_CombiningDatasets.index import CombiningDatasets as G_CombiningDatasets
from .H_CombiningDatasets.index import CombiningDatasets as H_CombiningDatasets
from .I_Aggregationand.index import Aggregationand as I_Aggregationand
from .J_PivotTables.index import PivotTables as J_PivotTables
from .K_VectorizedString.index import VectorizedString as K_VectorizedString
from .L_Workingwith.index import Workingwith as L_Workingwith
from .M_HighPerformancePandas.index import HighPerformancePandas as M_HighPerformancePandas
from .N_FurtherResources.index import FurtherResources as N_FurtherResources

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                                                                         CHAPTER 3
#                        Data Manipulation with Pandas
# 
# 
# 
# 
# In the previous chapter, we dove into detail on NumPy and its ndarray object, which
# provides efficient storage and manipulation of dense typed arrays in Python. Here
# we’ll build on this knowledge by looking in detail at the data structures provided by
# the Pandas library. Pandas is a newer package built on top of NumPy, and provides an
# efficient implementation of a DataFrame. DataFrames are essentially multidimen‐
# sional arrays with attached row and column labels, and often with heterogeneous
# types and/or missing data. As well as offering a convenient storage interface for
# labeled data, Pandas implements a number of powerful data operations familiar to
# users of both database frameworks and spreadsheet programs.
# As we saw, NumPy’s ndarray data structure provides essential features for the type of
# clean, well-organized data typically seen in numerical computing tasks. While it
# serves this purpose very well, its limitations become clear when we need more flexi‐
# bility (attaching labels to data, working with missing data, etc.) and when attempting
# operations that do not map well to element-wise broadcasting (groupings, pivots,
# etc.), each of which is an important piece of analyzing the less structured data avail‐
# able in many forms in the world around us. Pandas, and in particular its Series and
# DataFrame objects, builds on the NumPy array structure and provides efficient access
# to these sorts of “data munging” tasks that occupy much of a data scientist’s time.
# In this chapter, we will focus on the mechanics of using Series, DataFrame, and
# related structures effectively. We will use examples drawn from real datasets where
# appropriate, but these examples are not necessarily the focus.
# 
# Installing and Using Pandas
# Installing Pandas on your system requires NumPy to be installed, and if you’re build‐
# ing the library from source, requires the appropriate tools to compile the C and
# 
# 
#                                                                                      97
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 3. Data Manipulation with Pandas",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter3(HierNode):
    def __init__(self):
        super().__init__("Chapter 3. Data Manipulation with Pandas")
        self.add(Content())
        self.add(A_Installingand())
        self.add(B_IntroducingPandas())
        self.add(C_DataIndexing())
        self.add(D_Operatingon())
        self.add(E_HandlingMissing())
        self.add(F_HierarchicalIndexing())
        self.add(G_CombiningDatasets())
        self.add(H_CombiningDatasets())
        self.add(I_Aggregationand())
        self.add(J_PivotTables())
        self.add(K_VectorizedString())
        self.add(L_Workingwith())
        self.add(M_HighPerformancePandas())
        self.add(N_FurtherResources())

# eof
