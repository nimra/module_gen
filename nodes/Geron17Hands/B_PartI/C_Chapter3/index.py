# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_MNIST.index import MNIST as A_MNIST
from .B_Traininga.index import Traininga as B_Traininga
from .C_PerformanceMeasures.index import PerformanceMeasures as C_PerformanceMeasures
from .D_MulticlassClassification.index import MulticlassClassification as D_MulticlassClassification
from .E_ErrorAnalysis.index import ErrorAnalysis as E_ErrorAnalysis
from .F_MultilabelClassification.index import MultilabelClassification as F_MultilabelClassification
from .G_MultioutputClassification.index import MultioutputClassification as G_MultioutputClassification
from .H_Exercises.index import Exercises as H_Exercises

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 3. Classification",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 3. Classification"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter3(HierNode):
    def __init__(self):
        super().__init__("Chapter 3. Classification")
        self.add(Content())
        self.add(A_MNIST())
        self.add(B_Traininga())
        self.add(C_PerformanceMeasures())
        self.add(D_MulticlassClassification())
        self.add(E_ErrorAnalysis())
        self.add(F_MultilabelClassification())
        self.add(G_MultioutputClassification())
        self.add(H_Exercises())

# eof
