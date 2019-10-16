# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Slice Cells by Row and Column from a DataFrame
# First let’s create a DataFrame. Remember, we use iloc when no explicit index or row
# labels are assigned.
# 
# my_DF = pd.DataFrame({'age': [15,17,21,29,25], \
#             'state_of_origin':['Lagos', 'Cross River', 'Kano', 'Abia',
#              'Benue']})
# my_DF
# 'Output':
#    age state_of_origin
# 0   15          Lagos
# 1   17    Cross River
# 2   21            Kano
# 3   29            Abia
# 4   25          Benue
# # select the third row and second column
# my_DF.iloc[2,1]
# 'Output': 'Kano'
# # slice the first 2 rows - indexed from zero, excluding the final index
# my_DF.iloc[:2,]
# 'Output':
#    age state_of_origin
# 0   15          Lagos
# 1   17    Cross River
# # slice the last three rows from the last column
# my_DF.iloc[-3:,-1]
# 'Output':
# 2     Kano
# 3     Abia
# 4    Benue
# Name: state_of_origin, dtype: object

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Slice Cells by Row and Column from a DataFrame",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Slice Cells by Row and Column from a DataFrame"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SliceCells(HierNode):
    def __init__(self):
        super().__init__("Slice Cells by Row and Column from a DataFrame")
        self.add(Content())

# eof
