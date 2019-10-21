# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Selecting a Column from a DataFrame
# Remember that the data type of a DataFrame column is a Series because it is a vector or
# 1-D array.
# 
# my_DF['age']
# 'Output':
# 0    15
# 1    17
# 2    21
# 3    29
# 4    25
# Name: age, dtype: int64
# # check data type
# type(my_DF['age'])
# 'Output':  pandas.core.series.Series
# 
#    To select multiple columns, enclose the column names as strings with the double
# square brackets [[ ]]. The following code is an example:
# 
# my_DF[['age','state_of_origin']]
# 'Output':
#    age state_of_origin
# 0   15          Lagos
# 1   17    Cross River
# 2   21            Kano
# 3   29            Abia
# 4   25          Benue

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Selecting a Column from a DataFrame",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Selecting a Column from a DataFrame"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Selectinga(HierNode):
    def __init__(self):
        super().__init__("Selecting a Column from a DataFrame")
        self.add(Content())

# eof
