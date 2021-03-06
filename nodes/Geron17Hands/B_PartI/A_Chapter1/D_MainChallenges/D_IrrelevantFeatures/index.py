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
#                  Download from finelybook www.finelybook.com
#   Instead, Roosevelt won with 62% of the votes. The flaw was in the Literary Digest’s
#   sampling method:
# 
#     • First, to obtain the addresses to send the polls to, the Literary Digest used tele‐
#       phone directories, lists of magazine subscribers, club membership lists, and the
#       like. All of these lists tend to favor wealthier people, who are more likely to vote
#       Republican (hence Landon).
#     • Second, less than 25% of the people who received the poll answered. Again, this
#       introduces a sampling bias, by ruling out people who don’t care much about poli‐
#       tics, people who don’t like the Literary Digest, and other key groups. This is a spe‐
#       cial type of sampling bias called nonresponse bias.
# 
#   Here is another example: say you want to build a system to recognize funk music vid‐
#   eos. One way to build your training set is to search “funk music” on YouTube and use
#   the resulting videos. But this assumes that YouTube’s search engine returns a set of
#   videos that are representative of all the funk music videos on YouTube. In reality, the
#   search results are likely to be biased toward popular artists (and if you live in Brazil
#   you will get a lot of “funk carioca” videos, which sound nothing like James Brown).
#   On the other hand, how else can you get a large training set?
# 
# 
# Poor-Quality Data
# Obviously, if your training data is full of errors, outliers, and noise (e.g., due to poor-
# quality measurements), it will make it harder for the system to detect the underlying
# patterns, so your system is less likely to perform well. It is often well worth the effort
# to spend time cleaning up your training data. The truth is, most data scientists spend
# a significant part of their time doing just that. For example:
# 
#   • If some instances are clearly outliers, it may help to simply discard them or try to
#     fix the errors manually.
#   • If some instances are missing a few features (e.g., 5% of your customers did not
#     specify their age), you must decide whether you want to ignore this attribute alto‐
#     gether, ignore these instances, fill in the missing values (e.g., with the median
#     age), or train one model with the feature and one model without it, and so on.
# 
# 
# Irrelevant Features
# As the saying goes: garbage in, garbage out. Your system will only be capable of learn‐
# ing if the training data contains enough relevant features and not too many irrelevant
# ones. A critical part of the success of a Machine Learning project is coming up with a
# good set of features to train on. This process, called feature engineering, involves:
# 
# 
# 
#                                                          Main Challenges of Machine Learning   |   25
# 
#                     Download from finelybook www.finelybook.com
#      • Feature selection: selecting the most useful features to train on among existing
#        features.
#      • Feature extraction: combining existing features to produce a more useful one (as
#        we saw earlier, dimensionality reduction algorithms can help).
#      • Creating new features by gathering new data.
# 
# Now that we have looked at many examples of bad data, let’s look at a couple of exam‐
# ples of bad algorithms.
# 
# Overfitting the Training Data
# Say you are visiting a foreign country and the taxi driver rips you off. You might be
# tempted to say that all taxi drivers in that country are thieves. Overgeneralizing is
# something that we humans do all too often, and unfortunately machines can fall into
# the same trap if we are not careful. In Machine Learning this is called overfitting: it
# means that the model performs well on the training data, but it does not generalize
# well.
# Figure 1-22 shows an example of a high-degree polynomial life satisfaction model
# that strongly overfits the training data. Even though it performs much better on the
# training data than the simple linear model, would you really trust its predictions?
# 
# 
# 
# 
# Figure 1-22. Overfitting the training data
# 
# Complex models such as deep neural networks can detect subtle patterns in the data,
# but if the training set is noisy, or if it is too small (which introduces sampling noise),
# then the model is likely to detect patterns in the noise itself. Obviously these patterns
# will not generalize to new instances. For example, say you feed your life satisfaction
# model many more attributes, including uninformative ones such as the country’s
# name. In that case, a complex model may detect patterns like the fact that all coun‐
# tries in the training data with a w in their name have a life satisfaction greater than 7:
# New Zealand (7.3), Norway (7.4), Sweden (7.2), and Switzerland (7.5). How confident
# 
# 
# 26    |   Chapter 1: The Machine Learning Landscape
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Irrelevant Features",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class IrrelevantFeatures(HierNode):
    def __init__(self):
        super().__init__("Irrelevant Features")
        self.add(Content(), "content")

# eof
