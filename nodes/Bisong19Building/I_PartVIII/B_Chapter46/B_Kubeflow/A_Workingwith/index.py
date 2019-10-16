# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                Chapter 46    Kubeflow and Kubeflow Pipelines
# 
# Table 46-1. (continued)
# 
# Component         Description
# 
#                   PyTorch is a Python deep learning library developed by Facebook based on
#                   the Torch library for Lua, a programming language.
# 
# PyTorch
#                   TensorRT is a platform for high-performance and scalable deployment of deep
#                   learning models for inference.
# 
# NVIDIA TensorRT
#                   Seldon is an open source platform for deploying machine learning models on
#                   Kubernetes.
# Seldon
#                   TensorFlow provides an ecosystem for the large-scale productionalization
#                   of deep learning models. This includes distributed training using TFJob,
#                   serving with TF Serving, and other Tensorflow Extended components such as
#                   TensorFlow Model Analysis (TFMA) and TensorFlow Transform (TFT).
# TensorFlow
# 
# 
# Working with Kubeflow
#      1. Set up a Kubernetes cluster on GKE.
# 
#           # create a GKE cluster
#           gcloud container clusters create ekaba-gke-cluster
# 
#           # view the nodes of the kubernetes cluster on GKE
#           kubectl get nodes
# 
#      2. Create OAuth client ID to identify Cloud IAP: Kubeflow uses
#         Cloud Identity-Aware Proxy (Cloud IAP) to connect to Jupyter and
#         other running web apps securely. Kubeflow uses email addresses
#         for authentication. In this section, we’ll create an OAuth client ID
#         which will be used to identify Cloud IAP when requesting access
#         to a user’s email account:
#                                                                                               675
# 
# Chapter 46       Kubeflow and Kubeflow Pipelines
# 
#              •    Go to the APIs & Services ➤ Credentials page in GCP Console.
# 
#              •    Go to the OAuth consent screen (see Figure 46-2).
# 
#                   •   Assign an Application name, for example, My-Kubeflow-App.
# 
#                   •   For authorized domains, use [YOUR_PRODJECT_ID].
#                       cloud.goog.
# 
# 
# 
# 
# Figure 46-2. OAuth consent screen
# 
# 
# 
# 
# 676
# 
#                                             Chapter 46     Kubeflow and Kubeflow Pipelines
# 
#         •   Go to the Credentials tab (see Figure 46-3).
# 
#             •   Click Create credentials, and then click OAuth client ID.
# 
#             •   Under Application type, select Web application.
# 
# 
# 
# 
# Figure 46-3. GCP Credentials tab
# 
#         •   Choose a Name to identify the OAuth client ID (see Figure 46-4).
# 
# 
# 
# 
#                                                                                       677
# 
# Chapter 46       Kubeflow and Kubeflow Pipelines
# 
# 
# 
# 
# Figure 46-4. Create OAuth client ID
# 
#              •    In the Authorized redirect URIs box, enter the following:
# 
#                   https://<deployment_name>.endpoints.<project>.cloud.
#                   goog/_gcp_gatekeeper/authenticate
# 
#              •    <deployment_name> must be the name of the Kubeflow
#                   deployment.
# 
#              •    <project> is the GCP project ID.
# 
# 678
# 
#                                                  Chapter 46    Kubeflow and Kubeflow Pipelines
# 
#            •   In this case, it will be
# 
#                https://ekaba-kubeflow-app.endpoints.oceanic-
#                sky-230504.cloud.goog/_gcp_gatekeeper/authenticate
# 
#            •   Take note of the client ID and client secret that appear in the
#                OAuth client window. This is needed to enable Cloud IAP.
# 
#                # Create environment variables from the OAuth client ID and
#                secret earlier obtained.
#                export CLIENT_ID=506126439013-drbrj036hihvdolgki6lflovm4bjb6c1.
#                apps.googleusercontent.com
#                export CLIENT_SECRET=bACWJuojIVm7PIMphzTOYz9D
#                export PROJECT=oceanic-sky-230504
# 
# D
#  ownload kfctl.sh
# The file kfctl.sh is the Kubeflow installation shell script. As at this time of writing, the
# latest Kubeflow tag is 0.5.0.
# 
# # create a folder on the local machine
# mkdir kubeflow
# 
# # move to created folder
# cd kubeflow
# 
# # save folder path as a variable
# export KUBEFLOW_SRC=$(pwd)
# 
# # download kubeflow `kfctl.sh`
# export KUBEFLOW_TAG=v0.5.0
# 
# curl https://raw.githubusercontent.com/kubeflow/kubeflow/${KUBEFLOW_TAG}/
# scripts/download.sh | bash
# 
# # list directory elements
# ls -la
# drwxr-xr-x   6 ekababisong  staff   204 17 Mar 04:15 .
# drwxr-xr-x  25 ekababisong  staff   850 17 Mar 04:09 ..
# drwxr-xr-x   4 ekababisong  staff   136 17 Mar 04:18 deployment
# 
# 
#                                                                                                679
# 
# Chapter 46   Kubeflow and Kubeflow Pipelines
# 
# drwxr-xr-x  36 ekababisong  staff  1224 17 Mar 04:14 kubeflow
# drwxr-xr-x  16 ekababisong  staff   544 17 Mar 04:14 scripts
# 
# D
#  eploy Kubeflow
# Run the following code block to deploy Kubeflow.
# 
# # assign the name for the Kubeflow deployment
# # The ksonnet app is created in the directory ${KFAPP}/ks_app
# export KFAPP=ekaba-kubeflow-app
# 
# # run setup script
# ${KUBEFLOW_SRC}/scripts/kfctl.sh init ${KFAPP} --platform gcp --project
# ${PROJECT}
# 
# # navigate to the deployment directory
# cd ${KFAPP}
# 
# # creates config files defining the various resources for gcp
# ${KUBEFLOW_SRC}/scripts/kfctl.sh generate platform
# 
# # creates or updates gcp resources
# ${KUBEFLOW_SRC}/scripts/kfctl.sh apply platform
# 
# # creates config files defining the various resources for gke
# ${KUBEFLOW_SRC}/scripts/kfctl.sh generate k8s
# 
# # creates or updates gke resources
# ${KUBEFLOW_SRC}/scripts/kfctl.sh apply k8s
# 
# # view resources deployed in namespace kubeflow
# kubectl -n kubeflow get  all
# 
#     Kubeflow is available at a URL that will be unique for your deployment. In this
# case, Kubeflow is available to me at https://ekaba-kubeflow-app.endpoints.
# oceanic-sky-230504.cloud.goog/ (see Figure 46-5). Again, this URL is unique for your
# deployment.
# 
# 
# 
# 
# 680
# 
#                                           Chapter 46   Kubeflow and Kubeflow Pipelines
# 
# 
# 
# 
# Figure 46-5. The Kubeflow homescreen
# 
# 
#  Note It can take 10–15 minutes for the URI to become available. Kubeflow needs
#  to provision a signed SSL certificate and register a DNS name.
# 
# 
# 
# Kubeflow Pipelines – Kubeflow for Poets
# Kubeflow Pipelines is a simple platform for building and deploying containerized
# machine learning workflows on Kubernetes. Kubeflow pipelines make it easy to
# implement production-grade machine learning pipelines without bothering on the low-­
# level details of managing a Kubernetes cluster.
#     Kubeflow Pipelines is a core component of Kubeflow and is also deployed when
# Kubeflow is deployed. The Pipelines dashboard is shown in Figure 46-6.
# 
# 
# 
# 
#                                                                                   681
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Working with Kubeflow",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Working with Kubeflow"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Workingwith(HierNode):
    def __init__(self):
        super().__init__("Working with Kubeflow")
        self.add(Content())

# eof
