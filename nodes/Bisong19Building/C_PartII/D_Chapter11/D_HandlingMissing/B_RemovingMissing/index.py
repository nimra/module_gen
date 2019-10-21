# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Removing Missing Data
# Pandas has a function dropna() which is used to filter or remove missing data from
# a DataFrame. dropna() returns a new DataFrame without missing data. Let’s see
# examples of how this works.
# 
# # let's see our dataframe with missing data
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
# # let's run dropna() to remove all rows with missing values
# my_DF.dropna()
# 'Output':
#     age state_of_origin
# 0  15.0           Lagos
# 1  17.0     Cross River
# 3  29.0            Abia
# 
#     As we will observe from the preceding code block, dropna() drops all rows that
# contain a missing value. But we may not want that. We may rather, for example,
# want to drop columns with missing data or drop rows where all the observations are
# missing or better still remove consequent on the number of observations present in a
# particular row.
#     Let’s see examples of this option. First let’s expand our example dataset.
# 
# my_DF = pd.DataFrame({'Capital': ['Yola', np.nan, np.nan, 'Port-Harcourt',
#                        'Jalingo'],
#  'Population': [3178950, np.nan, 2321339, np.nan, 2294800],
#  'State': ['Adamawa', np.nan, 'Yobe', np.nan, 'Taraba'],
#  'LGAs': [22, np.nan, 17, 23, 16]})
# my_DF
# 'Output':
#          Capital  LGAs  Population    State
# 0           Yola  22.0   3178950.0  Adamawa
# 1            NaN   NaN         NaN      NaN
# 2            NaN  17.0   2321339.0     Yobe
# 3  Port-Harcourt  23.0         NaN      NaN
# 4        Jalingo  16.0   2294800.0   Taraba
# 
#       Drop columns with NaN. This option is not often used in practice.
# 
# my_DF.dropna(axis=1)
# 'Output':
# Empty DataFrame
# Columns: []
# Index: [0, 1, 2, 3, 4]
# 
#    Drop rows where all the observations are missing.
# 
# my_DF.dropna(how='all')
# 'Output':
#          Capital  LGAs  Population    State
# 0           Yola  22.0   3178950.0  Adamawa
# 2            NaN  17.0   2321339.0     Yobe
# 3  Port-Harcourt  23.0         NaN      NaN
# 4        Jalingo  16.0   2294800.0   Taraba
# 
#    Drop rows based on an observation threshold. By adjusting the thresh attribute, we
# can drop rows where the number of observations in the row is less than the thresh value.
# 
# # drop rows where number of NaN is less than 3
# my_DF.dropna(thresh=3)
# 'Output':
#    Capital  LGAs  Population    State
# 0     Yola  22.0   3178950.0  Adamawa
# 2      NaN  17.0   2321339.0     Yobe
# 4  Jalingo  16.0   2294800.0   Taraba

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Removing Missing Data",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Removing Missing Data"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RemovingMissing(HierNode):
    def __init__(self):
        super().__init__("Removing Missing Data")
        self.add(Content())

# eof
