# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_LinearRegression.index import LinearRegression as A_LinearRegression
from .B_GradientDescent.index import GradientDescent as B_GradientDescent
from .C_PolynomialRegression.index import PolynomialRegression as C_PolynomialRegression
from .D_LearningCurves.index import LearningCurves as D_LearningCurves
from .E_RegularizedLinear.index import RegularizedLinear as E_RegularizedLinear
from .F_LogisticRegression.index import LogisticRegression as F_LogisticRegression
from .G_Exercises.index import Exercises as G_Exercises

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                  Download from finelybook www.finelybook.com
# 
# 
#                                                                          CHAPTER 4
#                                                        Training Models
# 
# 
# 
# 
# So far we have treated Machine Learning models and their training algorithms mostly
# like black boxes. If you went through some of the exercises in the previous chapters,
# you may have been surprised by how much you can get done without knowing any‐
# thing about what’s under the hood: you optimized a regression system, you improved
# a digit image classifier, and you even built a spam classifier from scratch—all this
# without knowing how they actually work. Indeed, in many situations you don’t really
# need to know the implementation details.
# However, having a good understanding of how things work can help you quickly
# home in on the appropriate model, the right training algorithm to use, and a good set
# of hyperparameters for your task. Understanding what’s under the hood will also help
# you debug issues and perform error analysis more efficiently. Lastly, most of the top‐
# ics discussed in this chapter will be essential in understanding, building, and training
# neural networks (discussed in Part II of this book).
# In this chapter, we will start by looking at the Linear Regression model, one of the
# simplest models there is. We will discuss two very different ways to train it:
# 
#   • Using a direct “closed-form” equation that directly computes the model parame‐
#     ters that best fit the model to the training set (i.e., the model parameters that
#     minimize the cost function over the training set).
#   • Using an iterative optimization approach, called Gradient Descent (GD), that
#     gradually tweaks the model parameters to minimize the cost function over the
#     training set, eventually converging to the same set of parameters as the first
#     method. We will look at a few variants of Gradient Descent that we will use again
#     and again when we study neural networks in Part II: Batch GD, Mini-batch GD,
#     and Stochastic GD.
# 
# 
# 
#                                                                                      105
# 
#                    Download from finelybook www.finelybook.com
# Next we will look at Polynomial Regression, a more complex model that can fit non‐
# linear datasets. Since this model has more parameters than Linear Regression, it is
# more prone to overfitting the training data, so we will look at how to detect whether
# or not this is the case, using learning curves, and then we will look at several regulari‐
# zation techniques that can reduce the risk of overfitting the training set.
# Finally, we will look at two more models that are commonly used for classification
# tasks: Logistic Regression and Softmax Regression.
# 
#                       There will be quite a few math equations in this chapter, using basic
#                       notions of linear algebra and calculus. To understand these equa‐
#                       tions, you will need to know what vectors and matrices are, how to
#                       transpose them, what the dot product is, what matrix inverse is,
#                       and what partial derivatives are. If you are unfamiliar with these
#                       concepts, please go through the linear algebra and calculus intro‐
#                       ductory tutorials available as Jupyter notebooks in the online sup‐
#                       plemental material. For those who are truly allergic to
#                       mathematics, you should still go through this chapter and simply
#                       skip the equations; hopefully, the text will be sufficient to help you
#                       understand most of the concepts.
# 
# 
# Linear Regression
# In Chapter 1, we looked at a simple regression model of life satisfaction: life_satisfac‐
# tion = θ0 + θ1 × GDP_per_capita.
# This model is just a linear function of the input feature GDP_per_capita. θ0 and θ1 are
# the model’s parameters.
# More generally, a linear model makes a prediction by simply computing a weighted
# sum of the input features, plus a constant called the bias term (also called the intercept
# term), as shown in Equation 4-1.
# 
#       Equation 4-1. Linear Regression model prediction
#       y = θ0 + θ1x1 + θ2x2 + ⋯ + θnxn
# 
# 
#   • ŷ is the predicted value.
#   • n is the number of features.
#   • xi is the ith feature value.
#   • θj is the jth model parameter (including the bias term θ0 and the feature weights
#     θ1, θ2, ⋯, θn).
# 
# 
# 
# 106    |   Chapter 4: Training Models
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 4. Training Models",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Chapter 4. Training Models"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter4(HierNode):
    def __init__(self):
        super().__init__("Chapter 4. Training Models")
        self.add(Content())
        self.add(A_LinearRegression())
        self.add(B_GradientDescent())
        self.add(C_PolynomialRegression())
        self.add(D_LearningCurves())
        self.add(E_RegularizedLinear())
        self.add(F_LogisticRegression())
        self.add(G_Exercises())

# eof
