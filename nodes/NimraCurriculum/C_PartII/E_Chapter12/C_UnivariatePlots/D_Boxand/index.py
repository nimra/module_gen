# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                         Chapter 12   Matplotlib and Seaborn
# 
# Box and Whisker Plots
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
#                                                                                          157
# 
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
        super().__init__("Box and Whisker Plots")
        self.add(MarkdownBlock("# Box and Whisker Plots"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Boxand(HierNode):
    def __init__(self):
        super().__init__("Box and Whisker Plots")
        self.add(Content())

# eof
