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

from .A_GeneralMatplotlib.index import GeneralMatplotlib as A_GeneralMatplotlib
from .B_TwoInterfaces.index import TwoInterfaces as B_TwoInterfaces
from .C_SimpleLine.index import SimpleLine as C_SimpleLine
from .D_SimpleScatter.index import SimpleScatter as D_SimpleScatter
from .E_VisualizingErrors.index import VisualizingErrors as E_VisualizingErrors
from .F_Densityand.index import Densityand as F_Densityand
from .G_HistogramsBinnings.index import HistogramsBinnings as G_HistogramsBinnings
from .H_CustomizingPlot.index import CustomizingPlot as H_CustomizingPlot
from .I_CustomizingColorbars.index import CustomizingColorbars as I_CustomizingColorbars
from .J_MultipleSubplots.index import MultipleSubplots as J_MultipleSubplots
from .K_Textand.index import Textand as K_Textand
from .L_CustomizingTicks.index import CustomizingTicks as L_CustomizingTicks
from .M_CustomizingMatplotlib.index import CustomizingMatplotlib as M_CustomizingMatplotlib
from .N_ThreeDimensionalPlotting.index import ThreeDimensionalPlotting as N_ThreeDimensionalPlotting
from .O_GeographicData.index import GeographicData as O_GeographicData
from .P_Visualizationwith.index import Visualizationwith as P_Visualizationwith
from .Q_FurtherResources.index import FurtherResources as Q_FurtherResources

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                                                                         CHAPTER 4
#                             Visualization with Matplotlib
# 
# 
# 
# 
# We’ll now take an in-depth look at the Matplotlib tool for visualization in Python.
# Matplotlib is a multiplatform data visualization library built on NumPy arrays, and
# designed to work with the broader SciPy stack. It was conceived by John Hunter in
# 2002, originally as a patch to IPython for enabling interactive MATLAB-style plotting
# via gnuplot from the IPython command line. IPython’s creator, Fernando Perez, was
# at the time scrambling to finish his PhD, and let John know he wouldn’t have time to
# review the patch for several months. John took this as a cue to set out on his own, and
# the Matplotlib package was born, with version 0.1 released in 2003. It received an
# early boost when it was adopted as the plotting package of choice of the Space Tele‐
# scope Science Institute (the folks behind the Hubble Telescope), which financially
# supported Matplotlib’s development and greatly expanded its capabilities.
# One of Matplotlib’s most important features is its ability to play well with many oper‐
# ating systems and graphics backends. Matplotlib supports dozens of backends and
# output types, which means you can count on it to work regardless of which operating
# system you are using or which output format you wish. This cross-platform,
# everything-to-everyone approach has been one of the great strengths of Matplotlib. It
# has led to a large userbase, which in turn has led to an active developer base and Mat‐
# plotlib’s powerful tools and ubiquity within the scientific Python world.
# In recent years, however, the interface and style of Matplotlib have begun to show
# their age. Newer tools like ggplot and ggvis in the R language, along with web visuali‐
# zation toolkits based on D3js and HTML5 canvas, often make Matplotlib feel clunky
# and old-fashioned. Still, I’m of the opinion that we cannot ignore Matplotlib’s
# strength as a well-tested, cross-platform graphics engine. Recent Matplotlib versions
# make it relatively easy to set new global plotting styles (see “Customizing Matplotlib:
# Configurations and Stylesheets” on page 282), and people have been developing new
# packages that build on its powerful internals to drive Matplotlib via cleaner, more
# 
# 
#                                                                                     217
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 4. Visualization with Matplotlib",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter4(HierNode):
    def __init__(self):
        super().__init__("Chapter 4. Visualization with Matplotlib")
        self.add(Content())
        self.add(A_GeneralMatplotlib())
        self.add(B_TwoInterfaces())
        self.add(C_SimpleLine())
        self.add(D_SimpleScatter())
        self.add(E_VisualizingErrors())
        self.add(F_Densityand())
        self.add(G_HistogramsBinnings())
        self.add(H_CustomizingPlot())
        self.add(I_CustomizingColorbars())
        self.add(J_MultipleSubplots())
        self.add(K_Textand())
        self.add(L_CustomizingTicks())
        self.add(M_CustomizingMatplotlib())
        self.add(N_ThreeDimensionalPlotting())
        self.add(O_GeographicData())
        self.add(P_Visualizationwith())
        self.add(Q_FurtherResources())

# eof
