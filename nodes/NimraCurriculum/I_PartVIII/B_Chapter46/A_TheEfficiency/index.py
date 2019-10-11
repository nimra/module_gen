# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 46   Kubeflow and Kubeflow Pipelines
# 
# 
# 
# 
# Figure 46-1. Machine learning production pipeline
# 
#     From the preceding diagram, observe that the process flow in the pipeline is
# iterative. This repetitive pattern is central to machine learning experimentation, design,
# and deployment.
# 
# 
# 
# The Efficiency Challenge
# It is easy to recognize that the pipeline requires a significant amount of development
# operations for the seamless transition from one component to another when building a
# learning model. This interoperability of parts has given rise to Machine Learning Ops,
# also known as MLOps. The term is coined as an amalgam of Machine Learning and
# DevOps.
#       The conventional way of doing machine learning is to perform all of the Experiment
# and development work in Jupyter notebooks, and the model is exported and sent off to
# the software development team for deployment and endpoint generation for integration
# 
# 
# 
# 672
# 
#                                               Chapter 46    Kubeflow and Kubeflow Pipelines
# 
# into downstream software products, while the DevOps team handles the infrastructure
# and configuration of the machine for model development. This monolithic style of
# working results in a machine learning process that is not reusable, difficult to scale and
# maintain, and even tougher to audit and perform model improvement, and it is easily
# fraught with errors and unnecessary complexities.
#     However, by incorporating the microservice design pattern to machine learning
# development, we can address a host of these concerns and really streamline the
# productionalization process.
# 
# 
# 
# K
#  ubeflow
# Kubeflow is a platform that is created to enhance and simplify the process of deploying
# machine learning workflows on Kubernetes. Using Kubeflow, it becomes easier to
# manage a distributed machine learning deployment by placing components in the
# deployment pipeline such as the training, serving, monitoring, and logging components
# into containers on the Kubernetes cluster.
#     The goal of Kubeflow is to abstract away the technicalities of managing a Kubernetes
# cluster so that a machine learning practitioner can quickly leverage the power of
# Kubernetes and the benefits of deploying products within a microservice framework.
# Kubeflow has its history as an internal Google framework for implementing machine
# learning pipelines on Kubernetes before being open sourced late 2017.
#     Table 46-1 is a sample of some of the components that run on Kubeflow.
# 
# 
# 
# 
#                                                                                         673
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("The Efficiency Challenge")
        self.add(MarkdownBlock("# The Efficiency Challenge"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheEfficiency(HierNode):
    def __init__(self):
        super().__init__("The Efficiency Challenge")
        self.add(Content())

# eof
