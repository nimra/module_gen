# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Free Up Storage Resource
# To delete a bucket or free up a storage resource to prevent billing on a resource that is not
# used, click the checkbox beside the bucket in question, and click ‘DELETE’ to remove
# the bucket and its contents. This action is not recoverable. See Figures 4-7 and 4-8.
# 
# 
# 
# 
# 
# Figure 4-7. Select bucket to delete
# 
# 
# 
# 
# Figure 4-8. Delete bucket

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Free Up Storage Resource",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Free Up Storage Resource"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FreeUp(HierNode):
    def __init__(self):
        super().__init__("Free Up Storage Resource")
        self.add(Content())

# eof
