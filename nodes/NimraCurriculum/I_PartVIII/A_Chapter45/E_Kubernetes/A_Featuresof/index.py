# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                      Chapter 45   Containers and Google Kubernetes Engine
# 
# F eatures of Kubernetes
# The following are some features of Kubernetes:
# 
#       •   Horizontal auto-scaling: Dynamically scales containers based on
#           resource demands
# 
#       •   Self-healing: Re-provisions failed nodes in response to health checks
# 
#       •   Load balancing: Efficiently distributes requests between containers
#           in a pod
# 
#       •   Rollbacks and updates: Easily update or revert to a previous
#           container deployment without causing application downtime
# 
#       •   DNS service discovery: Uses Domain Name System (DNS) to manage
#           container groups as a Kubernetes service
# 
# 
# C
#  omponents of Kubernetes
# The main components of the Kubernetes engine are
# 
#       •   Master node(s): Manages the Kubernetes cluster. There may be more
#           than one master node in high availability mode for fault-tolerance
#           purposes. In this case, only one is the master, and the others follow.
# 
#       •   Worker node(s): Machine(s) that runs containerized applications that
#           are scheduled as pod(s).
# 
#    The illustration in Figure 45-6 provides an overview of the Kubernetes architecture.
# 
# 
# 
# 
#                                                                                      665
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Features of Kubernetes")
        self.add(MarkdownBlock("# Features of Kubernetes"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Featuresof(HierNode):
    def __init__(self):
        super().__init__("Features of Kubernetes")
        self.add(Content())

# eof
