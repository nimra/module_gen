# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Uploading Notebooks
# Notebooks can be uploaded from Google Drive, GitHub, or the local machine (see
# Figure 7-6).
# 
# 
# 
# 
# Figure 7-6. Opening Notebooks
# 
#     This chapter introduces Google Colaboratory as an alternative platform to quickly
# spin up a high-performance computing infrastructure running Jupyter notebooks for
# rapid data science and data modeling tasks.
#     This is the last chapter in Part 1 on “Getting Started with Google Cloud Platform.” In
# Part 2, containing Chapters 8–12, we will go over the fundamentals of “Programming for
# Data Science.” The code samples in the ensuing chapters can be executed either using
# Jupyter notebooks running on Google Deep Learning VMs or running on Google Colab.
#     The advantage of working with Google Colab is that you do not need to log into
# the Google Cloud Console and it is free to use. When security and privacy are not a
# premium, Google Colab is a good option for modeling as it saves computing cost as far
# as data science and machine learning prototyping is concerned.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Uploading Notebooks",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Uploading Notebooks"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UploadingNotebooks(HierNode):
    def __init__(self):
        super().__init__("Uploading Notebooks")
        self.add(Content())

# eof
