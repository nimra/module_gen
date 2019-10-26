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
#                   Download from finelybook www.finelybook.com
# default hyperparameter values (which was 52,634). Congratulations, you have suc‐
# cessfully fine-tuned your best model!
# 
#                       Don’t forget that you can treat some of the data preparation steps as
#                       hyperparameters. For example, the grid search will automatically
#                       find out whether or not to add a feature you were not sure about
#                       (e.g., using the add_bedrooms_per_room hyperparameter of your
#                       CombinedAttributesAdder transformer). It may similarly be used
#                       to automatically find the best way to handle outliers, missing fea‐
#                       tures, feature selection, and more.
# 
# 
# Randomized Search
# The grid search approach is fine when you are exploring relatively few combinations,
# like in the previous example, but when the hyperparameter search space is large, it is
# often preferable to use RandomizedSearchCV instead. This class can be used in much
# the same way as the GridSearchCV class, but instead of trying out all possible combi‐
# nations, it evaluates a given number of random combinations by selecting a random
# value for each hyperparameter at every iteration. This approach has two main bene‐
# fits:
# 
#      • If you let the randomized search run for, say, 1,000 iterations, this approach will
#        explore 1,000 different values for each hyperparameter (instead of just a few val‐
#        ues per hyperparameter with the grid search approach).
#      • You have more control over the computing budget you want to allocate to hyper‐
#        parameter search, simply by setting the number of iterations.
# 
# 
# Ensemble Methods
# Another way to fine-tune your system is to try to combine the models that perform
# best. The group (or “ensemble”) will often perform better than the best individual
# model (just like Random Forests perform better than the individual Decision Trees
# they rely on), especially if the individual models make very different types of errors.
# We will cover this topic in more detail in Chapter 7.
# 
# Analyze the Best Models and Their Errors
# You will often gain good insights on the problem by inspecting the best models. For
# example, the RandomForestRegressor can indicate the relative importance of each
# attribute for making accurate predictions:
#        >>> feature_importances = grid_search.best_estimator_.feature_importances_
#        >>> feature_importances
#        array([ 7.14156423e-02,    6.76139189e-02,   4.44260894e-02,
# 
# 
# 74    |   Chapter 2: End-to-End Machine Learning Project
# 
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Randomized Search",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        [self.add(a) for a in blocks]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RandomizedSearch(HierNode):
    def __init__(self):
        super().__init__("Randomized Search")
        self.add(Content(), "content")

# eof
