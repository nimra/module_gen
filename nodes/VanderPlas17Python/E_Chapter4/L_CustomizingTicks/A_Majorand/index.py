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
# Major and Minor Ticks
# Within each axis, there is the concept of a major tick mark and a minor tick mark. As
# the names would imply, major ticks are usually bigger or more pronounced, while
# minor ticks are usually smaller. By default, Matplotlib rarely makes use of minor
# ticks, but one place you can see them is within logarithmic plots (Figure 4-73):
#       In[1]: %matplotlib inline
#              import matplotlib.pyplot as plt
#              plt.style.use('seaborn-whitegrid')
#              import numpy as np
#       In[2]: ax = plt.axes(xscale='log', yscale='log')
# 
# 
# 
# 
# Figure 4-73. Example of logarithmic scales and labels
# 
# We see here that each major tick shows a large tick mark and a label, while each
# minor tick shows a smaller tick mark with no label.
# We can customize these tick properties—that is, locations and labels—by setting the
# formatter and locator objects of each axis. Let’s examine these for the x axis of the
# plot just shown:
#       In[3]: print(ax.xaxis.get_major_locator())
#              print(ax.xaxis.get_minor_locator())
#       <matplotlib.ticker.LogLocator object at 0x107530cc0>
#       <matplotlib.ticker.LogLocator object at 0x107530198>
#       In[4]: print(ax.xaxis.get_major_formatter())
#              print(ax.xaxis.get_minor_formatter())
#       <matplotlib.ticker.LogFormatterMathtext object at 0x107512780>
#       <matplotlib.ticker.NullFormatter object at 0x10752dc18>
# We see that both major and minor tick labels have their locations specified by a
# LogLocator (which makes sense for a logarithmic plot). Minor ticks, though, have
# their labels formatted by a NullFormatter; this says that no labels will be shown.
# 
# 
# 
# 276   | Chapter 4: Visualization with Matplotlib
# 
# We’ll now show a few examples of setting these locators and formatters for various
# plots.
# 
# Hiding Ticks or Labels
# Perhaps the most common tick/label formatting operation is the act of hiding ticks or
# labels. We can do this using plt.NullLocator() and plt.NullFormatter(), as
# shown here (Figure 4-74):
#     In[5]: ax = plt.axes()
#            ax.plot(np.random.rand(50))
# 
#            ax.yaxis.set_major_locator(plt.NullLocator())
#            ax.xaxis.set_major_formatter(plt.NullFormatter())
# 
# 
# 
# 
# Figure 4-74. Plot with hidden tick labels (x-axis) and hidden ticks (y-axis)
# 
# Notice that we’ve removed the labels (but kept the ticks/gridlines) from the x axis,
# and removed the ticks (and thus the labels as well) from the y axis. Having no ticks at
# all can be useful in many situations—for example, when you want to show a grid of
# images. For instance, consider Figure 4-75, which includes images of different faces,
# an example often used in supervised machine learning problems (for more informa‐
# tion, see “In-Depth: Support Vector Machines” on page 405):
#     In[6]: fig, ax = plt.subplots(5, 5, figsize=(5, 5))
#            fig.subplots_adjust(hspace=0, wspace=0)
# 
#            # Get some face data from scikit-learn
#            from sklearn.datasets import fetch_olivetti_faces
#            faces = fetch_olivetti_faces().images
# 
#            for i in range(5):
#                for j in range(5):
#                    ax[i, j].xaxis.set_major_locator(plt.NullLocator())
#                    ax[i, j].yaxis.set_major_locator(plt.NullLocator())
#                    ax[i, j].imshow(faces[10 * i + j], cmap="bone")
# 
# 
# 
# 
#                                                                       Customizing Ticks   |   277
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Major and Minor Ticks",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Majorand(HierNode):
    def __init__(self):
        super().__init__("Major and Minor Ticks")
        self.add(Content())

# eof
