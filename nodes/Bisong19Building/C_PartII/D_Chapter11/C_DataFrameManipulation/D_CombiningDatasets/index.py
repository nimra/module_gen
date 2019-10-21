# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Combining Datasets
# We may need to combine two or more datasets together; Pandas provides methods for
# such operations. We would consider the simple case of combining data frames with
# shared column names using the concat method.
# 
# # combine two dataframes column-wise
# pd.concat([df_A, df_B])
# 'Output':
#    First  Second  Third
# 0      2       3      9
# 1      8       7      7
# 2      8       6      4
# 0      3       6      3
# 1      2       2      1
# 2      9       3      8
# 3      2       9      2
# 
#     Observe that the concat method preserves indices by default. We can also
# concatenate or combine two dataframes by rows (or horizontally). This is done by setting
# the axis parameter to 1.
# 
# # combine two dataframes horizontally
# pd.concat([df_A, df_B], axis=1)
# 
# 'Output':
# Out[246]:
#    First  Second  Third  First  Second  Third
# 0    2.0     3.0    9.0     3        6     3
# 1    8.0     7.0    7.0     2        2     1
# 2    8.0     6.0    4.0     9        3     8
# 3    NaN     NaN    NaN     2        9     2

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Combining Datasets",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Combining Datasets"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CombiningDatasets(HierNode):
    def __init__(self):
        super().__init__("Combining Datasets")
        self.add(Content())

# eof
