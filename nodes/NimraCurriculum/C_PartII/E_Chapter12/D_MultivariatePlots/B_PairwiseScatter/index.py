# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 12   Matplotlib and Seaborn
# 
# 
# 
# 
# Figure 12-10. Scatter plot with seaborn
# 
# Pairwise Scatter Plot
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
# 160
# 
#                                                   Chapter 12   Matplotlib and Seaborn
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
#                                                                                  161
# 
# Chapter 12   Matplotlib and Seaborn
# 
# 
# 
# 
# Figure 12-12. Pairwise scatter plot with seaborn
# 
# 
# Correlation Matrix Plots
# Again, correlation shows how much relationship exists between two variables. By
# plotting the correlation matrix, we get a visual representation of which variables in the
# dataset are highly correlated. Remember that parametric machine learning methods
# such as logistic and linear regression can take a performance hit when variables are
# 
# 
# 
# 162
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Pairwise Scatter Plot")
        self.add(MarkdownBlock("# Pairwise Scatter Plot"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PairwiseScatter(HierNode):
    def __init__(self):
        super().__init__("Pairwise Scatter Plot")
        self.add(Content())

# eof
