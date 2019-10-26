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
# Figure 1-2. Parts of the iris flower
# 
# Because we have measurements for which we know the correct species of iris, this is a
# supervised learning problem. In this problem, we want to predict one of several
# options (the species of iris). This is an example of a classification problem. The possi‐
# ble outputs (different species of irises) are called classes. Every iris in the dataset
# belongs to one of three classes, so this problem is a three-class classification problem.
# The desired output for a single data point (an iris) is the species of this flower. For a
# particular data point, the species it belongs to is called its label.
# 
# Meet the Data
# The data we will use for this example is the Iris dataset, a classical dataset in machine
# learning and statistics. It is included in scikit-learn in the datasets module. We
# can load it by calling the load_iris function:
# In[10]:
#      from sklearn.datasets import load_iris
#      iris_dataset = load_iris()
# 
# The iris object that is returned by load_iris is a Bunch object, which is very similar
# to a dictionary. It contains keys and values:
# 
# 
# 14   | Chapter 1: Introduction
# 
# In[11]:
#     print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))
# 
# Out[11]:
#     Keys of iris_dataset:
#     dict_keys(['target_names', 'feature_names', 'DESCR', 'data', 'target'])
# 
# The value of the key DESCR is a short description of the dataset. We show the begin‐
# ning of the description here (feel free to look up the rest yourself):
# In[12]:
#     print(iris_dataset['DESCR'][:193] + "\n...")
# 
# Out[12]:
#     Iris Plants Database
#     ====================
# 
#     Notes
#     ----
#     Data Set Characteristics:
#          :Number of Instances: 150 (50 in each of three classes)
#          :Number of Attributes: 4 numeric, predictive att
#     ...
#     ----
# 
# The value of the key target_names is an array of strings, containing the species of
# flower that we want to predict:
# In[13]:
#     print("Target names: {}".format(iris_dataset['target_names']))
# 
# Out[13]:
#     Target names: ['setosa' 'versicolor' 'virginica']
# 
# The value of feature_names is a list of strings, giving the description of each feature:
# In[14]:
#     print("Feature names: \n{}".format(iris_dataset['feature_names']))
# 
# Out[14]:
#     Feature names:
#     ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
#      'petal width (cm)']
# 
# The data itself is contained in the target and data fields. data contains the numeric
# measurements of sepal length, sepal width, petal length, and petal width in a NumPy
# array:
# 
# 
#                                                     A First Application: Classifying Iris Species   |   15
# 
# In[15]:
#      print("Type of data: {}".format(type(iris_dataset['data'])))
# 
# Out[15]:
#      Type of data: <class 'numpy.ndarray'>
# 
# The rows in the data array correspond to flowers, while the columns represent the
# four measurements that were taken for each flower:
# In[16]:
#      print("Shape of data: {}".format(iris_dataset['data'].shape))
# 
# Out[16]:
#      Shape of data: (150, 4)
# We see that the array contains measurements for 150 different flowers. Remember
# that the individual items are called samples in machine learning, and their properties
# are called features. The shape of the data array is the number of samples multiplied by
# the number of features. This is a convention in scikit-learn, and your data will
# always be assumed to be in this shape. Here are the feature values for the first five
# samples:
# In[17]:
#      print("First five columns of data:\n{}".format(iris_dataset['data'][:5]))
# 
# Out[17]:
#      First five columns of data:
#      [[ 5.1 3.5 1.4 0.2]
#       [ 4.9 3.    1.4 0.2]
#       [ 4.7 3.2 1.3 0.2]
#       [ 4.6 3.1 1.5 0.2]
#       [ 5.   3.6 1.4 0.2]]
# From this data, we can see that all of the first five flowers have a petal width of 0.2 cm
# and that the first flower has the longest sepal, at 5.1 cm.
# The target array contains the species of each of the flowers that were measured, also
# as a NumPy array:
# In[18]:
#      print("Type of target: {}".format(type(iris_dataset['target'])))
# 
# Out[18]:
#      Type of target: <class 'numpy.ndarray'>
# 
# target is a one-dimensional array, with one entry per flower:
# 
# 
# 
# 16   |   Chapter 1: Introduction
# 
# In[19]:
#     print("Shape of target: {}".format(iris_dataset['target'].shape))
# 
# Out[19]:
#     Shape of target: (150,)
# The species are encoded as integers from 0 to 2:
# In[20]:
#     print("Target:\n{}".format(iris_dataset['target']))
# 
# Out[20]:
#     Target:
#     [0 0 0 0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
#      0 0 0 0   0   0   0   0   0   0   0   0   0   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1
#      1 1 1 1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   2   2   2   2   2   2   2   2   2   2   2
#      2 2 2 2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2
#      2 2]
# 
# The meanings of the numbers are given by the iris['target_names'] array:
# 0 means setosa, 1 means versicolor, and 2 means virginica.
# 
# Measuring Success: Training and Testing Data
# We want to build a machine learning model from this data that can predict the spe‐
# cies of iris for a new set of measurements. But before we can apply our model to new
# measurements, we need to know whether it actually works—that is, whether we
# should trust its predictions.
# Unfortunately, we cannot use the data we used to build the model to evaluate it. This
# is because our model can always simply remember the whole training set, and will
# therefore always predict the correct label for any point in the training set. This
# “remembering” does not indicate to us whether our model will generalize well (in
# other words, whether it will also perform well on new data).
# To assess the model’s performance, we show it new data (data that it hasn’t seen
# before) for which we have labels. This is usually done by splitting the labeled data we
# have collected (here, our 150 flower measurements) into two parts. One part of the
# data is used to build our machine learning model, and is called the training data or
# training set. The rest of the data will be used to assess how well the model works; this
# is called the test data, test set, or hold-out set.
# scikit-learn contains a function that shuffles the dataset and splits it for you: the
# train_test_split function. This function extracts 75% of the rows in the data as the
# training set, together with the corresponding labels for this data. The remaining 25%
# of the data, together with the remaining labels, is declared as the test set. Deciding
# 
# 
#                                                                                        A First Application: Classifying Iris Species               |   17
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Meet the Data",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Meetthe(HierNode):
    def __init__(self):
        super().__init__("Meet the Data")
        self.add(Content(), "content")

# eof
