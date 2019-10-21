# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Cloud Compute
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
# Figure 2-1. Cloud compute services
# 
#    For our purposes of machine learning modeling, the cloud compute engine is what
# we will concentrate on. As later seen in Chapter 6, JupyterLab will provision a compute
# engine with all the relevant tools, packages, and frameworks for data analytics and
# modeling machine learning and deep learning solutions.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Cloud Compute",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Cloud Compute"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CloudCompute(HierNode):
    def __init__(self):
        super().__init__("Cloud Compute")
        self.add(Content())

# eof
