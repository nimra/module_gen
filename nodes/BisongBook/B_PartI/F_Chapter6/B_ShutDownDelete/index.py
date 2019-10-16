# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Shut Down/Delete a Notebook Instance
# The following steps provide a walk-through for shutting down and deleting a Notebook
# instance:
# 
#      1. From the ‘Notebook instances’ dashboard, click ‘STOP’ to shut
#         down the instance when not in use so as to save compute costs on
#         GCP (see Figure 6-7).
# 
# 
# 
# 
# Figure 6-7. Stop Notebook instance
# 
#       2. When the instance is no longer needed, click ‘DELETE’ to
#          permanently remove the instance. Note that this option is non-
#          recoverable (see Figure 6-8).
# 
# 
# 
# 
# Figure 6-8. Delete a Notebook instance

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Shut Down/Delete a Notebook Instance",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Shut Down/Delete a Notebook Instance"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ShutDownDelete(HierNode):
    def __init__(self):
        super().__init__("Shut Down/Delete a Notebook Instance")
        self.add(Content())

# eof
