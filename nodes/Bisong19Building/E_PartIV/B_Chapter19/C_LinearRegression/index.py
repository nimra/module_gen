# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Linear Regression with Scikit-learn
# In this example, we will implement a linear regression model with Scikit-learn. The
# model will predict house prices from the Boston house-prices dataset. The dataset
# contains 506 observations and 13 features.
#     We begin by importing the following packages:
# 
# sklearn.linear_model.LinearRegression: function that implements the
# LinearRegression model.
# sklearn.datasets: function to load sample datasets integrated with scikit-­
# learn for experimental and learning purposes.
# sklearn.model_selection.train_test_split: function that partitions the
# dataset into train and test splits.
# sklearn.metrics.mean_squared_error: function to load the evaluation metric
# for checking the performance of the model.
# 
# math.sqrt: imports the square-root math function. It is used later to
# calculate the RMSE when evaluating the model.
# # import packages
# from sklearn.linear_model import LinearRegression
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# from math import sqrt
# 
# # load dataset
# data = datasets.load_boston()
# # separate features and target
# X = data.data
# y = data.target
# 
# # split in train and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True)
# 
# # create the model
# # setting normalize to true normalizes the dataset before fitting the model
# linear_reg = LinearRegression(normalize = True)
# 
# # fit the model on the training set
# linear_reg.fit(X_train, y_train)
# 'Output': LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1,
# normalize=True)
# 
# # make predictions on the test set
# predictions = linear_reg.predict(X_test)
# 
# # evaluate the model performance using the root mean square error metric
# print("Root mean squared error (RMSE): %.2f" % sqrt(mean_squared_error(y_
# test, predictions)))
# 'Output':
# Root mean squared error (RMSE): 4.33
# 
#      In the preceding code, using the train_test_split() function, the dataset is split
# into training and testing sets. The linear regression algorithm is applied to the training
# dataset to find the optimal values that parameterize the weights of the model. The model
# is evaluated by calling the .predict() function on the test set.
#      The error of the model is evaluated using the RMSE error metric (discussed in
# Chapter 14).

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Linear Regression with Scikit-learn",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Linear Regression with Scikit-learn"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LinearRegression(HierNode):
    def __init__(self):
        super().__init__("Linear Regression with Scikit-learn")
        self.add(Content())

# eof
