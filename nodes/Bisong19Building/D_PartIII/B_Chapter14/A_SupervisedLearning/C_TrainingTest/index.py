# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Training, Test, and Validation Datasets
# The goal of supervised machine learning is to be able to predict or classify the targets on
# unseen examples correctly. We can misjudge the performance of our learning models if
# we evaluate the model performance with the same samples used to train the model as
# explained previously.
#     To properly evaluate the performance of a learning algorithm, we need to set aside
# some data for testing purposes. This held-out data is called a test set.
#     Another situation arises when we have trained the model on a dataset, and we
# now need to improve the performance of the model by adjusting some of the learning
# algorithm’s parameters.
#     We cannot use the test set for model tuning because if we do that, the model’s
# parameters are trained with the test dataset rendering it unusable as an unseen held-out
# sample for model evaluation. Hence, it is typical to divide the entire dataset into
# 
#       •   The training set (to train the model)
# 
#       •   The validation set (to tune the model)
# 
#       •   The test set (to evaluate the effectiveness of the model)
# 
#    A common and straightforward strategy is to split 60% of the dataset for training,
# 20% for validation, and the final 20% for testing. This strategy is popularly known as the
# 60/20/20 rule. We will discuss more sophisticated methods for resampling (i.e., using
# subsets of available data) for machine learning later in this chapter. See Figure 14-4.
# 
# 
# 
# 
# 
# Figure 14-4. Training, test, and validation set

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Training, Test, and Validation Datasets",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Training, Test, and Validation Datasets"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TrainingTest(HierNode):
    def __init__(self):
        super().__init__("Training, Test, and Validation Datasets")
        self.add(Content())

# eof
