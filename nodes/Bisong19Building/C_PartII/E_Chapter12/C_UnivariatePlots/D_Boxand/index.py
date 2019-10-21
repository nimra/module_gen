# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Box and Whisker Plots
# Boxplot, also popularly called box and whisker plot, is another useful visualization
# technique for gaining insights into the underlying data distribution. The boxplot draws
# a box with the upper line representing the 75th percentile and the lower line the 25th
# percentile. A line is drawn at the center of the box indicating the 50th percentile or median
# value. The whiskers at both ends give an estimation of the spread or variance of the data
# values. The dots at the tail end of the whiskers represent possible outlier values. The
# outputs with matplotlib and seaborn are shown in Figure 12-7 and Figure 12-8, respectively.
# 
# # create data points
# data = np.random.randn(1000)
# ## box plot with matplotlib
# plt.boxplot(data)
# plt.show()
# ## box plot with seaborn
# sns.boxplot(data)
# plt.show()
# 
# 
# 
# 
# Figure 12-7. Boxplot with Matplotlib
# 
# 
# 
# 
# Figure 12-8. Boxplot with seaborn

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Box and Whisker Plots",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Box and Whisker Plots"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Boxand(HierNode):
    def __init__(self):
        super().__init__("Box and Whisker Plots")
        self.add(Content())

# eof
