# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                 Chapter 44   Model to Predict the Critical Temperature of Superconductors
# 
# 
# 
# 
# Figure 44-1. Modeling architecture on GCP
# 
# 
# Stage Raw Data in GCS
# Retrieve the raw data from the book code repository for modeling:
# 
#       •   Create a GCS bucket.
# 
#           gsutil mb gs://superconductor
# 
#       •   Navigate to the chapter folder and transfer the raw data to GCS.
# 
#           gsutil cp train.csv gs://superconductor/raw-data/
# 
# 
# 
# Load Data into BigQuery for Analytics
# Move the dataset from Google Cloud Storage to BigQuery:
# 
#       •   Create a Dataset in BigQuery.
# 
#           bq mk superconductor
# 
# 
#                                                                                      615
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Stage Raw Data in GCS",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Stage Raw Data in GCS"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class StageRaw(HierNode):
    def __init__(self):
        super().__init__("Stage Raw Data in GCS")
        self.add(Content())

# eof
