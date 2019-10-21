# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Provisioninga.index import Provisioninga as A_Provisioninga
from .B_ShutDownDelete.index import ShutDownDelete as B_ShutDownDelete
from .C_Startinga.index import Startinga as C_Startinga

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 6: JupyterLab Notebooks",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 6: JupyterLab Notebooks"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter6(HierNode):
    def __init__(self):
        super().__init__("Chapter 6: JupyterLab Notebooks")
        self.add(Content())
        self.add(A_Provisioninga())
        self.add(B_ShutDownDelete())
        self.add(C_Startinga())

# eof
