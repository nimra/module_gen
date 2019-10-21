# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Selecting a Row from a DataFrame
# Pandas makes use of two unique wrapper attributes for indexing rows from a
# DataFrame or a cell from a Series data structure. These attributes are the iloc and loc –
# they are also known as indexers. The iloc attribute allows you to select or slice row(s) of
# a DataFrame using the intrinsic Python index format, whereas the loc attribute uses the
# explicit indices assigned to the DataFrame. If no explicit index is found, loc returns the
# same value as iloc.
#     Remember that the data type of a DataFrame row is a Series because it is a vector or
# 1-D array.
#     Let’s select the first row from the DataFrame.
# 
# # using explicit indexing
# my_DF.loc[0]
# 'Output':
# age                   15
# state_of_origin    Lagos
# Name: 0, dtype: object
# # using implicit indexing
# my_DF.iloc[0]
# 'Output':
# age                   15
# state_of_origin    Lagos
# Name: 0, dtype: object
# # let's see the data type
# type(my_DF.loc[0])
# 'Output':  pandas.core.series.Series
# 
#      Now let’s create a DataFrame with explicit indexing and test out the iloc and loc
# methods. Pandas will return an error if iloc is used for explicit indexing or if loc is used
# for implicit Python indexing.
# 
# my_DF = pd.DataFrame({'age': [15,17,21,29,25], \
#             'state_of_origin':['Lagos', 'Cross River', 'Kano', 'Abia',
#              'Benue']},\
#             index=['a','a','b','b','c'])
# # observe the string indices
# 
# my_DF
# 'Output':
#    age state_of_origin
# a   15          Lagos
# a   17    Cross River
# b   21            Kano
# b   29            Abia
# c   25          Benue
# # select using explicit indexing
# my_DF.loc['a']
# Out[196]:
#    age state_of_origin
# a   15          Lagos
# a   17    Cross River
# # let's try to use loc for implicit indexing
# my_DF.loc[0]
# 'Output':
#     Traceback (most recent call last):
#     TypeError: cannot do label indexing on <class 'pandas.core.indexes.
#      base.Index'>
#         with these indexers [0] of <class 'int'>

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Selecting a Row from a DataFrame",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Selecting a Row from a DataFrame"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Selectinga(HierNode):
    def __init__(self):
        super().__init__("Selecting a Row from a DataFrame")
        self.add(Content())

# eof
