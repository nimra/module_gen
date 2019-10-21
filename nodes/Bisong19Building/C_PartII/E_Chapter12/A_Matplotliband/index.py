# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Matplotlib and Seaborn
# Matplotlib is a graphics package for data visualization in Python. Matplotlib has arisen
# as a key component in the Python data science stack and is well integrated with NumPy
# and Pandas. The pyplot module mirrors the MATLAB plotting commands closely.
# Hence, MATLAB users can easily transit to plotting with Python.
#     Seaborn, on the other hand, extends the Matplotlib library for creating beautiful
# graphics with Python using a more straightforward set of methods. Seaborn is more
# integrated for working with Pandas DataFrames. We will go through creating simple
# essential plots with Matplotlib and seaborn.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Matplotlib and Seaborn",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Matplotlib and Seaborn"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Matplotliband(HierNode):
    def __init__(self):
        super().__init__("Matplotlib and Seaborn")
        self.add(Content())

# eof
