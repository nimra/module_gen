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

from .A_Typesof.index import Typesof as A_Typesof
from .B_Challengesin.index import Challengesin as B_Challengesin
from .C_Preprocessingand.index import Preprocessingand as C_Preprocessingand
from .D_DimensionalityReduction.index import DimensionalityReduction as D_DimensionalityReduction
from .E_Clustering.index import Clustering as E_Clustering
from .F_Summaryand.index import Summaryand as F_Summaryand

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                                                                           CHAPTER 3
#    Unsupervised Learning and Preprocessing
# 
# 
# 
# 
# The second family of machine learning algorithms that we will discuss is unsuper‐
# vised learning algorithms. Unsupervised learning subsumes all kinds of machine
# learning where there is no known output, no teacher to instruct the learning algo‐
# rithm. In unsupervised learning, the learning algorithm is just shown the input data
# and asked to extract knowledge from this data.
# 
# Types of Unsupervised Learning
# We will look into two kinds of unsupervised learning in this chapter: transformations
# of the dataset and clustering.
# Unsupervised transformations of a dataset are algorithms that create a new representa‐
# tion of the data which might be easier for humans or other machine learning algo‐
# rithms to understand compared to the original representation of the data. A common
# application of unsupervised transformations is dimensionality reduction, which takes
# a high-dimensional representation of the data, consisting of many features, and finds
# a new way to represent this data that summarizes the essential characteristics with
# fewer features. A common application for dimensionality reduction is reduction to
# two dimensions for visualization purposes.
# Another application for unsupervised transformations is finding the parts or compo‐
# nents that “make up” the data. An example of this is topic extraction on collections of
# text documents. Here, the task is to find the unknown topics that are talked about in
# each document, and to learn what topics appear in each document. This can be useful
# for tracking the discussion of themes like elections, gun control, or pop stars on social
# media.
# Clustering algorithms, on the other hand, partition data into distinct groups of similar
# items. Consider the example of uploading photos to a social media site. To allow you
# 
# 
#                                                                                       131
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 3. Unsupervised Learning and Preprocessing",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter3(HierNode):
    def __init__(self):
        super().__init__("Chapter 3. Unsupervised Learning and Preprocessing")
        self.add(Content(), "content")
        self.add(A_Typesof())
        self.add(B_Challengesin())
        self.add(C_Preprocessingand())
        self.add(D_DimensionalityReduction())
        self.add(E_Clustering())
        self.add(F_Summaryand())

# eof
