# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                        Chapter 1   What Is Cloud Computing?
# 
#       •   Private cloud: In a private cloud, an organization is solely responsible
#           for the management and servicing of its computing infrastructure.
#           The machines in a private cloud can be located on-premises, or it
#           can be hosted with a cloud service provider but routed on a private
#           network.
# 
#       •   Hybrid cloud: The hybrid cloud is a compromise between the cost
#           and efficiency of a public cloud and the data sovereignty and in-­
#           house security assurances of the private cloud. Many companies
#           and institutions opt for a hybrid cloud and multi-cloud by using
#           technology solutions to facilitate easy porting and sharing of data and
#           applications between on-premise and cloud-based infrastructures.
# 
# 
# 
# Cloud Computing Models
# Cloud computing is also categorized into three models of service delivery. They are
# illustrated as a pyramid as shown in Figure 1-2, where the layers of infrastructure
# abstraction increase as we approach the apex of the pyramid:
# 
#       •   Infrastructure as a Service (IaaS): This model is best suited for
#           enterprises or individuals who want to manage the hardware
#           infrastructure that hosts their data and applications. This level
#           of fine-grained management requires the necessary system
#           administration skills.
# 
#       •   Platform as a Service (PaaS): In the PaaS model, the hardware
#           configuration is managed by the cloud service provider, as well as
#           other system and development tools. This relieves the user to focus
#           on the business logic for quick and easy deployment of application
#           and database solutions. Another concept that comes up together
#           with PaaS is the idea of Serverless, where the cloud service provider
#           manages a scalable infrastructure that utilizes and relinquishes
#           resources according to demand.
# 
#       •   Software as a Service (SaaS): The SaaS model is most recognizable
#           by the general public, as a great deal of users interact with SaaS
#           applications without knowing. The typical examples of SaaS
# 
# 
#                                                                                          5
# 
# Chapter 1    What Is Cloud Computing?
# 
#             applications are enterprise email suites such as Gmail, Outlook, and
#             Yahoo! Mail. Others include storage platforms like Google Drive and
#             Dropbox, photo software like Google Photos, and CRM e-suites like
#             Salesforce and Oracle E-business Suite.
# 
# 
# 
# 
# Figure 1-2. Models of cloud computing
# 
#     In this chapter, we summarized the practice of cloud computing by explaining the
# different categories of cloud solutions and the models for service delivery over the cloud.
#     The next chapters in Part 1 will provide an introduction to Google Cloud Platform
# Infrastructure and Services and introduce JupyterLab Instances, and Google
# Colaboratory for prototyping machine learning models and doing data science and
# analytics tasks.
# 
# 
# 
# 
# 6
# 
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
        super().__init__("Cloud Computing Models")
        self.add(MarkdownBlock("# Cloud Computing Models"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CloudComputing(HierNode):
    def __init__(self):
        super().__init__("Cloud Computing Models")
        self.add(Content())

# eof