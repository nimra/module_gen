# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The Cloud Shell
# The Cloud Shell is a vital component for working with GCP resources. Cloud Shell
# provisions an ephemeral virtual machine with command-line tools installed for
# interacting with GCP resources. It gives the user cloud-based command-line access to
# manipulate resources directly from within the GCP perimeter without installing the
# Google Cloud SDK on a local machine.
#     The Cloud Shell is accessed by clicking the prompt icon in the top-left corner of the
# window. See Figures 3-9, 3-10, and 3-11.
# 
# 
# 
# 
# Figure 3-9. Activate Cloud Shell
# 
# 
# 
# 
# Figure 3-10. Start Cloud Shell
# 
# 
# 
# 
# Figure 3-11. Cloud Shell interface

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Cloud Shell",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# The Cloud Shell"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheCloud(HierNode):
    def __init__(self):
        super().__init__("The Cloud Shell")
        self.add(Content())

# eof
