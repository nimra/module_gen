# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Subset Data Columns and Find Summaries
# Get the closing prices of Bitcoin stocks for the month of January.
# 
# data.loc[data.slug == 'bitcoin', 'close']['2018-01']
# 'Output':
# date
# 2018-01-01    13657.2
# 2018-01-02    14982.1
# 2018-01-03    15201.0
# 2018-01-04    15599.2
# 2018-01-05    17429.5
# 2018-01-06    17527.0
# 2018-01-07    16477.6
# 2018-01-08    15170.1
# 2018-01-09    14595.4
# 2018-01-10    14973.3
# 
#    Find the mean market value of Ethereum for the month of January.
# 
# data.loc[data.slug == 'ethereum', 'market']['2018-01'].mean()
# 'Output':
# 96739480000.0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Subset Data Columns and Find Summaries",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Subset Data Columns and Find Summaries"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SubsetData(HierNode):
    def __init__(self):
        super().__init__("Subset Data Columns and Find Summaries")
        self.add(Content())

# eof
