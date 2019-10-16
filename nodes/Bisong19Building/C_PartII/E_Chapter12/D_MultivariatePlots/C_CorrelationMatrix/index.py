# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Correlation Matrix Plots
# Again, correlation shows how much relationship exists between two variables. By
# plotting the correlation matrix, we get a visual representation of which variables in the
# dataset are highly correlated. Remember that parametric machine learning methods
# such as logistic and linear regression can take a performance hit when variables are
# highly correlated. Also, in practice, the correlation values that are greater than –0.7 or
# 0.7 are for the most part highly correlated. The outputs with matplotlib and seaborn are
# shown in Figure 12-13 and Figure 12-14, respectively.
# 
# # create the dataset
# data = np.random.random([1000,6])
# # plot covariance matrix using the Matplotlib matshow function
# fig = plt.figure()
# ax = fig.add_subplot(111)
# my_plot = ax.matshow(pd.DataFrame(data).corr(), vmin=-1, vmax=1)
# fig.colorbar(my_plot)
# plt.show()
# 
# 
# 
# 
# Figure 12-13. Correlation matrix with Matplotlib
# 
# # plot covariance matrix with seaborn heatmap function
# sns.heatmap(pd.DataFrame(data).corr(), vmin=-1, vmax=1)
# plt.show()
# 
# 
# 
# 
# Figure 12-14. Correlation matrix with seaborn

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Correlation Matrix Plots",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Correlation Matrix Plots"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CorrelationMatrix(HierNode):
    def __init__(self):
        super().__init__("Correlation Matrix Plots")
        self.add(Content())

# eof
