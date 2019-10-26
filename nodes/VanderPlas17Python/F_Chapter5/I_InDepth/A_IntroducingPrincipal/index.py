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
# A primary disadvantage of random forests is that the results are not easily interpreta‐
# ble; that is, if you would like to draw conclusions about the meaning of the classifica‐
# tion model, random forests may not be the best choice.
# 
# In Depth: Principal Component Analysis
# Up until now, we have been looking in depth at supervised learning estimators: those
# estimators that predict labels based on labeled training data. Here we begin looking at
# several unsupervised estimators, which can highlight interesting aspects of the data
# without reference to any known labels.
# In this section, we explore what is perhaps one of the most broadly used of unsuper‐
# vised algorithms, principal component analysis (PCA). PCA is fundamentally a
# dimensionality reduction algorithm, but it can also be useful as a tool for visualiza‐
# tion, for noise filtering, for feature extraction and engineering, and much more. After
# a brief conceptual discussion of the PCA algorithm, we will see a couple examples of
# these further applications. We begin with the standard imports:
#     In[1]: %matplotlib inline
#            import numpy as np
#            import matplotlib.pyplot as plt
#            import seaborn as sns; sns.set()
# 
# 
# Introducing Principal Component Analysis
# Principal component analysis is a fast and flexible unsupervised method for dimen‐
# sionality reduction in data, which we saw briefly in “Introducing Scikit-Learn” on
# page 343. Its behavior is easiest to visualize by looking at a two-dimensional dataset.
# Consider the following 200 points (Figure 5-80):
#     In[2]: rng = np.random.RandomState(1)
#            X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
#            plt.scatter(X[:, 0], X[:, 1])
#            plt.axis('equal');
# By eye, it is clear that there is a nearly linear relationship between the x and y vari‐
# ables. This is reminiscent of the linear regression data we explored in “In Depth: Lin‐
# ear Regression” on page 390, but the problem setting here is slightly different: rather
# than attempting to predict the y values from the x values, the unsupervised learning
# problem attempts to learn about the relationship between the x and y values.
# 
# 
# 
# 
#                                                     In Depth: Principal Component Analysis   |   433
# 
# Figure 5-80. Data for demonstration of PCA
# 
# In principal component analysis, one quantifies this relationship by finding a list of
# the principal axes in the data, and using those axes to describe the dataset. Using
# Scikit-Learn’s PCA estimator, we can compute this as follows:
#       In[3]: from sklearn.decomposition import PCA
#              pca = PCA(n_components=2)
#              pca.fit(X)
#       Out[3]: PCA(copy=True, n_components=2, whiten=False)
# The fit learns some quantities from the data, most importantly the “components” and
# “explained variance”:
#       In[4]: print(pca.components_)
#       [[ 0.94446029 0.32862557]
#        [ 0.32862557 -0.94446029]]
#       In[5]: print(pca.explained_variance_)
#       [ 0.75871884      0.01838551]
# To see what these numbers mean, let’s visualize them as vectors over the input data,
# using the “components” to define the direction of the vector, and the “explained var‐
# iance” to define the squared-length of the vector (Figure 5-81):
#       In[6]: def draw_vector(v0, v1, ax=None):
#                  ax = ax or plt.gca()
#                  arrowprops=dict(arrowstyle='->',
#                                  linewidth=2,
#                                  shrinkA=0, shrinkB=0)
#                  ax.annotate('', v1, v0, arrowprops=arrowprops)
# 
#                # plot data
# 
# 
# 
# 434   |   Chapter 5: Machine Learning
# 
#            plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
#            for length, vector in zip(pca.explained_variance_, pca.components_):
#                v = vector * 3 * np.sqrt(length)
#                draw_vector(pca.mean_, pca.mean_ + v)
#            plt.axis('equal');
# 
# 
# 
# 
# Figure 5-81. Visualization of the principal axes in the data
# 
# These vectors represent the principal axes of the data, and the length shown in
# Figure 5-81 is an indication of how “important” that axis is in describing the distribu‐
# tion of the data—more precisely, it is a measure of the variance of the data when pro‐
# jected onto that axis. The projection of each data point onto the principal axes are the
# “principal components” of the data.
# If we plot these principal components beside the original data, we see the plots shown
# in Figure 5-82.
# 
# 
# 
# 
# Figure 5-82. Transformed principal axes in the data
# 
# 
# 
# 
#                                                       In Depth: Principal Component Analysis   |   435
# 
# This transformation from data axes to principal axes is as an affine transformation,
# which basically means it is composed of a translation, rotation, and uniform scaling.
# While this algorithm to find principal components may seem like just a mathematical
# curiosity, it turns out to have very far-reaching applications in the world of machine
# learning and data exploration.
# 
# PCA as dimensionality reduction
# Using PCA for dimensionality reduction involves zeroing out one or more of the
# smallest principal components, resulting in a lower-dimensional projection of the
# data that preserves the maximal data variance.
# Here is an example of using PCA as a dimensionality reduction transform:
#       In[7]: pca = PCA(n_components=1)
#              pca.fit(X)
#              X_pca = pca.transform(X)
#              print("original shape:    ", X.shape)
#              print("transformed shape:", X_pca.shape)
#       original shape:    (200, 2)
#       transformed shape: (200, 1)
# The transformed data has been reduced to a single dimension. To understand the
# effect of this dimensionality reduction, we can perform the inverse transform of this
# reduced data and plot it along with the original data (Figure 5-83):
#       In[8]: X_new = pca.inverse_transform(X_pca)
#              plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
#              plt.scatter(X_new[:, 0], X_new[:, 1], alpha=0.8)
#              plt.axis('equal');
# 
# 
# 
# 
# Figure 5-83. Visualization of PCA as dimensionality reduction
# 
# 
# 
# 436   | Chapter 5: Machine Learning
# 
# The light points are the original data, while the dark points are the projected version.
# This makes clear what a PCA dimensionality reduction means: the information along
# the least important principal axis or axes is removed, leaving only the component(s)
# of the data with the highest variance. The fraction of variance that is cut out (propor‐
# tional to the spread of points about the line formed in Figure 5-83) is roughly a meas‐
# ure of how much “information” is discarded in this reduction of dimensionality.
# This reduced-dimension dataset is in some senses “good enough” to encode the most
# important relationships between the points: despite reducing the dimension of the
# data by 50%, the overall relationship between the data points is mostly preserved.
# 
# PCA for visualization: Handwritten digits
# The usefulness of the dimensionality reduction may not be entirely apparent in only
# two dimensions, but becomes much more clear when we look at high-dimensional
# data. To see this, let’s take a quick look at the application of PCA to the digits data we
# saw in “In-Depth: Decision Trees and Random Forests” on page 421.
# We start by loading the data:
#     In[9]: from sklearn.datasets import load_digits
#            digits = load_digits()
#            digits.data.shape
#     Out[9]:
#     (1797, 64)
# Recall that the data consists of 8×8 pixel images, meaning that they are 64-
# dimensional. To gain some intuition into the relationships between these points, we
# can use PCA to project them to a more manageable number of dimensions, say two:
#     In[10]: pca = PCA(2) # project from 64 to 2 dimensions
#             projected = pca.fit_transform(digits.data)
#             print(digits.data.shape)
#             print(projected.shape)
#     (1797, 64)
#     (1797, 2)
# We can now plot the first two principal components of each point to learn about the
# data (Figure 5-84):
#     In[11]: plt.scatter(projected[:, 0], projected[:, 1],
#                         c=digits.target, edgecolor='none', alpha=0.5,
#                         cmap=plt.cm.get_cmap('spectral', 10))
#             plt.xlabel('component 1')
#             plt.ylabel('component 2')
#             plt.colorbar();
# 
# 
# 
# 
#                                                      In Depth: Principal Component Analysis   |   437
# 
# Figure 5-84. PCA applied to the handwritten digits data
# 
# Recall what these components mean: the full data is a 64-dimensional point cloud,
# and these points are the projection of each data point along the directions with the
# largest variance. Essentially, we have found the optimal stretch and rotation in 64-
# dimensional space that allows us to see the layout of the digits in two dimensions, and
# have done this in an unsupervised manner—that is, without reference to the labels.
# 
# What do the components mean?
# We can go a bit further here, and begin to ask what the reduced dimensions mean.
# This meaning can be understood in terms of combinations of basis vectors. For
# example, each image in the training set is defined by a collection of 64 pixel values,
# which we will call the vector x:
# 
#       x = x1, x2, x3⋯x64
# 
# One way we can think about this is in terms of a pixel basis. That is, to construct the
# image, we multiply each element of the vector by the pixel it describes, and then add
# the results together to build the image:
# 
#       image x = x1 · pixel 1 + x2 · pixel 2 + x3 · pixel 3 ⋯x64 · pixel 64
# 
# One way we might imagine reducing the dimension of this data is to zero out all but a
# few of these basis vectors. For example, if we use only the first eight pixels, we get an
# eight-dimensional projection of the data (Figure 5-85), but it is not very reflective of
# the whole image: we’ve thrown out nearly 90% of the pixels!
# 
# 
# 438    |   Chapter 5: Machine Learning
# 
# Figure 5-85. A naive dimensionality reduction achieved by discarding pixels
# 
# The upper row of panels shows the individual pixels, and the lower row shows the
# cumulative contribution of these pixels to the construction of the image. Using only
# eight of the pixel-basis components, we can only construct a small portion of the 64-
# pixel image. Were we to continue this sequence and use all 64 pixels, we would
# recover the original image.
# But the pixel-wise representation is not the only choice of basis. We can also use other
# basis functions, which each contain some predefined contribution from each pixel,
# and write something like:
# 
#    image x = mean + x1 · basis 1 + x2 · basis 2 + x3 · basis 3 ⋯
# 
# PCA can be thought of as a process of choosing optimal basis functions, such that
# adding together just the first few of them is enough to suitably reconstruct the bulk of
# the elements in the dataset. The principal components, which act as the low-
# dimensional representation of our data, are simply the coefficients that multiply each
# of the elements in this series. Figure 5-86 is a similar depiction of reconstructing this
# digit using the mean plus the first eight PCA basis functions.
# 
# 
# 
# 
# Figure 5-86. A more sophisticated dimensionality reduction achieved by discarding the
# least important principal components (compare to Figure 5-85)
# 
# Unlike the pixel basis, the PCA basis allows us to recover the salient features of the
# input image with just a mean plus eight components! The amount of each pixel in
# each component is the corollary of the orientation of the vector in our two-
# dimensional example. This is the sense in which PCA provides a low-dimensional
# representation of the data: it discovers a set of basis functions that are more efficient
# than the native pixel-basis of the input data.
# 
# 
# 
# 
#                                                     In Depth: Principal Component Analysis   |   439
# 
# Choosing the number of components
# A vital part of using PCA in practice is the ability to estimate how many components
# are needed to describe the data. We can determine this by looking at the cumulative
# explained variance ratio as a function of the number of components (Figure 5-87):
#       In[12]: pca = PCA().fit(digits.data)
#               plt.plot(np.cumsum(pca.explained_variance_ratio_))
#               plt.xlabel('number of components')
#               plt.ylabel('cumulative explained variance');
# 
# 
# 
# 
# Figure 5-87. The cumulative explained variance, which measures how well PCA pre‐
# serves the content of the data
# 
# This curve quantifies how much of the total, 64-dimensional variance is contained
# within the first N components. For example, we see that with the digits the first 10
# components contain approximately 75% of the variance, while you need around 50
# components to describe close to 100% of the variance.
# Here we see that our two-dimensional projection loses a lot of information (as meas‐
# ured by the explained variance) and that we’d need about 20 components to retain
# 90% of the variance. Looking at this plot for a high-dimensional dataset can help you
# understand the level of redundancy present in multiple observations.
# 
# PCA as Noise Filtering
# PCA can also be used as a filtering approach for noisy data. The idea is this: any com‐
# ponents with variance much larger than the effect of the noise should be relatively
# unaffected by the noise. So if you reconstruct the data using just the largest subset of
# principal components, you should be preferentially keeping the signal and throwing
# out the noise.
# 
# 
# 440   | Chapter 5: Machine Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Introducing Principal Component Analysis",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IntroducingPrincipal(HierNode):
    def __init__(self):
        super().__init__("Introducing Principal Component Analysis")
        self.add(Content())

# eof
