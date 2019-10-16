# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                   Download from finelybook www.finelybook.com
# Measuring Accuracy Using Cross-Validation
# A good way to evaluate a model is to use cross-validation, just as you did in Chap‐
# ter 2.
# 
# 
#                           Implementing Cross-Validation
#   Occasionally you will need more control over the cross-validation process than what
#   cross_val_score() and similar functions provide. In these cases, you can implement
#   cross-validation yourself; it is actually fairly straightforward. The following code does
#   roughly the same thing as the preceding cross_val_score() code, and prints the
#   same result:
#       from sklearn.model_selection import StratifiedKFold
#       from sklearn.base import clone
# 
#       skfolds = StratifiedKFold(n_splits=3, random_state=42)
# 
#       for train_index, test_index in skfolds.split(X_train, y_train_5):
#           clone_clf = clone(sgd_clf)
#           X_train_folds = X_train[train_index]
#           y_train_folds = (y_train_5[train_index])
#           X_test_fold = X_train[test_index]
#           y_test_fold = (y_train_5[test_index])
# 
#           clone_clf.fit(X_train_folds, y_train_folds)
#           y_pred = clone_clf.predict(X_test_fold)
#           n_correct = sum(y_pred == y_test_fold)
#           print(n_correct / len(y_pred)) # prints 0.9502, 0.96565 and 0.96495
# 
#   The StratifiedKFold class performs stratified sampling (as explained in Chapter 2)
#   to produce folds that contain a representative ratio of each class. At each iteration the
#   code creates a clone of the classifier, trains that clone on the training folds, and makes
#   predictions on the test fold. Then it counts the number of correct predictions and
#   outputs the ratio of correct predictions.
# 
# 
# Let’s use the cross_val_score() function to evaluate your SGDClassifier model
# using K-fold cross-validation, with three folds. Remember that K-fold cross-
# validation means splitting the training set into K-folds (in this case, three), then mak‐
# ing predictions and evaluating them on each fold using a model trained on the
# remaining folds (see Chapter 2):
#     >>> from sklearn.model_selection import cross_val_score
#     >>> cross_val_score(sgd_clf, X_train, y_train_5, cv=3, scoring="accuracy")
#     array([ 0.9502 , 0.96565, 0.96495])
# 
# 
# 
# 
#                                                                      Performance Measures   |   83
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Measuring Accuracy Using Cross-Validation",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Measuring Accuracy Using Cross-Validation"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MeasuringAccuracy(HierNode):
    def __init__(self):
        super().__init__("Measuring Accuracy Using Cross-Validation")
        self.add(Content())

# eof