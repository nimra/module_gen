# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Histogram/Density Plots
# Histogram and density plots are essential for examining the statistical distribution of
# a variable. For a simple histogram, we’ll create a set of 100,000 points from the normal
# distribution. The outputs with matplotlib and seaborn are shown in Figure 12-5 and
# Figure 12-6, respectively.
# 
# # create 100000 data points from the normal distributions
# data = np.random.randn(100000)
# # create a histogram plot
# plt.hist(data)
# plt.show()
# # crate a density plot using seaborn
# my_fig = sns.distplot(data, hist=False)
# plt.show()
# 
# 
# 
# 
# 
# Figure 12-5. Histogram with Matplotlib
# 
# 
# 
# 
# Figure 12-6. Histogram with seaborn

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Histogram/Density Plots",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Histogram/Density Plots"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HistogramDensityPlots(HierNode):
    def __init__(self):
        super().__init__("Histogram/Density Plots")
        self.add(Content())

# eof
