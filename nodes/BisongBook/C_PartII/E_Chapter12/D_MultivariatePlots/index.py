# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_ScatterPlot.index import ScatterPlot as A_ScatterPlot
from .B_PairwiseScatter.index import PairwiseScatter as B_PairwiseScatter
from .C_CorrelationMatrix.index import CorrelationMatrix as C_CorrelationMatrix

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Multivariate Plots
# Common multivariate visualizations include the scatter plot and its extension the
# pairwise plot, parallel coordinate plots, and the covariance matrix plot.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Multivariate Plots",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Multivariate Plots"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MultivariatePlots(HierNode):
    def __init__(self):
        super().__init__("Multivariate Plots")
        self.add(Content())
        self.add(A_ScatterPlot())
        self.add(B_PairwiseScatter())
        self.add(C_CorrelationMatrix())

# eof
