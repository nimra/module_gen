# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Selecting Multiple Rows and Columns from a DataFrame
# Let’s use the loc method to select multiple rows and columns from a Pandas DataFrame.
# 
# # select rows with age greater than 20
# my_DF.loc[my_DF.age > 20]
# 'Output':
#    age state_of_origin
# 2   21            Kano
# 3   29            Abia
# 4   25          Benue
# # find states of origin with age greater than or equal to 25
# my_DF.loc[my_DF.age >= 25, 'state_of_origin']
# 
# 'Output':
# Out[29]:
# 3     Abia
# 4    Benue

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Selecting Multiple Rows and Columns from a DataFrame",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Selecting Multiple Rows and Columns from a DataFrame"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SelectingMultiple(HierNode):
    def __init__(self):
        super().__init__("Selecting Multiple Rows and Columns from a DataFrame")
        self.add(Content())

# eof
