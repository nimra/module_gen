# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imputing Values into Missing Data
# Imputing values as substitutes for missing data is a standard practice in preparing data
# for machine learning. Pandas has a fillna() function for this purpose. A simple approach
# is to fill NaNs with zeros.
# 
# my_DF.fillna(0) # we can also run my_DF.replace(np.nan, 0)
# 'Output':
#          Capital  LGAs  Population    State
# 0           Yola  22.0   3178950.0  Adamawa
# 1              0   0.0         0.0       0
# 2              0  17.0   2321339.0     Yobe
# 3  Port-Harcourt  23.0         0.0        0
# 4        Jalingo  16.0   2294800.0   Taraba
# 
#       Another tactic is to fill missing values with the mean of the column value.
# 
# my_DF.fillna(my_DF.mean())
# 'Output':
#          Capital  LGAs  Population    State
# 0           Yola  22.0   3178950.0  Adamawa
# 1            NaN  19.5   2598363.0      NaN
# 2            NaN  17.0   2321339.0     Yobe
# 3  Port-Harcourt  23.0   2598363.0      NaN
# 4        Jalingo  16.0   2294800.0   Taraba

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Imputing Values into Missing Data",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Imputing Values into Missing Data"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ImputingValues(HierNode):
    def __init__(self):
        super().__init__("Imputing Values into Missing Data")
        self.add(Content())

# eof
