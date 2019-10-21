# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Matplotliband.index import Matplotliband as A_Matplotliband
from .B_PandasPlotting.index import PandasPlotting as B_PandasPlotting
from .C_UnivariatePlots.index import UnivariatePlots as C_UnivariatePlots
from .D_MultivariatePlots.index import MultivariatePlots as D_MultivariatePlots
from .E_Images.index import Images as E_Images

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 12
# 
# 
# 
# Matplotlib and Seaborn
# It is critical to be able to plot the observations and variables of a dataset before subjecting
# the dataset to some machine learning algorithm or another. Data visualization is
# essential to understand your data and to glean insights into the underlying structure of
# the dataset. These insights help the scientist in deciding with statistical analysis or which
# learning algorithm is more appropriate for the given dataset. Also, the scientist can get
# ideas on suitable transformations to apply to the dataset.
#       In general, visualization in data science can conveniently be split into univariate
# and multivariate data visualizations. Univariate data visualization involves plotting
# a single variable to understand more about its distribution and structure, while
# multivariate plots expose the relationship and structure between two or more variables.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 12: Matplotlib and Seaborn",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 12: Matplotlib and Seaborn"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter12(HierNode):
    def __init__(self):
        super().__init__("Chapter 12: Matplotlib and Seaborn")
        self.add(Content())
        self.add(A_Matplotliband())
        self.add(B_PandasPlotting())
        self.add(C_UnivariatePlots())
        self.add(D_MultivariatePlots())
        self.add(E_Images())

# eof
