# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                       Chapter 6   JupyterLab Notebooks
# 
# 
# 
# 
# Figure 6-6. Python 3 Notebook
# 
# 
# Shut Down/Delete a Notebook Instance
# The following steps provide a walk-through for shutting down and deleting a Notebook
# instance:
# 
#      1. From the ‘Notebook instances’ dashboard, click ‘STOP’ to shut
#         down the instance when not in use so as to save compute costs on
#         GCP (see Figure 6-7).
# 
# 
# 
# 
# Figure 6-7. Stop Notebook instance
# 
# 
#                                                                                    53
# 
# Chapter 6   JupyterLab Notebooks
# 
#       2. When the instance is no longer needed, click ‘DELETE’ to
#          permanently remove the instance. Note that this option is non-
#          recoverable (see Figure 6-8).
# 
# 
# 
# 
# Figure 6-8. Delete a Notebook instance
# 
# 
#  tarting a Notebook Instance from the Command
# S
# Line
# In this section, we’ll examine how the command line is used to launch and shut down a
# pre-configured deep learning VM integrated with JupyterLab.
#     Create a Datalab instance: To create a Notebook instance, execute the code
# 
# export IMAGE_FAMILY="tf-latest-cpu-experimental"
# export ZONE="us-west1-b"
# export INSTANCE_NAME="my-instance"
# 
# 
# 
# 
# 54
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Shut Down/Delete a Notebook Instance")
        self.add(MarkdownBlock("# Shut Down/Delete a Notebook Instance"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ShutDownDelete(HierNode):
    def __init__(self):
        super().__init__("Shut Down/Delete a Notebook Instance")
        self.add(Content())

# eof
