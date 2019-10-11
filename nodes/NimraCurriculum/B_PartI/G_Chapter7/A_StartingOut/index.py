# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# Chapter 7   Google Colaboratory
# 
# 
# 
# 
# Figure 7-1. Google Colab homepage
# 
#       2. Open a Python 3 Notebook (see Figure 7-2).
# 
# 
# 
# 
# Figure 7-2. Python 3 Notebook
# 
# 
# 60
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Starting Out with Colab")
        self.add(MarkdownBlock("# Starting Out with Colab"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class StartingOut(HierNode):
    def __init__(self):
        super().__init__("Starting Out with Colab")
        self.add(Content())

# eof
