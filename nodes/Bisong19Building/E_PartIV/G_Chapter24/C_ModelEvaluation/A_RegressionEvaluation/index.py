# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Regression Evaluation Metrics
# The following code is an example of regression evaluation metrics implemented
# stand-­alone.
# 
# # import packages
# from sklearn.linear_model import LinearRegression
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import mean_absolute_error
# from sklearn.metrics import r2_score
# 
# # load dataset
# data = datasets.load_boston()
# 
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
# # evaluate the model performance using mean square error metric
# print("Mean squared error: %.2f" % mean_squared_error(y_test, predictions))
# 'Output':
# Mean squared error: 14.46
# 
# # evaluate the model performance using mean absolute error metric
# print("Mean absolute error: %.2f" % mean_absolute_error(y_test,
# predictions))
# 'Output':
# Mean absolute error: 3.63
# 
# # evaluate the model performance using r-squared error metric
# print("R-squared score: %.2f" % r2_score(y_test, predictions))
# 'Output':
# R-squared score: 0.69
# 
#     The following code is an example of regression evaluation metrics implemented with
# cross-validation. The MSE and MAE metrics for cross-validation are implemented with
# the sign inverted. The simple way to interpret this is to have it in mind that the closer the
# values are to zero, the better the model.
# 
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import KFold
# from sklearn.model_selection import cross_val_score
# 
# # load dataset
# data = datasets.load_boston()
# 
# # separate features and target
# X = data.data
# y = data.target
# 
# # initialize KFold - with shuffle = True, shuffle the data before splitting
# kfold = KFold(n_splits=3, shuffle=True)
# 
# # create the model
# linear_reg = LinearRegression(normalize = True)
# 
# # fit the model using cross validation - score with Mean square error (MSE)
# mse_cv_result = cross_val_score(linear_reg, X, y, cv=kfold, scoring="neg_
# mean_squared_error")
# # print mse cross validation output
# print("Negative Mean squared error: %.3f%% (%.3f%%)" % (mse_cv_result.
# mean(), mse_cv_result.std()))
# 'Output':
# Negtive Mean squared error: -24.275% (4.093%)
# 
# # fit the model using cross validation - score with Mean absolute error (MAE)
# mae_cv_result = cross_val_score(linear_reg, X, y, cv=kfold, scoring="neg_
# mean_absolute_error")
# # print mse cross validation output
# print("Negtive Mean absolute error: %.3f%% (%.3f%%)" % (mae_cv_result.
# mean(), mae_cv_result.std()))
# 'Output':
# Negtive Mean absolute error: -3.442% (4.093%)
# 
# # fit the model using cross validation - score with R-squared
# r2_cv_result = cross_val_score(linear_reg, X, y, cv=kfold, scoring="r2")
# # print mse cross validation output
# 
# print("R-squared score: %.3f%% (%.3f%%)" % (r2_cv_result.mean(), r2_cv_
# result.std()))
# 'Output':
# R-squared score: 0.707% (0.030%)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Regression Evaluation Metrics",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Regression Evaluation Metrics"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RegressionEvaluation(HierNode):
    def __init__(self):
        super().__init__("Regression Evaluation Metrics")
        self.add(Content())

# eof
