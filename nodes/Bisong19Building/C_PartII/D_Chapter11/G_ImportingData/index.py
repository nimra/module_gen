# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Importing Data
# Again, getting data into the programming environment for analysis is a fundamental and
# first step for any data analytics or machine learning task. In practice, data usually comes
# in a comma-separated value, csv, format.
# 
# my_DF = pd.read_csv('link_to_file/csv_file', sep=',', header = None)
# 
#       To export a DataFrame back to csv
# 
# my_DF.to_csv('file_name.csv')
# 
#    For the next example, the dataset ‘states.csv’ is found in the chapter folder of the
# code repository of this book.
# 
# my_DF = pd.read_csv('states.csv', sep=',', header = 0)
# 
# # read the top 5 rows
# my_DF.head()
# 
# # save DataFrame to csv
# my_DF.to_csv('save_states.csv')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Importing Data",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Importing Data"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ImportingData(HierNode):
    def __init__(self):
        super().__init__("Importing Data")
        self.add(Content())

# eof
