# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_ScatterPlot.index import ScatterPlot as A_ScatterPlot
from .B_PairwiseScatter.index import PairwiseScatter as B_PairwiseScatter
from .C_CorrelationMatrix.index import CorrelationMatrix as C_CorrelationMatrix

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 12   Matplotlib and Seaborn
# 
# 
# 
# 
# Figure 12-8. Boxplot with seaborn
# 
# 
# M
#  ultivariate Plots
# Common multivariate visualizations include the scatter plot and its extension the
# pairwise plot, parallel coordinate plots, and the covariance matrix plot.
# 
# 
# S
#  catter Plot
# Scatter plot exposes the relationships between two variables in a dataset. The outputs
# with matplotlib and seaborn are shown in Figure 12-9 and Figure 12-10, respectively.
# 
# #   create the dataset
# x   = np.random.sample(100)
# y   = 0.9 * np.asarray(x) + 1 + np.random.uniform(0,0.8, size=(100,))
# #   scatter plot with matplotlib
# 
# 158
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Multivariate Plots")
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
