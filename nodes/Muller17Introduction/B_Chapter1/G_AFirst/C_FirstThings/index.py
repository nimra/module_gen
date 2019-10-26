# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.HierBlock import HierBlock as hbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.ListBlock import ListBlock as lbk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# In[23]:
#     print("X_test shape: {}".format(X_test.shape))
#     print("y_test shape: {}".format(y_test.shape))
# 
# Out[23]:
#     X_test shape: (38, 4)
#     y_test shape: (38,)
# 
# 
# First Things First: Look at Your Data
# Before building a machine learning model it is often a good idea to inspect the data,
# to see if the task is easily solvable without machine learning, or if the desired infor‐
# mation might not be contained in the data.
# Additionally, inspecting your data is a good way to find abnormalities and peculiari‐
# ties. Maybe some of your irises were measured using inches and not centimeters, for
# example. In the real world, inconsistencies in the data and unexpected measurements
# are very common.
# One of the best ways to inspect data is to visualize it. One way to do this is by using a
# scatter plot. A scatter plot of the data puts one feature along the x-axis and another
# along the y-axis, and draws a dot for each data point. Unfortunately, computer
# screens have only two dimensions, which allows us to plot only two (or maybe three)
# features at a time. It is difficult to plot datasets with more than three features this way.
# One way around this problem is to do a pair plot, which looks at all possible pairs of
# features. If you have a small number of features, such as the four we have here, this is
# quite reasonable. You should keep in mind, however, that a pair plot does not show
# the interaction of all of features at once, so some interesting aspects of the data may
# not be revealed when visualizing it this way.
# Figure 1-3 is a pair plot of the features in the training set. The data points are colored
# according to the species the iris belongs to. To create the plot, we first convert the
# NumPy array into a pandas DataFrame. pandas has a function to create pair plots
# called scatter_matrix. The diagonal of this matrix is filled with histograms of each
# feature:
# In[24]:
#     # create dataframe from data in X_train
#     # label the columns using the strings in iris_dataset.feature_names
#     iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
#     # create a scatter matrix from the dataframe, color by y_train
#     grr = pd.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
#                             hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
# 
# 
# 
# 
#                                                      A First Application: Classifying Iris Species   |   19
# 
# Figure 1-3. Pair plot of the Iris dataset, colored by class label
# 
# From the plots, we can see that the three classes seem to be relatively well separated
# using the sepal and petal measurements. This means that a machine learning model
# will likely be able to learn to separate them.
# 
# Building Your First Model: k-Nearest Neighbors
# Now we can start building the actual machine learning model. There are many classi‐
# fication algorithms in scikit-learn that we could use. Here we will use a k-nearest
# neighbors classifier, which is easy to understand. Building this model only consists of
# storing the training set. To make a prediction for a new data point, the algorithm
# finds the point in the training set that is closest to the new point. Then it assigns the
# label of this training point to the new data point.
# 
# 
# 20   |   Chapter 1: Introduction
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "First Things First: Look at Your Data",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FirstThings(HierNode):
    def __init__(self):
        super().__init__("First Things First: Look at Your Data")
        self.add(Content(), "content")

# eof
