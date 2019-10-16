# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_GridSearch.index import GridSearch as A_GridSearch
from .B_RandomizedSearch.index import RandomizedSearch as B_RandomizedSearch

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Model Tuning
# Each machine learning model has a set of options or configurations that can be tuned
# to optimize the model when fitting to data. These configurations are called hyper-­
# parameters. Hence, for each hyper-parameter, there exist a range of values that can be
# chosen. Taking into consideration the number of hyper-parameters that an algorithm
# has, the entire space can become exponentially large and infeasible to explore all of
# them. Scikit-learn provides two convenient modules for searching through the hyper-­
# parameter space of an algorithm to find the best values for each hyper-parameter that
# optimizes the model.
#     These modules are the
# 
#       •   Grid search
# 
#       •   Randomized search

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Model Tuning",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Model Tuning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ModelTuning(HierNode):
    def __init__(self):
        super().__init__("Model Tuning")
        self.add(Content())
        self.add(A_GridSearch())
        self.add(B_RandomizedSearch())

# eof
