# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Functionsand.index import Functionsand as A_Functionsand
from .B_LossFunctions.index import LossFunctions as B_LossFunctions
from .C_GradientDescent.index import GradientDescent as C_GradientDescent
from .D_AutomaticDifferentiation.index import AutomaticDifferentiation as D_AutomaticDifferentiation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                                        CHAPTER 3
#                           Linear and Logistic Regression
#                                        with TensorFlow
# 
# 
# 
# 
# This chapter will show you how to build simple, but nontrivial, examples of learning
# systems in TensorFlow. The first part of this chapter reviews the mathematical foun‐
# dations for building learning systems and in particular will cover functions, continu‐
# ity, and differentiability. We introduce the idea of loss functions, then discuss how
# machine learning boils down to the ability to find the minimal points of complicated
# loss functions. We then cover the notion of gradient descent, and explain how it can
# be used to minimize loss functions. We end the first section by briefly discussing the
# algorithmic idea of automatic differentiation. The second section focuses on intro‐
# ducing the TensorFlow concepts underpinned by these mathematical ideas. These
# concepts include placeholders, scopes, optimizers, and TensorBoard, and enable the
# practical construction and analysis of learning systems. The final section provides
# case studies of how to train linear and logistic regression models in TensorFlow.
# This chapter is long and introduces many new ideas. It’s OK if you don’t grasp all the
# subtleties of these ideas in a first reading. We recommend moving forward and com‐
# ing back to refer to the concepts here as needed later. We will repeatedly use these
# fundamentals in the remainder of the book in order to let these ideas sink in
# gradually.
# 
# Mathematical Review
# This first section reviews the mathematical tools needed to conceptually understand
# machine learning. We attempt to minimize the number of Greek symbols required,
# and focus instead on building conceptual understanding rather than technical
# manipulations.
# 
# 
# 
#                                                                                     43
# 
# Functions and Differentiability
# This section will provide you with a brief overview of the concepts of functions and
# differentiability. A function f is a rule that takes an input to an output. There are func‐
# tions in all computer programming languages, and the mathematical definition of a
# function isn’t really much different. However, mathematical functions commonly
# used in physics and engineering have other important properties such as continuity
# and differentiability. A continuous function, loosely speaking, is one that can be
# drawn without lifting your pencil from the paper, as shown in Figure 3-1. (This is of
# course not the technical definition, but it captures the spirit of the continuity
# condition.)
# 
# 
# 
# 
# Figure 3-1. Some continuous functions.
# 
# Differentiability is a type of smoothness condition on functions. It says no sharp cor‐
# ners or turns are allowed in the function (Figure 3-2).
# 
# 
# 
# 
# Figure 3-2. A differentiable function.
# 
# 
# 
# 
# 44   | Chapter 3: Linear and Logistic Regression with TensorFlow
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Mathematical Review",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(mbk("# Mathematical Review"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MathematicalReview(HierNode):
    def __init__(self):
        super().__init__("Mathematical Review")
        self.add(Content())
        self.add(A_Functionsand())
        self.add(B_LossFunctions())
        self.add(C_GradientDescent())
        self.add(D_AutomaticDifferentiation())

# eof
