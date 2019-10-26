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
#                   Download from finelybook www.finelybook.com
# Wow! Above 95% accuracy (ratio of correct predictions) on all cross-validation folds?
# This looks amazing, doesn’t it? Well, before you get too excited, let’s look at a very
# dumb classifier that just classifies every single image in the “not-5” class:
#      from sklearn.base import BaseEstimator
# 
#      class Never5Classifier(BaseEstimator):
#          def fit(self, X, y=None):
#              pass
#          def predict(self, X):
#              return np.zeros((len(X), 1), dtype=bool)
# Can you guess this model’s accuracy? Let’s find out:
#      >>> never_5_clf = Never5Classifier()
#      >>> cross_val_score(never_5_clf, X_train, y_train_5, cv=3, scoring="accuracy")
#      array([ 0.909 , 0.90715, 0.9128 ])
# That’s right, it has over 90% accuracy! This is simply because only about 10% of the
# images are 5s, so if you always guess that an image is not a 5, you will be right about
# 90% of the time. Beats Nostradamus.
# This demonstrates why accuracy is generally not the preferred performance measure
# for classifiers, especially when you are dealing with skewed datasets (i.e., when some
# classes are much more frequent than others).
# 
# Confusion Matrix
# A much better way to evaluate the performance of a classifier is to look at the confu‐
# sion matrix. The general idea is to count the number of times instances of class A are
# classified as class B. For example, to know the number of times the classifier confused
# images of 5s with 3s, you would look in the 5th row and 3rd column of the confusion
# matrix.
# To compute the confusion matrix, you first need to have a set of predictions, so they
# can be compared to the actual targets. You could make predictions on the test set, but
# let’s keep it untouched for now (remember that you want to use the test set only at the
# very end of your project, once you have a classifier that you are ready to launch).
# Instead, you can use the cross_val_predict() function:
#      from sklearn.model_selection import cross_val_predict
# 
#      y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3)
# 
# Just like the cross_val_score() function, cross_val_predict() performs K-fold
# cross-validation, but instead of returning the evaluation scores, it returns the predic‐
# tions made on each test fold. This means that you get a clean prediction for each
# instance in the training set (“clean” meaning that the prediction is made by a model
# that never saw the data during training).
# 
# 
# 84   |   Chapter 3: Classification
# 
#                 Download from finelybook www.finelybook.com
# Now you are ready to get the confusion matrix using the confusion_matrix() func‐
# tion. Just pass it the target classes (y_train_5) and the predicted classes
# (y_train_pred):
#     >>> from sklearn.metrics import confusion_matrix
#     >>> confusion_matrix(y_train_5, y_train_pred)
#     array([[53272, 1307],
#            [ 1077, 4344]])
# Each row in a confusion matrix represents an actual class, while each column repre‐
# sents a predicted class. The first row of this matrix considers non-5 images (the nega‐
# tive class): 53,272 of them were correctly classified as non-5s (they are called true
# negatives), while the remaining 1,307 were wrongly classified as 5s (false positives).
# The second row considers the images of 5s (the positive class): 1,077 were wrongly
# classified as non-5s (false negatives), while the remaining 4,344 were correctly classi‐
# fied as 5s (true positives). A perfect classifier would have only true positives and true
# negatives, so its confusion matrix would have nonzero values only on its main diago‐
# nal (top left to bottom right):
#     >>> confusion_matrix(y_train_5, y_train_perfect_predictions)
#     array([[54579,    0],
#            [    0, 5421]])
# The confusion matrix gives you a lot of information, but sometimes you may prefer a
# more concise metric. An interesting one to look at is the accuracy of the positive pre‐
# dictions; this is called the precision of the classifier (Equation 3-1).
# 
#    Equation 3-1. Precision
#                    TP
#    precision =
#                  TP + FP
# 
# TP is the number of true positives, and FP is the number of false positives.
# A trivial way to have perfect precision is to make one single positive prediction and
# ensure it is correct (precision = 1/1 = 100%). This would not be very useful since the
# classifier would ignore all but one positive instance. So precision is typically used
# along with another metric named recall, also called sensitivity or true positive rate
# (TPR): this is the ratio of positive instances that are correctly detected by the classifier
# (Equation 3-2).
# 
#    Equation 3-2. Recall
#                 TP
#    recall =
#               TP + FN
# 
# FN is of course the number of false negatives.
# 
# 
#                                                                    Performance Measures   |   85
# 
#                  Download from finelybook www.finelybook.com
# If you are confused about the confusion matrix, Figure 3-2 may help.
# 
# 
# 
# 
# Figure 3-2. An illustrated confusion matrix
# 
# Precision and Recall
# Scikit-Learn provides several functions to compute classifier metrics, including preci‐
# sion and recall:
#      >>> from sklearn.metrics import precision_score, recall_score
#      >>> precision_score(y_train_5, y_pred)     # == 4344 / (4344 + 1307)
#      0.76871350203503808
#      >>> recall_score(y_train_5, y_train_pred) # == 4344 / (4344 + 1077)
#      0.79136690647482011
# Now your 5-detector does not look as shiny as it did when you looked at its accuracy.
# When it claims an image represents a 5, it is correct only 77% of the time. Moreover,
# it only detects 79% of the 5s.
# It is often convenient to combine precision and recall into a single metric called the F1
# score, in particular if you need a simple way to compare two classifiers. The F1 score is
# the harmonic mean of precision and recall (Equation 3-3). Whereas the regular mean
# treats all values equally, the harmonic mean gives much more weight to low values.
# As a result, the classifier will only get a high F1 score if both recall and precision are
# high.
# 
#      Equation 3-3. F1 score
#                       2                      precision × recall       TP
#      F1 =                              =2×                      =
#                 1
#                           +
#                                 1            precision + recall   TP +
#                                                                        FN + FP
#             precision         recall                                      2
# 
# 
# 
# 
# 86   |   Chapter 3: Classification
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Confusion Matrix",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ConfusionMatrix(HierNode):
    def __init__(self):
        super().__init__("Confusion Matrix")
        self.add(Content(), "content")

# eof
