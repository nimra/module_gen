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
# To be fair, the Matplotlib team is addressing this: it has recently added the plt.style
# tools (discussed in “Customizing Matplotlib: Configurations and Stylesheets” on page
# 282), and is starting to handle Pandas data more seamlessly. The 2.0 release of the
# library will include a new default stylesheet that will improve on the current status
# quo. But for all the reasons just discussed, Seaborn remains an extremely useful
# add-on.
# 
# Seaborn Versus Matplotlib
# Here is an example of a simple random-walk plot in Matplotlib, using its classic plot
# formatting and colors. We start with the typical imports:
#       In[1]: import matplotlib.pyplot as plt
#              plt.style.use('classic')
#              %matplotlib inline
#              import numpy as np
#              import pandas as pd
# Now we create some random walk data:
#       In[2]: # Create some data
#              rng = np.random.RandomState(0)
#              x = np.linspace(0, 10, 500)
#              y = np.cumsum(rng.randn(500, 6), 0)
# And do a simple plot (Figure 4-111):
#       In[3]: # Plot the data with Matplotlib defaults
#              plt.plot(x, y)
#              plt.legend('ABCDEF', ncol=2, loc='upper left');
# 
# 
# 
# 
# Figure 4-111. Data in Matplotlib’s default style
# 
# Although the result contains all the information we’d like it to convey, it does so in a
# way that is not all that aesthetically pleasing, and even looks a bit old-fashioned in the
# context of 21st-century data visualization.
# 
# 
# 
# 312   | Chapter 4: Visualization with Matplotlib
# 
# Now let’s take a look at how it works with Seaborn. As we will see, Seaborn has many
# of its own high-level plotting routines, but it can also overwrite Matplotlib’s default
# parameters and in turn get even simple Matplotlib scripts to produce vastly superior
# output. We can set the style by calling Seaborn’s set() method. By convention, Sea‐
# born is imported as sns:
#     In[4]: import seaborn as sns
#            sns.set()
# Now let’s rerun the same two lines as before (Figure 4-112):
#     In[5]: # same plotting code as above!
#            plt.plot(x, y)
#            plt.legend('ABCDEF', ncol=2, loc='upper left');
# 
# 
# 
# 
# Figure 4-112. Data in Seaborn’s default style
# 
# Ah, much better!
# 
# Exploring Seaborn Plots
# The main idea of Seaborn is that it provides high-level commands to create a variety
# of plot types useful for statistical data exploration, and even some statistical model
# fitting.
# Let’s take a look at a few of the datasets and plot types available in Seaborn. Note that
# all of the following could be done using raw Matplotlib commands (this is, in fact,
# what Seaborn does under the hood), but the Seaborn API is much more convenient.
# 
# 
# 
# 
#                                                                Visualization with Seaborn   |   313
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Seaborn Versus Matplotlib",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SeabornVersus(HierNode):
    def __init__(self):
        super().__init__("Seaborn Versus Matplotlib")
        self.add(Content())

# eof