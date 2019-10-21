# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Data Alignment
# Pandas utilizes data alignment to align indices when performing some binary arithmetic
# operation on DataFrames. If two or more DataFrames in an arithmetic operation do not
# share a common index, a NaN is introduced denoting missing data. Let’s see examples
# of this.
# 
# # create a 3x3 dataframe - remember randint(low, high, size)
# df_A = pd.DataFrame(np.random.randint(1,10,[3,3]),\
#             columns=['First','Second','Third'])
# df_A
# 
# 'Output':
#    First  Second  Third
# 0      2       3      9
# 1      8       7      7
# 2      8       6      4
# # create a 4x3 dataframe
# df_B = pd.DataFrame(np.random.randint(1,10,[4,3]),\
#             columns=['First','Second','Third'])
# df_B
# 'Output':
#    First  Second  Third
# 0      3       6      3
# 1      2       2      1
# 2      9       3      8
# 3      2       9      2
# # add df_A and df_B together
# df_A + df_B
# 'Output':
#    First  Second  Third
# 0    5.0     9.0   12.0
# 1   10.0    9.0    8.0
# 2   17.0    9.0   12.0
# 3    NaN     NaN    NaN
# # divide both dataframes
# df_A / df_B
# 'Output':
#       First  Second  Third
# 0  0.666667     0.5    3.0
# 1  4.000000     3.5    7.0
# 2  0.888889     2.0    0.5
# 3       NaN     NaN    NaN
# 
#      If we do not want a NaN signifying missing values to be imputed, we can use the
# fill_value attribute to substitute with a default value. However, to take advantage of the
# fill_value attribute, we have to use the Pandas arithmetic methods: add(), sub(), mul(),
# div(), floordiv(), mod(), and pow() for addition, subtraction, multiplication, integer
# division, numeric division, remainder division, and exponentiation. Let’s see examples.
# 
# df_A.add(df_B, fill_value=10)
# 'Output':
#    First  Second  Third
# 0    5.0     9.0   12.0
# 1   10.0    9.0    8.0
# 2   17.0    9.0   12.0
# 3   12.0    19.0   12.0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Data Alignment",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Data Alignment"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataAlignment(HierNode):
    def __init__(self):
        super().__init__("Data Alignment")
        self.add(Content())

# eof
