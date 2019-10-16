# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                          Download from finelybook www.finelybook.com
# Nonrepresentative Training Data
# In order to generalize well, it is crucial that your training data be representative of the
# new cases you want to generalize to. This is true whether you use instance-based
# learning or model-based learning.
# For example, the set of countries we used earlier for training the linear model was not
# perfectly representative; a few countries were missing. Figure 1-21 shows what the
# data looks like when you add the missing countries.
# 
# 
# 
# 
# Figure 1-21. A more representative training sample
# 
# If you train a linear model on this data, you get the solid line, while the old model is
# represented by the dotted line. As you can see, not only does adding a few missing
# countries significantly alter the model, but it makes it clear that such a simple linear
# model is probably never going to work well. It seems that very rich countries are not
# happier than moderately rich countries (in fact they seem unhappier), and conversely
# some poor countries seem happier than many rich countries.
# By using a nonrepresentative training set, we trained a model that is unlikely to make
# accurate predictions, especially for very poor and very rich countries.
# It is crucial to use a training set that is representative of the cases you want to general‐
# ize to. This is often harder than it sounds: if the sample is too small, you will have
# sampling noise (i.e., nonrepresentative data as a result of chance), but even very large
# samples can be nonrepresentative if the sampling method is flawed. This is called
# sampling bias.
# 
# 
#                                A Famous Example of Sampling Bias
#      Perhaps the most famous example of sampling bias happened during the US presi‐
#      dential election in 1936, which pitted Landon against Roosevelt: the Literary Digest
#      conducted a very large poll, sending mail to about 10 million people. It got 2.4 million
#      answers, and predicted with high confidence that Landon would get 57% of the votes.
# 
# 
# 24     |   Chapter 1: The Machine Learning Landscape
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Nonrepresentative Training Data",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Nonrepresentative Training Data"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NonrepresentativeTraining(HierNode):
    def __init__(self):
        super().__init__("Nonrepresentative Training Data")
        self.add(Content())

# eof
