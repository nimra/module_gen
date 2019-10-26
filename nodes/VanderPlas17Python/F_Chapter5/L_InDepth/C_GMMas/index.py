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
# Choosing the covariance type
# If you look at the details of the preceding fits, you will see that the covariance_type
# option was set differently within each. This hyperparameter controls the degrees of
# freedom in the shape of each cluster; it is essential to set this carefully for any given
# problem. The default is covariance_type="diag", which means that the size of the
# cluster along each dimension can be set independently, with the resulting ellipse
# constrained to align with the axes. A slightly simpler and faster model is cova
# riance_type="spherical", which constrains the shape of the cluster such that all
# dimensions are equal. The resulting clustering will have similar characteristics to that
# of k-means, though it is not entirely equivalent. A more complicated and computa‐
# tionally expensive model (especially as the number of dimensions grows) is to use
# covariance_type="full", which allows each cluster to be modeled as an ellipse with
# arbitrary orientation.
# We can see a visual representation of these three choices for a single cluster within
# Figure 5-131:
# 
# 
# 
# 
# Figure 5-131. Visualization of GMM covariance types
# 
# GMM as Density Estimation
# Though GMM is often categorized as a clustering algorithm, fundamentally it is an
# algorithm for density estimation. That is to say, the result of a GMM fit to some data is
# technically not a clustering model, but a generative probabilistic model describing the
# distribution of the data.
# As an example, consider some data generated from Scikit-Learn’s make_moons func‐
# tion (visualized in Figure 5-132), which we saw in “In Depth: k-Means Clustering” on
# page 462:
#       In[13]: from sklearn.datasets import make_moons
#               Xmoon, ymoon = make_moons(200, noise=.05, random_state=0)
#               plt.scatter(Xmoon[:, 0], Xmoon[:, 1]);
# 
# 
# 
# 
# 484   | Chapter 5: Machine Learning
# 
# Figure 5-132. GMM applied to clusters with nonlinear boundaries
# 
# If we try to fit this to a two-component GMM viewed as a clustering model, the
# results are not particularly useful (Figure 5-133):
#    In[14]: gmm2 = GMM(n_components=2, covariance_type='full', random_state=0)
#            plot_gmm(gmm2, Xmoon)
# 
# 
# 
# 
# Figure 5-133. Two component GMM fit to nonlinear clusters
# 
# But if we instead use many more components and ignore the cluster labels, we find a
# fit that is much closer to the input data (Figure 5-134):
#    In[15]: gmm16 = GMM(n_components=16, covariance_type='full', random_state=0)
#            plot_gmm(gmm16, Xmoon, label=False)
# 
# 
# 
# 
#                                                      In Depth: Gaussian Mixture Models   |   485
# 
# Figure 5-134. Using many GMM clusters to model the distribution of points
# 
# Here the mixture of 16 Gaussians serves not to find separated clusters of data, but
# rather to model the overall distribution of the input data. This is a generative model of
# the distribution, meaning that the GMM gives us the recipe to generate new random
# data distributed similarly to our input. For example, here are 400 new points drawn
# from this 16-component GMM fit to our original data (Figure 5-135):
#       In[16]: Xnew = gmm16.sample(400, random_state=42)
#               plt.scatter(Xnew[:, 0], Xnew[:, 1]);
# 
# 
# 
# 
# Figure 5-135. New data drawn from the 16-component GMM
# 
# GMM is convenient as a flexible means of modeling an arbitrary multidimensional
# distribution of data.
# 
# 
# 
# 486   |   Chapter 5: Machine Learning
# 
# How many components?
# The fact that GMM is a generative model gives us a natural means of determining the
# optimal number of components for a given dataset. A generative model is inherently
# a probability distribution for the dataset, and so we can simply evaluate the likelihood
# of the data under the model, using cross-validation to avoid overfitting. Another
# means of correcting for overfitting is to adjust the model likelihoods using some ana‐
# lytic criterion such as the Akaike information criterion (AIC) or the Bayesian infor‐
# mation criterion (BIC). Scikit-Learn’s GMM estimator actually includes built-in
# methods that compute both of these, and so it is very easy to operate on this
# approach.
# Let’s look at the AIC and BIC as a function as the number of GMM components for
# our moon dataset (Figure 5-136):
#     In[17]: n_components = np.arange(1, 21)
#             models = [GMM(n, covariance_type='full', random_state=0).fit(Xmoon)
#                       for n in n_components]
# 
#             plt.plot(n_components, [m.bic(Xmoon) for m in models], label='BIC')
#             plt.plot(n_components, [m.aic(Xmoon) for m in models], label='AIC')
#             plt.legend(loc='best')
#             plt.xlabel('n_components');
# 
# 
# 
# 
# Figure 5-136. Visualization of AIC and BIC for choosing the number of GMM
# components
# 
# The optimal number of clusters is the value that minimizes the AIC or BIC, depend‐
# ing on which approximation we wish to use. The AIC tells us that our choice of 16
# components was probably too many: around 8–12 components would have been a
# 
# 
# 
# 
#                                                        In Depth: Gaussian Mixture Models   |   487
# 
# better choice. As is typical with this sort of problem, the BIC recommends a simpler
# model.
# Notice the important point: this choice of number of components measures how well
# GMM works as a density estimator, not how well it works as a clustering algorithm. I’d
# encourage you to think of GMM primarily as a density estimator, and use it for clus‐
# tering only when warranted within simple datasets.
# 
# Example: GMM for Generating New Data
# We just saw a simple example of using GMM as a generative model of data in order to
# create new samples from the distribution defined by the input data. Here we will run
# with this idea and generate new handwritten digits from the standard digits corpus
# that we have used before.
# To start with, let’s load the digits data using Scikit-Learn’s data tools:
#       In[18]: from sklearn.datasets import load_digits
#               digits = load_digits()
#               digits.data.shape
#       Out[18]: (1797, 64)
# Next let’s plot the first 100 of these to recall exactly what we’re looking at
# (Figure 5-137):
#       In[19]: def plot_digits(data):
#                   fig, ax = plt.subplots(10, 10, figsize=(8, 8),
#                                          subplot_kw=dict(xticks=[], yticks=[]))
#                   fig.subplots_adjust(hspace=0.05, wspace=0.05)
#                   for i, axi in enumerate(ax.flat):
#                       im = axi.imshow(data[i].reshape(8, 8), cmap='binary')
#                       im.set_clim(0, 16)
#               plot_digits(digits.data)
# We have nearly 1,800 digits in 64 dimensions, and we can build a GMM on top of
# these to generate more. GMMs can have difficulty converging in such a high dimen‐
# sional space, so we will start with an invertible dimensionality reduction algorithm on
# the data. Here we will use a straightforward PCA, asking it to preserve 99% of the
# variance in the projected data:
#       In[20]: from sklearn.decomposition import PCA
#               pca = PCA(0.99, whiten=True)
#               data = pca.fit_transform(digits.data)
#               data.shape
#       Out[20]: (1797, 41)
# 
# 
# 
# 
# 488   |   Chapter 5: Machine Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "GMM as Density Estimation",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GMMas(HierNode):
    def __init__(self):
        super().__init__("GMM as Density Estimation")
        self.add(Content())

# eof
