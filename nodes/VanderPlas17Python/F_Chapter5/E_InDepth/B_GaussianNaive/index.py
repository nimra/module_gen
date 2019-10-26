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
# Bayesian Classification
# Naive Bayes classifiers are built on Bayesian classification methods. These rely on
# Bayes’s theorem, which is an equation describing the relationship of conditional
# probabilities of statistical quantities. In Bayesian classification, we’re interested in
# finding the probability of a label given some observed features, which we can write as
# P L features . Bayes’s theorem tells us how to express this in terms of quantities we
# can compute more directly:
# 
#                           P features L P L
#    PL     features =          P features
# 
# 
# If we are trying to decide between two labels—let’s call them L1 and L2—then one way
# to make this decision is to compute the ratio of the posterior probabilities for each
# label:
# 
#    P L1   features       P features   L1 P L1
#                      =
#    P L1   features       P features   L2 P L2
# 
# 
# All we need now is some model by which we can compute P features Li for each
# label. Such a model is called a generative model because it specifies the hypothetical
# random process that generates the data. Specifying this generative model for each
# label is the main piece of the training of such a Bayesian classifier. The general ver‐
# sion of such a training step is a very difficult task, but we can make it simpler through
# the use of some simplifying assumptions about the form of this model.
# This is where the “naive” in “naive Bayes” comes in: if we make very naive assump‐
# tions about the generative model for each label, we can find a rough approximation of
# the generative model for each class, and then proceed with the Bayesian classification.
# Different types of naive Bayes classifiers rest on different naive assumptions about the
# data, and we will examine a few of these in the following sections. We begin with the
# standard imports:
#     In[1]: %matplotlib inline
#            import numpy as np
#            import matplotlib.pyplot as plt
#            import seaborn as sns; sns.set()
# 
# 
# Gaussian Naive Bayes
# Perhaps the easiest naive Bayes classifier to understand is Gaussian naive Bayes. In
# this classifier, the assumption is that data from each label is drawn from a simple Gaus‐
# sian distribution. Imagine that you have the following data (Figure 5-38):
# 
# 
# 
#                                                        In Depth: Naive Bayes Classification |   383
# 
#       In[2]: from sklearn.datasets import make_blobs
#              X, y = make_blobs(100, 2, centers=2, random_state=2, cluster_std=1.5)
#              plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu');
# 
# 
# 
# 
# Figure 5-38. Data for Gaussian naive Bayes classification
# 
# One extremely fast way to create a simple model is to assume that the data is
# described by a Gaussian distribution with no covariance between dimensions. We can
# fit this model by simply finding the mean and standard deviation of the points within
# each label, which is all you need to define such a distribution. The result of this naive
# Gaussian assumption is shown in Figure 5-39.
# 
# 
# 
# 
# Figure 5-39. Visualization of the Gaussian naive Bayes model
# 
# 
# 
# 384   | Chapter 5: Machine Learning
# 
# The ellipses here represent the Gaussian generative model for each label, with larger
# probability toward the center of the ellipses. With this generative model in place for
# each class, we have a simple recipe to compute the likelihood P features L1 for any
# data point, and thus we can quickly compute the posterior ratio and determine which
# label is the most probable for a given point.
# This procedure is implemented in Scikit-Learn’s sklearn.naive_bayes.GaussianNB
# estimator:
#     In[3]: from sklearn.naive_bayes import GaussianNB
#            model = GaussianNB()
#            model.fit(X, y);
# Now let’s generate some new data and predict the label:
#     In[4]: rng = np.random.RandomState(0)
#            Xnew = [-6, -14] + [14, 18] * rng.rand(2000, 2)
#            ynew = model.predict(Xnew)
# Now we can plot this new data to get an idea of where the decision boundary is
# (Figure 5-40):
#     In[5]: plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
#            lim = plt.axis()
#            plt.scatter(Xnew[:, 0], Xnew[:, 1], c=ynew, s=20, cmap='RdBu', alpha=0.1)
#            plt.axis(lim);
# 
# 
# 
# 
# Figure 5-40. Visualization of the Gaussian naive Bayes classification
# 
# We see a slightly curved boundary in the classifications—in general, the boundary in
# Gaussian naive Bayes is quadratic.
# A nice piece of this Bayesian formalism is that it naturally allows for probabilistic
# classification, which we can compute using the predict_proba method:
# 
# 
#                                                        In Depth: Naive Bayes Classification |   385
# 
#       In[6]: yprob = model.predict_proba(Xnew)
#              yprob[-8:].round(2)
#       Out[6]: array([[      0.89, 0.11],
#                      [      1. , 0. ],
#                      [      1. , 0. ],
#                      [      1. , 0. ],
#                      [      1. , 0. ],
#                      [      1. , 0. ],
#                      [      0. , 1. ],
#                      [      0.15, 0.85]])
# The columns give the posterior probabilities of the first and second label, respectively.
# If you are looking for estimates of uncertainty in your classification, Bayesian
# approaches like this can be a useful approach.
# Of course, the final classification will only be as good as the model assumptions that
# lead to it, which is why Gaussian naive Bayes often does not produce very good
# results. Still, in many cases—especially as the number of features becomes large—this
# assumption is not detrimental enough to prevent Gaussian naive Bayes from being a
# useful method.
# 
# Multinomial Naive Bayes
# The Gaussian assumption just described is by no means the only simple assumption
# that could be used to specify the generative distribution for each label. Another useful
# example is multinomial naive Bayes, where the features are assumed to be generated
# from a simple multinomial distribution. The multinomial distribution describes the
# probability of observing counts among a number of categories, and thus multinomial
# naive Bayes is most appropriate for features that represent counts or count rates.
# The idea is precisely the same as before, except that instead of modeling the data dis‐
# tribution with the best-fit Gaussian, we model the data distribution with a best-fit
# multinomial distribution.
# 
# Example: Classifying text
# One place where multinomial naive Bayes is often used is in text classification, where
# the features are related to word counts or frequencies within the documents to be
# classified. We discussed the extraction of such features from text in “Feature Engi‐
# neering” on page 375; here we will use the sparse word count features from the 20
# Newsgroups corpus to show how we might classify these short documents into
# categories.
# Let’s download the data and take a look at the target names:
#       In[7]: from sklearn.datasets import fetch_20newsgroups
# 
# 
# 
# 
# 386   |   Chapter 5: Machine Learning
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Gaussian Naive Bayes",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GaussianNaive(HierNode):
    def __init__(self):
        super().__init__("Gaussian Naive Bayes")
        self.add(Content())

# eof
