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
#                         Download from finelybook www.finelybook.com
# Multilabel Classification
# Until now each instance has always been assigned to just one class. In some cases you
# may want your classifier to output multiple classes for each instance. For example,
# consider a face-recognition classifier: what should it do if it recognizes several people
# on the same picture? Of course it should attach one label per person it recognizes. Say
# the classifier has been trained to recognize three faces, Alice, Bob, and Charlie; then
# when it is shown a picture of Alice and Charlie, it should output [1, 0, 1] (meaning
# “Alice yes, Bob no, Charlie yes”). Such a classification system that outputs multiple
# binary labels is called a multilabel classification system.
# We won’t go into face recognition just yet, but let’s look at a simpler example, just for
# illustration purposes:
#       from sklearn.neighbors import KNeighborsClassifier
# 
#       y_train_large = (y_train >= 7)
#       y_train_odd = (y_train % 2 == 1)
#       y_multilabel = np.c_[y_train_large, y_train_odd]
# 
#       knn_clf = KNeighborsClassifier()
#       knn_clf.fit(X_train, y_multilabel)
# 
# This code creates a y_multilabel array containing two target labels for each digit
# image: the first indicates whether or not the digit is large (7, 8, or 9) and the second
# indicates whether or not it is odd. The next lines create a KNeighborsClassifier
# instance (which supports multilabel classification, but not all classifiers do) and we
# train it using the multiple targets array. Now you can make a prediction, and notice
# that it outputs two labels:
#       >>> knn_clf.predict([some_digit])
#       array([[False, True]], dtype=bool)
# 
# And it gets it right! The digit 5 is indeed not large (False) and odd (True).
# There are many ways to evaluate a multilabel classifier, and selecting the right metric
# really depends on your project. For example, one approach is to measure the F1 score
# for each individual label (or any other binary classifier metric discussed earlier), then
# simply compute the average score. This code computes the average F1 score across all
# labels:
#       >>> y_train_knn_pred = cross_val_predict(knn_clf, X_train, y_train, cv=3)
#       >>> f1_score(y_train, y_train_knn_pred, average="macro")
#       0.96845540180280221
# This assumes that all labels are equally important, which may not be the case. In par‐
# ticular, if you have many more pictures of Alice than of Bob or Charlie, you may want
# to give more weight to the classifier’s score on pictures of Alice. One simple option is
# 
# 
# 
# 100   |   Chapter 3: Classification
# 
#                    Download from finelybook www.finelybook.com
# to give each label a weight equal to its support (i.e., the number of instances with that
# target label). To do this, simply set average="weighted" in the preceding code.4
# 
# Multioutput Classification
# The last type of classification task we are going to discuss here is called multioutput-
# multiclass classification (or simply multioutput classification). It is simply a generaliza‐
# tion of multilabel classification where each label can be multiclass (i.e., it can have
# more than two possible values).
# To illustrate this, let’s build a system that removes noise from images. It will take as
# input a noisy digit image, and it will (hopefully) output a clean digit image, repre‐
# sented as an array of pixel intensities, just like the MNIST images. Notice that the
# classifier’s output is multilabel (one label per pixel) and each label can have multiple
# values (pixel intensity ranges from 0 to 255). It is thus an example of a multioutput
# classification system.
# 
#                     The line between classification and regression is sometimes blurry,
#                     such as in this example. Arguably, predicting pixel intensity is more
#                     akin to regression than to classification. Moreover, multioutput
#                     systems are not limited to classification tasks; you could even have
#                     a system that outputs multiple labels per instance, including both
#                     class labels and value labels.
# 
# Let’s start by creating the training and test sets by taking the MNIST images and
# adding noise to their pixel intensities using NumPy’s randint() function. The target
# images will be the original images:
#      noise = rnd.randint(0, 100, (len(X_train), 784))
#      noise = rnd.randint(0, 100, (len(X_test), 784))
#      X_train_mod = X_train + noise
#      X_test_mod = X_test + noise
#      y_train_mod = X_train
#      y_test_mod = X_test
# Let’s take a peek at an image from the test set (yes, we’re snooping on the test data, so
# you should be frowning right now):
# 
# 
# 
# 
# 4 Scikit-Learn offers a few other averaging options and multilabel classifier metrics; see the documentation for
#   more details.
# 
# 
# 
#                                                                                Multioutput Classification   |   101
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Multilabel Classification",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MultilabelClassification(HierNode):
    def __init__(self):
        super().__init__("Multilabel Classification")
        self.add(Content(), "content")

# eof
