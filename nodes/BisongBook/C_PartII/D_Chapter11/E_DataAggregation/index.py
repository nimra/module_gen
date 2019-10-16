# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Data Aggregation (Grouping)
# We will touch briefly on a common practice in data science, and that is grouping a set
# of data attributes, either for retrieving some group statistics or applying a particular set
# of functions to the group. Grouping is commonly used for data exploration and plotting
# graphs to understand more about the dataset. Missing data are automatically excluded
# in a grouping operation.
#      Let’s see examples of how this works.
# 
# # create a data frame
# my_DF = pd.DataFrame({'Sex': ['M', 'F', 'M', 'F','M', 'F','M', 'F'],
#  'Age': np.random.randint(15,60,8),
#  'Salary': np.random.rand(8)*10000})
# my_DF
# 'Output':
#    Age       Salary Sex
# 0   54  6092.596170   M
# 1   57  3148.886141   F
# 2   37  5960.916038   M
# 3   23  6713.133849   F
# 4   34  5208.240349   M
# 5   25  2469.118934   F
# 6   50  1277.511182   M
# 7   54  3529.201109   F
# 
#    Let’s find the mean age and salary for observations in our dataset grouped by Sex.
# 
# my_DF.groupby('Sex').mean()
# 'Output':
#        Age       Salary
# Sex
# F    39.75  3965.085008
# M    43.75  4634.815935
# 
#     We can group by more than one variable. In this case for each Sex group, also group
# the age and find the mean of the other numeric variables.
# 
# my_DF.groupby([my_DF['Sex'], my_DF['Age']]).mean()
# 'Output':
#               Salary
# Sex Age
# F   23   6713.133849
#     25   2469.118934
#     54   3529.201109
#     57   3148.886141
# M   34   5208.240349
#     37   5960.916038
#     50   1277.511182
#     54   6092.596170
# 
#     Also, we can use a variable as a group key to run a group function on another
# variable or sets of variables.
# 
# my_DF['Age'].groupby(my_DF['Salary']).mean()
# 'Output':
# Salary
# 1277.511182    50
# 2469.118934    25
# 3148.886141    57
# 3529.201109    54
# 5208.240349    34
# 5960.916038    37
# 6092.596170    54
# 6713.133849    23
# Name: Age, dtype: int64

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Data Aggregation (Grouping)",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Data Aggregation (Grouping)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DataAggregation(HierNode):
    def __init__(self):
        super().__init__("Data Aggregation (Grouping)")
        self.add(Content())

# eof
