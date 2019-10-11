# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#                                                        Chapter 6   JupyterLab Notebooks
# 
# gcloud compute instances create $INSTANCE_NAME \
#   --zone=$ZONE \
#   --image-family=$IMAGE_FAMILY \
#   --image-project=deeplearning-platform-release
# 
# where
# 
#       •   --image-family can be any of the available images supported by
#           Google Deep Learning VM; "tf-latest-cpu-experimental"
#           launches an image with TensorFlow 2.0 pre-configured.
# 
#       •   --image-project must be set to deeplearning-platform-release
# 
#    Here’s the output when the instance is created:
# 
# Created ­[https://www.googleapis.com/compute/v1/projects/ekabasandbox/zones/
# us-west1-b/instances/my-instance].
# NAME         ZONE        MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  
# EXTERNAL_IP   STATUS
# my-instance  us-west1-b  n1-standard-1               10.138.0.6  
# 34.83.90.154  RUNNING
# 
#    Connect to the instance: To connect to JupyterLab running on the instance, run the
# command
# 
# export INSTANCE_NAME="my-instance"
# gcloud compute ssh $INSTANCE_NAME -- -L 8080:localhost:8080
# 
#     Then on your local machine, visit http://localhost:8080 in your browser
# (see Figure 6-9).
# 
# 
# 
# 
#                                                                                     55
# 
# Chapter 6   JupyterLab Notebooks
# 
# 
# 
# 
# Figure 6-9. JupyterLab instance launched from terminal
# 
#     Stop the instance: To stop the instance, run the following command from your local
# terminal (not on the instance):
# 
# gcloud compute instances stop $INSTANCE_NAME
# Stopping instance(s) my-instance...done.
# Updated [https://www.googleapis.com/compute/v1/projects/ekabasandbox/zones/
# us-west1-b/instances/my-instance].
# 
#    Delete the instance: The Notebook instance is basically a Google Compute Engine.
# Hence, the instance is deleted the same way a Compute Engine VM is deleted.
# 
# gcloud compute instances delete $INSTANCE_NAME
# The following instances will be deleted. Any attached disks configured
#  to be auto-deleted will be deleted unless they are attached to any
# other instances or the `--keep-disks` flag is given and specifies them
#  for keeping. Deleting a disk is irreversible and any data on the disk
#  will be lost.
#  - [my-instance] in [us-west1-b]
# 
# 
# 
# 56
# 
#                                                        Chapter 6   JupyterLab Notebooks
# 
# Do you want to continue (Y/n)?  Y
# 
# Deleted [https://www.googleapis.com/compute/v1/projects/ekabasandbox/zones/
# us-west1-b/instances/my-instance].
# 
#      This chapter introduces Jupyter notebooks running on Google Deep Learning VMs
# for interactive programming of data science tasks and prototyping deep learning and
# machine learning models.
#      In the next chapter, we will introduce another product for programming and rapid
# prototyping of learning models called Google Colaboratory.
# 
# 
# 
# 
#                                                                                         57
# 
# CHAPTER 7
# 
# 
# 
# Google Colaboratory
# Google Colaboratory more commonly referred to as “Google Colab” or just simply
# “Colab” is a research project for prototyping machine learning models on powerful
# hardware options such as GPUs and TPUs. It provides a serverless Jupyter notebook
# environment for interactive development. Google Colab is free to use like other G Suite
# products.
# 
# 
# 
# Starting Out with Colab
# The following steps provide a walk-through for launching a Notebook on Google Colab:
# 
#        1. Go to https://colab.research.google.com/ and log in using
#           your existing Google account to access the Colab homepage
#           (see Figure 7-1).
# 
# 
# 
# 
#                                                                                           59
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_7
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Starting a Notebook Instance from the Command Line")
        self.add(MarkdownBlock("# Starting a Notebook Instance from the Command Line"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Startinga(HierNode):
    def __init__(self):
        super().__init__("Starting a Notebook Instance from the Command Line")
        self.add(Content())

# eof
