# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_EnableAutoML.index import EnableAutoML as A_EnableAutoML
from .B_Preparingthe.index import Preparingthe as B_Preparingthe
from .C_Buildinga.index import Buildinga as C_Buildinga

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 43
# 
# 
# 
# Google AutoML: Cloud
# Natural Language
# Processing
# This chapter will build a language toxicity classification model to classify and recognize
# toxic and non-toxic or clean phrases using Google Cloud AutoML for natural language
# processing (NLP). The data used in this project is from the Toxic Comment Classification
# Challenge on Kaggle by Jigsaw and Google. The data is modified to have a sample of
# 16,000 toxic and 16,000 non-toxic words as inputs to build the model on AutoML NLP.
# 
# 
# 
# Enable AutoML NLP on GCP
# The following steps will enable AutoML NLP on GCP:
# 
#        1. Click the triple dash in the top-left corner of the interface and
#           select Natural Language under the category ARTIFICIAL
#           INTELLIGENCE as shown in Figure 43-1.
# 
# 
# 
# 
#                                                                                           599
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_43
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 43: Google AutoML: Cloud Natural Language Processing",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 43: Google AutoML: Cloud Natural Language Processing"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter43(HierNode):
    def __init__(self):
        super().__init__("Chapter 43: Google AutoML: Cloud Natural Language Processing")
        self.add(Content())
        self.add(A_EnableAutoML())
        self.add(B_Preparingthe())
        self.add(C_Buildinga())

# eof
