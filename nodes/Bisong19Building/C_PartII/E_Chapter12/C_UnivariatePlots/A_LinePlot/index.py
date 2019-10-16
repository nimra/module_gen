# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Line Plot
# Let’s plot a sine graph of 100 points from the negative to positive exponential range. The
# plot method allows us to plot lines or markers to the figure. The outputs of the sine and
# cosine line plot are shown in Figure 12-1 and Figure 12-2, respectively.
# 
# data = np.linspace(-np.e, np.e, 100, endpoint=True)
# # plot a line plot of the sine wave
# plt.plot(np.sin(data))
# plt.show()
# # plot a red cosine wave with dash and dot markers
# plt.plot(np.cos(data), 'r-.')
# plt.show()
# 
# 
# 
# 
# 
# Figure 12-1. Lineplot with Matplotlib
# 
# 
# 
# 
# Figure 12-2. Lineplot with seaborn

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Line Plot",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Line Plot"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LinePlot(HierNode):
    def __init__(self):
        super().__init__("Line Plot")
        self.add(Content())

# eof
