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
#     In[5]: counts, bin_edges = np.histogram(data, bins=5)
#            print(counts)
#     [ 12 190 468 301   29]
# 
# 
# Two-Dimensional Histograms and Binnings
# Just as we create histograms in one dimension by dividing the number line into bins,
# we can also create histograms in two dimensions by dividing points among two-
# dimensional bins. We’ll take a brief look at several ways to do this here. We’ll start by
# defining some data—an x and y array drawn from a multivariate Gaussian
# distribution:
#     In[6]: mean = [0, 0]
#            cov = [[1, 1], [1, 2]]
#            x, y = np.random.multivariate_normal(mean, cov, 10000).T
# 
# plt.hist2d: Two-dimensional histogram
# One straightforward way to plot a two-dimensional histogram is to use Matplotlib’s
# plt.hist2d function (Figure 4-38):
#     In[12]: plt.hist2d(x, y, bins=30, cmap='Blues')
#             cb = plt.colorbar()
#             cb.set_label('counts in bin')
# 
# 
# 
# 
# Figure 4-38. A two-dimensional histogram with plt.hist2d
# 
# Just as with plt.hist, plt.hist2d has a number of extra options to fine-tune the plot
# and the binning, which are nicely outlined in the function docstring. Further, just as
# plt.hist has a counterpart in np.histogram, plt.hist2d has a counterpart in
# np.histogram2d, which can be used as follows:
#     In[8]: counts, xedges, yedges = np.histogram2d(x, y, bins=30)
# For the generalization of this histogram binning in dimensions higher than two, see
# the np.histogramdd function.
# 
# 
#                                                         Histograms, Binnings, and Density   |   247
# 
# plt.hexbin: Hexagonal binnings
# The two-dimensional histogram creates a tessellation of squares across the axes.
# Another natural shape for such a tessellation is the regular hexagon. For this purpose,
# Matplotlib provides the plt.hexbin routine, which represents a two-dimensional
# dataset binned within a grid of hexagons (Figure 4-39):
#       In[9]: plt.hexbin(x, y, gridsize=30, cmap='Blues')
#              cb = plt.colorbar(label='count in bin')
# 
# 
# 
# 
# Figure 4-39. A two-dimensional histogram with plt.hexbin
# 
# plt.hexbin has a number of interesting options, including the ability to specify
# weights for each point, and to change the output in each bin to any NumPy aggregate
# (mean of weights, standard deviation of weights, etc.).
# 
# Kernel density estimation
# Another common method of evaluating densities in multiple dimensions is kernel
# density estimation (KDE). This will be discussed more fully in “In-Depth: Kernel
# Density Estimation” on page 491, but for now we’ll simply mention that KDE can be
# thought of as a way to “smear out” the points in space and add up the result to obtain
# a smooth function. One extremely quick and simple KDE implementation exists in
# the scipy.stats package. Here is a quick example of using the KDE on this data
# (Figure 4-40):
#       In[10]: from scipy.stats import gaussian_kde
# 
#                 # fit an array of size [Ndim, Nsamples]
#                 data = np.vstack([x, y])
#                 kde = gaussian_kde(data)
# 
#                 # evaluate on a regular grid
#                 xgrid = np.linspace(-3.5, 3.5, 40)
#                 ygrid = np.linspace(-6, 6, 40)
#                 Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
#                 Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))
# 
# 
# 248   | Chapter 4: Visualization with Matplotlib
# 
#             # Plot the result as an image
#             plt.imshow(Z.reshape(Xgrid.shape),
#                        origin='lower', aspect='auto',
#                        extent=[-3.5, 3.5, -6, 6],
#                        cmap='Blues')
#             cb = plt.colorbar()
#             cb.set_label("density")
# 
# 
# 
# 
# Figure 4-40. A kernel density representation of a distribution
# 
# KDE has a smoothing length that effectively slides the knob between detail and
# smoothness (one example of the ubiquitous bias–variance trade-off). The literature
# on choosing an appropriate smoothing length is vast: gaussian_kde uses a rule of
# thumb to attempt to find a nearly optimal smoothing length for the input data.
# Other KDE implementations are available within the SciPy ecosystem, each with its
# own various strengths and weaknesses; see, for example, sklearn.neighbors.Kernel
# Density and statsmodels.nonparametric.kernel_density.KDEMultivariate. For
# visualizations based on KDE, using Matplotlib tends to be overly verbose. The Sea‐
# born library, discussed in “Visualization with Seaborn” on page 311, provides a much
# more terse API for creating KDE-based visualizations.
# 
# Customizing Plot Legends
# Plot legends give meaning to a visualization, assigning labels to the various plot ele‐
# ments. We previously saw how to create a simple legend; here we’ll take a look at cus‐
# tomizing the placement and aesthetics of the legend in Matplotlib.
# The simplest legend can be created with the plt.legend() command, which auto‐
# matically creates a legend for any labeled plot elements (Figure 4-41):
#     In[1]: import matplotlib.pyplot as plt
#            plt.style.use('classic')
# 
# 
# 
# 
#                                                                  Customizing Plot Legends   |   249
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Two-Dimensional Histograms and Binnings",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TwoDimensionalHistograms(HierNode):
    def __init__(self):
        super().__init__("Two-Dimensional Histograms and Binnings")
        self.add(Content())

# eof
