# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_CloudCompute.index import CloudCompute as A_CloudCompute
from .B_CloudStorage.index import CloudStorage as B_CloudStorage
from .C_BigData.index import BigData as C_BigData
from .D_CloudArtificial.index import CloudArtificial as D_CloudArtificial

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 2
# 
# 
# 
# An Overview of Google
# Cloud Platform Services
# Google Cloud Platform offers a wide range of services for securing, storing, serving,
# and analyzing data. These cloud services form a secure cloud perimeter for data, where
# different operations and transformations can be carried out on the data without it ever
# leaving the cloud ecosystem.
#      The services offered by Google Cloud include compute, storage, big data/analytics,
# artificial intelligence (AI), and other networking, developer, and management services.
# Let’s briefly review some of the features of the Google Cloud ecosystem.
# 
# 
# 
# C
#  loud Compute
# Google Compute offers a range of products shown in Figure 2-1 for catering to a wide
# range of computational needs. The compute products consist of the Compute Engine
# (virtual computing instances for custom processing), App Engine (a cloud-managed
# platform for developing web, mobile, and IoT app), Kubernetes Engine (orchestration
# manager for custom docker containers based on Kubernetes), Container Registry
# (private container storage), Serverless Cloud Functions (cloud-based functions to
# connect or extend cloud services), and Cloud Run (managed compute platform that
# automatically scales your stateless containers).
# 
# 
# 
# 
#                                                                                           7
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_2
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Chapter 2: An Overview of Google Cloud Platform Services")
        self.add(MarkdownBlock("# Chapter 2: An Overview of Google Cloud Platform Services"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter2(HierNode):
    def __init__(self):
        super().__init__("Chapter 2: An Overview of Google Cloud Platform Services")
        self.add(Content())
        self.add(A_CloudCompute())
        self.add(B_CloudStorage())
        self.add(C_BigData())
        self.add(D_CloudArtificial())

# eof
