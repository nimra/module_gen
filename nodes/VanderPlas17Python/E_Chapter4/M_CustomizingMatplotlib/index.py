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

from .A_PlotCustomization.index import PlotCustomization as A_PlotCustomization
from .B_Changingthe.index import Changingthe as B_Changingthe
from .C_Stylesheets.index import Stylesheets as C_Stylesheets

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# Locator class             Description
# LinearLocator             Evenly spaced ticks from min to max
# LogLocator                Logarithmically ticks from min to max
# MultipleLocator           Ticks and range are a multiple of base
# MaxNLocator               Finds up to a max number of ticks at nice locations
# AutoLocator               (Default) MaxNLocator with simple defaults
# AutoMinorLocator Locator for minor ticks
# 
# 
# Formatter class              Description
# NullFormatter                No labels on the ticks
# IndexFormatter               Set the strings from a list of labels
# FixedFormatter               Set the strings manually for the labels
# FuncFormatter                User-defined function sets the labels
# FormatStrFormatter Use a format string for each value
# ScalarFormatter              (Default) Formatter for scalar values
# LogFormatter                 Default formatter for log axes
# 
# We’ll see additional examples of these throughout the remainder of the book.
# 
# Customizing Matplotlib: Configurations and Stylesheets
# Matplotlib’s default plot settings are often the subject of complaint among its users.
# While much is slated to change in the 2.0 Matplotlib release, the ability to customize
# default settings helps bring the package in line with your own aesthetic preferences.
# Here we’ll walk through some of Matplotlib’s runtime configuration (rc) options, and
# take a look at the newer stylesheets feature, which contains some nice sets of default
# configurations.
# 
# Plot Customization by Hand
# Throughout this chapter, we’ve seen how it is possible to tweak individual plot set‐
# tings to end up with something that looks a little bit nicer than the default. It’s possi‐
# ble to do these customizations for each individual plot. For example, here is a fairly
# drab default histogram (Figure 4-81):
#       In[1]: import matplotlib.pyplot as plt
#              plt.style.use('classic')
#              import numpy as np
# 
#                 %matplotlib inline
# 
# 
# 
# 
# 282   |   Chapter 4: Visualization with Matplotlib
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Customizing Matplotlib: Configurations and Stylesheets",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CustomizingMatplotlib(HierNode):
    def __init__(self):
        super().__init__("Customizing Matplotlib: Configurations and Stylesheets")
        self.add(Content())
        self.add(A_PlotCustomization())
        self.add(B_Changingthe())
        self.add(C_Stylesheets())

# eof
