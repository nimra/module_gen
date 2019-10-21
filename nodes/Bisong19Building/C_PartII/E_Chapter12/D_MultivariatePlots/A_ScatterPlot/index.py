# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Scatter Plot
# Scatter plot exposes the relationships between two variables in a dataset. The outputs
# with matplotlib and seaborn are shown in Figure 12-9 and Figure 12-10, respectively.
# 
# #   create the dataset
# x   = np.random.sample(100)
# y   = 0.9 * np.asarray(x) + 1 + np.random.uniform(0,0.8, size=(100,))
# #   scatter plot with matplotlib
# plt.scatter(x,y)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()
# # scatter plot with seaborn
# sns.regplot(x=x, y=y, fit_reg=False)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()
# 
# 
# 
# 
# Figure 12-9. Scatter plot with Matplotlib
# 
# 
# 
# 
# 
# Figure 12-10. Scatter plot with seaborn

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Scatter Plot",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Scatter Plot"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ScatterPlot(HierNode):
    def __init__(self):
        super().__init__("Scatter Plot")
        self.add(Content())

# eof
