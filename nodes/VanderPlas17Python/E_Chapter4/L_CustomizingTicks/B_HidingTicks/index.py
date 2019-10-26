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
# Figure 4-75. Hiding ticks within image plots
# 
# Notice that each image has its own axes, and we’ve set the locators to null because the
# tick values (pixel number in this case) do not convey relevant information for this
# particular visualization.
# 
# Reducing or Increasing the Number of Ticks
# One common problem with the default settings is that smaller subplots can end up
# with crowded labels. We can see this in the plot grid shown in Figure 4-76:
#       In[7]: fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)
# 
# 
# 
# 
# Figure 4-76. A default plot with crowded ticks
# 
# Particularly for the x ticks, the numbers nearly overlap, making them quite difficult to
# decipher. We can fix this with the plt.MaxNLocator(), which allows us to specify the
# maximum number of ticks that will be displayed. Given this maximum number, Mat‐
# plotlib will use internal logic to choose the particular tick locations (Figure 4-77):
# 
# 
# 
# 
# 278   |   Chapter 4: Visualization with Matplotlib
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Hiding Ticks or Labels",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HidingTicks(HierNode):
    def __init__(self):
        super().__init__("Hiding Ticks or Labels")
        self.add(Content())

# eof