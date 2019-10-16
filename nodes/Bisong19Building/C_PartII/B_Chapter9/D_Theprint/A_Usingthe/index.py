# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Using the Formatter
# Formatters add a placeholder for inputting a data value into a string output using the
# curly brace {}. The format method from the str class is invoked to receive the value as a
# parameter. The number of parameters in the format method should match the number
# of placeholders in the string representation. Other format specifiers can be added with
# the placeholder curly brackets.
# 
# print("{} {} {}".format(a, b, c))
# 'Output': I Love You
# # re-ordering the output
# print("{2} {1} {0}".format(a, b, c))
# 'Output': You Love I

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Using the Formatter",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Using the Formatter"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Usingthe(HierNode):
    def __init__(self):
        super().__init__("Using the Formatter")
        self.add(Content())

# eof
