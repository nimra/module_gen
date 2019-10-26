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
#     In[10]: r = np.linspace(0, 6, 20)
#             theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
#             r, theta = np.meshgrid(r, theta)
# 
#             X = r * np.sin(theta)
#             Y = r * np.cos(theta)
#             Z = f(X, Y)
# 
#             ax = plt.axes(projection='3d')
#             ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                             cmap='viridis', edgecolor='none');
# 
# 
# 
# 
# Figure 4-98. A polar surface plot
# 
# Surface Triangulations
# For some applications, the evenly sampled grids required by the preceding routines
# are overly restrictive and inconvenient. In these situations, the triangulation-based
# plots can be very useful. What if rather than an even draw from a Cartesian or a polar
# grid, we instead have a set of random draws?
#     In[11]: theta = 2 * np.pi * np.random.random(1000)
#             r = 6 * np.random.random(1000)
#             x = np.ravel(r * np.sin(theta))
#             y = np.ravel(r * np.cos(theta))
#             z = f(x, y)
# We could create a scatter plot of the points to get an idea of the surface we’re sampling
# from (Figure 4-99):
#     In[12]: ax = plt.axes(projection='3d')
#             ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5);
# 
# 
# 
# 
#                                                    Three-Dimensional Plotting in Matplotlib   |   295
# 
# Figure 4-99. A three-dimensional sampled surface
# 
# This leaves a lot to be desired. The function that will help us in this case is
# ax.plot_trisurf, which creates a surface by first finding a set of triangles formed
# between adjacent points (the result is shown in Figure 4-100; remember that x, y, and
# z here are one-dimensional arrays):
#       In[13]: ax = plt.axes(projection='3d')
#               ax.plot_trisurf(x, y, z,
#                               cmap='viridis', edgecolor='none');
# 
# 
# 
# 
# Figure 4-100. A triangulated surface plot
# 
# The result is certainly not as clean as when it is plotted with a grid, but the flexibility
# of such a triangulation allows for some really interesting three-dimensional plots. For
# example, it is actually possible to plot a three-dimensional Möbius strip using this, as
# we’ll see next.
# 
# Example: Visualizing a Möbius strip
# A Möbius strip is similar to a strip of paper glued into a loop with a half-twist. Topo‐
# logically, it’s quite interesting because despite appearances it has only a single side!
# Here we will visualize such an object using Matplotlib’s three-dimensional tools. The
# key to creating the Möbius strip is to think about its parameterization: it’s a two-
# 
# 
# 296   | Chapter 4: Visualization with Matplotlib
# 
# dimensional strip, so we need two intrinsic dimensions. Let’s call them θ, which
# ranges from 0 to 2π around the loop, and w which ranges from –1 to 1 across the
# width of the strip:
#     In[14]: theta = np.linspace(0, 2 * np.pi, 30)
#             w = np.linspace(-0.25, 0.25, 8)
#             w, theta = np.meshgrid(w, theta)
# Now from this parameterization, we must determine the (x, y, z) positions of the
# embedded strip.
# Thinking about it, we might realize that there are two rotations happening: one is the
# position of the loop about its center (what we’ve called θ), while the other is the twist‐
# ing of the strip about its axis (we’ll call this ϕ). For a Möbius strip, we must have the
# strip make half a twist during a full loop, or Δϕ = Δθ/2.
#     In[15]: phi = 0.5 * theta
# Now we use our recollection of trigonometry to derive the three-dimensional embed‐
# ding. We’ll define r, the distance of each point from the center, and use this to find the
# embedded x, y, z coordinates:
#     In[16]: # radius in x-y plane
#             r = 1 + w * np.cos(phi)
# 
#             x = np.ravel(r * np.cos(theta))
#             y = np.ravel(r * np.sin(theta))
#             z = np.ravel(w * np.sin(phi))
# Finally, to plot the object, we must make sure the triangulation is correct. The best
# way to do this is to define the triangulation within the underlying parameterization,
# and then let Matplotlib project this triangulation into the three-dimensional space of
# the Möbius strip. This can be accomplished as follows (Figure 4-101):
#     In[17]: # triangulate in the underlying parameterization
#             from matplotlib.tri import Triangulation
#             tri = Triangulation(np.ravel(w), np.ravel(theta))
# 
#             ax = plt.axes(projection='3d')
#             ax.plot_trisurf(x, y, z, triangles=tri.triangles,
#                             cmap='viridis', linewidths=0.2);
# 
#             ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1);
# 
# 
# 
# 
#                                                    Three-Dimensional Plotting in Matplotlib   |   297
# 
# Figure 4-101. Visualizing a Möbius strip
# 
# Combining all of these techniques, it is possible to create and display a wide variety of
# three-dimensional objects and patterns in Matplotlib.
# 
# Geographic Data with Basemap
# One common type of visualization in data science is that of geographic data. Matplot‐
# lib’s main tool for this type of visualization is the Basemap toolkit, which is one of
# several Matplotlib toolkits that live under the mpl_toolkits namespace. Admittedly,
# Basemap feels a bit clunky to use, and often even simple visualizations take much
# longer to render than you might hope. More modern solutions, such as leaflet or the
# Google Maps API, may be a better choice for more intensive map visualizations. Still,
# Basemap is a useful tool for Python users to have in their virtual toolbelts. In this sec‐
# tion, we’ll show several examples of the type of map visualization that is possible with
# this toolkit.
# Installation of Basemap is straightforward; if you’re using conda you can type this and
# the package will be downloaded:
#       $ conda install basemap
# We add just a single new import to our standard boilerplate:
#       In[1]: %matplotlib inline
#              import numpy as np
#              import matplotlib.pyplot as plt
#              from mpl_toolkits.basemap import Basemap
# Once you have the Basemap toolkit installed and imported, geographic plots are just
# a few lines away (the graphics in Figure 4-102 also require the PIL package in Python
# 2, or the pillow package in Python 3):
#       In[2]: plt.figure(figsize=(8, 8))
#              m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
#              m.bluemarble(scale=0.5);
# 
# 
# 
# 
# 298   |   Chapter 4: Visualization with Matplotlib
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Surface Triangulations",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SurfaceTriangulations(HierNode):
    def __init__(self):
        super().__init__("Surface Triangulations")
        self.add(Content())

# eof
