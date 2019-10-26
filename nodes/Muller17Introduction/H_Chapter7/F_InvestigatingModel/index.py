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
# Features with low tf–idf are those that either are very commonly used across docu‐
# ments or are only used sparingly, and only in very long documents. Interestingly,
# many of the high-tf–idf features actually identify certain shows or movies. These
# terms only appear in reviews for this particular show or franchise, but tend to appear
# very often in these particular reviews. This is very clear, for example, for "pokemon",
# "smallville", and "doodlebops", but "scanners" here actually also refers to a
# movie title. These words are unlikely to help us in our sentiment classification task
# (unless maybe some franchises are universally reviewed positively or negatively) but
# certainly contain a lot of specific information about the reviews.
# We can also find the words that have low inverse document frequency—that is, those
# that appear frequently and are therefore deemed less important. The inverse docu‐
# ment frequency values found on the training set are stored in the idf_ attribute:
# In[25]:
#       sorted_by_idf = np.argsort(vectorizer.idf_)
#       print("Features with lowest idf:\n{}".format(
#           feature_names[sorted_by_idf[:100]]))
# Out[25]:
#       Features with lowest idf:
#       ['the' 'and' 'of' 'to' 'this' 'is' 'it' 'in' 'that' 'but' 'for' 'with'
#        'was' 'as' 'on' 'movie' 'not' 'have' 'one' 'be' 'film' 'are' 'you' 'all'
#        'at' 'an' 'by' 'so' 'from' 'like' 'who' 'they' 'there' 'if' 'his' 'out'
#        'just' 'about' 'he' 'or' 'has' 'what' 'some' 'good' 'can' 'more' 'when'
#        'time' 'up' 'very' 'even' 'only' 'no' 'would' 'my' 'see' 'really' 'story'
#        'which' 'well' 'had' 'me' 'than' 'much' 'their' 'get' 'were' 'other'
#        'been' 'do' 'most' 'don' 'her' 'also' 'into' 'first' 'made' 'how' 'great'
#        'because' 'will' 'people' 'make' 'way' 'could' 'we' 'bad' 'after' 'any'
#        'too' 'then' 'them' 'she' 'watch' 'think' 'acting' 'movies' 'seen' 'its'
#        'him']
# As expected, these are mostly English stopwords like "the" and "no". But some are
# clearly domain-specific to the movie reviews, like "movie", "film", "time", "story",
# and so on. Interestingly, "good", "great", and "bad" are also among the most fre‐
# quent and therefore “least relevant” words according to the tf–idf measure, even
# though we might expect these to be very important for our sentiment analysis task.
# 
# Investigating Model Coefficients
# Finally, let’s look in a bit more detail into what our logistic regression model actually
# learned from the data. Because there are so many features—27,271 after removing the
# infrequent ones—we clearly cannot look at all of the coefficients at the same time.
# However, we can look at the largest coefficients, and see which words these corre‐
# spond to. We will use the last model that we trained, based on the tf–idf features.
# The following bar chart (Figure 7-2) shows the 25 largest and 25 smallest coefficients
# of the logistic regression model, with the bars showing the size of each coefficient:
# 
# 
# 338   |   Chapter 7: Working with Text Data
# 
# In[26]:
#     mglearn.tools.visualize_coefficients(
#         grid.best_estimator_.named_steps["logisticregression"].coef_,
#         feature_names, n_top_features=40)
# 
# 
# 
# 
# Figure 7-2. Largest and smallest coefficients of logistic regression trained on tf-idf fea‐
# tures
# 
# The negative coefficients on the left belong to words that according to the model are
# indicative of negative reviews, while the positive coefficients on the right belong to
# words that according to the model indicate positive reviews. Most of the terms are
# quite intuitive, like "worst", "waste", "disappointment", and "laughable" indicat‐
# ing bad movie reviews, while "excellent", "wonderful", "enjoyable", and
# "refreshing" indicate positive movie reviews. Some words are slightly less clear, like
# "bit", "job", and "today", but these might be part of phrases like “good job” or “best
# today.”
# 
# Bag-of-Words with More Than One Word (n-Grams)
# One of the main disadvantages of using a bag-of-words representation is that word
# order is completely discarded. Therefore, the two strings “it’s bad, not good at all” and
# “it’s good, not bad at all” have exactly the same representation, even though the mean‐
# ings are inverted. Putting “not” in front of a word is only one example (if an extreme
# one) of how context matters. Fortunately, there is a way of capturing context when
# using a bag-of-words representation, by not only considering the counts of single
# tokens, but also the counts of pairs or triplets of tokens that appear next to each other.
# Pairs of tokens are known as bigrams, triplets of tokens are known as trigrams, and
# more generally sequences of tokens are known as n-grams. We can change the range
# of tokens that are considered as features by changing the ngram_range parameter of
# CountVectorizer or TfidfVectorizer. The ngram_range parameter is a tuple, con‐
# 
# 
# 
# 
#                                                Bag-of-Words with More Than One Word (n-Grams)   |   339
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Investigating Model Coefficients",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class InvestigatingModel(HierNode):
    def __init__(self):
        super().__init__("Investigating Model Coefficients")
        self.add(Content(), "content")

# eof
