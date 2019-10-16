# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Correlation
# Correlation shows how much relationship exists between two variables. Parametric
# machine learning methods such as logistic and linear regression can take a performance
# hit when variables are highly correlated. The correlation values range from –1 to 1, with
# 0 indicating no correlation at all. –1 signifies that the variables are strongly negatively
# correlated, while 1 shows that the variables are strongly positively correlated. In practice,
# it is safe to eliminate variables that have a correlation value greater than –0.7 or 0.7. A
# common correlation estimate in use is the Pearson’s correlation coefficient.
# 
# my_DF.corr(method='pearson')
# 'Output':
#            First    Second     Third    Fourth
# First   1.000000  0.587645 -0.014100 -0.317333
# Second  0.587645  1.000000 -0.768495 -0.345265
# Third  -0.014100 -0.768495  1.000000  0.334169
# Fourth -0.317333 -0.345265  0.334169  1.000000

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Correlation",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Correlation"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Correlation(HierNode):
    def __init__(self):
        super().__init__("Correlation")
        self.add(Content())

# eof
