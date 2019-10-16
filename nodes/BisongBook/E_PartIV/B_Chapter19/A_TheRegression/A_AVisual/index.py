# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A Visual Representation of Linear Regression
# To provide more intuition, let us draw a 2-D plot of the first feature x1 and the target
# variable y of the dataset with all 50 records. We are using just one feature in this
# illustration because it is easier to visualize with a 2-D scatter plot (see Figure 19-2).
# 
# 
# 
# 
# Figure 19-2. Scatter plot of x1 (on the x axis) and y (on the y axis)
# 
#      The goal of the linear model is to find a line that gives the best approximation or best
# fit to the data points. When found, this line will look like something in Figure 19-3. The
# line of best fit is known as the regression line.
# 
# 
# 
# 
# Figure 19-3. Scatter plot of x1 (on the x axis) and y (on the y axis) with
# regression line

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "A Visual Representation of Linear Regression",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# A Visual Representation of Linear Regression"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AVisual(HierNode):
    def __init__(self):
        super().__init__("A Visual Representation of Linear Regression")
        self.add(Content())

# eof
