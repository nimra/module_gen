# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_TheCloud.index import TheCloud as A_TheCloud
from .B_Preparingfor.index import Preparingfor as B_Preparingfor
from .C_Packagingthe.index import Packagingthe as C_Packagingthe
from .D_TheTensorFlow.index import TheTensorFlow as D_TheTensorFlow
from .E_TheApplication.index import TheApplication as E_TheApplication
from .F_Trainingon.index import Trainingon as F_Trainingon
from .G_ExecuteTraining.index import ExecuteTraining as G_ExecuteTraining
from .H_MakingPredictions.index import MakingPredictions as H_MakingPredictions
from .I_RunBatch.index import RunBatch as I_RunBatch
from .J_Trainingwith.index import Trainingwith as J_Trainingwith
from .K_Scikitlearnon.index import Scikitlearnon as K_Scikitlearnon
from .L_Movethe.index import Movethe as L_Movethe
from .M_Preparethe.index import Preparethe as M_Preparethe
from .N_Executea.index import Executea as N_Executea
from .O_Createa.index import Createa as O_Createa
from .P_MakeOnline.index import MakeOnline as P_MakeOnline

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 41
# 
# 
# 
# Google Cloud
# Machine Learning
# Engine (Cloud MLE)
# The Google Cloud Machine Learning Engine, simply known as Cloud MLE, is a managed
# Google infrastructure for training and serving “large-scale” machine learning models.
# Cloud ML Engine is a part of GCP AI Platform. This managed infrastructure can train
# large-scale machine learning models built with TensorFlow, Keras, Scikit-learn, or
# XGBoost. It also provides modes of serving or consuming the trained models either as
# an online or batch prediction service. Using online prediction, the infrastructure scales
# in response to request throughout, while with the batch mode, Cloud MLE can provide
# inference for TBs of data.
#     Two important features of Cloud MLE is the ability to perform distribution training
# and automatic hyper-parameter tuning of your models while training. The big advantage
# of automatic hyper-parameter tuning is the ability to find the best set of parameters
# that minimize the model cost or loss function. This saves time of development hours in
# iterative experiments.
# 
# 
# 
# The Cloud MLE Train/Deploy Process
# The high-level overview of the train/deploy process on Cloud MLE is depicted in
# Figure 41-1:
# 
#        1. The data for training/inference is kept on GCS.
# 
#        2. The execution script uses the application logic to train the model
#           on Cloud MLE using the training data.
#                                                                                           545
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_41
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Chapter 41: Google Cloud Machine Learning Engine (Cloud MLE)")
        self.add(MarkdownBlock("# Chapter 41: Google Cloud Machine Learning Engine (Cloud MLE)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter41(HierNode):
    def __init__(self):
        super().__init__("Chapter 41: Google Cloud Machine Learning Engine (Cloud MLE)")
        self.add(Content())
        self.add(A_TheCloud())
        self.add(B_Preparingfor())
        self.add(C_Packagingthe())
        self.add(D_TheTensorFlow())
        self.add(E_TheApplication())
        self.add(F_Trainingon())
        self.add(G_ExecuteTraining())
        self.add(H_MakingPredictions())
        self.add(I_RunBatch())
        self.add(J_Trainingwith())
        self.add(K_Scikitlearnon())
        self.add(L_Movethe())
        self.add(M_Preparethe())
        self.add(N_Executea())
        self.add(O_Createa())
        self.add(P_MakeOnline())

# eof
