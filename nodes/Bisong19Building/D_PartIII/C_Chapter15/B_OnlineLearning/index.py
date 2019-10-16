# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Online Learning
# In online learning, data streams (either individually or in mini-batches) into the learning
# algorithm and updates the model. Online learning is ideal in situations where data is
# generated continuously in time, and we need to use real-time data samples to build a
# prediction model. A typical example of this case is in stock market prediction.
#     Online learning is illustrated in Figure 15-2.
# 
# 
# 
# 
# 
# Figure 15-2. Online learning
# 
# 
#     This brief chapter explained the contrast between batch learning and online
# learning. In the next chapter, we will focus our attention on a vital optimization
# algorithm for machine learning, gradient descent.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Online Learning",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Online Learning"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OnlineLearning(HierNode):
    def __init__(self):
        super().__init__("Online Learning")
        self.add(Content())

# eof
