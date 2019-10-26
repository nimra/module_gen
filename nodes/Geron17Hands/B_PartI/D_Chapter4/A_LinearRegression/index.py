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

from .A_TheNormal.index import TheNormal as A_TheNormal
from .B_ComputationalComplexity.index import ComputationalComplexity as B_ComputationalComplexity

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
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
#                  Download from finelybook www.finelybook.com
# This can be written much more concisely using a vectorized form, as shown in Equa‐
# tion 4-2.
# 
#     Equation 4-2. Linear Regression model prediction (vectorized form)
#     y = hθ � = θT · �
# 
# 
#   • θ is the model’s parameter vector, containing the bias term θ0 and the feature
#     weights θ1 to θn.
#   • θT is the transpose of θ (a row vector instead of a column vector).
#   • x is the instance’s feature vector, containing x0 to xn, with x0 always equal to 1.
#   • θT · x is the dot product of θT and x.
#   • hθ is the hypothesis function, using the model parameters θ.
# 
# Okay, that’s the Linear Regression model, so now how do we train it? Well, recall that
# training a model means setting its parameters so that the model best fits the training
# set. For this purpose, we first need a measure of how well (or poorly) the model fits
# the training data. In Chapter 2 we saw that the most common performance measure
# of a regression model is the Root Mean Square Error (RMSE) (Equation 2-1). There‐
# fore, to train a Linear Regression model, you need to find the value of θ that minimi‐
# zes the RMSE. In practice, it is simpler to minimize the Mean Square Error (MSE)
# than the RMSE, and it leads to the same result (because the value that minimizes a
# function also minimizes its square root).1
# The MSE of a Linear Regression hypothesis hθ on a training set X is calculated using
# Equation 4-3.
# 
#     Equation 4-3. MSE cost function for a Linear Regression model
# 
#                        1 m T                       2
#                        mi∑
#                                 i
#     MSE �, hθ =             θ ·� −yi
#                          =1
# 
# 
# Most of these notations were presented in Chapter 2 (see “Notations” on page 38).
# The only difference is that we write hθ instead of just h in order to make it clear that
# the model is parametrized by the vector θ. To simplify notations, we will just write
# MSE(θ) instead of MSE(X, hθ).
# 
# 
# 
# 1 It is often the case that a learning algorithm will try to optimize a different function than the performance
#   measure used to evaluate the final model. This is generally because that function is easier to compute, because
#   it has useful differentiation properties that the performance measure lacks, or because we want to constrain
#   the model during training, as we will see when we discuss regularization.
# 
# 
# 
#                                                                                         Linear Regression   |     107
# 
#                         Download from finelybook www.finelybook.com
# The Normal Equation
# To find the value of θ that minimizes the cost function, there is a closed-form solution
# —in other words, a mathematical equation that gives the result directly. This is called
# the Normal Equation (Equation 4-4).2
# 
#       Equation 4-4. Normal Equation
#               T       −1     T
#       θ = � ·�             ·� ·�
# 
# 
#   • θ is the value of θ that minimizes the cost function.
#   • y is the vector of target values containing y(1) to y(m).
# 
# Let’s generate some linear-looking data to test this equation on (Figure 4-1):
#       import numpy as np
# 
#       X = 2 * np.random.rand(100, 1)
#       y = 4 + 3 * X + np.random.randn(100, 1)
# 
# 
# 
# 
# Figure 4-1. Randomly generated linear dataset
# 
# 
# 
# 
# 2 The demonstration that this returns the value of θ that minimizes the cost function is outside the scope of this
#   book.
# 
# 
# 
# 108    |   Chapter 4: Training Models
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Linear Regression",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LinearRegression(HierNode):
    def __init__(self):
        super().__init__("Linear Regression")
        self.add(Content(), "content")
        self.add(A_TheNormal())
        self.add(B_ComputationalComplexity())

# eof
