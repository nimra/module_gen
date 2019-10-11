# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 45    Containers and Google Kubernetes Engine
# 
#     Microservices interact with each other using representational state transfer (REST)
# communications for stateless interoperability. By stateless, we mean that “the server
# does not store state about the client session.” These protocols can be HTTP request/
# response APIs or an asynchronous messaging queue. This flexibility allows the
# microservice to easily scale and respond to request even if another microservice fails.
#     Advantages of Microservices
# 
#         •   Loosely coupled components make the application fault tolerant.
# 
#         •   Ability to scale out making each component highly available.
# 
#         •   The modularity of components makes it easier to extend existing
#             capabilities.
# 
#       Challenges with Microservices
# 
#         •   The software architecture increases in complexity.
# 
#         •   Overhead in management and orchestration of microservices. We
#             will, however, see in the next sessions how Docker and Kubernetes
#             work to mitigate this challenge.
# 
# 
# 
# D
#  ocker
# Docker is a virtualization application that abstracts applications into isolated
# environments known as containers. The idea behind a container is to provide a
# unified platform that includes the software tools and dependencies for developing and
# deploying an application.
#     The traditional way of developing applications is where an application is designed
# and hosted on a single server. This is illustrated in Figure 45-2. This setup is prone to
# several problems including the famous “it works on my machine but not on yours”. Also
# in this architecture, apps are difficult to scale and to migrate resulting in huge costs and
# slow deployment.
# 
# 
# 
# 
# 656
# 
#                                       Chapter 45   Containers and Google Kubernetes Engine
# 
# 
# 
# 
# Figure 45-2. Application running on a single server
# 
# 
# Virtual Machines vs. Containers
# Virtual machines (VMs), illustrated in Figure 45-3, emulate the capabilities of a physical
# machine making it possible to install and run operating systems by using a hypervisor.
# The hypervisor is a piece of software on the physical machine (the host) that makes it
# possible to carry out virtualization where multiple guest machines are managed by the
# host machine.
# 
# 
# 
# 
#                                                                                        657
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Docker")
        self.add(MarkdownBlock("# Docker"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Docker(HierNode):
    def __init__(self):
        super().__init__("Docker")
        self.add(Content())

# eof
