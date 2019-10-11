# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 2   An Overview of Google Cloud Platform Services
# 
# 
# Cloud Artificial Intelligence (AI)
# Google Cloud AI offers cloud services for businesses and individuals to leverage pre-­
# trained models for custom artificial intelligence tasks through the use of REST APIs.
# It also exposes services for developing custom models for domain use cases such as
# AutoML Vision for image classification and object detection tasks and AutoML tables to
# deploy AI models on structured data.
#      Google Cloud AI services in Figure 2-4 include Cloud AutoML (train custom
# machine learning models leveraging transfer learning), Cloud Machine Learning Engine
# (for large-scale distributed training and deployment of machine learning models),
# Cloud TPU (to quickly train large-scale models), Video Intelligence (train custom video
# models), Cloud Natural Language API (extract/analyze text from documents), Cloud
# Speech API (transcribe audio to text), Cloud Vision API (classification/segmentation of
# images), Cloud Translate API (translate from one language to another), and Cloud Video
# Intelligence API (extract metadata from video files).
# 
# 
# 
# 
# Figure 2-4. Cloud AI services
# 
#      This chapter provides a high-level overview of the products and services offered on
# Google Cloud Platform.
#      The next chapter will introduce the Google Cloud software development kit (SDK)
# for interacting with cloud resources from the command line on the local machine
# and the cloud command-line interface (CLI) for doing the same via the cloud console
# interface on GCP.
# 
# 
# 
# 
# 10
# 
# CHAPTER 3
# 
# 
# 
# The Google Cloud SDK
# and Web CLI
# GCP provides a command-line interface (CLI) for interacting with cloud products and
# services. GCP resources can be accessed via the web-based CLI on GCP or by installing
# the Google Cloud software development kit (SDK) on your local machine to interact with
# GCP via the local command-line terminal.
#     GCP contains shell commands for a wide range of GCP products such as the
# Compute Engine, Cloud Storage, Cloud ML Engine, BigQuery, and Datalab, to mention
# just a few. Major tools of the Cloud SDK include
# 
#        •    gcloud tool: Responsible for cloud authentication, configuration, and
#             other interactions on GCP
# 
#        •    gsutil tool: Responsible for interacting with Google Cloud Storage
#             buckets and objects
# 
#        •    bq tool: Used for interacting and managing Google BigQuery via the
#             command line
# 
#        •    kubectl tool: Used for managing Kubernetes container clusters on GCP
# 
#     The Google Cloud SDK also installs client libraries for developers to
# programmatically interact with GCP products and services through APIs.1 As of this time
# of writing, the Go, Java, Node.js, Python, Ruby, PHP, and C# languages are covered. Many
# more are expected to be added to this list.
#     This chapter works through setting up an account on GCP, installing the Google
# Cloud SDK, and then exploring GCP commands using the CLI.
# 
# 
# 1
#   PIs stands for application programming interfaces, which are packages and tools used in
#  A
#  building software applications.
#                                                                                              11
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_3
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Cloud Artificial Intelligence (AI)")
        self.add(MarkdownBlock("# Cloud Artificial Intelligence (AI)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CloudArtificial(HierNode):
    def __init__(self):
        super().__init__("Cloud Artificial Intelligence (AI)")
        self.add(Content())

# eof
