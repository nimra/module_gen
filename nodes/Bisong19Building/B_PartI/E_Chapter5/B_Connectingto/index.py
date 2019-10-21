# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Connecting to the VM Instance
# In the VM instances page that lists the created VMs, click ‘SSH’ beside the created
# instance as shown in Figure 5-7. This launches a new window with terminal access to the
# created VM as shown in Figures 5-8 and 5-9.
# 
# 
# 
# 
# 
# Figure 5-7. SSH into VM instances
# 
# 
# 
# 
# 
# Figure 5-8. Connecting to VM instances via SSH
# 
# 
# 
# 
# 
# Figure 5-9. Terminal window access to the instance

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Connecting to the VM Instance",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Connecting to the VM Instance"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Connectingto(HierNode):
    def __init__(self):
        super().__init__("Connecting to the VM Instance")
        self.add(Content())

# eof
