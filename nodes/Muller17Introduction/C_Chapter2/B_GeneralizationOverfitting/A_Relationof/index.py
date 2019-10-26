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
# Figure 2-1. Trade-off of model complexity against training and test accuracy
# 
# Relation of Model Complexity to Dataset Size
# It’s important to note that model complexity is intimately tied to the variation of
# inputs contained in your training dataset: the larger variety of data points your data‐
# set contains, the more complex a model you can use without overfitting. Usually, col‐
# lecting more data points will yield more variety, so larger datasets allow building
# more complex models. However, simply duplicating the same data points or collect‐
# ing very similar data will not help.
# Going back to the boat selling example, if we saw 10,000 more rows of customer data,
# and all of them complied with the rule “If the customer is older than 45, and has less
# than 3 children or is not divorced, then they want to buy a boat,” we would be much
# more likely to believe this to be a good rule than when it was developed using only
# the 12 rows in Table 2-1.
# Having more data and building appropriately more complex models can often work
# wonders for supervised learning tasks. In this book, we will focus on working with
# datasets of fixed sizes. In the real world, you often have the ability to decide how
# much data to collect, which might be more beneficial than tweaking and tuning your
# model. Never underestimate the power of more data.
# 
# Supervised Machine Learning Algorithms
# We will now review the most popular machine learning algorithms and explain how
# they learn from data and how they make predictions. We will also discuss how the
# concept of model complexity plays out for each of these models, and provide an over‐
# 
# 
#                                                     Supervised Machine Learning Algorithms   |   29
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Relation of Model Complexity to Dataset Size",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Relationof(HierNode):
    def __init__(self):
        super().__init__("Relation of Model Complexity to Dataset Size")
        self.add(Content(), "content")

# eof
