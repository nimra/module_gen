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
# Benefits of Cross-Validation
# There are several benefits to using cross-validation instead of a single split into a
# training and a test set. First, remember that train_test_split performs a random
# split of the data. Imagine that we are “lucky” when randomly splitting the data, and
# all examples that are hard to classify end up in the training set. In that case, the test
# set will only contain “easy” examples, and our test set accuracy will be unrealistically
# high. Conversely, if we are “unlucky,” we might have randomly put all the hard-to-
# classify examples in the test set and consequently obtain an unrealistically low score.
# However, when using cross-validation, each example will be in the training set exactly
# once: each example is in one of the folds, and each fold is the test set once. Therefore,
# the model needs to generalize well to all of the samples in the dataset for all of the
# cross-validation scores (and their mean) to be high.
# Having multiple splits of the data also provides some information about how sensi‐
# tive our model is to the selection of the training dataset. For the iris dataset, we saw
# accuracies between 90% and 100%. This is quite a range, and it provides us with an
# idea about how the model might perform in the worst case and best case scenarios
# when applied to new data.
# Another benefit of cross-validation as compared to using a single split of the data is
# that we use our data more effectively. When using train_test_split, we usually use
# 75% of the data for training and 25% of the data for evaluation. When using five-fold
# cross-validation, in each iteration we can use four-fifths of the data (80%) to fit the
# model. When using 10-fold cross-validation, we can use nine-tenths of the data
# (90%) to fit the model. More data will usually result in more accurate models.
# The main disadvantage of cross-validation is increased computational cost. As we are
# now training k models instead of a single model, cross-validation will be roughly k
# times slower than doing a single split of the data.
# 
#                     It is important to keep in mind that cross-validation is not a way to
#                     build a model that can be applied to new data. Cross-validation
#                     does not return a model. When calling cross_val_score, multiple
#                     models are built internally, but the purpose of cross-validation is
#                     only to evaluate how well a given algorithm will generalize when
#                     trained on a specific dataset.
# 
# 
# Stratified k-Fold Cross-Validation and Other Strategies
# Splitting the dataset into k folds by starting with the first one-k-th part of the data, as
# described in the previous section, might not always be a good idea. For example, let’s
# have a look at the iris dataset:
# 
# 
# 
# 
# 254   |   Chapter 5: Model Evaluation and Improvement
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Benefits of Cross-Validation",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Benefitsof(HierNode):
    def __init__(self):
        super().__init__("Benefits of Cross-Validation")
        self.add(Content(), "content")

# eof
