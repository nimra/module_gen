# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The Role of Data
# Data is at the core of machine learning. It is central to the current evolution and further
# advancement of this field. Just as it is for humans, it is the same way for machines.
# Learning is not possible without data.
#     Humans learn how to perform tasks by collecting information from the
# Environment. This information is the data the brain uses to construct patterns and
# gain an understanding of the Environment. For a human being, data is captured
# through the sense organs. For example, the eyes capture visual data, the ears capture
# auditory data, the skin receives tactile data, while the nose and tongue detect olfactory
# and taste data, respectively.
#     As with humans, this same process of learning from data is replicated with
# machines. Let’s take, for example, the task of identifying spam emails. In this example,
# the computer is provided email examples as data. It then uses an algorithm to learn to
# distinguish spam emails from regular emails.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Role of Data",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# The Role of Data"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheRole(HierNode):
    def __init__(self):
        super().__init__("The Role of Data")
        self.add(Content())

# eof
