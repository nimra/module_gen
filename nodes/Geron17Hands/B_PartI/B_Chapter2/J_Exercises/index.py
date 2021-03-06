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
#                    Download from finelybook www.finelybook.com
# likely to refresh your model only every six months (at best), and your system’s perfor‐
# mance may fluctuate severely over time. If your system is an online learning system,
# you should make sure you save snapshots of its state at regular intervals so you can
# easily roll back to a previously working state.
# 
# Try It Out!
# Hopefully this chapter gave you a good idea of what a Machine Learning project
# looks like, and showed you some of the tools you can use to train a great system. As
# you can see, much of the work is in the data preparation step, building monitoring
# tools, setting up human evaluation pipelines, and automating regular model training.
# The Machine Learning algorithms are also important, of course, but it is probably
# preferable to be comfortable with the overall process and know three or four algo‐
# rithms well rather than to spend all your time exploring advanced algorithms and not
# enough time on the overall process.
# So, if you have not already done so, now is a good time to pick up a laptop, select a
# dataset that you are interested in, and try to go through the whole process from A to
# Z. A good place to start is on a competition website such as http://kaggle.com/: you
# will have a dataset to play with, a clear goal, and people to share the experience with.
# 
# Exercises
# Using this chapter’s housing dataset:
# 
#  1. Try a Support Vector Machine regressor (sklearn.svm.SVR), with various hyper‐
#     parameters such as kernel="linear" (with various values for the C hyperpara‐
#     meter) or kernel="rbf" (with various values for the C and gamma
#     hyperparameters). Don’t worry about what these hyperparameters mean for now.
#     How does the best SVR predictor perform?
#  2. Try replacing GridSearchCV with RandomizedSearchCV.
#  3. Try adding a transformer in the preparation pipeline to select only the most
#     important attributes.
#  4. Try creating a single pipeline that does the full data preparation plus the final
#     prediction.
#  5. Automatically explore some preparation options using GridSearchCV.
# 
# Solutions to these exercises are available in the online Jupyter notebooks at https://
# github.com/ageron/handson-ml.
# 
# 
# 
# 
#                                                                           Try It Out!   |   77
# 
# Download from finelybook www.finelybook.com
# 
#                      Download from finelybook www.finelybook.com
# 
# 
#                                                                                            CHAPTER 3
#                                                                             Classification
# 
# 
# 
# 
# In Chapter 1 we mentioned that the most common supervised learning tasks are
# regression (predicting values) and classification (predicting classes). In Chapter 2 we
# explored a regression task, predicting housing values, using various algorithms such
# as Linear Regression, Decision Trees, and Random Forests (which will be explained
# in further detail in later chapters). Now we will turn our attention to classification
# systems.
# 
# MNIST
# In this chapter, we will be using the MNIST dataset, which is a set of 70,000 small
# images of digits handwritten by high school students and employees of the US Cen‐
# sus Bureau. Each image is labeled with the digit it represents. This set has been stud‐
# ied so much that it is often called the “Hello World” of Machine Learning: whenever
# people come up with a new classification algorithm, they are curious to see how it
# will perform on MNIST. Whenever someone learns Machine Learning, sooner or
# later they tackle MNIST.
# Scikit-Learn provides many helper functions to download popular datasets. MNIST is
# one of them. The following code fetches the MNIST dataset:1
#     >>> from sklearn.datasets import fetch_mldata
#     >>> mnist = fetch_mldata('MNIST original')
#     >>> mnist
#     {'COL_NAMES': ['label', 'data'],
#      'DESCR': 'mldata.org dataset: mnist-original',
#      'data': array([[0, 0, 0, ..., 0, 0, 0],
#             [0, 0, 0, ..., 0, 0, 0],
# 
# 
# 
# 1 By default Scikit-Learn caches downloaded datasets in a directory called $HOME/scikit_learn_data.
# 
# 
# 
#                                                                                                       79
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Exercises",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Exercises(HierNode):
    def __init__(self):
        super().__init__("Exercises")
        self.add(Content(), "content")

# eof
