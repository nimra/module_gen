# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Pairwise Scatter Plot
# Pairwise scatter plot is an effective window for visualizing the relationships among
# multiple variables within the same plot. However, with higher-dimension datasets,
# the plot may become clogged up, so use it with care. Let’s see an example of this with
# Matplotlib and seaborn.
#     Here, we will use the method scatter_matrix, one of the plotting functions in Pandas
# to graph a pairwise scatter plot matrix. The outputs with matplotlib and seaborn are
# shown in Figure 12-11 and Figure 12-12, respectively.
# 
# # create the dataset
# data = np.random.randn(1000,6)
# # using Pandas scatter_matrix
# pd.plotting.scatter_matrix(pd.DataFrame(data), alpha=0.5, figsize=(12, 12),
# diagonal='kde')
# plt.show()
# 
# 
# 
# 
# Figure 12-11. Pairwise scatter plot with Pandas
# 
# 
# # pairwise scatter with seaborn
# sns.pairplot(pd.DataFrame(data))
# plt.show()
# 
# 
# 
# 
# 
# Figure 12-12. Pairwise scatter plot with seaborn

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Pairwise Scatter Plot",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Pairwise Scatter Plot"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PairwiseScatter(HierNode):
    def __init__(self):
        super().__init__("Pairwise Scatter Plot")
        self.add(Content())

# eof
