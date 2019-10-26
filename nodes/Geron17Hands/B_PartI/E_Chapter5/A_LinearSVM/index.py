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

from .A_SoftMargin.index import SoftMargin as A_SoftMargin

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                   Download from finelybook www.finelybook.com
# 
# 
#                                                                             CHAPTER 5
#                                       Support Vector Machines
# 
# 
# 
# 
# A Support Vector Machine (SVM) is a very powerful and versatile Machine Learning
# model, capable of performing linear or nonlinear classification, regression, and even
# outlier detection. It is one of the most popular models in Machine Learning, and any‐
# one interested in Machine Learning should have it in their toolbox. SVMs are partic‐
# ularly well suited for classification of complex but small- or medium-sized datasets.
# This chapter will explain the core concepts of SVMs, how to use them, and how they
# work.
# 
# Linear SVM Classification
# The fundamental idea behind SVMs is best explained with some pictures. Figure 5-1
# shows part of the iris dataset that was introduced at the end of Chapter 4. The two
# classes can clearly be separated easily with a straight line (they are linearly separable).
# The left plot shows the decision boundaries of three possible linear classifiers. The
# model whose decision boundary is represented by the dashed line is so bad that it
# does not even separate the classes properly. The other two models work perfectly on
# this training set, but their decision boundaries come so close to the instances that
# these models will probably not perform as well on new instances. In contrast, the
# solid line in the plot on the right represents the decision boundary of an SVM classi‐
# fier; this line not only separates the two classes but also stays as far away from the
# closest training instances as possible. You can think of an SVM classifier as fitting the
# widest possible street (represented by the parallel dashed lines) between the classes.
# This is called large margin classification.
# 
# 
# 
# 
#                                                                                         145
# 
#                        Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 5-1. Large margin classification
# 
# Notice that adding more training instances “off the street” will not affect the decision
# boundary at all: it is fully determined (or “supported”) by the instances located on the
# edge of the street. These instances are called the support vectors (they are circled in
# Figure 5-1).
# 
#                     SVMs are sensitive to the feature scales, as you can see in
#                     Figure 5-2: on the left plot, the vertical scale is much larger than the
#                     horizontal scale, so the widest possible street is close to horizontal.
#                     After feature scaling (e.g., using Scikit-Learn’s StandardScaler),
#                     the decision boundary looks much better (on the right plot).
# 
# 
# 
# 
# Figure 5-2. Sensitivity to feature scales
# 
# Soft Margin Classification
# If we strictly impose that all instances be off the street and on the right side, this is
# called hard margin classification. There are two main issues with hard margin classifi‐
# cation. First, it only works if the data is linearly separable, and second it is quite sensi‐
# tive to outliers. Figure 5-3 shows the iris dataset with just one additional outlier: on
# the left, it is impossible to find a hard margin, and on the right the decision boundary
# ends up very different from the one we saw in Figure 5-1 without the outlier, and it
# will probably not generalize as well.
# 
# 
# 
# 
# 146   |   Chapter 5: Support Vector Machines
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Linear SVM Classification",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LinearSVM(HierNode):
    def __init__(self):
        super().__init__("Linear SVM Classification")
        self.add(Content(), "content")
        self.add(A_SoftMargin())

# eof
