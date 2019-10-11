# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                        Chapter 7   Google Colaboratory
# 
# 
# Change Runtime Settings
# The following steps provide a walk-through for changing the Notebook runtime settings:
# 
#      1. Go to Runtime ➤ Change runtime type (see Figure 7-3).
# 
# 
# 
# 
# Figure 7-3. Python 3 Notebook
# 
# 
# 
# 
#                                                                                     61
# 
# Chapter 7   Google Colaboratory
# 
#       2. Here, the options exist to change the Python runtime and
#          hardware accelerator to a GPU or TPU (see Figure 7-4).
# 
# 
# 
# 
# Figure 7-4. Change runtime
# 
# 
# S
#  toring Notebooks
# Notebooks on Colab are stored on Google Drive. They can also be saved to GitHub or
# published as a GitHub Gist. They can also be downloaded to the local machine.
#    Figure 7-5 highlights the options for storing Jupyter notebooks running on Google
# Colab.
# 
# 
# 
# 
# 62
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Change Runtime Settings")
        self.add(MarkdownBlock("# Change Runtime Settings"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ChangeRuntime(HierNode):
    def __init__(self):
        super().__init__("Change Runtime Settings")
        self.add(Content())

# eof
