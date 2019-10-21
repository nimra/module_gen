# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#        Chapter 47   Deploying an End-to-­End Machine Learning Solution on Kubeflow Pipelines
# 
# 
#  uild Containers Before Uploading to Kubeflow
# B
# Pipelines
# Before uploading the pipeline to Kubeflow Pipelines, be sure to build the component
# containers so that the latest version of the code is packaged and uploaded as images to
# the container registry. The code provides a handy bash script to build all containers.
# 
# 
# 
#  ompile the Pipeline Using the Kubeflow
# C
# Pipelines DSL Language
# The pipeline code contains a specification on how the components interact with one
# another. Each component has an output that serves as an input to the next component
# in the pipeline. The Kubeflow pipeline DSL language dsl-compile from the Kubeflow
# Pipelines SDK is used to compile the pipeline code in Python for upload to Kubeflow
# Pipelines.
#     Ensure the Kubeflow Pipelines SDK is installed on the local machine by running
# 
# # install kubeflow pipeline sdk
# pip install https://storage.googleapis.com/ml-pipeline/release/0.1.12/kfp.
# tar.gz --upgrade
# 
# # verify the install
# which dsl-compile
# 
#    Compile the pipeline by running
# 
# # compile the pipeline
# python3 [path/to/python/file.py] [path/to/output/tar.gz]
# 
#    For the sample code, we used
# 
# python3 crypto_pipeline.py crypto_pipeline.tar.gz
# 
# 
# 
# 
#                                                                                         689
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Build Containers Before Uploading to Kubeflow Pipelines",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Build Containers Before Uploading to Kubeflow Pipelines"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BuildContainers(HierNode):
    def __init__(self):
        super().__init__("Build Containers Before Uploading to Kubeflow Pipelines")
        self.add(Content())

# eof
