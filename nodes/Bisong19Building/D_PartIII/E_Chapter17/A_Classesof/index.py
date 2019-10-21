# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Classes of Supervised Algorithms
# Supervised machine learning algorithms are broadly classified into
#        •    Linear
# 
#        •    Non-linear
#        •    Ensemble methods
# 
#       Let’s briefly go through them:
# 
#         •   Linear methods are also known as parametric methods or
#             algorithms. Linear methods assume that the underlying structure
#             of the data is linear, put in another form, that there exists a linear
#             interaction between the features of the dataset. Examples of linear
#             algorithms are
# 
#             •    Linear regression
#             •    Logistic regression
# 
#             •    Support vector machines
# 
#         •   Non-linear methods (also known as non-parametric methods) do
#             not assume any parametric or structural form of the dataset. Instead,
#             they attempt to learn the internal relationships or representation
#             between the features of the dataset. Examples of non-linear
#             algorithms are
# 
#             •    K-nearest neighbors
# 
#             •    Classification and regression trees (they form the foundation for
#                  ensemble methods such as boosting and bagging)
# 
#             •    Support vector machines
# 
#             •    Neural networks
# 
#         •   Ensemble methods combine the output of multiple algorithms to
#             build a better model estimator that generalizes to unseen examples.
#             Two major classes of ensemble methods are
# 
#             •    Boosting (stochastic gradient boosting)
# 
#             •    Bagging (Random forests)
# 
#     As we can see from the preceding list, some algorithms can function as both a linear
# and non-linear model. An example is support vector machine (SVM) which applies the so-
# called kernel trick to use it as a non-linear classification algorithm (more on this later).
#     Supervised machine learning algorithms can also be grouped as regression or
# classification algorithms. As we saw in Chapter 14 on regression vs. classification,
# regression is when the target variable is real-valued and classification is when the target
# variable is class labels.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Classes of Supervised Algorithms",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Classes of Supervised Algorithms"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Classesof(HierNode):
    def __init__(self):
        super().__init__("Classes of Supervised Algorithms")
        self.add(Content())

# eof
