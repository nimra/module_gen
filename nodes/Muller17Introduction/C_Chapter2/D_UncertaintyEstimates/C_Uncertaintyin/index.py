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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
# Figure 2-56. Decision boundary (left) and predicted probabilities for the gradient boost‐
# ing model shown in Figure 2-55
# 
# The boundaries in this plot are much more well-defined, and the small areas of
# uncertainty are clearly visible.
# The scikit-learn website has a great comparison of many models and what their
# uncertainty estimates look like. We’ve reproduced this in Figure 2-57, and we encour‐
# age you to go though the example there.
# 
# 
# 
# 
# Figure 2-57. Comparison of several classifiers in scikit-learn on synthetic datasets (image
# courtesy http://scikit-learn.org)
# 
# Uncertainty in Multiclass Classification
# So far, we’ve only talked about uncertainty estimates in binary classification. But the
# decision_function and predict_proba methods also work in the multiclass setting.
# Let’s apply them on the Iris dataset, which is a three-class classification dataset:
# 
# 
# 124   |   Chapter 2: Supervised Learning
# 
# In[115]:
#     from sklearn.datasets import load_iris
# 
#     iris = load_iris()
#     X_train, X_test, y_train, y_test = train_test_split(
#         iris.data, iris.target, random_state=42)
# 
#     gbrt = GradientBoostingClassifier(learning_rate=0.01, random_state=0)
#     gbrt.fit(X_train, y_train)
# 
# In[116]:
#     print("Decision function shape: {}".format(gbrt.decision_function(X_test).shape))
#     # plot the first few entries of the decision function
#     print("Decision function:\n{}".format(gbrt.decision_function(X_test)[:6, :]))
# 
# Out[116]:
#     Decision   function shape: (38, 3)
#     Decision   function:
#     [[-0.529    1.466 -0.504]
#      [ 1.512   -0.496 -0.503]
#      [-0.524   -0.468 1.52 ]
#      [-0.529    1.466 -0.504]
#      [-0.531    1.282 0.215]
#      [ 1.512   -0.496 -0.503]]
# 
# In the multiclass case, the decision_function has the shape (n_samples,
# n_classes) and each column provides a “certainty score” for each class, where a large
# score means that a class is more likely and a small score means the class is less likely.
# You can recover the predictions from these scores by finding the maximum entry for
# each data point:
# In[117]:
#     print("Argmax of decision function:\n{}".format(
#           np.argmax(gbrt.decision_function(X_test), axis=1)))
#     print("Predictions:\n{}".format(gbrt.predict(X_test)))
# 
# Out[117]:
#     Argmax of decision function:
#     [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1 0]
#     Predictions:
#     [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1 0]
# 
# The output of predict_proba has the same shape, (n_samples, n_classes). Again,
# the probabilities for the possible classes for each data point sum to 1:
# 
# 
# 
# 
#                                                      Uncertainty Estimates from Classifiers |   125
# 
# In[118]:
#       # show the first few entries of predict_proba
#       print("Predicted probabilities:\n{}".format(gbrt.predict_proba(X_test)[:6]))
#       # show that sums across rows are one
#       print("Sums: {}".format(gbrt.predict_proba(X_test)[:6].sum(axis=1)))
# 
# Out[118]:
#       Predicted probabilities:
#       [[ 0.107 0.784 0.109]
#        [ 0.789 0.106 0.105]
#        [ 0.102 0.108 0.789]
#        [ 0.107 0.784 0.109]
#        [ 0.108 0.663 0.228]
#        [ 0.789 0.106 0.105]]
#       Sums: [ 1. 1. 1. 1. 1.               1.]
# 
# We can again recover the predictions by computing the argmax of predict_proba:
# In[119]:
#       print("Argmax of predicted probabilities:\n{}".format(
#           np.argmax(gbrt.predict_proba(X_test), axis=1)))
#       print("Predictions:\n{}".format(gbrt.predict(X_test)))
# 
# Out[119]:
#       Argmax of predicted probabilities:
#       [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1 0]
#       Predictions:
#       [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1 0]
# 
# To summarize, predict_proba and decision_function always have shape (n_sam
# ples, n_classes)—apart from decision_function in the special binary case. In the
# binary case, decision_function only has one column, corresponding to the “posi‐
# tive” class classes_[1]. This is mostly for historical reasons.
# You can recover the prediction when there are n_classes many columns by comput‐
# ing the argmax across columns. Be careful, though, if your classes are strings, or you
# use integers but they are not consecutive and starting from 0. If you want to compare
# results obtained with predict to results obtained via decision_function or pre
# dict_proba, make sure to use the classes_ attribute of the classifier to get the actual
# class names:
# 
# 
# 
# 
# 126   |   Chapter 2: Supervised Learning
# 
# In[120]:
#     logreg = LogisticRegression()
# 
#     # represent each target by its class name in the iris dataset
#     named_target = iris.target_names[y_train]
#     logreg.fit(X_train, named_target)
#     print("unique classes in training data: {}".format(logreg.classes_))
#     print("predictions: {}".format(logreg.predict(X_test)[:10]))
#     argmax_dec_func = np.argmax(logreg.decision_function(X_test), axis=1)
#     print("argmax of decision function: {}".format(argmax_dec_func[:10]))
#     print("argmax combined with classes_: {}".format(
#             logreg.classes_[argmax_dec_func][:10]))
# 
# Out[120]:
#     unique classes in training data: ['setosa' 'versicolor' 'virginica']
#     predictions: ['versicolor' 'setosa' 'virginica' 'versicolor' 'versicolor'
#      'setosa' 'versicolor' 'virginica' 'versicolor' 'versicolor']
#     argmax of decision function: [1 0 2 1 1 0 1 2 1 1]
#     argmax combined with classes_: ['versicolor' 'setosa' 'virginica' 'versicolor'
#      'versicolor' 'setosa' 'versicolor' 'virginica' 'versicolor' 'versicolor']
# 
# 
# Summary and Outlook
# We started this chapter with a discussion of model complexity, then discussed gener‐
# alization, or learning a model that is able to perform well on new, previously unseen
# data. This led us to the concepts of underfitting, which describes a model that cannot
# capture the variations present in the training data, and overfitting, which describes a
# model that focuses too much on the training data and is not able to generalize to new
# data very well.
# We then discussed a wide array of machine learning models for classification and
# regression, what their advantages and disadvantages are, and how to control model
# complexity for each of them. We saw that for many of the algorithms, setting the right
# parameters is important for good performance. Some of the algorithms are also sensi‐
# tive to how we represent the input data, and in particular to how the features are
# scaled. Therefore, blindly applying an algorithm to a dataset without understanding
# the assumptions the model makes and the meanings of the parameter settings will
# rarely lead to an accurate model.
# This chapter contains a lot of information about the algorithms, and it is not neces‐
# sary for you to remember all of these details for the following chapters. However,
# some knowledge of the models described here—and which to use in a specific situa‐
# tion—is important for successfully applying machine learning in practice. Here is a
# quick summary of when to use each model:
# 
# 
# 
# 
#                                                                Summary and Outlook   |   127
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Uncertainty in Multiclass Classification",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Uncertaintyin(HierNode):
    def __init__(self):
        super().__init__("Uncertainty in Multiclass Classification")
        self.add(Content(), "content")

# eof
