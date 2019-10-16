# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Batch Learning
# In batch learning the machine learning model is trained using the entire dataset that
# is available at a certain point in time. Once we have a model that performs well on the
# test set, the model is shipped for production and thus learning ends. This process is also
# called offline learning. If in the process of time, new data becomes available, and there is
# need to update the model based on the new data, the model is trained from scratch all
# over again using both the previous data samples and the new data samples.
#      This pipeline is further illustrated in Figure 15-1.
# 
# 
# 
# 
# Figure 15-1. Batch learning
# 
#     In a situation where there is a need to train the model with data that is generated
# continuously from the source, batch learning becomes inappropriate to deal with that
# situation. In such a circumstance, we want to be able to update our learning model on
# the go, based on the new data samples that are available.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Batch Learning",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Batch Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BatchLearning(HierNode):
    def __init__(self):
        super().__init__("Batch Learning")
        self.add(Content())

# eof
