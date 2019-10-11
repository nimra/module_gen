# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 6
# 
# 
# 
# JupyterLab Notebooks
# Google deep learning virtual machines (VMs) are a part of GCP AI Platform. It provisions
# a Compute Engine instance that comes pre-configured with the relevant software
# packages for carrying out analytics and modeling tasks. It also makes available high-­
# performance computing TPU and GPU processing capabilities at a single click. These
# VMs expose a JupyterLab notebook environment for analyzing data and designing
# machine learning models.
#     In this chapter, we’ll launch a JupyterLab notebook instance using the web-based
# console and the command line.
# 
# 
# 
# Provisioning a Notebook Instance
# The following steps provide a walk-through for deploying a Notebook instance on a deep
# learning VM:
# 
#        1. In the group named ‘ARTIFICIAL INTELLIGENCE’ on the GCP
#           resources drawer, click the arrow beside ‘AI Platform’ and select
#           ‘Notebooks’ as shown in Figure 6-1.
# 
# 
# 
# 
#                                                                                           49
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_6
# 
# Chapter 6   JupyterLab Notebooks
# 
# 
# 
# 
# Figure 6-1. Open Notebooks on GCP AI Platform
# 
#       2. Click ‘NEW INSTANCE’ to initiate a notebook instance as shown
#          in Figure 6-2; there is an option to customize your instance or
#          to use one of the pre-configured instances with TensorFlow,
#          PyTorch, or RAPIDS XGBoost installed.
# 
# 
# 
# 
# Figure 6-2. Start a new Notebook instance
# 50
# 
#                                                       Chapter 6     JupyterLab Notebooks
# 
#      3. For this example, we will create a Notebook instance pre-
#         configured with TensorFlow 2.0 (see Figure 6-3).
# 
# 
# 
# 
# Figure 6-3. Start a new Notebook instance
# 
#      4. Click ‘OPEN JUPYTERLAB’ to launch the JupyterLab notebook
#         instance in a new window (see Figure 6-4).
# 
# 
# 
# 
# Figure 6-4. Open JupyterLab
#                                                                                      51
# 
# Chapter 6   JupyterLab Notebooks
# 
#       5. From the JupyterLab Launcher in Figure 6-5, options exist to open
#          a Python notebook, a Python interactive shell, a bash terminal,
#          a text file, or a Tensorboard dashboard (more on Tensorboard in
#          Part 6).
# 
# 
# 
# 
# Figure 6-5. JupyterLab Launcher
# 
#       6. Open a Python 3 Notebook (see Figure 6-6). We’ll work with
#          Python notebooks in later chapters to carry out data science tasks.
# 
# 
# 
# 
# 52
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Provisioning a Notebook Instance")
        self.add(MarkdownBlock("# Provisioning a Notebook Instance"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Provisioninga(HierNode):
    def __init__(self):
        super().__init__("Provisioning a Notebook Instance")
        self.add(Content())

# eof
