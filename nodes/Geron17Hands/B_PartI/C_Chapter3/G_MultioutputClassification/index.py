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
#                         Download from finelybook www.finelybook.com
# 
# 
# 
# 
# On the left is the noisy input image, and on the right is the clean target image. Now
# let’s train the classifier and make it clean this image:
#       knn_clf.fit(X_train_mod, y_train_mod)
#       clean_digit = knn_clf.predict([X_test_mod[some_index]])
#       plot_digit(clean_digit)
# 
# 
# 
# 
# Looks close enough to the target! This concludes our tour of classification. Hopefully
# you should now know how to select good metrics for classification tasks, pick the
# appropriate precision/recall tradeoff, compare classifiers, and more generally build
# good classification systems for a variety of tasks.
# 
# Exercises
#  1. Try to build a classifier for the MNIST dataset that achieves over 97% accuracy
#     on the test set. Hint: the KNeighborsClassifier works quite well for this task;
#     you just need to find good hyperparameter values (try a grid search on the
#     weights and n_neighbors hyperparameters).
#  2. Write a function that can shift an MNIST image in any direction (left, right, up,
#     or down) by one pixel.5 Then, for each image in the training set, create four shif‐
#     ted copies (one per direction) and add them to the training set. Finally, train your
#     best model on this expanded training set and measure its accuracy on the test set.
#     You should observe that your model performs even better now! This technique of
# 
# 
# 
# 5 You can use the shift() function from the scipy.ndimage.interpolation module. For example,
#   shift(image, [2, 1], cval=0) shifts the image 2 pixels down and 1 pixel to the right.
# 
# 
# 
# 102   |   Chapter 3: Classification
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Multioutput Classification",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MultioutputClassification(HierNode):
    def __init__(self):
        super().__init__("Multioutput Classification")
        self.add(Content(), "content")

# eof
