# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Pandas Plotting Methods
# Pandas also has a robust set of plotting functions which we will also use for visualizing
# our dataset. The reader will observe how we can easily convert datasets from NumPy to
# Pandas and vice versa to take advantage of one functionality or the other. The plotting
# features of Pandas are found in the plotting module.
# 
#     There are many options and properties for working with matplotlib, seaborn,
# and pandas.plotting functions for data visualization, but as is the theme of
# this material, the goal is to keep it simple and give the reader just enough to be
# dangerous. Deep competency comes with experience and continuous usage. These
# cannot really be taught.
#     To begin, we will load Matplotlib by importing the pyplot module from the
# matplotlib package and the seaborn package.
# 
# import matplotlib.pyplot as plt
# import seaborn as sns
# 
#       We’ll also import the numpy and pandas packages to create our datasets.
# 
# import pandas as pd
# import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Pandas Plotting Methods",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Pandas Plotting Methods"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PandasPlotting(HierNode):
    def __init__(self):
        super().__init__("Pandas Plotting Methods")
        self.add(Content())

# eof
