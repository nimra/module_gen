# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Multi-class Classification/Multinomial Logistic Regression
#
# In multi-class or multinomial logistic regression, the labels of the dataset contain more
# than 2 classes. The multinomial logistic regression setup (i.e., the cost function and
# optimization procedure) is structurally similar to logistic regression; the only difference
# is that the output of logistic regression is 2 classes, while multinomial has greater than 2
# classes (see Figure 20-6).
#      In Figure 20-6, the multi-class logistic regression builds a one-vs.-rest classifier to
# construct decision boundaries for the different class memberships.
# 
# 
# 
# 
# Figure 20-6. An illustration of multinomial regression
# 
#      At this point, we introduce a critical function in machine learning called the softmax
# function. The softmax function is used to compute the probability that an instance
# belongs to one of the K classes when K > 2. We will see the softmax function show up
# again when we discuss (artificial) neural networks.
#      In order to build a classification model with k classes, the multinomial logistic model
# is formally defined as
# 
#                                  ŷ ( k ) = q 0k + q1k x1 + q 2k x 2 +¼+ qnk xn
# 
# 
#       The preceding model takes into consideration the parameters for the k different classes.
#       The softmax function is formally written as
# 
#                                                                                yˆ ( k )i
#                                                                            e
#                                      p ( k ) = s ( yˆ ( k ) )i =                  yˆ ( k ) j  ( k j
#                                                                    å
#                                                                        K
#                                                                        j =1
#                                                                            e
# 
# 
#       where
# 
#         •   i = {1, …, K} classes.
# 
#         •   s ( ŷ ( k ) )i outputs the probability estimates that an example in the
#             training dataset belongs to one of the K classes.
# 
#     The cost function for learning the class labels in a multinomial logistic regression
# model is called the cross-entropy cost function. Gradient descent is used to find the
# optimal values of the parameter θ that will minimize the cost function to predict the
# class with the highest probability estimate accurately.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Multi-class Classification/Multinomial Logistic Regression",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Multi-class Classification/Multinomial Logistic Regression"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MulticlassClassificationMultinomial(HierNode):
    def __init__(self):
        super().__init__("Multi-class Classification/Multinomial Logistic Regression")
        self.add(Content())

# eof
