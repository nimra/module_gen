# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#                                           Chapter 46   Kubeflow and Kubeflow Pipelines
# 
# Executing a Sample Pipeline
#      1. Click the name [Sample] Basic - Condition (see Figure 46-7).
# 
# 
# 
# 
# Figure 46-7. Select a Pipeline
# 
#      2. Click Start an Experiment (see Figure 46-8).
# 
# 
# 
# 
# Figure 46-8. Create a new Experiment
# 
#                                                                                   683
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Components of Kubeflow Pipelines",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Components of Kubeflow Pipelines"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Componentsof(HierNode):
    def __init__(self):
        super().__init__("Components of Kubeflow Pipelines")
        self.add(Content())

# eof
