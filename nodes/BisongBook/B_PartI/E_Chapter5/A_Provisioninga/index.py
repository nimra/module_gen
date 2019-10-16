# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Provisioning a VM Instance
# To deploy a VM instance, click the triple dash in the top-left corner of the web page to
# pull out the GCP resources drawer. In the group named ‘COMPUTE’, click the arrow
# beside ‘Compute Engine’ and select ‘VM instances’ as shown in Figure 5-1.
# 
# 
# 
# 
# Figure 5-1. Select VM instances
# 
#      Click ‘Create’ to begin the process of deploying a VM instance (see Figure 5-2).
# 
# 
# 
# 
# 
# Figure 5-2. Begin process of deploying a VM instance
# 
# 
# 
# 
# 
# 
# 
# Figure 5-3. Options for creating an instance
# 
#      The labeled numbers in Figure 5-3 are explained here:
# 
#        1. Choose the instance name. This name must start with a lowercase
#           letter and can include numbers or hyphens, but should not end
#           with a hyphen.
# 
#        2. Select the instance region and zone. This is the geographical
#           region where your computing instance is located, while the zone
#           is a location within a region.
# 
#        3. Select the machine type. This allows for customization of the
#           cores, memory, and GPUs for the VM (see Figure 5-4).
# 
# 
# 
# 
# 
# Figure 5-4. Select machine type
# 
#      4. Select the boot disk. This option selects a disk to boot from. This
#         disk could be created from an OS image, an application image, a
#         custom image, or a snapshot of an image (see Figure 5-5).
# 
# 
# 
# 
# 
# Figure 5-5. Select boot disk
# 
#       5. Select ‘Allow HTTP traffic’ to allow network traffic from the
#          Internet as shown in Figure 5-6.
# 
# 
# 
# 
# 
# Figure 5-6. Allow network traffic to VM
# 
#       6. Click ‘Create’ in Figure 5-6 to deploy the VM instance.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Provisioning a VM Instance",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Provisioning a VM Instance"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Provisioninga(HierNode):
    def __init__(self):
        super().__init__("Provisioning a VM Instance")
        self.add(Content())

# eof
