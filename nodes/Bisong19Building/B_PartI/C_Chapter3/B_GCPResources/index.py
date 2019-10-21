# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GCP Resources: Projects
# All the services and features of the Google Cloud Platform are called resources. These
# resources are arranged in a hierarchical order, with the top level being the project.
# The project is like a container that houses all GCP resources. Billing on an account is
# attached to a project. Multiple projects can be created for an account. A project must be
# created before working with GCP.
#    To view the projects in the account in Figure 3-5, click the scope picker in the cloud
# console (marked with an oval in Figure 3-6).
# 
# 
# 
# 
# Figure 3-5. Select projects
# 
# 
# 
# 
# Figure 3-6. Scope picker to select projects

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "GCP Resources: Projects",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# GCP Resources: Projects"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GCPResources(HierNode):
    def __init__(self):
        super().__init__("GCP Resources: Projects")
        self.add(Content())

# eof
