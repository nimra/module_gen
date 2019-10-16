# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Logistic Regression with Regularization
# This code block here is also similar to the example in Chapter 20 on logistic regression.
# The model will predict the three species of flowers from the Iris dataset. The addition to
# this code segment is the inclusion of a regularization term to the logistic model using the
# ‘RidgeClassifier’ package.
# 
# # import packages
# from sklearn.linear_model import RidgeClassifier
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# 
# # load dataset
# data = datasets.load_iris()
# 
# # separate features and target
# X = data.data
# y = data.target
# 
# # split in train and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True)
# 
# # create the logistic regression model
# logistic_reg = RidgeClassifier()
# 
# # fit the model on the training set
# logistic_reg.fit(X_train, y_train)
# 
# # make predictions on the test set
# predictions = logistic_reg.predict(X_test)
# 
# # evaluate the model performance using accuracy metric
# print("Accuracy: %.2f" % accuracy_score(y_test, predictions))
# 
# 'Output':
# Accuracy: 0.76
# 
#     In the preceding code block, logistic regression with regularization is implemented
# by the method ‘RidgeClassifier()’. The reduced accuracy observed in this example when
# regularization is applied to logistic regression is because the algorithm is restricting
# the values of the model parameters to prevent high variance on a dataset that is fairly
# simplistic and already has high accuracy on test samples without regularization.
#     This chapter discusses the role of regularization in linear models like linear and
# logistic regression. Other forms of regularization exist for other model types such as
# early stopping for neural networks (to be discussed later in Chapter 34). Regularization
# is an important technique when designing machine learning models. The next chapter
# will discuss and implement another important machine learning algorithm known as
# support vector machines.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Logistic Regression with Regularization",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Logistic Regression with Regularization"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LogisticRegression(HierNode):
    def __init__(self):
        super().__init__("Logistic Regression with Regularization")
        self.add(Content())

# eof
