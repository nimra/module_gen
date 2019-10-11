# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_EnableAutoML.index import EnableAutoML as A_EnableAutoML
from .B_Preparingthe.index import Preparingthe as B_Preparingthe
from .C_BuildingCustom.index import BuildingCustom as C_BuildingCustom

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 42
# 
# 
# 
# Google AutoML:
# Cloud Vision
# Google Cloud AutoML Vision facilitates the creation of custom vision models for image
# recognition use cases. This managed service works with the concepts of transfer learning
# and neural architecture search under the hood to find the best network architecture
# and the optimal hyper-parameter configuration of that architecture that minimizes the
# loss function of the model. This chapter will go through a sample project of building a
# custom image recognition model using Google Cloud AutoML Vision. In this chapter, we
# will build an image model to recognize select cereal boxes.
# 
# 
# 
# Enable AutoML Cloud Vision on GCP
# Step through the following steps to enable AutoML Cloud Vision on GCP:
# 
#        1. Open Cloud Vision by clicking the triple dash at the top-left corner
#           of the GCP dashboard. Select Vision under the product section
#           ARTIFICIAL INTELLIGENCE as shown in Figure 42-1.
# 
# 
# 
# 
#                                                                                           581
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_42
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Chapter 42: Google AutoML: Cloud Vision")
        self.add(MarkdownBlock("# Chapter 42: Google AutoML: Cloud Vision"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter42(HierNode):
    def __init__(self):
        super().__init__("Chapter 42: Google AutoML: Cloud Vision")
        self.add(Content())
        self.add(A_EnableAutoML())
        self.add(B_Preparingthe())
        self.add(C_BuildingCustom())

# eof
