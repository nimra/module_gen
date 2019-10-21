# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# Chapter 45   Containers and Google Kubernetes Engine
# 
# 
# 
# 
# Figure 45-3. Virtual machines
# 
#     Containers on the other hand isolate the environment for hosting an application
# with its own libraries and software dependencies; however, as opposed to a VM,
# containers on a machine all share the same operating system kernel. Docker is an
# example of a container. This is illustrated in Figure 45-4.
# 
# 
# 
# 
# 658
# 
#                                       Chapter 45    Containers and Google Kubernetes Engine
# 
# 
# 
# 
# Figure 45-4. Containers
# 
# W
#  orking with Docker
# Google Cloud Shell comes pre-configured with Docker.
#    Key concepts to note are
# 
#       •   Dockerfile: A Dockerfile is a text file that specifies how an image will
#           be created.
# 
#       •   Docker images: Images are created by building a Dockerfile.
# 
#       •   Docker containers: Docker containers are the running instance of an
#           image.
#    The diagram in Figure 45-5 highlights the process to build an image and run a
# Docker container.
# 
# 
# 
# 
#                                                                                        659
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Virtual Machines vs. Containers",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Virtual Machines vs. Containers"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class VirtualMachines(HierNode):
    def __init__(self):
        super().__init__("Virtual Machines vs. Containers")
        self.add(Content())

# eof
