# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Creating2D.index import Creating2D as A_Creating2D
from .B_Creating3D.index import Creating3D as B_Creating3D
from .C_IndexingSlicingof.index import IndexingSlicingof as C_IndexingSlicingof

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Higher-Dimensional Arrays
# As we’ve seen earlier, the strength of NumPy is its ability to construct and manipulate
# n-dimensional arrays with highly optimized (i.e., vectorized) operations. Previously,
# we covered the creation of 1-D arrays (or vectors) in NumPy to get a feel of how NumPy
# works.
#      This section will now consider working with 2-D and 3-D arrays. 2-D arrays are ideal
# for storing data for analysis. Structured data is usually represented in a grid of rows and
# columns. And even when data is not necessarily represented in this format, it is often
# transformed into a tabular form before doing any data analytics or machine learning.
# Each column represents a feature or attribute and each row an observation.
#      Also, other data forms like images are adequately represented using 3-D arrays. A
# colored image is composed of n × n pixel intensity values with a color depth of three for
# the red, green, and blue (RGB) color profiles.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Higher-Dimensional Arrays",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Higher-Dimensional Arrays"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HigherDimensionalArrays(HierNode):
    def __init__(self):
        super().__init__("Higher-Dimensional Arrays")
        self.add(Content())
        self.add(A_Creating2D())
        self.add(B_Creating3D())
        self.add(C_IndexingSlicingof())

# eof
