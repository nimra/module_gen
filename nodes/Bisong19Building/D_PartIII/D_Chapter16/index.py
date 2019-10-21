# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_TheLearning.index import TheLearning as A_TheLearning
from .B_Classesof.index import Classesof as B_Classesof
from .C_OptimizingGradient.index import OptimizingGradient as C_OptimizingGradient

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 16
# 
# 
# 
# Optimization for Machine
# Learning: Gradient
# Descent
# Gradient descent is an optimization algorithm that is used to minimize the cost function
# of a machine learning algorithm. Gradient descent is called an iterative optimization
# algorithm because, in a stepwise looping fashion, it tries to find an approximate solution
# by basing the next step off its present step until a terminating condition is reached that
# ends the loop.
#     Take the following convex function in Figure 16-1 as a visual of gradient descent
# finding the minimum point of a function space.
# 
# 
# 
# 
# Figure 16-1. Contour figure – gradient descent
# 
#     The image in Figure 16-1 is an example of a function space. This type of function
# is known as a convex or a bowl-shaped function. The role of gradient descent in
# the function space is to find the set of values for the parameters of the function that
# minimizes the cost of the function and brings it to the global minimum. The global
# minimum is the lowest point of the function space.
#     For example, the mean squared error cost function for linear regression is nicely
# convex, so gradient descent is almost guaranteed to find the global minimum. However,
# this is not always the case for other types of non-convex function spaces. Remember,
# gradient descent is a global optimizer for minimizing any function space.
#     Some functions may have more than one minimum region; these regions are called
# local minima. The lowest region of the function space is called the global minimum.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 16: Optimization for Machine Learning: Gradient Descent",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 16: Optimization for Machine Learning: Gradient Descent"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter16(HierNode):
    def __init__(self):
        super().__init__("Chapter 16: Optimization for Machine Learning: Gradient Descent")
        self.add(Content())
        self.add(A_TheLearning())
        self.add(B_Classesof())
        self.add(C_OptimizingGradient())

# eof
