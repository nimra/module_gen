# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Logistic Regression with Scikit-learn
# In this example, we will implement a multi-class logistic regression model with Scikit-­
# learn. The model will predict the three species of flowers from the Iris dataset. The
# dataset contains 150 observations and 4 features. For this example, we use the accuracy
# metric and confusion matrix to access the model’s performance.
# 
# # import packages
# from sklearn.linear_model import LogisticRegression
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import multilabel_confusion_matrix
# 
# # load dataset
# data = datasets.load_iris()
# # separate features and target
# X = data.data
# y = data.target
# 
# # split in train and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True)
# 
# # create the model
# logistic_reg = LogisticRegression(solver='lbfgs', multi_class='ovr')
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
# Accuracy: 0.97
# 
# # print the confusion matrix
# multilabel_confusion_matrix(y_test, predictions)
# 
# 'Output':
# array([[[26,  0],
#         [ 0, 12]],
# 
#        [[25,  0],
#         [ 1, 12]],
# 
#        [[24,  1],
#         [ 0, 13]]])
# 
#       Take note of the following in the preceding code block:
# 
#         •   The logistic regression model is initialized by calling the method Logi
#             sticRegression(solver=‘lbfgs’, multi_class=‘ovr’). The attribute ‘multi_
#             class’ is set to ‘ovr’ to create a one-vs.-rest classifier.
# 
#         •   The confusion matrix for a multi-class learning problem uses the
#             `multilabel_confusion_matrix’ to calculate classwise confusion
#             matrices where the labels are binned in a one-vs.-rest manner. As an
#             example, the first matrix is interpreted as the difference between the
#             actual and predicted targets for class 1 against other classes.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Logistic Regression with Scikit-learn",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Logistic Regression with Scikit-learn"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LogisticRegression(HierNode):
    def __init__(self):
        super().__init__("Logistic Regression with Scikit-learn")
        self.add(Content())

# eof
