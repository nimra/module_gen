# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_LinePlot.index import LinePlot as A_LinePlot
from .B_BarPlot.index import BarPlot as B_BarPlot
from .C_HistogramDensityPlots.index import HistogramDensityPlots as C_HistogramDensityPlots
from .D_Boxand.index import Boxand as D_Boxand

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Univariate Plots
# Some common and essential univariate plots are line plots, bar plots, histograms and
# density plots, and the box and whisker plot, to mention just a few.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Univariate Plots",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Univariate Plots"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UnivariatePlots(HierNode):
    def __init__(self):
        super().__init__("Univariate Plots")
        self.add(Content())
        self.add(A_LinePlot())
        self.add(B_BarPlot())
        self.add(C_HistogramDensityPlots())
        self.add(D_Boxand())

# eof
