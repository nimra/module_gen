# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_TheModeling.index import TheModeling as A_TheModeling
from .B_StageRaw.index import StageRaw as B_StageRaw
from .C_LoadData.index import LoadData as C_LoadData
from .D_ExploratoryData.index import ExploratoryData as D_ExploratoryData
from .E_SpotChecking.index import SpotChecking as E_SpotChecking
from .F_Dataflowand.index import Dataflowand as F_Dataflowand
from .G_Trainingon.index import Trainingon as G_Trainingon
from .H_DeployTrained.index import DeployTrained as H_DeployTrained
from .I_BatchPrediction.index import BatchPrediction as I_BatchPrediction

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 44
# 
# 
# 
# Model to Predict the
# Critical Temperature
# of Superconductors
# This chapter builds a regression machine learning model to predict the critical
# temperature of superconductors. The features for this dataset were derived based on the
# following superconductor properties:
# 
#        •    Atomic mass
# 
#        •    First ionization energy
# 
#        •    Atomic radius
# 
#        •    Density
# 
#        •    Electron affinity
#        •    Fusion heat
# 
#        •    Thermal conductivity
# 
#        •    Valence
#      And for each property, the mean, weighted mean, geometric mean, weighted
# geometric mean, entropy, weighted entropy, range, weighted range, standard deviation,
# and weighted standard deviation are extracted. Thus, this results in a total number of
# 8 x 10 = 80 features. In addition to this, a feature that contains the number of elements in
# the superconductor is added to the design matrix. The predictor variable is the critical
# temperature of the superconductor. Hence, the dataset has a total of 81 features and
# 21,263 rows.
# 
#                                                                                           613
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_44
# 
# Chapter 44   Model to Predict the Critical Temperature of Superconductors
# 
#    This dataset is made available by Kam Hamidieh of the University of Pennsylvania
# and submitted to the UCI Machine Learning Repository. The goal of this section is to
# demonstrate delivering an end-to-end machine learning modeling pipeline on Google
# Cloud Platform.
# 
# 
# 
# The Modeling Architecture on GCP
# The goal of this end-to-end project is to demonstrate building a large-scale learning
# model on GCP using the components already discussed in this book. The modeling
# architecture is illustrated in Figure 44-1. Let’s briefly explain the connections:
# 
#       1. Stage the raw data on GCS.
# 
#       2. Load data into BigQuery for analytics.
# 
#       3. Exploratory data analysis.
# 
#       4. Large-scale data processing with Dataflow.
# 
#       5. Place transformed training and evaluation data on GCS.
# 
#       6. Train the model on Cloud MLE.
# 
#       7. Place the trained model output on GCS.
# 
#       8. Deploy the model for inference on Cloud MLE.
# 
# 
# 
# 
# 614
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 44: Model to Predict the Critical Temperature of Superconductors",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 44: Model to Predict the Critical Temperature of Superconductors"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter44(HierNode):
    def __init__(self):
        super().__init__("Chapter 44: Model to Predict the Critical Temperature of Superconductors")
        self.add(Content())
        self.add(A_TheModeling())
        self.add(B_StageRaw())
        self.add(C_LoadData())
        self.add(D_ExploratoryData())
        self.add(E_SpotChecking())
        self.add(F_Dataflowand())
        self.add(G_Trainingon())
        self.add(H_DeployTrained())
        self.add(I_BatchPrediction())

# eof
