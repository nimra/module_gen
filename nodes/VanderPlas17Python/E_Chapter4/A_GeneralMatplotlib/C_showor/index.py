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
# modern APIs—for example, Seaborn (discussed in “Visualization with Seaborn” on
# page 311), ggplot, HoloViews, Altair, and even Pandas itself can be used as wrappers
# around Matplotlib’s API. Even with wrappers like these, it is still often useful to dive
# into Matplotlib’s syntax to adjust the final plot output. For this reason, I believe that
# Matplotlib itself will remain a vital piece of the data visualization stack, even if new
# tools mean the community gradually moves away from using the Matplotlib API
# directly.
# 
# General Matplotlib Tips
# Before we dive into the details of creating visualizations with Matplotlib, there are a
# few useful things you should know about using the package.
# 
# Importing matplotlib
# Just as we use the np shorthand for NumPy and the pd shorthand for Pandas, we will
# use some standard shorthands for Matplotlib imports:
#       In[1]: import matplotlib as mpl
#              import matplotlib.pyplot as plt
# 
# The plt interface is what we will use most often, as we’ll see throughout this chapter.
# 
# Setting Styles
# We will use the plt.style directive to choose appropriate aesthetic styles for our fig‐
# ures. Here we will set the classic style, which ensures that the plots we create use the
# classic Matplotlib style:
#       In[2]: plt.style.use('classic')
# Throughout this section, we will adjust this style as needed. Note that the stylesheets
# used here are supported as of Matplotlib version 1.5; if you are using an earlier ver‐
# sion of Matplotlib, only the default style is available. For more information on style‐
# sheets, see “Customizing Matplotlib: Configurations and Stylesheets” on page 282.
# 
# show() or No show()? How to Display Your Plots
# A visualization you can’t see won’t be of much use, but just how you view your Mat‐
# plotlib plots depends on the context. The best use of Matplotlib differs depending on
# how you are using it; roughly, the three applicable contexts are using Matplotlib in a
# script, in an IPython terminal, or in an IPython notebook.
# 
# 
# 
# 
# 218   |   Chapter 4: Visualization with Matplotlib
# 
# Plotting from a script
# If you are using Matplotlib from within a script, the function plt.show() is your
# friend. plt.show() starts an event loop, looks for all currently active figure objects,
# and opens one or more interactive windows that display your figure or figures.
# So, for example, you may have a file called myplot.py containing the following:
#     # ------- file: myplot.py ------
#     import matplotlib.pyplot as plt
#     import numpy as np
# 
#     x = np.linspace(0, 10, 100)
# 
#     plt.plot(x, np.sin(x))
#     plt.plot(x, np.cos(x))
# 
#     plt.show()
# You can then run this script from the command-line prompt, which will result in a
# window opening with your figure displayed:
#     $ python myplot.py
# 
# The plt.show() command does a lot under the hood, as it must interact with your
# system’s interactive graphical backend. The details of this operation can vary greatly
# from system to system and even installation to installation, but Matplotlib does its
# best to hide all these details from you.
# One thing to be aware of: the plt.show() command should be used only once per
# Python session, and is most often seen at the very end of the script. Multiple show()
# commands can lead to unpredictable backend-dependent behavior, and should
# mostly be avoided.
# 
# Plotting from an IPython shell
# It can be very convenient to use Matplotlib interactively within an IPython shell (see
# Chapter 1). IPython is built to work well with Matplotlib if you specify Matplotlib
# mode. To enable this mode, you can use the %matplotlib magic command after start‐
# ing ipython:
#     In [1]: %matplotlib
#     Using matplotlib backend: TkAgg
# 
#     In [2]: import matplotlib.pyplot as plt
# 
# At this point, any plt plot command will cause a figure window to open, and further
# commands can be run to update the plot. Some changes (such as modifying proper‐
# ties of lines that are already drawn) will not draw automatically; to force an update,
# use plt.draw(). Using plt.show() in Matplotlib mode is not required.
# 
# 
#                                                               General Matplotlib Tips   |   219
# 
# Plotting from an IPython notebook
# The IPython notebook is a browser-based interactive data analysis tool that can com‐
# bine narrative, code, graphics, HTML elements, and much more into a single exe‐
# cutable document (see Chapter 1).
# Plotting interactively within an IPython notebook can be done with the %matplotlib
# command, and works in a similar way to the IPython shell. In the IPython notebook,
# you also have the option of embedding graphics directly in the notebook, with two
# possible options:
# 
#   • %matplotlib notebook will lead to interactive plots embedded within the
#     notebook
#   • %matplotlib inline will lead to static images of your plot embedded in the
#     notebook
# 
# For this book, we will generally opt for %matplotlib inline:
#       In[3]: %matplotlib inline
# After you run this command (it needs to be done only once per kernel/session), any
# cell within the notebook that creates a plot will embed a PNG image of the resulting
# graphic (Figure 4-1):
#       In[4]: import numpy as np
#              x = np.linspace(0, 10, 100)
# 
#                fig = plt.figure()
#                plt.plot(x, np.sin(x), '-')
#                plt.plot(x, np.cos(x), '--');
# 
# 
# 
# 
# Figure 4-1. Basic plotting example
# 
# 
# 
# 
# 220   |   Chapter 4: Visualization with Matplotlib
# 
# Saving Figures to File
# One nice feature of Matplotlib is the ability to save figures in a wide variety of for‐
# mats. You can save a figure using the savefig() command. For example, to save the
# previous figure as a PNG file, you can run this:
#     In[5]: fig.savefig('my_figure.png')
# We now have a file called my_figure.png in the current working directory:
#     In[6]: !ls -lh my_figure.png
#     -rw-r--r--   1 jakevdp   staff   16K Aug 11 10:59 my_figure.png
# 
# To confirm that it contains what we think it contains, let’s use the IPython Image
# object to display the contents of this file (Figure 4-2):
#     In[7]: from IPython.display import Image
#            Image('my_figure.png')
# 
# 
# 
# 
# Figure 4-2. PNG rendering of the basic plot
# 
# In savefig(), the file format is inferred from the extension of the given filename.
# Depending on what backends you have installed, many different file formats are
# available. You can find the list of supported file types for your system by using the
# following method of the figure canvas object:
#     In[8]: fig.canvas.get_supported_filetypes()
#     Out[8]: {'eps': 'Encapsulated Postscript',
#              'jpeg': 'Joint Photographic Experts Group',
#              'jpg': 'Joint Photographic Experts Group',
#              'pdf': 'Portable Document Format',
#              'pgf': 'PGF code for LaTeX',
#              'png': 'Portable Network Graphics',
#              'ps': 'Postscript',
#              'raw': 'Raw RGBA bitmap',
#              'rgba': 'Raw RGBA bitmap',
# 
# 
#                                                               General Matplotlib Tips   |   221
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "show() or No show()? How to Display Your Plots",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class showor(HierNode):
    def __init__(self):
        super().__init__("show() or No show()? How to Display Your Plots")
        self.add(Content())

# eof
