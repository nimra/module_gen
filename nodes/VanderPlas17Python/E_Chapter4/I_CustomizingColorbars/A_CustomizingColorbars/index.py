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
# Figure 4-49. A simple colorbar legend
# 
# We’ll now discuss a few ideas for customizing these colorbars and using them effec‐
# tively in various situations.
# 
# Customizing Colorbars
# We can specify the colormap using the cmap argument to the plotting function that is
# creating the visualization (Figure 4-50):
#       In[4]: plt.imshow(I, cmap='gray');
# 
# 
# 
# 
# Figure 4-50. A grayscale colormap
# 
# All the available colormaps are in the plt.cm namespace; using IPython’s tab-
# completion feature will give you a full list of built-in possibilities:
#       plt.cm.<TAB>
# But being able to choose a colormap is just the first step: more important is how to
# decide among the possibilities! The choice turns out to be much more subtle than you
# might initially expect.
# 
# 
# 
# 256   |   Chapter 4: Visualization with Matplotlib
# 
# Choosing the colormap
# A full treatment of color choice within visualization is beyond the scope of this book,
# but for entertaining reading on this subject and others, see the article “Ten Simple
# Rules for Better Figures”. Matplotlib’s online documentation also has an interesting
# discussion of colormap choice.
# Broadly, you should be aware of three different categories of colormaps:
# Sequential colormaps
#     These consist of one continuous sequence of colors (e.g., binary or viridis).
# Divergent colormaps
#     These usually contain two distinct colors, which show positive and negative devi‐
#     ations from a mean (e.g., RdBu or PuOr).
# Qualitative colormaps
#    These mix colors with no particular sequence (e.g., rainbow or jet).
# The jet colormap, which was the default in Matplotlib prior to version 2.0, is an
# example of a qualitative colormap. Its status as the default was quite unfortunate,
# because qualitative maps are often a poor choice for representing quantitative data.
# Among the problems is the fact that qualitative maps usually do not display any uni‐
# form progression in brightness as the scale increases.
# We can see this by converting the jet colorbar into black and white (Figure 4-51):
#     In[5]:
#     from matplotlib.colors import LinearSegmentedColormap
# 
#     def grayscale_cmap(cmap):
#         """Return a grayscale version of the given colormap"""
#         cmap = plt.cm.get_cmap(cmap)
#         colors = cmap(np.arange(cmap.N))
# 
#         # convert RGBA to perceived grayscale luminance
#         # cf. http://alienryderflex.com/hsp.html
#         RGB_weight = [0.299, 0.587, 0.114]
#         luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
#         colors[:, :3] = luminance[:, np.newaxis]
# 
#         return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)
# 
# 
#     def view_colormap(cmap):
#         """Plot a colormap with its grayscale equivalent"""
#         cmap = plt.cm.get_cmap(cmap)
#         colors = cmap(np.arange(cmap.N))
# 
#         cmap = grayscale_cmap(cmap)
#         grayscale = cmap(np.arange(cmap.N))
# 
# 
#                                                                Customizing Colorbars   |   257
# 
#            fig, ax = plt.subplots(2, figsize=(6, 2),
#                                   subplot_kw=dict(xticks=[], yticks=[]))
#            ax[0].imshow([colors], extent=[0, 10, 0, 1])
#            ax[1].imshow([grayscale], extent=[0, 10, 0, 1])
#       In[6]: view_colormap('jet')
# 
# 
# 
# 
# Figure 4-51. The jet colormap and its uneven luminance scale
# 
# Notice the bright stripes in the grayscale image. Even in full color, this uneven bright‐
# ness means that the eye will be drawn to certain portions of the color range, which
# will potentially emphasize unimportant parts of the dataset. It’s better to use a color‐
# map such as viridis (the default as of Matplotlib 2.0), which is specifically construc‐
# ted to have an even brightness variation across the range. Thus, it not only plays well
# with our color perception, but also will translate well to grayscale printing
# (Figure 4-52):
#       In[7]: view_colormap('viridis')
# 
# 
# 
# 
# Figure 4-52. The viridis colormap and its even luminance scale
# 
# If you favor rainbow schemes, another good option for continuous data is the
# cubehelix colormap (Figure 4-53):
#       In[8]: view_colormap('cubehelix')
# 
# 
# 
# 
# Figure 4-53. The cubehelix colormap and its luminance
# 
# For other situations, such as showing positive and negative deviations from some
# mean, dual-color colorbars such as RdBu (short for Red-Blue) can be useful. However,
# 
# 
# 258   |   Chapter 4: Visualization with Matplotlib
# 
# as you can see in Figure 4-54, it’s important to note that the positive-negative infor‐
# mation will be lost upon translation to grayscale!
#     In[9]: view_colormap('RdBu')
# 
# 
# 
# 
# Figure 4-54. The RdBu (Red-Blue) colormap and its luminance
# 
# We’ll see examples of using some of these color maps as we continue.
# There are a large number of colormaps available in Matplotlib; to see a list of them,
# you can use IPython to explore the plt.cm submodule. For a more principled
# approach to colors in Python, you can refer to the tools and documentation within
# the Seaborn library (see “Visualization with Seaborn” on page 311).
# 
# Color limits and extensions
# Matplotlib allows for a large range of colorbar customization. The colorbar itself is
# simply an instance of plt.Axes, so all of the axes and tick formatting tricks we’ve
# learned are applicable. The colorbar has some interesting flexibility; for example, we
# can narrow the color limits and indicate the out-of-bounds values with a triangular
# arrow at the top and bottom by setting the extend property. This might come in
# handy, for example, if you’re displaying an image that is subject to noise
# (Figure 4-55):
#     In[10]: # make noise in 1% of the image pixels
#             speckles = (np.random.random(I.shape) < 0.01)
#             I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))
# 
#              plt.figure(figsize=(10, 3.5))
# 
#              plt.subplot(1, 2, 1)
#              plt.imshow(I, cmap='RdBu')
#              plt.colorbar()
# 
#              plt.subplot(1, 2, 2)
#              plt.imshow(I, cmap='RdBu')
#              plt.colorbar(extend='both')
#              plt.clim(-1, 1);
# 
# 
# 
# 
#                                                                Customizing Colorbars   |   259
# 
# Figure 4-55. Specifying colormap extensions
# 
# Notice that in the left panel, the default color limits respond to the noisy pixels, and
# the range of the noise completely washes out the pattern we are interested in. In the
# right panel, we manually set the color limits, and add extensions to indicate values
# that are above or below those limits. The result is a much more useful visualization of
# our data.
# 
# Discrete colorbars
# Colormaps are by default continuous, but sometimes you’d like to represent discrete
# values. The easiest way to do this is to use the plt.cm.get_cmap() function, and pass
# the name of a suitable colormap along with the number of desired bins (Figure 4-56):
#       In[11]: plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
#               plt.colorbar()
#               plt.clim(-1, 1);
# 
# 
# 
# 
# Figure 4-56. A discretized colormap
# 
# The discrete version of a colormap can be used just like any other colormap.
# 
# 
# 
# 
# 260   |   Chapter 4: Visualization with Matplotlib
# 
# Example: Handwritten Digits
# For an example of where this might be useful, let’s look at an interesting visualization
# of some handwritten digits data. This data is included in Scikit-Learn, and consists of
# nearly 2,000 8×8 thumbnails showing various handwritten digits.
# For now, let’s start by downloading the digits data and visualizing several of the exam‐
# ple images with plt.imshow() (Figure 4-57):
#     In[12]: # load images of the digits 0 through 5 and visualize several of them
#             from sklearn.datasets import load_digits
#             digits = load_digits(n_class=6)
# 
#             fig, ax = plt.subplots(8, 8, figsize=(6, 6))
#             for i, axi in enumerate(ax.flat):
#                 axi.imshow(digits.images[i], cmap='binary')
#                 axi.set(xticks=[], yticks=[])
# 
# 
# 
# 
# Figure 4-57. Sample of handwritten digit data
# 
# Because each digit is defined by the hue of its 64 pixels, we can consider each digit to
# be a point lying in 64-dimensional space: each dimension represents the brightness of
# one pixel. But visualizing relationships in such high-dimensional spaces can be
# extremely difficult. One way to approach this is to use a dimensionality reduction
# technique such as manifold learning to reduce the dimensionality of the data while
# maintaining the relationships of interest. Dimensionality reduction is an example of
# unsupervised machine learning, and we will discuss it in more detail in “What Is
# Machine Learning?” on page 332.
# Deferring the discussion of these details, let’s take a look at a two-dimensional mani‐
# fold learning projection of this digits data (see “In-Depth: Manifold Learning” on
# page 445 for details):
# 
# 
#                                                                 Customizing Colorbars   |   261
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Customizing Colorbars",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CustomizingColorbars(HierNode):
    def __init__(self):
        super().__init__("Customizing Colorbars")
        self.add(Content())

# eof