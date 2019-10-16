# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Series
# The Series data structure is for storing a 1-D array (or vector) of data elements. A series
# data structure also provides labels to the data items in the form of an index. The user
# can specify this label via the index parameter in the Series function, but if the index
# parameter is left unspecified, a default label of 0 to one minus the size of the data
# elements is assigned.
# 
#       Let us consider an example of creating a Series data structure.
# 
# # create a Series object
# my_series = pd.Series([2,4,6,8], index=['e1','e2','e3','e4'])
# # print out data in Series data structure
# my_series
# 'Output':
# e1    2
# e2    4
# e3    6
# e4    8
# dtype: int64
# # check the data type of the variable
# type(my_series)
# 'Output': pandas.core.series.Series
# # return the elements of the Series data structure
# my_series.values
# 'Output': array([2, 4, 6, 8])
# # retrieve elements from Series data structure based on their assigned
# indices
# my_series['e1']
# 'Output': 2
# # return all indices of the Series data structure
# my_series.index
# 'Output': Index(['e1', 'e2', 'e3', 'e4'], dtype='object')
# 
#       Elements in a Series data structure can be assigned the same indices.
# 
# # create a Series object with elements sharing indices
# my_series = pd.Series([2,4,6,8], index=['e1','e2','e1','e2'])
# # note the same index assigned to various elements
# my_series
# 'Output':
# e1    2
# e2    4
# e1    6
# e2    8
# 
# dtype: int64
# # get elements using their index
# my_series['e1']
# 'Output':
# e1    2
# e1    6
# dtype: int64

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Series",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Series"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Series(HierNode):
    def __init__(self):
        super().__init__("Series")
        self.add(Content())

# eof
