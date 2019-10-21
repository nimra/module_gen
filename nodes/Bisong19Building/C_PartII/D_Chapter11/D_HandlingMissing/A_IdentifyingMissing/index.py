# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Identifying Missing Data
# In this section, we’ll use the isnull() method to check if missing cells exist in a
# DataFrame.
# 
# # let's create a data frame with missing data
# my_DF = pd.DataFrame({'age': [15,17,np.nan,29,25], \
#             'state_of_origin':['Lagos', 'Cross River', 'Kano',
#              'Abia', np.nan]})
# my_DF
# 'Output':
#     age state_of_origin
# 0  15.0           Lagos
# 1  17.0     Cross River
# 2   NaN            Kano
# 3  29.0            Abia
# 4  25.0             NaN
# 
#    Let’s check for missing data in this data frame. The isnull() method will return True
# where there is a missing data, whereas the notnull() function returns False.
# 
# my_DF.isnull()
# 'Output':
#      age  state_of_origin
# 0  False            False
# 1  False            False
# 2   True            False
# 3  False            False
# 4  False             True
# 
#     However, if we want a single answer (i.e., either True or False) to report if there is a
# missing data in the data frame, we will first convert the DataFrame to a NumPy array and
# use the function any().
#     The any function returns True when at least one of the elements in the dataset is
# True. In this case, isnull() returns a DataFrame of booleans where True designates a cell
# with a missing value.
#     Let’s see how that works.
# 
# my_DF.isnull().values.any()
# 'Output':  True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Identifying Missing Data",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Identifying Missing Data"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IdentifyingMissing(HierNode):
    def __init__(self):
        super().__init__("Identifying Missing Data")
        self.add(Content())

# eof
