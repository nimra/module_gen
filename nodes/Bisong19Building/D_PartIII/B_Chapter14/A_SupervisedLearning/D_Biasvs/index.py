# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Bias vs. Variance Trade-Off
# The concept of bias vs. variance is central to machine learning and is critical to
# understanding how the model is performing, as well as in suggesting the direction in
# which to improve the model.
#     A model is said to have high bias when it oversimplifies the learning problem
# or when the model fails to accurately capture the complex relationships that exist
# between the input features of the dataset. High bias makes the model unable to
# generalize to new examples.
# 
#      High variance, on the other hand, is when the model learns too closely the intricate
# patterns of the dataset input features, and in the process, it learns the irreducible noise
# of the dataset samples. When the learning algorithm learns very closely the patterns
# of the training samples, including the noise, it will fail to generalize when exposed to
# previously unseen data.
#      Hence, we observe that there is a need to strike the right balance between bias and
# variance, and often it is down to the skill of the model builder to discover this middle
# ground. However, there exists practical rules of thumb for finding the right trade-off
# between bias and variance.
# 
#  ow Do We Recognize the Presence of Bias or Variance
# H
# in the Results?
# High bias is observed when the model performs poorly on the trained data. Of course,
# it will also perform poorly (or even worse) on the test data with high prediction errors.
# When high bias occurs, it can be said that the model has underfit the data. High variance
# is observed when the trained model learns the training data very well but performs
# poorly on unseen (test) data. In the event of high variance, we can say that the model has
# overfit the dataset.
#     The graph in Figure 14-5 illustrates the effect of bias and variance on the quality/
# performance of a machine learning model. In Figure 14-6, the reader will observe that
# there is a sweet spot somewhere in the middle where the model has good performances
# on both the training and the test datasets.
# 
# 
# 
# 
# 
# Figure 14-5. Bias and variance
# 
#     To recap, our goal is to have a model that strikes a balance between high bias and
# high variance. Figure 14-6 provides further illustration on the effects of models with high
# bias and variance on a dataset. As seen in the image to the left of Figure 14-6, we want
# to have a model that can generalize to previously unseen example, such a model should
# have good prediction accuracy.
# 
# 
# 
# 
# Figure 14-6. Left: Good fit. Center: Underfit (high bias). Right: Overfit (high
# variance)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Bias vs. Variance Trade-Off",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Bias vs. Variance Trade-Off"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Biasvs(HierNode):
    def __init__(self):
        super().__init__("Bias vs. Variance Trade-Off")
        self.add(Content())

# eof
