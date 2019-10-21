# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Change Runtime Settings
# The following steps provide a walk-through for changing the Notebook runtime settings:
# 
#      1. Go to Runtime ➤ Change runtime type (see Figure 7-3).
# 
# 
# 
# 
# Figure 7-3. Python 3 Notebook
# 
#       2. Here, the options exist to change the Python runtime and
#          hardware accelerator to a GPU or TPU (see Figure 7-4).
# 
# 
# 
# 
# Figure 7-4. Change runtime

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Change Runtime Settings",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Change Runtime Settings"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ChangeRuntime(HierNode):
    def __init__(self):
        super().__init__("Change Runtime Settings")
        self.add(Content())

# eof
