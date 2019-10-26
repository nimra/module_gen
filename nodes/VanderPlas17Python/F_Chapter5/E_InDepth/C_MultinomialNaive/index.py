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
#            data = fetch_20newsgroups()
#            data.target_names
#     Out[7]: ['alt.atheism',
#              'comp.graphics',
#              'comp.os.ms-windows.misc',
#              'comp.sys.ibm.pc.hardware',
#              'comp.sys.mac.hardware',
#              'comp.windows.x',
#              'misc.forsale',
#              'rec.autos',
#              'rec.motorcycles',
#              'rec.sport.baseball',
#              'rec.sport.hockey',
#              'sci.crypt',
#              'sci.electronics',
#              'sci.med',
#              'sci.space',
#              'soc.religion.christian',
#              'talk.politics.guns',
#              'talk.politics.mideast',
#              'talk.politics.misc',
#              'talk.religion.misc']
# For simplicity, we will select just a few of these categories, and download the training
# and testing set:
#     In[8]:
#     categories = ['talk.religion.misc', 'soc.religion.christian', 'sci.space',
#                   'comp.graphics']
#     train = fetch_20newsgroups(subset='train', categories=categories)
#     test = fetch_20newsgroups(subset='test', categories=categories)
# Here is a representative entry from the data:
#     In[9]: print(train.data[5])
#     From: dmcgee@uluhe.soest.hawaii.edu (Don McGee)
#     Subject: Federal Hearing
#     Originator: dmcgee@uluhe
#     Organization: School of Ocean and Earth Science and Technology
#     Distribution: usa
#     Lines: 10
# 
# 
#     Fact or rumor....? Madalyn Murray O'Hare an atheist who eliminated the
#     use of the bible reading and prayer in public schools 15 years ago is now
#     going to appear before the FCC with a petition to stop the reading of the
#     Gospel on the airways of America. And she is also campaigning to remove
#     Christmas programs, songs, etc from the public schools. If it is true
#     then mail to Federal Communications Commission 1919 H Street Washington DC
#     20054 expressing your opposition to her request. Reference Petition number
#     2493.
# 
# 
# 
# 
#                                                       In Depth: Naive Bayes Classification |   387
# 
# In order to use this data for machine learning, we need to be able to convert the con‐
# tent of each string into a vector of numbers. For this we will use the TF–IDF vector‐
# izer (discussed in “Feature Engineering” on page 375), and create a pipeline that
# attaches it to a multinomial naive Bayes classifier:
#       In[10]: from sklearn.feature_extraction.text import TfidfVectorizer
#               from sklearn.naive_bayes import MultinomialNB
#               from sklearn.pipeline import make_pipeline
# 
#                 model = make_pipeline(TfidfVectorizer(), MultinomialNB())
# With this pipeline, we can apply the model to the training data, and predict labels for
# the test data:
#       In[11]: model.fit(train.data, train.target)
#               labels = model.predict(test.data)
# Now that we have predicted the labels for the test data, we can evaluate them to learn
# about the performance of the estimator. For example, here is the confusion matrix
# between the true and predicted labels for the test data (Figure 5-41):
#       In[12]:
#       from sklearn.metrics import confusion_matrix
#       mat = confusion_matrix(test.target, labels)
#       sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
#                   xticklabels=train.target_names, yticklabels=train.target_names)
#       plt.xlabel('true label')
#       plt.ylabel('predicted label');
# 
# 
# 
# 
# Figure 5-41. Confusion matrix for the multinomial naive Bayes text classifier
# 
# 
# 388   |   Chapter 5: Machine Learning
# 
# Evidently, even this very simple classifier can successfully separate space talk from
# computer talk, but it gets confused between talk about religion and talk about Chris‐
# tianity. This is perhaps an expected area of confusion!
# The very cool thing here is that we now have the tools to determine the category for
# any string, using the predict() method of this pipeline. Here’s a quick utility func‐
# tion that will return the prediction for a single string:
#     In[13]: def predict_category(s, train=train, model=model):
#                 pred = model.predict([s])
#                 return train.target_names[pred[0]]
# Let’s try it out:
#     In[14]: predict_category('sending a payload to the ISS')
#     Out[14]: 'sci.space'
#     In[15]: predict_category('discussing islam vs atheism')
#     Out[15]: 'soc.religion.christian'
#     In[16]: predict_category('determining the screen resolution')
#     Out[16]: 'comp.graphics'
# Remember that this is nothing more sophisticated than a simple probability model
# for the (weighted) frequency of each word in the string; nevertheless, the result is
# striking. Even a very naive algorithm, when used carefully and trained on a large set
# of high-dimensional data, can be surprisingly effective.
# 
# When to Use Naive Bayes
# Because naive Bayesian classifiers make such stringent assumptions about data, they
# will generally not perform as well as a more complicated model. That said, they have
# several advantages:
# 
#   • They are extremely fast for both training and prediction
#   • They provide straightforward probabilistic prediction
#   • They are often very easily interpretable
#   • They have very few (if any) tunable parameters
# 
# These advantages mean a naive Bayesian classifier is often a good choice as an initial
# baseline classification. If it performs suitably, then congratulations: you have a very
# fast, very interpretable classifier for your problem. If it does not perform well, then
# you can begin exploring more sophisticated models, with some baseline knowledge of
# how well they should perform.
# Naive Bayes classifiers tend to perform especially well in one of the following
# situations:
# 
#                                                       In Depth: Naive Bayes Classification |   389
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Multinomial Naive Bayes",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MultinomialNaive(HierNode):
    def __init__(self):
        super().__init__("Multinomial Naive Bayes")
        self.add(Content())

# eof
