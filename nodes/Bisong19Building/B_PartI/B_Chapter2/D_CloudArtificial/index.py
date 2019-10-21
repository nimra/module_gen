# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Cloud Artificial Intelligence (AI)
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Cloud Artificial Intelligence (AI)",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Cloud Artificial Intelligence (AI)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CloudArtificial(HierNode):
    def __init__(self):
        super().__init__("Cloud Artificial Intelligence (AI)")
        self.add(Content())

# eof
