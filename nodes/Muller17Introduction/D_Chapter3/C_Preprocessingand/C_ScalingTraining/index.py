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
# The transformed data has the same shape as the original data—the features are simply
# shifted and scaled. You can see that all of the features are now between 0 and 1, as
# desired.
# To apply the SVM to the scaled data, we also need to transform the test set. This is
# again done by calling the transform method, this time on X_test:
# In[7]:
#       # transform test data
#       X_test_scaled = scaler.transform(X_test)
#       # print test data properties after scaling
#       print("per-feature minimum after scaling:\n{}".format(X_test_scaled.min(axis=0)))
#       print("per-feature maximum after scaling:\n{}".format(X_test_scaled.max(axis=0)))
# 
# Out[7]:
#       per-feature minimum after scaling:
#       [ 0.034 0.023 0.031 0.011 0.141 0.044 0.      0.     0.154 -0.006
#        -0.001 0.006 0.004 0.001 0.039 0.011 0.      0.    -0.032 0.007
#         0.027 0.058 0.02     0.009 0.109 0.026 0.   0.    -0.    -0.002]
#       per-feature maximum after scaling:
#       [ 0.958 0.815 0.956 0.894 0.811 1.22     0.88 0.933 0.932 1.037
#         0.427 0.498 0.441 0.284 0.487 0.739 0.767 0.629 1.337 0.391
#         0.896 0.793 0.849 0.745 0.915 1.132 1.07    0.924 1.205 1.631]
# Maybe somewhat surprisingly, you can see that for the test set, after scaling, the mini‐
# mum and maximum are not 0 and 1. Some of the features are even outside the 0–1
# range! The explanation is that the MinMaxScaler (and all the other scalers) always
# applies exactly the same transformation to the training and the test set. This means
# the transform method always subtracts the training set minimum and divides by the
# training set range, which might be different from the minimum and range for the test
# set.
# 
# Scaling Training and Test Data the Same Way
# It is important to apply exactly the same transformation to the training set and the
# test set for the supervised model to work on the test set. The following example
# (Figure 3-2) illustrates what would happen if we were to use the minimum and range
# of the test set instead:
# In[8]:
#       from sklearn.datasets import make_blobs
#       # make synthetic data
#       X, _ = make_blobs(n_samples=50, centers=5, random_state=4, cluster_std=2)
#       # split it into training and test sets
#       X_train, X_test = train_test_split(X, random_state=5, test_size=.1)
# 
#       # plot the training and test sets
#       fig, axes = plt.subplots(1, 3, figsize=(13, 4))
# 
# 
# 136   | Chapter 3: Unsupervised Learning and Preprocessing
# 
#     axes[0].scatter(X_train[:, 0], X_train[:, 1],
#                     c=mglearn.cm2(0), label="Training set", s=60)
#     axes[0].scatter(X_test[:, 0], X_test[:, 1], marker='^',
#                     c=mglearn.cm2(1), label="Test set", s=60)
#     axes[0].legend(loc='upper left')
#     axes[0].set_title("Original Data")
# 
#     # scale the data using MinMaxScaler
#     scaler = MinMaxScaler()
#     scaler.fit(X_train)
#     X_train_scaled = scaler.transform(X_train)
#     X_test_scaled = scaler.transform(X_test)
# 
#     # visualize the properly scaled data
#     axes[1].scatter(X_train_scaled[:, 0], X_train_scaled[:, 1],
#                     c=mglearn.cm2(0), label="Training set", s=60)
#     axes[1].scatter(X_test_scaled[:, 0], X_test_scaled[:, 1], marker='^',
#                     c=mglearn.cm2(1), label="Test set", s=60)
#     axes[1].set_title("Scaled Data")
# 
#     # rescale the test set separately
#     # so test set min is 0 and test set max is 1
#     # DO NOT DO THIS! For illustration purposes only.
#     test_scaler = MinMaxScaler()
#     test_scaler.fit(X_test)
#     X_test_scaled_badly = test_scaler.transform(X_test)
# 
#     # visualize wrongly scaled data
#     axes[2].scatter(X_train_scaled[:, 0], X_train_scaled[:, 1],
#                     c=mglearn.cm2(0), label="training set", s=60)
#     axes[2].scatter(X_test_scaled_badly[:, 0], X_test_scaled_badly[:, 1],
#                     marker='^', c=mglearn.cm2(1), label="test set", s=60)
#     axes[2].set_title("Improperly Scaled Data")
# 
#     for ax in axes:
#         ax.set_xlabel("Feature 0")
#         ax.set_ylabel("Feature 1")
# 
# 
# 
# 
# Figure 3-2. Effect of scaling training and test data shown on the left together (center) and
# separately (right)
# 
# 
# 
#                                                                 Preprocessing and Scaling   |   137
# 
# The first panel is an unscaled two-dimensional dataset, with the training set shown as
# circles and the test set shown as triangles. The second panel is the same data, but
# scaled using the MinMaxScaler. Here, we called fit on the training set, and then
# called transform on the training and test sets. You can see that the dataset in the sec‐
# ond panel looks identical to the first; only the ticks on the axes have changed. Now all
# the features are between 0 and 1. You can also see that the minimum and maximum
# feature values for the test data (the triangles) are not 0 and 1.
# The third panel shows what would happen if we scaled the training set and test set
# separately. In this case, the minimum and maximum feature values for both the train‐
# ing and the test set are 0 and 1. But now the dataset looks different. The test points
# moved incongruously to the training set, as they were scaled differently. We changed
# the arrangement of the data in an arbitrary way. Clearly this is not what we want to
# do.
# As another way to think about this, imagine your test set is a single point. There is no
# way to scale a single point correctly, to fulfill the minimum and maximum require‐
# ments of the MinMaxScaler. But the size of your test set should not change your
# processing.
# 
# 
#                                Shortcuts and Efficient Alternatives
#   Often, you want to fit a model on some dataset, and then transform it. This is a very
#   common task, which can often be computed more efficiently than by simply calling
#   fit and then transform. For this use case, all models that have a transform method
#   also have a fit_transform method. Here is an example using StandardScaler:
#   In[9]:
#           from sklearn.preprocessing import StandardScaler
#           scaler = StandardScaler()
#           # calling fit and transform in sequence (using method chaining)
#           X_scaled = scaler.fit(X).transform(X)
#           # same result, but more efficient computation
#           X_scaled_d = scaler.fit_transform(X)
# 
#   While fit_transform is not necessarily more efficient for all models, it is still good
#   practice to use this method when trying to transform the training set.
# 
# 
# The Effect of Preprocessing on Supervised Learning
# Now let’s go back to the cancer dataset and see the effect of using the MinMaxScaler
# on learning the SVC (this is a different way of doing the same scaling we did in Chap‐
# ter 2). First, let’s fit the SVC on the original data again for comparison:
# 
# 
# 
# 
# 138   |    Chapter 3: Unsupervised Learning and Preprocessing
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Scaling Training and Test Data the Same Way",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ScalingTraining(HierNode):
    def __init__(self):
        super().__init__("Scaling Training and Test Data the Same Way")
        self.add(Content(), "content")

# eof
