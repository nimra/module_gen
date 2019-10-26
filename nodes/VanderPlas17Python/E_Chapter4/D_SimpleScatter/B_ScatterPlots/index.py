# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# Figure 4-23. Customizing line and point numbers
# 
# This type of flexibility in the plt.plot function allows for a wide variety of possible
# visualization options. For a full description of the options available, refer to the
# plt.plot documentation.
# 
# Scatter Plots with plt.scatter
# A second, more powerful method of creating scatter plots is the plt.scatter func‐
# tion, which can be used very similarly to the plt.plot function (Figure 4-24):
#     In[6]: plt.scatter(x, y, marker='o');
# 
# 
# 
# 
# Figure 4-24. A simple scatter plot
# 
# The primary difference of plt.scatter from plt.plot is that it can be used to create
# scatter plots where the properties of each individual point (size, face color, edge color,
# etc.) can be individually controlled or mapped to data.
# Let’s show this by creating a random scatter plot with points of many colors and sizes.
# In order to better see the overlapping results, we’ll also use the alpha keyword to
# adjust the transparency level (Figure 4-25):
# 
# 
# 
#                                                                    Simple Scatter Plots   |   235
# 
#       In[7]: rng = np.random.RandomState(0)
#              x = rng.randn(100)
#              y = rng.randn(100)
#              colors = rng.rand(100)
#              sizes = 1000 * rng.rand(100)
# 
#               plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
#                           cmap='viridis')
#               plt.colorbar(); # show color scale
# 
# 
# 
# 
# Figure 4-25. Changing size, color, and transparency in scatter points
# 
# Notice that the color argument is automatically mapped to a color scale (shown here
# by the colorbar() command), and the size argument is given in pixels. In this way,
# the color and size of points can be used to convey information in the visualization, in
# order to illustrate multidimensional data.
# For example, we might use the Iris data from Scikit-Learn, where each sample is one
# of three types of flowers that has had the size of its petals and sepals carefully meas‐
# ured (Figure 4-26):
#       In[8]: from sklearn.datasets import load_iris
#              iris = load_iris()
#              features = iris.data.T
# 
#               plt.scatter(features[0], features[1], alpha=0.2,
#                           s=100*features[3], c=iris.target, cmap='viridis')
#               plt.xlabel(iris.feature_names[0])
#               plt.ylabel(iris.feature_names[1]);
# 
# 
# 
# 
# 236   | Chapter 4: Visualization with Matplotlib
# 
# Figure 4-26. Using point properties to encode features of the Iris data
# 
# We can see that this scatter plot has given us the ability to simultaneously explore
# four different dimensions of the data: the (x, y) location of each point corresponds to
# the sepal length and width, the size of the point is related to the petal width, and the
# color is related to the particular species of flower. Multicolor and multifeature scatter
# plots like this can be useful for both exploration and presentation of data.
# 
# plot Versus scatter: A Note on Efficiency
# Aside from the different features available in plt.plot and plt.scatter, why might
# you choose to use one over the other? While it doesn’t matter as much for small
# amounts of data, as datasets get larger than a few thousand points, plt.plot can be
# noticeably more efficient than plt.scatter. The reason is that plt.scatter has the
# capability to render a different size and/or color for each point, so the renderer must
# do the extra work of constructing each point individually. In plt.plot, on the other
# hand, the points are always essentially clones of each other, so the work of determin‐
# ing the appearance of the points is done only once for the entire set of data. For large
# datasets, the difference between these two can lead to vastly different performance,
# and for this reason, plt.plot should be preferred over plt.scatter for large
# datasets.
# 
# Visualizing Errors
# For any scientific measurement, accurate accounting for errors is nearly as important,
# if not more important, than accurate reporting of the number itself. For example,
# imagine that I am using some astrophysical observations to estimate the Hubble Con‐
# stant, the local measurement of the expansion rate of the universe. I know that the
# current literature suggests a value of around 71 (km/s)/Mpc, and I measure a value of
# 74 (km/s)/Mpc with my method. Are the values consistent? The only correct answer,
# given this information, is this: there is no way to know.
# 
# 
#                                                                           Visualizing Errors   |   237
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Scatter Plots with plt.scatter",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ScatterPlots(HierNode):
    def __init__(self):
        super().__init__("Scatter Plots with plt.scatter")
        self.add(Content())

# eof
