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

from .A_Meetthe.index import Meetthe as A_Meetthe
from .B_MeasuringSuccess.index import MeasuringSuccess as B_MeasuringSuccess
from .C_FirstThings.index import FirstThings as C_FirstThings
from .D_BuildingYour.index import BuildingYour as D_BuildingYour
from .E_MakingPredictions.index import MakingPredictions as E_MakingPredictions
from .F_Evaluatingthe.index import Evaluatingthe as F_Evaluatingthe

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# Out[9]:
#     Python version: 3.5.2 |Anaconda 4.1.1 (64-bit)| (default, Jul               2 2016, 17:53:06)
#     [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]
#     pandas version: 0.18.1
#     matplotlib version: 1.5.1
#     NumPy version: 1.11.1
#     SciPy version: 0.17.1
#     IPython version: 5.1.0
#     scikit-learn version: 0.18
# While it is not important to match these versions exactly, you should have a version
# of scikit-learn that is as least as recent as the one we used.
# Now that we have everything set up, let’s dive into our first application of machine
# learning.
# 
#                 This book assumes that you have version 0.18 or later of scikit-
#                 learn. The model_selection module was added in 0.18, and if you
#                 use an earlier version of scikit-learn, you will need to adjust the
#                 imports from this module.
# 
# 
# A First Application: Classifying Iris Species
# In this section, we will go through a simple machine learning application and create
# our first model. In the process, we will introduce some core concepts and terms.
# Let’s assume that a hobby botanist is interested in distinguishing the species of some
# iris flowers that she has found. She has collected some measurements associated with
# each iris: the length and width of the petals and the length and width of the sepals, all
# measured in centimeters (see Figure 1-2).
# She also has the measurements of some irises that have been previously identified by
# an expert botanist as belonging to the species setosa, versicolor, or virginica. For these
# measurements, she can be certain of which species each iris belongs to. Let’s assume
# that these are the only species our hobby botanist will encounter in the wild.
# Our goal is to build a machine learning model that can learn from the measurements
# of these irises whose species is known, so that we can predict the species for a new
# iris.
# 
# 
# 
# 
#                                                      A First Application: Classifying Iris Species   |   13
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "A First Application: Classifying Iris Species",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AFirst(HierNode):
    def __init__(self):
        super().__init__("A First Application: Classifying Iris Species")
        self.add(Content(), "content")
        self.add(A_Meetthe())
        self.add(B_MeasuringSuccess())
        self.add(C_FirstThings())
        self.add(D_BuildingYour())
        self.add(E_MakingPredictions())
        self.add(F_Evaluatingthe())

# eof
