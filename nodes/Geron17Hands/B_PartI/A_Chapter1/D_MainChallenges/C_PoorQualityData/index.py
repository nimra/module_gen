# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
            "Poor-Quality Data",
            # Stage.CROP_TEXT,
            # Stage.CODE_BLOCKS,
            # Stage.MARKDOWN_BLOCKS,
            # Stage.FIGURES,
            # Stage.EXERCISES,
            # Stage.CUSTOMIZED,
        )
        self.add(MarkdownBlock("# Poor-Quality Data"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PoorQualityData(HierNode):
    def __init__(self):
        super().__init__("Poor-Quality Data")
        self.add(Content())

# eof
