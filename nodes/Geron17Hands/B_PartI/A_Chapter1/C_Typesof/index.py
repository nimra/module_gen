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

from .A_SupervisedUnsupervisedLearning.index import SupervisedUnsupervisedLearning as A_SupervisedUnsupervisedLearning
from .B_Batchand.index import Batchand as B_Batchand
from .C_InstanceBasedVersus.index import InstanceBasedVersus as C_InstanceBasedVersus

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
blocks = [
#                  Download from finelybook www.finelybook.com
# 
# 
# 
# 
# Figure 1-4. Machine Learning can help humans learn
# 
# To summarize, Machine Learning is great for:
# 
#   • Problems for which existing solutions require a lot of hand-tuning or long lists of
#     rules: one Machine Learning algorithm can often simplify code and perform bet‐
#     ter.
#   • Complex problems for which there is no good solution at all using a traditional
#     approach: the best Machine Learning techniques can find a solution.
#   • Fluctuating environments: a Machine Learning system can adapt to new data.
#   • Getting insights about complex problems and large amounts of data.
# 
# 
# Types of Machine Learning Systems
# There are so many different types of Machine Learning systems that it is useful to
# classify them in broad categories based on:
# 
#   • Whether or not they are trained with human supervision (supervised, unsuper‐
#     vised, semisupervised, and Reinforcement Learning)
#   • Whether or not they can learn incrementally on the fly (online versus batch
#     learning)
#   • Whether they work by simply comparing new data points to known data points,
#     or instead detect patterns in the training data and build a predictive model, much
#     like scientists do (instance-based versus model-based learning)
# 
# These criteria are not exclusive; you can combine them in any way you like. For
# example, a state-of-the-art spam filter may learn on the fly using a deep neural net‐
# 
# 
# 
#                                                         Types of Machine Learning Systems   |   7
# 
#                  Download from finelybook www.finelybook.com
# work model trained using examples of spam and ham; this makes it an online, model-
# based, supervised learning system.
# Let’s look at each of these criteria a bit more closely.
# 
# Supervised/Unsupervised Learning
# Machine Learning systems can be classified according to the amount and type of
# supervision they get during training. There are four major categories: supervised
# learning, unsupervised learning, semisupervised learning, and Reinforcement Learn‐
# ing.
# 
# Supervised learning
# In supervised learning, the training data you feed to the algorithm includes the desired
# solutions, called labels (Figure 1-5).
# 
# 
# 
# 
# Figure 1-5. A labeled training set for supervised learning (e.g., spam classification)
# 
# A typical supervised learning task is classification. The spam filter is a good example
# of this: it is trained with many example emails along with their class (spam or ham),
# and it must learn how to classify new emails.
# Another typical task is to predict a target numeric value, such as the price of a car,
# given a set of features (mileage, age, brand, etc.) called predictors. This sort of task is
# called regression (Figure 1-6).1 To train the system, you need to give it many examples
# of cars, including both their predictors and their labels (i.e., their prices).
# 
# 
# 
# 
# 1 Fun fact: this odd-sounding name is a statistics term introduced by Francis Galton while he was studying the
#     fact that the children of tall people tend to be shorter than their parents. Since children were shorter, he called
#     this regression to the mean. This name was then applied to the methods he used to analyze correlations
#     between variables.
# 
# 
# 
# 8    |   Chapter 1: The Machine Learning Landscape
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Types of Machine Learning Systems",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Typesof(HierNode):
    def __init__(self):
        super().__init__("Types of Machine Learning Systems")
        self.add(Content(), "content")
        self.add(A_SupervisedUnsupervisedLearning())
        self.add(B_Batchand())
        self.add(C_InstanceBasedVersus())

# eof
