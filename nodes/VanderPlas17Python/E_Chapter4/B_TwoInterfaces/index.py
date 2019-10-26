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
#                   'svg': 'Scalable Vector Graphics',
#                   'svgz': 'Scalable Vector Graphics',
#                   'tif': 'Tagged Image File Format',
#                   'tiff': 'Tagged Image File Format'}
# 
# Note that when saving your figure, it’s not necessary to use plt.show() or related
# commands discussed earlier.
# 
# Two Interfaces for the Price of One
# A potentially confusing feature of Matplotlib is its dual interfaces: a convenient
# MATLAB-style state-based interface, and a more powerful object-oriented interface.
# We’ll quickly highlight the differences between the two here.
# 
# MATLAB-style interface
# Matplotlib was originally written as a Python alternative for MATLAB users, and
# much of its syntax reflects that fact. The MATLAB-style tools are contained in the
# pyplot (plt) interface. For example, the following code will probably look quite
# familiar to MATLAB users (Figure 4-3):
#       In[9]: plt.figure()          # create a plot figure
# 
#                # create the first of two panels and set current axis
#                plt.subplot(2, 1, 1) # (rows, columns, panel number)
#                plt.plot(x, np.sin(x))
# 
#                # create the second panel and set current axis
#                plt.subplot(2, 1, 2)
#                plt.plot(x, np.cos(x));
# 
# 
# 
# 
# Figure 4-3. Subplots using the MATLAB-style interface
# 
# It’s important to note that this interface is stateful: it keeps track of the “current” figure
# and axes, which are where all plt commands are applied. You can get a reference to
# 
# 
# 
# 222   |   Chapter 4: Visualization with Matplotlib
# 
# these using the plt.gcf() (get current figure) and plt.gca() (get current axes)
# routines.
# While this stateful interface is fast and convenient for simple plots, it is easy to run
# into problems. For example, once the second panel is created, how can we go back
# and add something to the first? This is possible within the MATLAB-style interface,
# but a bit clunky. Fortunately, there is a better way.
# 
# Object-oriented interface
# The object-oriented interface is available for these more complicated situations, and
# for when you want more control over your figure. Rather than depending on some
# notion of an “active” figure or axes, in the object-oriented interface the plotting func‐
# tions are methods of explicit Figure and Axes objects. To re-create the previous plot
# using this style of plotting, you might do the following (Figure 4-4):
#     In[10]: # First create a grid of plots
#             # ax will be an array of two Axes objects
#             fig, ax = plt.subplots(2)
# 
#              # Call plot() method on the appropriate object
#              ax[0].plot(x, np.sin(x))
#              ax[1].plot(x, np.cos(x));
# 
# 
# 
# 
# Figure 4-4. Subplots using the object-oriented interface
# 
# For more simple plots, the choice of which style to use is largely a matter of prefer‐
# ence, but the object-oriented approach can become a necessity as plots become more
# complicated. Throughout this chapter, we will switch between the MATLAB-style
# and object-oriented interfaces, depending on what is most convenient. In most cases,
# the difference is as small as switching plt.plot() to ax.plot(), but there are a few
# gotchas that we will highlight as they come up in the following sections.
# 
# 
# 
# 
#                                                            Two Interfaces for the Price of One   |   223
# 
# Simple Line Plots
# Perhaps the simplest of all plots is the visualization of a single function y = f x . Here
# we will take a first look at creating a simple plot of this type. As with all the following
# sections, we’ll start by setting up the notebook for plotting and importing the func‐
# tions we will use:
#       In[1]: %matplotlib inline
#              import matplotlib.pyplot as plt
#              plt.style.use('seaborn-whitegrid')
#              import numpy as np
# For all Matplotlib plots, we start by creating a figure and an axes. In their simplest
# form, a figure and axes can be created as follows (Figure 4-5):
#       In[2]: fig = plt.figure()
#              ax = plt.axes()
# 
# 
# 
# 
# Figure 4-5. An empty gridded axes
# 
# In Matplotlib, the figure (an instance of the class plt.Figure) can be thought of as a
# single container that contains all the objects representing axes, graphics, text, and
# labels. The axes (an instance of the class plt.Axes) is what we see above: a bounding
# box with ticks and labels, which will eventually contain the plot elements that make
# up our visualization. Throughout this book, we’ll commonly use the variable name
# fig to refer to a figure instance, and ax to refer to an axes instance or group of axes
# instances.
# Once we have created an axes, we can use the ax.plot function to plot some data.
# Let’s start with a simple sinusoid (Figure 4-6):
#       In[3]: fig = plt.figure()
#              ax = plt.axes()
# 
#               x = np.linspace(0, 10, 1000)
#               ax.plot(x, np.sin(x));
# 
# 
# 
# 224   | Chapter 4: Visualization with Matplotlib
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Two Interfaces for the Price of One",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TwoInterfaces(HierNode):
    def __init__(self):
        super().__init__("Two Interfaces for the Price of One")
        self.add(Content())

# eof
