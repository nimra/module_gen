# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reinforcement Learning
# Reinforcement learning presents an approach to learning that is quite different from
# what we have seen so far in supervised and unsupervised machine learning techniques.
# In reinforcement learning, an agent interacts with an environment in a feedback
# configuration and updates its strategy for choosing an action based on the responses it
# gets from the environment. An illustration of this scenario is shown in Figure 14-18.
# 
# 
# 
# 
# Figure 14-18. Reinforcement learning model
# 
#     This book will not cover reinforcement learning techniques as it presents a different
# approach to the problem of learning from random environments that is distinct from the
# approach used in supervised and unsupervised learning problems.
#     In this chapter, we covered the three main components of machine learning, which
# are supervised, unsupervised, and reinforcement learning. The chapter largely focused
# on the principles for performing supervised machine learning such as framing a
# problem as a regression or classification task; splitting the dataset into training, test, and
# validation sets; understanding the bias/variance trade-off and consequently issues of
# overfitting and underfitting; and the evaluation metrics for assessing the performance of
# a learning model.
#     In the next chapter, we will briefly look at the differences between batch and online
# learning.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Reinforcement Learning",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Reinforcement Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ReinforcementLearning(HierNode):
    def __init__(self):
        super().__init__("Reinforcement Learning")
        self.add(Content())

# eof
