# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                    Chapter 5   Google Compute Engine (GCE)
# 
# 
# 
# 
# Figure 5-6. Allow network traffic to VM
# 
#       6. Click ‘Create’ in Figure 5-6 to deploy the VM instance.
# 
# 
# 
# Connecting to the VM Instance
# In the VM instances page that lists the created VMs, click ‘SSH’ beside the created
# instance as shown in Figure 5-7. This launches a new window with terminal access to the
# created VM as shown in Figures 5-8 and 5-9.
# 
# 
# 
# 
#                                                                                        41
# 
# Chapter 5   Google Compute Engine (GCE)
# 
# 
# 
# 
# Figure 5-7. SSH into VM instances
# 
# 
# 
# 
# 42
# 
#                                             Chapter 5   Google Compute Engine (GCE)
# 
# 
# 
# 
# Figure 5-8. Connecting to VM instances via SSH
# 
# 
# 
# 
#                                                                                 43
# 
# Chapter 5   Google Compute Engine (GCE)
# 
# 
# 
# 
# Figure 5-9. Terminal window access to the instance
# 
# Tearing Down the Instance
# It is good practice to delete compute instances that are no longer in use to save cost for
# utilizing GCP resources. To delete a compute instance, on the ‘VM instances’ page, select
# the instance for deletion and click ‘DELETE’ (in red) as shown in Figure 5-10.
# 
# 
# 
# 
# 44
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Connecting to the VM Instance")
        self.add(MarkdownBlock("# Connecting to the VM Instance"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Connectingto(HierNode):
    def __init__(self):
        super().__init__("Connecting to the VM Instance")
        self.add(Content())

# eof
