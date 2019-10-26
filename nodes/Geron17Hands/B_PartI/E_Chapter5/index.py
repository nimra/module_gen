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

from .A_LinearSVM.index import LinearSVM as A_LinearSVM
from .B_NonlinearSVM.index import NonlinearSVM as B_NonlinearSVM
from .C_SVMRegression.index import SVMRegression as C_SVMRegression
from .D_Underthe.index import Underthe as D_Underthe
from .E_Exercises.index import Exercises as E_Exercises

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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 5. Support Vector Machines",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter5(HierNode):
    def __init__(self):
        super().__init__("Chapter 5. Support Vector Machines")
        self.add(Content(), "content")
        self.add(A_LinearSVM())
        self.add(B_NonlinearSVM())
        self.add(C_SVMRegression())
        self.add(D_Underthe())
        self.add(E_Exercises())

# eof
