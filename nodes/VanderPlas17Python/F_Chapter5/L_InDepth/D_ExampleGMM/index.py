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
# Figure 5-137. Handwritten digits input
# 
# The result is 41 dimensions, a reduction of nearly 1/3 with almost no information
# loss. Given this projected data, let’s use the AIC to get a gauge for the number of
# GMM components we should use (Figure 5-138):
#     In[21]: n_components = np.arange(50, 210, 10)
#             models = [GMM(n, covariance_type='full', random_state=0)
#                       for n in n_components]
#             aics = [model.fit(data).aic(data) for model in models]
#             plt.plot(n_components, aics);
# It appears that around 110 components minimizes the AIC; we will use this model.
# Let’s quickly fit this to the data and confirm that it has converged:
#     In[22]: gmm = GMM(110, covariance_type='full', random_state=0)
#             gmm.fit(data)
#             print(gmm.converged_)
#     True
# Now we can draw samples of 100 new points within this 41-dimensional projected
# space, using the GMM as a generative model:
#     In[23]: data_new = gmm.sample(100, random_state=0)
#             data_new.shape
#     Out[23]: (100, 41)
# 
# 
# 
# 
#                                                      In Depth: Gaussian Mixture Models   |   489
# 
# Figure 5-138. AIC curve for choosing the appropriate number of GMM components
# 
# Finally, we can use the inverse transform of the PCA object to construct the new dig‐
# its (Figure 5-139):
#       In[24]: digits_new = pca.inverse_transform(data_new)
#               plot_digits(digits_new)
# 
# 
# 
# 
# Figure 5-139. “New” digits randomly drawn from the underlying model of the GMM
# estimator
# 
# 
# 
# 490   |   Chapter 5: Machine Learning
# 
# The results for the most part look like plausible digits from the dataset!
# Consider what we’ve done here: given a sampling of handwritten digits, we have
# modeled the distribution of that data in such a way that we can generate brand new
# samples of digits from the data: these are “handwritten digits” that do not individu‐
# ally appear in the original dataset, but rather capture the general features of the input
# data as modeled by the mixture model. Such a generative model of digits can prove
# very useful as a component of a Bayesian generative classifier, as we shall see in the
# next section.
# 
# In-Depth: Kernel Density Estimation
# In the previous section we covered Gaussian mixture models (GMM), which are a
# kind of hybrid between a clustering estimator and a density estimator. Recall that a
# density estimator is an algorithm that takes a D-dimensional dataset and produces an
# estimate of the D-dimensional probability distribution which that data is drawn from.
# The GMM algorithm accomplishes this by representing the density as a weighted
# sum of Gaussian distributions. Kernel density estimation (KDE) is in some senses an
# algorithm that takes the mixture-of-Gaussians idea to its logical extreme: it uses a
# mixture consisting of one Gaussian component per point, resulting in an essentially
# nonparametric estimator of density. In this section, we will explore the motivation
# and uses of KDE. We begin with the standard imports:
#     In[1]: %matplotlib inline
#            import matplotlib.pyplot as plt
#            import seaborn as sns; sns.set()
#            import numpy as np
# 
# 
# Motivating KDE: Histograms
# As already discussed, a density estimator is an algorithm that seeks to model the
# probability distribution that generated a dataset. For one-dimensional data, you are
# probably already familiar with one simple density estimator: the histogram. A histo‐
# gram divides the data into discrete bins, counts the number of points that fall in each
# bin, and then visualizes the results in an intuitive manner.
# For example, let’s create some data that is drawn from two normal distributions:
#     In[2]: def make_data(N, f=0.3, rseed=1):
#                rand = np.random.RandomState(rseed)
#                x = rand.randn(N)
#                x[int(f * N):] += 5
#                return x
# 
#            x = make_data(1000)
# 
# 
# 
# 
#                                                        In-Depth: Kernel Density Estimation   |   491
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Example: GMM for Generating New Data",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ExampleGMM(HierNode):
    def __init__(self):
        super().__init__("Example: GMM for Generating New Data")
        self.add(Content())

# eof
