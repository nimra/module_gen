# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_LinearRegression.index import LinearRegression as A_LinearRegression
from .B_LogisticRegression.index import LogisticRegression as B_LogisticRegression

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 21   Regularization for Linear Models
# 
#     However, if the value of λ approaches zero, the regularization parameter has
# negligible effects on the model, hence resulting in overfitting the model. Regularization
# is an important technique and should be used when injecting polynomial features into
# linear or logistic regression classifiers to learn non-linear relationships.
# 
# 
# 
# Applying Regularization to Models with Scikit-learn
# The technique of adding a penalty to restrain the values of the parameters of the model
# is also known as Ridge regression or Tikhonov regularization. In this section we will
# build a linear and logistic regression model with regularization.
# 
# 
# Linear Regression with Regularization
# This code block is similar to the polynomial linear regression example in Chapter 19.
# The model will predict house prices from the Boston house-prices dataset. However, this
# model includes regularization.
# 
# # import packages
# from sklearn.linear_model import Ridge
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# from math import sqrt
# from sklearn.preprocessing import PolynomialFeatures
# 
# # load dataset
# data = datasets.load_boston()
# 
# # separate features and target
# X = data.data
# y = data.target
# 
# # create polynomial features
# polynomial_features = PolynomialFeatures(2)
# X_higher_order = polynomial_features.fit_transform(X)
# 
# 
# 
# 
# 252
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Applying Regularization to Models with Scikit-learn")
        self.add(MarkdownBlock("# Applying Regularization to Models with Scikit-learn"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ApplyingRegularization(HierNode):
    def __init__(self):
        super().__init__("Applying Regularization to Models with Scikit-learn")
        self.add(Content())
        self.add(A_LinearRegression())
        self.add(B_LogisticRegression())

# eof
