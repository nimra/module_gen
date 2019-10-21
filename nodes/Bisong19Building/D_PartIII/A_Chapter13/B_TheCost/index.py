# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The Cost of Data
# Data is expensive to collect, and high-quality data is even more costly to capture due
# to the associated costs in storing and cleaning the data. Over the years, the paucity of
# data had limited the performance of machine learning methods. However, in the early
# 1990s, the Internet was born, and by the dawn of the century, it became a super highway
# for data distribution. As a result, large and diverse data became readily available for the
# research and development of machine learning products across various domains.
#     In this chapter, we covered the definition and history of machine learning and the
# importance of data. Next, we will take it further by discussing the principles of machine
# learning in Chapter 14.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Cost of Data",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# The Cost of Data"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheCost(HierNode):
    def __init__(self):
        super().__init__("The Cost of Data")
        self.add(Content())

# eof
