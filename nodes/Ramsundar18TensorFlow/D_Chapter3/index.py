# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_MathematicalReview.index import MathematicalReview as A_MathematicalReview
from .B_Learningwith.index import Learningwith as B_Learningwith
from .C_TrainingLinear.index import TrainingLinear as C_TrainingLinear
from .D_Review.index import Review as D_Review

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 3. Linear and Logistic Regression with TensorFlow",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 3. Linear and Logistic Regression with TensorFlow"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter3(HierNode):
    def __init__(self):
        super().__init__("Chapter 3. Linear and Logistic Regression with TensorFlow")
        self.add(Content())
        self.add(A_MathematicalReview())
        self.add(B_Learningwith())
        self.add(C_TrainingLinear())
        self.add(D_Review())

# eof
