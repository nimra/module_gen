# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Higher-Order Linear Regression with Scikit-learn
# In this example, we will create higher-order polynomials from the dataset features in
# hope of fitting a more flexible model that may better capture the variance in the dataset.
# As seen in Chapter 18, we will use the PolynomialFeatures method to create these
# higher-order polynomial and interaction features. The following code example is similar
# to the previous code example except where it extends the feature matrix with higher-­
# order features.
# 
# # import packages
# from sklearn.linear_model import LinearRegression
# from sklearn import datasets
# from   sklearn.model_selection import train_test_split
# from   sklearn.metrics import mean_squared_error
# from   math import sqrt
# from   sklearn.preprocessing import PolynomialFeatures
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
# # split in train and test sets
# X_train, X_test, y_train, y_test = train_test_split(X_higher_order, y,
# shuffle=True)
# 
# # create the model
# # setting normalize to true normalizes the dataset before fitting the model
# linear_reg = LinearRegression(normalize = True)
# 
# # fit the model on the training set
# linear_reg.fit(X_train, y_train)
# 'Output': LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
# normalize=True)
# 
# # make predictions on the test set
# predictions = linear_reg.predict(X_test)
# 
# # evaluate the model performance using the root mean square error metric
# print("Root mean squared error (RMSE): %.2f" % sqrt(mean_squared_error(y_
# test, predictions)))
# 
# 'Output':
# Root mean squared error (RMSE): 3.01
# 
#     From the example, we can observe a slight improvement in the error score of the
# model with added higher-order features. This result is similar to what may most likely
# be observed in practice. It is rare to find datasets from real-world events where the
# features have a perfectly underlying linear structure. So adding higher-order terms
# is most likely to improve the model performance. But we must watch out to avoid
# overfitting the model.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Higher-Order Linear Regression with Scikit-learn",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Higher-Order Linear Regression with Scikit-learn"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class HigherOrderLinear(HierNode):
    def __init__(self):
        super().__init__("Higher-Order Linear Regression with Scikit-learn")
        self.add(Content())

# eof
