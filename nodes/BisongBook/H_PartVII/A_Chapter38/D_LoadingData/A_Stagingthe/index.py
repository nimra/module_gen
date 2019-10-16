# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                               Chapter 38   Google BigQuery
# 
#    After typing the query in the Query editor, the following should be noted, as
# numbered in Figure 38-4:
# 
#       1. Click the ‘Run query’ button to execute the query.
# 
#       2. The green status indicator shows that the query is a valid SQL
#          statement and shows by the side an estimate of the query size
#          estimation.
# 
#       3. The query results can be easily analyzed and visualized using Data
#          Studio.
# 
#       4. We can see that the query completed in just over a second.
# 
# 
# 
# Loading Data into BigQuery
# In this simple data ingestion example, we will load a CSV file stored on Google Cloud
# Storage (GCS) into BigQuery. In GCP, Google Cloud Storage is a general-purpose storage
# location for all variety of file types and is preferred as a staging area or an archival
# repository for data. Let’s walk through the following steps.
# 
# 
# Staging the Data in GCS
# Let’s go through the steps to stage the data in Google Cloud Storage:
# 
#       1. Activate Cloud Shell as shown in Figure 38-5.
# 
# 
# 
# 
# Figure 38-5. Activate Google Cloud Shell
# 
# 
# 
#                                                                                       491
# 
# Chapter 38   Google BigQuery
# 
#       2. Create a bucket on GCS (remember to give the bucket a unique
#          name).
# 
#           gsutil mb gs://my-test-data
# 
#       3. Transfer data into bucket. The CSV data used in this example is
#          a crypto-currency dataset stored in the code repository. Use the
#          ‘gsutil cp’ command to move the dataset to GCS bucket.
# 
#           gsutil cp crypto-markets.csv gs://my-test-data
# 
#       4. Show the transferred data in the bucket.
# 
#           gsutil ls gs://my-test-data/
# 
# 
# Loading Data Using the BigQuery Web UI
# Let’s go through the following steps to load data into BigQuery using the web UI:
# 
#       1. In the navigation panel, click the project name, and then click
#          CREATE DATASET in the Details panel (see Figure 38-6).
# 
# 
# 
# 
# Figure 38-6. Create Dataset
# 
#       2. Type ‘crypto_data’ as the DatasetID, and select ‘United States
#          (US)’ as the data location (see Figure 38-7).
# 
# 
# 
# 
# 492
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Staging the Data in GCS",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Staging the Data in GCS"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Stagingthe(HierNode):
    def __init__(self):
        super().__init__("Staging the Data in GCS")
        self.add(Content())

# eof
