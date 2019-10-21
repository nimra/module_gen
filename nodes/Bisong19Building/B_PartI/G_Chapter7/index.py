# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_StartingOut.index import StartingOut as A_StartingOut
from .B_ChangeRuntime.index import ChangeRuntime as B_ChangeRuntime
from .C_StoringNotebooks.index import StoringNotebooks as C_StoringNotebooks
from .D_UploadingNotebooks.index import UploadingNotebooks as D_UploadingNotebooks

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 7: Google Colaboratory",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 7: Google Colaboratory"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter7(HierNode):
    def __init__(self):
        super().__init__("Chapter 7: Google Colaboratory")
        self.add(Content())
        self.add(A_StartingOut())
        self.add(B_ChangeRuntime())
        self.add(C_StoringNotebooks())
        self.add(D_UploadingNotebooks())

# eof
