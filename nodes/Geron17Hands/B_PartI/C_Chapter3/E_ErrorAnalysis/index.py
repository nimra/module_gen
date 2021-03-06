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
# represents a 5. It also thinks that the image could instead be a 0 or a 3 (10% chance
# each).
# Now of course you want to evaluate these classifiers. As usual, you want to use cross-
# validation. Let’s evaluate the SGDClassifier’s accuracy using the cross_val_score()
# function:
#      >>> cross_val_score(sgd_clf, X_train, y_train, cv=3, scoring="accuracy")
#      array([ 0.84063187, 0.84899245, 0.86652998])
# It gets over 84% on all test folds. If you used a random classifier, you would get 10%
# accuracy, so this is not such a bad score, but you can still do much better. For exam‐
# ple, simply scaling the inputs (as discussed in Chapter 2) increases accuracy above
# 90%:
#      >>> from sklearn.preprocessing import StandardScaler
#      >>> scaler = StandardScaler()
#      >>> X_train_scaled = scaler.fit_transform(X_train.astype(np.float64))
#      >>> cross_val_score(sgd_clf, X_train_scaled, y_train, cv=3, scoring="accuracy")
#      array([ 0.91011798, 0.90874544, 0.906636 ])
# 
# 
# Error Analysis
# Of course, if this were a real project, you would follow the steps in your Machine
# Learning project checklist (see Appendix B): exploring data preparation options, try‐
# ing out multiple models, shortlisting the best ones and fine-tuning their hyperpara‐
# meters using GridSearchCV, and automating as much as possible, as you did in the
# previous chapter. Here, we will assume that you have found a promising model and
# you want to find ways to improve it. One way to do this is to analyze the types of
# errors it makes.
# First, you can look at the confusion matrix. You need to make predictions using the
# cross_val_predict() function, then call the confusion_matrix() function, just like
# you did earlier:
#      >>> y_train_pred = cross_val_predict(sgd_clf, X_train_scaled, y_train, cv=3)
#      >>> conf_mx = confusion_matrix(y_train, y_train_pred)
#      >>> conf_mx
#      array([[5725,     3,   24,   9,   10,   49,   50,   10,   39,    4],
#             [    2, 6493,   43,  25,    7,   40,    5,   10, 109,     8],
#             [ 51,     41, 5321, 104,   89,   26,   87,   60, 166,    13],
#             [ 47,     46, 141, 5342,    1, 231,    40,   50, 141,    92],
#             [ 19,     29,   41,  10, 5366,    9,   56,   37,   86, 189],
#             [ 73,     45,   36, 193,   64, 4582, 111,    30, 193,    94],
#             [ 29,     34,   44,   2,   42,   85, 5627,   10,   45,    0],
#             [ 25,     24,   74,  32,   54,   12,    6, 5787,   15, 236],
#             [ 52, 161,      73, 156,   10, 163,    61,   25, 5027, 123],
#             [ 43,     35,   26,  92, 178,    28,    2, 223,    82, 5240]])
# 
# 
# 
# 
# 96   |   Chapter 3: Classification
# 
#                   Download from finelybook www.finelybook.com
# That’s a lot of numbers. It’s often more convenient to look at an image representation
# of the confusion matrix, using Matplotlib’s matshow() function:
#     plt.matshow(conf_mx, cmap=plt.cm.gray)
#     plt.show()
# 
# 
# 
# 
# This confusion matrix looks fairly good, since most images are on the main diagonal,
# which means that they were classified correctly. The 5s look slightly darker than the
# other digits, which could mean that there are fewer images of 5s in the dataset or that
# the classifier does not perform as well on 5s as on other digits. In fact, you can verify
# that both are the case.
# Let’s focus the plot on the errors. First, you need to divide each value in the confusion
# matrix by the number of images in the corresponding class, so you can compare error
# rates instead of absolute number of errors (which would make abundant classes look
# unfairly bad):
#     row_sums = conf_mx.sum(axis=1, keepdims=True)
#     norm_conf_mx = conf_mx / row_sums
# Now let’s fill the diagonal with zeros to keep only the errors, and let’s plot the result:
#     np.fill_diagonal(norm_conf_mx, 0)
#     plt.matshow(norm_conf_mx, cmap=plt.cm.gray)
#     plt.show()
# 
# 
# 
# 
#                                                                            Error Analysis   |   97
# 
#                          Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Now you can clearly see the kinds of errors the classifier makes. Remember that rows
# represent actual classes, while columns represent predicted classes. The columns for
# classes 8 and 9 are quite bright, which tells you that many images get misclassified as
# 8s or 9s. Similarly, the rows for classes 8 and 9 are also quite bright, telling you that 8s
# and 9s are often confused with other digits. Conversely, some rows are pretty dark,
# such as row 1: this means that most 1s are classified correctly (a few are confused
# with 8s, but that’s about it). Notice that the errors are not perfectly symmetrical; for
# example, there are more 5s misclassified as 8s than the reverse.
# Analyzing the confusion matrix can often give you insights on ways to improve your
# classifier. Looking at this plot, it seems that your efforts should be spent on improving
# classification of 8s and 9s, as well as fixing the specific 3/5 confusion. For example,
# you could try to gather more training data for these digits. Or you could engineer
# new features that would help the classifier—for example, writing an algorithm to
# count the number of closed loops (e.g., 8 has two, 6 has one, 5 has none). Or you
# could preprocess the images (e.g., using Scikit-Image, Pillow, or OpenCV) to make
# some patterns stand out more, such as closed loops.
# Analyzing individual errors can also be a good way to gain insights on what your
# classifier is doing and why it is failing, but it is more difficult and time-consuming.
# For example, let’s plot examples of 3s and 5s:
#      cl_a, cl_b = 3, 5
#      X_aa = X_train[(y_train         ==   cl_a)   &   (y_train_pred   ==   cl_a)]
#      X_ab = X_train[(y_train         ==   cl_a)   &   (y_train_pred   ==   cl_b)]
#      X_ba = X_train[(y_train         ==   cl_b)   &   (y_train_pred   ==   cl_a)]
#      X_bb = X_train[(y_train         ==   cl_b)   &   (y_train_pred   ==   cl_b)]
# 
#      plt.figure(figsize=(8,8))
#      plt.subplot(221); plot_digits(X_aa[:25], images_per_row=5)
#      plt.subplot(222); plot_digits(X_ab[:25], images_per_row=5)
# 
# 
# 98   |   Chapter 3: Classification
# 
#                       Download from finelybook www.finelybook.com
#      plt.subplot(223); plot_digits(X_ba[:25], images_per_row=5)
#      plt.subplot(224); plot_digits(X_bb[:25], images_per_row=5)
#      plt.show()
# 
# 
# 
# 
# The two 5×5 blocks on the left show digits classified as 3s, and the two 5×5 blocks on
# the right show images classified as 5s. Some of the digits that the classifier gets wrong
# (i.e., in the bottom-left and top-right blocks) are so badly written that even a human
# would have trouble classifying them (e.g., the 5 on the 8th row and 1st column truly
# looks like a 3). However, most misclassified images seem like obvious errors to us,
# and it’s hard to understand why the classifier made the mistakes it did.3 The reason is
# that we used a simple SGDClassifier, which is a linear model. All it does is assign a
# weight per class to each pixel, and when it sees a new image it just sums up the weigh‐
# ted pixel intensities to get a score for each class. So since 3s and 5s differ only by a few
# pixels, this model will easily confuse them.
# The main difference between 3s and 5s is the position of the small line that joins the
# top line to the bottom arc. If you draw a 3 with the junction slightly shifted to the left,
# the classifier might classify it as a 5, and vice versa. In other words, this classifier is
# quite sensitive to image shifting and rotation. So one way to reduce the 3/5 confusion
# would be to preprocess the images to ensure that they are well centered and not too
# rotated. This will probably help reduce other errors as well.
# 
# 
# 
# 
# 3 But remember that our brain is a fantastic pattern recognition system, and our visual system does a lot of
#   complex preprocessing before any information reaches our consciousness, so the fact that it feels simple does
#   not mean that it is.
# 
# 
# 
#                                                                                             Error Analysis   |   99
# 
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
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Error Analysis",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ErrorAnalysis(HierNode):
    def __init__(self):
        super().__init__("Error Analysis")
        self.add(Content(), "content")

# eof
