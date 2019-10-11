# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Componentsof.index import Componentsof as A_Componentsof
from .B_Executinga.index import Executinga as B_Executinga

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# Chapter 46   Kubeflow and Kubeflow Pipelines
# 
# 
# 
# 
# Figure 46-6. Kubeflow Pipelines dashboard
# 
# Components of Kubeflow Pipelines
# A Pipeline describes a machine learning workflow, where each component of the
# pipeline is a self-contained set of codes that are packaged as Docker images. Each
# pipeline can be uploaded individually and shared on the Kubeflow Pipelines user
# interface (UI). A pipeline takes inputs (parameters) required to run the pipeline and the
# inputs and outputs of each component.
#     The Kubeflow Pipelines platform consists of
# 
#       •   A user interface (UI) for managing and tracking Experiments, jobs,
#           and runs
# 
#       •   An engine for scheduling multi-step ML workflows
# 
#       •   An SDK for defining and manipulating pipelines and components
# 
#       •   Notebooks for interacting with the system using the SDK (taken from
#           www.kubeflow.org/docs/pipelines/pipelines-overview/)
# 
# 
# 
# 
# 682
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Kubeflow Pipelines – Kubeflow for Poets")
        self.add(MarkdownBlock("# Kubeflow Pipelines – Kubeflow for Poets"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class KubeflowPipelines(HierNode):
    def __init__(self):
        super().__init__("Kubeflow Pipelines – Kubeflow for Poets")
        self.add(Content())
        self.add(A_Componentsof())
        self.add(B_Executinga())

# eof
