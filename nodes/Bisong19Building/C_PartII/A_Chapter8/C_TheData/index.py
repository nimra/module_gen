# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The Data Science Process
# The data science process involves components for data ingestion and serving of data
# models. However, we will discuss briefly on the steps for carrying out data analytics in
# lieu of data prediction modeling.
#     These steps consist of
# 
#       1. Data summaries: The vital statistical summaries of the datasets’
#          variables or features. This includes information such as the
#          number of variables, their data types, the number of observations,
#          and the count/percentage of missing data.
# 
#       2. Data visualization: This involves employing univariate and
#          multivariate data visualization methods to get a better intuition
#          on the properties of the data variables and their relationship with
#          each other. This includes metrics such as histograms, box and
#          whisker plots, and correlation plots.
# 
#       3. Data cleaning/preprocessing: This process involves sanitizing the
#          data to make it amenable for modeling. Data rarely comes clean
#          with each row representing an observation and each column an
#          entity. In this phase of a data science effort, the tasks involved
#          may include removing duplicate entries, choosing a strategy for
#          dealing with missing data, as well as converting
#          data features into numeric data types of encoded categories.
#          This phase may also involve carrying out statistical transformation
#          on the data features to normalize and/or standardize the data
#          elements. Data features of wildly differing scales can lead to poor
#          model results as they become more difficult for the learning
#          algorithm to converge to the global minimum.
# 
#       4. Feature engineering: This practice involves systematically pruning
#          the data feature space to only select those features relevant to the
#          modeling problem as part of the model task.
#          Good feature engineering is often the difference between an
#          average and high performant model.
# 
#       5. Data modeling and evaluation: This phase involves passing the
#          data through a learning algorithm to build a predictive model.
#          This process is usually an iterative process that involves constant
#          refinement in order to build a model that better minimizes the
#          cost function on the hold-out validation set and the test set.
# 
#    In this chapter, we provided a brief overview to the concept of data science, the
# challenge of big data, and its goal to unlock value from data. The next chapter will
# provide an introduction to programming with Python.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Data Science Process",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# The Data Science Process"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheData(HierNode):
    def __init__(self):
        super().__init__("The Data Science Process")
        self.add(Content())

# eof
