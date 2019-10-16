# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_MeasuringAccuracy.index import MeasuringAccuracy as A_MeasuringAccuracy
from .B_ConfusionMatrix.index import ConfusionMatrix as B_ConfusionMatrix
from .C_Precisionand.index import Precisionand as C_Precisionand
from .D_PrecisionRecallTradeoff.index import PrecisionRecallTradeoff as D_PrecisionRecallTradeoff
from .E_TheROC.index import TheROC as E_TheROC

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                          Download from finelybook www.finelybook.com
#      import numpy as np
# 
#      shuffle_index = np.random.permutation(60000)
#      X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]
# 
# 
# Training a Binary Classifier
# Let’s simplify the problem for now and only try to identify one digit—for example,
# the number 5. This “5-detector” will be an example of a binary classifier, capable of
# distinguishing between just two classes, 5 and not-5. Let’s create the target vectors for
# this classification task:
#      y_train_5 = (y_train == 5)       # True for all 5s, False for all other digits.
#      y_test_5 = (y_test == 5)
# Okay, now let’s pick a classifier and train it. A good place to start is with a Stochastic
# Gradient Descent (SGD) classifier, using Scikit-Learn’s SGDClassifier class. This clas‐
# sifier has the advantage of being capable of handling very large datasets efficiently.
# This is in part because SGD deals with training instances independently, one at a time
# (which also makes SGD well suited for online learning), as we will see later. Let’s create
# an SGDClassifier and train it on the whole training set:
#      from sklearn.linear_model import SGDClassifier
# 
#      sgd_clf = SGDClassifier(random_state=42)
#      sgd_clf.fit(X_train, y_train_5)
# 
# 
#                       The SGDClassifier relies on randomness during training (hence
#                       the name “stochastic”). If you want reproducible results, you
#                       should set the random_state parameter.
# 
# 
# 
# Now you can use it to detect images of the number 5:
#      >>> sgd_clf.predict([some_digit])
#      array([ True], dtype=bool)
# 
# The classifier guesses that this image represents a 5 (True). Looks like it guessed right
# in this particular case! Now, let’s evaluate this model’s performance.
# 
# Performance Measures
# Evaluating a classifier is often significantly trickier than evaluating a regressor, so we
# will spend a large part of this chapter on this topic. There are many performance
# measures available, so grab another coffee and get ready to learn many new concepts
# and acronyms!
# 
# 
# 
# 82   |   Chapter 3: Classification
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Performance Measures",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Performance Measures"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PerformanceMeasures(HierNode):
    def __init__(self):
        super().__init__("Performance Measures")
        self.add(Content())
        self.add(A_MeasuringAccuracy())
        self.add(B_ConfusionMatrix())
        self.add(C_Precisionand())
        self.add(D_PrecisionRecallTradeoff())
        self.add(E_TheROC())

# eof
