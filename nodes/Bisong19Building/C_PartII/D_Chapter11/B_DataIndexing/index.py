# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Selectinga.index import Selectinga as A_Selectinga
from .B_Selectinga.index import Selectinga as B_Selectinga
from .C_SelectingMultiple.index import SelectingMultiple as C_SelectingMultiple
from .D_SliceCells.index import SliceCells as D_SliceCells

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Data Indexing (Selection/Subsets)
# Similar to NumPy, Pandas objects can index or subset the dataset to retrieve a specific
# sub-record of the larger dataset. Note that data indexing returns a new DataFrame or
# Series if a 2-D or 1-D array is retrieved. They do not, however, alter the original dataset.
# Let’s go through some examples of indexing a Pandas DataFrame.
#     First let’s create a dataframe. Observe the default integer indices assigned.
# 
# # create the dataframe
# my_DF = pd.DataFrame({'age': [15,17,21,29,25], \
#             'state_of_origin':['Lagos', 'Cross River', 'Kano', 'Abia',
#              'Benue']})
# 
# my_DF
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
            "Data Indexing (Selection/Subsets)",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Data Indexing (Selection/Subsets)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataIndexing(HierNode):
    def __init__(self):
        super().__init__("Data Indexing (Selection/Subsets)")
        self.add(Content())
        self.add(A_Selectinga())
        self.add(B_Selectinga())
        self.add(C_SelectingMultiple())
        self.add(D_SliceCells())

# eof
