# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#                                                   Chapter 5   Google Compute Engine (GCE)
# 
# 
# 
# 
# Figure 5-10. Delete the VM instance
# 
# Working with GCE from the Command Line
# In this section, we’ll sample the commands for creating and deleting a compute instance
# on GCP using the command-line interface. To create a compute instance using ‘gcloud’
# from the command-line interface, there are a variety of options that can be added to the
# commands for different specifications of the machine. To learn more about a command,
# attach ‘help’ after the command:
# 
#       •   Provisioning a VM instance: To create a VM instance, use the code
#           syntax
# 
#           gcloud compute instances create [INSTANCE_NAME]
# 
#           For example, let’s create an instance named ‘ebisong-howad-instance’
# 
#           gcloud compute instances create ebisong-howad-instance
# 
# 
# 
# 
#                                                                                       45
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Tearing Down the Instance")
        self.add(MarkdownBlock("# Tearing Down the Instance"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TearingDown(HierNode):
    def __init__(self):
        super().__init__("Tearing Down the Instance")
        self.add(Content())

# eof
