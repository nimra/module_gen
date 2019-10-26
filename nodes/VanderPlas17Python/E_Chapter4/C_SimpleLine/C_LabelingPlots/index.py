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
# Figure 4-15. Example of a “tight” layout
# 
# It allows even higher-level specifications, such as ensuring an equal aspect ratio so
# that on your screen, one unit in x is equal to one unit in y (Figure 4-16):
#       In[13]: plt.plot(x, np.sin(x))
#               plt.axis('equal');
# 
# 
# 
# 
# Figure 4-16. Example of an “equal” layout, with units matched to the output resolution
# 
# For more information on axis limits and the other capabilities of the plt.axis()
# method, refer to the plt.axis() docstring.
# 
# Labeling Plots
# As the last piece of this section, we’ll briefly look at the labeling of plots: titles, axis
# labels, and simple legends.
# Titles and axis labels are the simplest such labels—there are methods that can be used
# to quickly set them (Figure 4-17):
#       In[14]: plt.plot(x, np.sin(x))
#               plt.title("A Sine Curve")
# 
# 
# 
# 
# 230   |   Chapter 4: Visualization with Matplotlib
# 
#             plt.xlabel("x")
#             plt.ylabel("sin(x)");
# 
# 
# 
# 
# Figure 4-17. Examples of axis labels and title
# 
# You can adjust the position, size, and style of these labels using optional arguments to
# the function. For more information, see the Matplotlib documentation and the doc‐
# strings of each of these functions.
# When multiple lines are being shown within a single axes, it can be useful to create a
# plot legend that labels each line type. Again, Matplotlib has a built-in way of quickly
# creating such a legend. It is done via the (you guessed it) plt.legend() method.
# Though there are several valid ways of using this, I find it easiest to specify the label
# of each line using the label keyword of the plot function (Figure 4-18):
#     In[15]: plt.plot(x, np.sin(x), '-g', label='sin(x)')
#             plt.plot(x, np.cos(x), ':b', label='cos(x)')
#             plt.axis('equal')
# 
#             plt.legend();
# 
# 
# 
# 
# Figure 4-18. Plot legend example
# 
# 
# 
#                                                                     Simple Line Plots   |   231
# 
# As you can see, the plt.legend() function keeps track of the line style and color, and
# matches these with the correct label. More information on specifying and formatting
# plot legends can be found in the plt.legend() docstring; additionally, we will cover
# some more advanced legend options in “Customizing Plot Legends” on page 249.
# 
# 
#                                              Matplotlib Gotchas
#   While most plt functions translate directly to ax methods (such as plt.plot() →
#   ax.plot(), plt.legend() → ax.legend(), etc.), this is not the case for all com‐
#   mands. In particular, functions to set limits, labels, and titles are slightly modified.
#   For transitioning between MATLAB-style functions and object-oriented methods,
#   make the following changes:
# 
#       • plt.xlabel() → ax.set_xlabel()
#       • plt.ylabel() → ax.set_ylabel()
#       • plt.xlim() → ax.set_xlim()
#       • plt.ylim() → ax.set_ylim()
#       • plt.title() → ax.set_title()
# 
#   In the object-oriented interface to plotting, rather than calling these functions indi‐
#   vidually, it is often more convenient to use the ax.set() method to set all these prop‐
#   erties at once (Figure 4-19):
#           In[16]: ax = plt.axes()
#                   ax.plot(x, np.sin(x))
#                   ax.set(xlim=(0, 10), ylim=(-2, 2),
#                          xlabel='x', ylabel='sin(x)',
#                          title='A Simple Plot');
# 
# 
# 
# 
#   Figure 4-19. Example of using ax.set to set multiple properties at once
# 
# 
# 
# 
# 232   |    Chapter 4: Visualization with Matplotlib
# 
# Simple Scatter Plots
# Another commonly used plot type is the simple scatter plot, a close cousin of the line
# plot. Instead of points being joined by line segments, here the points are represented
# individually with a dot, circle, or other shape. We’ll start by setting up the notebook
# for plotting and importing the functions we will use:
#     In[1]: %matplotlib inline
#            import matplotlib.pyplot as plt
#            plt.style.use('seaborn-whitegrid')
#            import numpy as np
# 
# 
# Scatter Plots with plt.plot
# In the previous section, we looked at plt.plot/ax.plot to produce line plots. It turns
# out that this same function can produce scatter plots as well (Figure 4-20):
#     In[2]: x = np.linspace(0, 10, 30)
#            y = np.sin(x)
# 
#             plt.plot(x, y, 'o', color='black');
# 
# 
# 
# 
# Figure 4-20. Scatter plot example
# 
# The third argument in the function call is a character that represents the type of sym‐
# bol used for the plotting. Just as you can specify options such as '-' and '--' to con‐
# trol the line style, the marker style has its own set of short string codes. The full list of
# available symbols can be seen in the documentation of plt.plot, or in Matplotlib’s
# online documentation. Most of the possibilities are fairly intuitive, and we’ll show a
# number of the more common ones here (Figure 4-21):
#     In[3]: rng = np.random.RandomState(0)
#            for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
#                plt.plot(rng.rand(5), rng.rand(5), marker,
#                         label="marker='{0}'".format(marker))
# 
# 
# 
# 
#                                                                      Simple Scatter Plots   |   233
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Labeling Plots",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LabelingPlots(HierNode):
    def __init__(self):
        super().__init__("Labeling Plots")
        self.add(Content())

# eof
