# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# One-vs.-One (OVO)
# In the one-vs.-one approach, when the number of classes, k, is greater than 2, the
#                                              ækö
# algorithm constructs “k combination 2”, ç ÷ classifiers, where each classifier is for a pair
#                                              è2ø
# of classes. So if we have 10 classes in our dataset, a total of 45 classifiers is constructed or
# trained for every pair of classes. This is illustrated with four classes in Figure 22-8.
#     After training, the classifiers are evaluated by comparing examples from the test set
#                       ækö
# against each of the ç ÷ classifiers. The predicted class is then determined by choosing
#                       è2ø
# the highest number of times an example is assigned to a particular class.
# 
#     The one-vs.-one multi-class technique can potentially lead to a large number of
# constructed classifiers and hence can result in slower processing time. Conversely, the
# classifiers are more robust to class imbalances when training each classifier.
# 
# 
# 
# 
# Figure 22-8. Suppose we have four classes in the dataset labeled A to D, this will
# result in six different classifiers

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "One-vs.-One (OVO)",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# One-vs.-One (OVO)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OnevsOneOVO(HierNode):
    def __init__(self):
        super().__init__("One-vs.-One (OVO)")
        self.add(Content())

# eof
