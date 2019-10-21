# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Correlation.index import Correlation as A_Correlation
from .B_Skewness.index import Skewness as B_Skewness

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Statistical Summaries
# Descriptive statistics is an essential component of the data science pipeline. By
# investigating the properties of the dataset, we can gain a better understanding of the
# data and the relationship between the variables. This information is useful in making
# decisions about the type of data transformations to carry out or the types of learning
# algorithms to spot check. Let’s see some examples of simple statistical functions in
# Pandas.
#     First, we’ll create a Pandas dataframe.
# 
# my_DF = pd.DataFrame(np.random.randint(10,80,[7,4]),\
#             columns=['First','Second','Third', 'Fourth'])
# 'Output':
#    First  Second  Third  Fourth
# 0     47      32     66      52
# 1     37      66     16      22
# 2     24      16     63      36
# 3     70      47     62      12
# 4     74      61     44      18
# 5     65      73     21      37
# 6     44      47     23      13
# 
#     Use the describe function to obtain summary statistics of a dataset. Eight statistical
# measures are displayed. They are count, mean, standard deviation, minimum value,
# 25th percentile, 50th percentile or median, 75th percentile, and the maximum value.
# 
# my_DF.describe()
# 'Output':
#            First     Second      Third     Fourth
# count   7.000000   7.000000   7.000000   7.000000
# mean   51.571429  48.857143  42.142857  27.142857
# std    18.590832  19.978560  21.980511  14.904458
# min    24.000000  16.000000  16.000000  12.000000
# 25%    40.500000  39.500000  22.000000  15.500000
# 50%    47.000000  47.000000  44.000000  22.000000
# 75%    67.500000  63.500000  62.500000  36.500000
# max    74.000000  73.000000  66.000000  52.000000

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Statistical Summaries",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Statistical Summaries"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class StatisticalSummaries(HierNode):
    def __init__(self):
        super().__init__("Statistical Summaries")
        self.add(Content())
        self.add(A_Correlation())
        self.add(B_Skewness())

# eof
