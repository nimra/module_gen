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
#       In[15]: pca = PCA(0.50).fit(noisy)
#               pca.n_components_
#       Out[15]: 12
# Here 50% of the variance amounts to 12 principal components. Now we compute
# these components, and then use the inverse of the transform to reconstruct the fil‐
# tered digits (Figure 5-90):
#       In[16]: components = pca.transform(noisy)
#               filtered = pca.inverse_transform(components)
#               plot_digits(filtered)
# 
# 
# 
# 
# Figure 5-90. Digits “denoised” using PCA
# 
# This signal preserving/noise filtering property makes PCA a very useful feature selec‐
# tion routine—for example, rather than training a classifier on very high-dimensional
# data, you might instead train the classifier on the lower-dimensional representation,
# which will automatically serve to filter out random noise in the inputs.
# 
# Example: Eigenfaces
# Earlier we explored an example of using a PCA projection as a feature selector for
# facial recognition with a support vector machine (“In-Depth: Support Vector
# Machines” on page 405). Here we will take a look back and explore a bit more of what
# went into that. Recall that we were using the Labeled Faces in the Wild dataset made
# available through Scikit-Learn:
#       In[17]: from sklearn.datasets import fetch_lfw_people
#               faces = fetch_lfw_people(min_faces_per_person=60)
#               print(faces.target_names)
#               print(faces.images.shape)
#       ['Ariel Sharon' 'Colin Powell' 'Donald Rumsfeld' 'George W Bush'
#        'Gerhard Schroeder' 'Hugo Chavez' 'Junichiro Koizumi' 'Tony Blair']
#       (1348, 62, 47)
# Let’s take a look at the principal axes that span this dataset. Because this is a large
# dataset, we will use RandomizedPCA—it contains a randomized method to approxi‐
# 
# 
# 442   | Chapter 5: Machine Learning
# 
# mate the first N principal components much more quickly than the standard PCA esti‐
# mator, and thus is very useful for high-dimensional data (here, a dimensionality of
# nearly 3,000). We will take a look at the first 150 components:
#     In[18]: from sklearn.decomposition import RandomizedPCA
#             pca = RandomizedPCA(150)
#             pca.fit(faces.data)
#     Out[18]: RandomizedPCA(copy=True, iterated_power=3, n_components=150,
#                     random_state=None, whiten=False)
# In this case, it can be interesting to visualize the images associated with the first sev‐
# eral principal components (these components are technically known as “eigenvec‐
# tors,” so these types of images are often called “eigenfaces”). As you can see in
# Figure 5-91, they are as creepy as they sound:
#     In[19]: fig, axes = plt.subplots(3, 8, figsize=(9, 4),
#                                      subplot_kw={'xticks':[], 'yticks':[]},
#                                      gridspec_kw=dict(hspace=0.1, wspace=0.1))
#             for i, ax in enumerate(axes.flat):
#                 ax.imshow(pca.components_[i].reshape(62, 47), cmap='bone')
# 
# 
# 
# 
# Figure 5-91. A visualization of eigenfaces learned from the LFW dataset
# 
# The results are very interesting, and give us insight into how the images vary: for
# example, the first few eigenfaces (from the top left) seem to be associated with the
# angle of lighting on the face, and later principal vectors seem to be picking out certain
# features, such as eyes, noses, and lips. Let’s take a look at the cumulative variance of
# these components to see how much of the data information the projection is preserv‐
# ing (Figure 5-92):
#     In[20]: plt.plot(np.cumsum(pca.explained_variance_ratio_))
#             plt.xlabel('number of components')
#             plt.ylabel('cumulative explained variance');
# 
# 
# 
# 
#                                                      In Depth: Principal Component Analysis   |   443
# 
# Figure 5-92. Cumulative explained variance for the LFW data
# 
# We see that these 150 components account for just over 90% of the variance. That
# would lead us to believe that using these 150 components, we would recover most of
# the essential characteristics of the data. To make this more concrete, we can compare
# the input images with the images reconstructed from these 150 components
# (Figure 5-93):
#       In[21]: # Compute the components and projected faces
#               pca = RandomizedPCA(150).fit(faces.data)
#               components = pca.transform(faces.data)
#               projected = pca.inverse_transform(components)
#       In[22]: # Plot the results
#               fig, ax = plt.subplots(2, 10, figsize=(10, 2.5),
#                                      subplot_kw={'xticks':[], 'yticks':[]},
#                                      gridspec_kw=dict(hspace=0.1, wspace=0.1))
#               for i in range(10):
#                   ax[0, i].imshow(faces.data[i].reshape(62, 47), cmap='binary_r')
#                   ax[1, i].imshow(projected[i].reshape(62, 47), cmap='binary_r')
# 
#                 ax[0, 0].set_ylabel('full-dim\ninput')
#                 ax[1, 0].set_ylabel('150-dim\nreconstruction');
# 
# 
# 
# 
# Figure 5-93. 150-dimensional PCA reconstruction of the LFW data
# 
# 
# 444   |   Chapter 5: Machine Learning
# 
# The top row here shows the input images, while the bottom row shows the recon‐
# struction of the images from just 150 of the ~3,000 initial features. This visualization
# makes clear why the PCA feature selection used in “In-Depth: Support Vector
# Machines” on page 405 was so successful: although it reduces the dimensionality of
# the data by nearly a factor of 20, the projected images contain enough information
# that we might, by eye, recognize the individuals in the image. What this means is that
# our classification algorithm needs to be trained on 150-dimensional data rather than
# 3,000-dimensional data, which depending on the particular algorithm we choose, can
# lead to a much more efficient classification.
# 
# Principal Component Analysis Summary
# In this section we have discussed the use of principal component analysis for dimen‐
# sionality reduction, for visualization of high-dimensional data, for noise filtering, and
# for feature selection within high-dimensional data. Because of the versatility and
# interpretability of PCA, it has been shown to be effective in a wide variety of contexts
# and disciplines. Given any high-dimensional dataset, I tend to start with PCA in
# order to visualize the relationship between points (as we did with the digits), to
# understand the main variance in the data (as we did with the eigenfaces), and to
# understand the intrinsic dimensionality (by plotting the explained variance ratio).
# Certainly PCA is not useful for every high-dimensional dataset, but it offers a
# straightforward and efficient path to gaining insight into high-dimensional data.
# PCA’s main weakness is that it tends to be highly affected by outliers in the data. For
# this reason, many robust variants of PCA have been developed, many of which act to
# iteratively discard data points that are poorly described by the initial components.
# Scikit-Learn contains a couple interesting variants on PCA, including RandomizedPCA
# and SparsePCA, both also in the sklearn.decomposition submodule. Randomi
# zedPCA, which we saw earlier, uses a nondeterministic method to quickly approxi‐
# mate the first few principal components in very high-dimensional data, while
# SparsePCA introduces a regularization term (see “In Depth: Linear Regression” on
# page 390) that serves to enforce sparsity of the components.
# In the following sections, we will look at other unsupervised learning methods that
# build on some of the ideas of PCA.
# 
# In-Depth: Manifold Learning
# We have seen how principal component analysis can be used in the dimensionality
# reduction task—reducing the number of features of a dataset while maintaining the
# essential relationships between the points. While PCA is flexible, fast, and easily
# interpretable, it does not perform so well when there are nonlinear relationships
# within the data; we will see some examples of these below.
# 
# 
# 
#                                                             In-Depth: Manifold Learning   |   445
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Example: Eigenfaces",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ExampleEigenfaces(HierNode):
    def __init__(self):
        super().__init__("Example: Eigenfaces")
        self.add(Content())

# eof
