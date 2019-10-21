# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Importing a Dataset with a DateTime Column
# When importing a dataset that has a column containing datetime entries, Pandas has an
# attribute in the read_csv method called parse_dates that converts the datetime column
# from strings into Pandas date datatype. The attribute index_col uses the column of
# datetimes as an index to the DataFrame.
#      The method head() prints out the first five rows of the DataFrame, while the method
# tail() prints out the last five rows of the DataFrame. This function is very useful for taking
# a peek at a large DataFrame without having to bear the computational cost of printing it
# out entirely.
# 
# # load the data
# data = pd.read_csv('crypto-markets.csv', parse_dates=['date'], index_
#         col='date')
# data.head()
# 'Output':
#   slug date  symbol name  ranknow     open    high     low   close   
# volume   market    close_ratio  spread
# 2013-04-28  bitcoin BTC Bitcoin 1   135.30  135.98  132.10  134.21  
#      0   1500520000     0.5438    3.88
# 2013-04-29  bitcoin BTC Bitcoin 1   134.44  147.49  134.00  144.54  
#      0   1491160000     0.7813   13.49
# 2013-04-30  bitcoin BTC Bitcoin 1   144.00  146.93  134.05  139.00  
#      0   1597780000     0.3843   12.88
# 2013-05-01  bitcoin BTC Bitcoin 1   139.00  139.89  107.72  116.99  
#      0   1542820000     0.2882   32.17
# 2013-05-02  bitcoin BTC Bitcoin 1   116.38  125.60  92.28   105.21  
#      0   1292190000     0.3881   33.32
# 
#     Let’s examine the index of the imported data. Notice that they are the datetime
# entries.
# 
# # get the row indices
# data.index
# 'Output':
# DatetimeIndex(['2013-04-28', '2013-04-29', '2013-04-30', '2013-05-01',
#                '2013-05-02', '2013-05-03', '2013-05-04', '2013-05-05',
#                '2013-05-06', '2013-05-07',
#                ...
#                '2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
#                '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08',
#                '2018-01-09', '2018-01-10'],
#               dtype='datetime64[ns]', name='date', length=659373,
#                freq=None)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Importing a Dataset with a DateTime Column",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Importing a Dataset with a DateTime Column"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Importinga(HierNode):
    def __init__(self):
        super().__init__("Importing a Dataset with a DateTime Column")
        self.add(Content())

# eof
