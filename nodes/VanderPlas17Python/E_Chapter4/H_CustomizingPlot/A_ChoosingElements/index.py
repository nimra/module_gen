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
# Figure 4-43. A two-column plot legend
# 
# We can use a rounded box (fancybox) or add a shadow, change the transparency
# (alpha value) of the frame, or change the padding around the text (Figure 4-44):
#     In[6]: ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
#            fig
# 
# 
# 
# 
# Figure 4-44. A fancybox plot legend
# 
# For more information on available legend options, see the plt.legend docstring.
# 
# Choosing Elements for the Legend
# As we’ve already seen, the legend includes all labeled elements by default. If this is not
# what is desired, we can fine-tune which elements and labels appear in the legend by
# using the objects returned by plot commands. The plt.plot() command is able to
# create multiple lines at once, and returns a list of created line instances. Passing any of
# these to plt.legend() will tell it which to identify, along with the labels we’d like to
# specify (Figure 4-45):
#     In[7]: y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
#            lines = plt.plot(x, y)
# 
# 
# 
#                                                                Customizing Plot Legends   |   251
# 
#                # lines is a list of plt.Line2D instances
#                plt.legend(lines[:2], ['first', 'second']);
# 
# 
# 
# 
# Figure 4-45. Customization of legend elements
# 
# I generally find in practice that it is clearer to use the first method, applying labels to
# the plot elements you’d like to show on the legend (Figure 4-46):
#       In[8]: plt.plot(x, y[:, 0], label='first')
#              plt.plot(x, y[:, 1], label='second')
#              plt.plot(x, y[:, 2:])
#              plt.legend(framealpha=1, frameon=True);
# 
# 
# 
# 
# Figure 4-46. Alternative method of customizing legend elements
# 
# Notice that by default, the legend ignores all elements without a label attribute set.
# 
# Legend for Size of Points
# Sometimes the legend defaults are not sufficient for the given visualization. For exam‐
# ple, perhaps you’re using the size of points to mark certain features of the data, and
# want to create a legend reflecting this. Here is an example where we’ll use the size of
# points to indicate populations of California cities. We’d like a legend that specifies the
# 
# 
# 
# 252   |   Chapter 4: Visualization with Matplotlib
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Choosing Elements for the Legend",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ChoosingElements(HierNode):
    def __init__(self):
        super().__init__("Choosing Elements for the Legend")
        self.add(Content())

# eof
