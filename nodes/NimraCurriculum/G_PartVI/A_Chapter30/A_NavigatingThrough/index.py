# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_TheLowLevel.index import TheLowLevel as A_TheLowLevel
from .B_TheMidLevel.index import TheMidLevel as B_TheMidLevel
from .C_TheHighLevel.index import TheHighLevel as C_TheHighLevel
from .D_TheAnatomy.index import TheAnatomy as D_TheAnatomy
from .E_TensorBoard.index import TensorBoard as E_TensorBoard
from .F_Featuresin.index import Featuresin as F_Featuresin
from .G_ASimple.index import ASimple as G_ASimple
from .H_BuildingEfficient.index import BuildingEfficient as H_BuildingEfficient
from .I_LinearRegression.index import LinearRegression as I_LinearRegression
from .J_Classificationwith.index import Classificationwith as J_Classificationwith
from .K_Visualizingwith.index import Visualizingwith as K_Visualizingwith
from .L_RunningTensorFlow.index import RunningTensorFlow as L_RunningTensorFlow
from .M_TensorFlowHighLevel.index import TensorFlowHighLevel as M_TensorFlowHighLevel
from .N_NeuralNetworks.index import NeuralNetworks as N_NeuralNetworks
from .O_Usingthe.index import Usingthe as O_Usingthe
from .P_Usingthe.index import Usingthe as P_Usingthe
from .Q_ModelVisualization.index import ModelVisualization as Q_ModelVisualization
from .R_TensorBoardwith.index import TensorBoardwith as R_TensorBoardwith
from .S_Checkpointingto.index import Checkpointingto as S_Checkpointingto

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 30
# 
# 
# 
# TensorFlow 2.0 and Keras
# TensorFlow (TF) is a specialized numerical computation library for deep learning. It is
# the preferred tool by numerous deep learning researchers and industry practitioners for
# developing deep learning models and architectures as well as for serving learned models
# into production servers and software products. This chapter is focused on TensorFlow 2.0.
# 
# 
# 
# Navigating Through the TensorFlow API
# Understanding the different levels of the TF API hierarchy is critical to working
# effectively with TF. The task of building a TF deep learning model may be addressed
# via different TF API levels. An understanding of the API hierarchy provides clarity on
# implementing neural network models with TF as well as navigating the TF ecosystem.
# The TF API hierarchy is primarily composed of three API levels, the high-level API, the
# mid-level API which provides components for building neural network models, and the
# low-level API. A diagrammatic representation of this is shown in Figure 30-1.
# 
# 
# 
# 
#                                                                                           347
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_30
# 
# Chapter 30   TensorFlow 2.0 and Keras
# 
# 
# 
# 
# Figure 30-1. TensorFlow API hierarchy
# 
# 
# The Low-Level TensorFlow APIs
# The low-level API gives the tools for building network graphs from the ground up using
# mathematical operations. This API level affords the greatest level of flexibility to tweak
# and tune the model as desired. Moreover, the higher-level APIs implement low-level
# operations under the hood.
# 
# 
# The Mid-Level TensorFlow APIs
# TensorFlow provides a set of reusable packages for simplifying the process involved in
# creating neural network models. Some examples of these functions include the layers
# (tf.keras.layers), Datasets (tf.data), metrics (tf.keras.metrics), loss (tf.keras.losses),
# and FeatureColumns (tf.feature_column) packages.
# 
# L ayers
# The layers package (tf.keras.layers) provides a handy set of functions to simplify the
# construction of layers in a neural network architecture. For example, consider the
# convolutional network architecture in Figure 30-2 and how the layers API simplifies the
# creation of the network layers.
# 
# 
# 
# 348
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Navigating Through the TensorFlow API")
        self.add(MarkdownBlock("# Navigating Through the TensorFlow API"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class NavigatingThrough(HierNode):
    def __init__(self):
        super().__init__("Navigating Through the TensorFlow API")
        self.add(Content())
        self.add(A_TheLowLevel())
        self.add(B_TheMidLevel())
        self.add(C_TheHighLevel())
        self.add(D_TheAnatomy())
        self.add(E_TensorBoard())
        self.add(F_Featuresin())
        self.add(G_ASimple())
        self.add(H_BuildingEfficient())
        self.add(I_LinearRegression())
        self.add(J_Classificationwith())
        self.add(K_Visualizingwith())
        self.add(L_RunningTensorFlow())
        self.add(M_TensorFlowHighLevel())
        self.add(N_NeuralNetworks())
        self.add(O_Usingthe())
        self.add(P_Usingthe())
        self.add(Q_ModelVisualization())
        self.add(R_TensorBoardwith())
        self.add(S_Checkpointingto())

# eof
