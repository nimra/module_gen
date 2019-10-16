# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#                                                            Chapter 38   Google BigQuery
# 
# 
# 
# 
# Figure 38-7. Create Dataset parameters
# 
#      3. Next, click the newly created Dataset in the navigation panel, and
#         then click CREATE TABLE in the Details panel (see Figure 38-8).
# 
# 
# 
# 
# Figure 38-8. Create Table
# 
# 
# 
# 
#                                                                                    493
# 
# Chapter 38   Google BigQuery
# 
#       4. We’ll create a table from a CSV file stored on Google Cloud
#          Storage. On the Create Table page, select the following parameters
#          as shown in Figure 38-9:
# 
#          a. Select ‘Google Cloud Storage’ for Source Data.
# 
#          b. Select the file ‘crypto-markets.csv’ from the bucket ‘my-test-data’.
# 
#          c. Choose CSV as the file format.
# 
#          d. Type ‘markets’ as the Destination table.
# 
#          e. Toggle ‘Edit as Text’ and enter the following as the schema:
# 
#              slug,symbol,name,date,ranknow,open,high,low,close,volume,market,
#              close_ratio,spread
# 
#          f. Expand ‘Advanced options’ and set ‘Header rows to skip’ to 1.
# 
#          g. Click Create table.
# 
# 
# 
# 
# Figure 38-9. Create table options
# 
# 
# 
# 494
# 
#                                                                Chapter 38   Google BigQuery
# 
#     Click Job history in the navigation panel to view the status of the loading job (see
# Figure 38-10).
# 
# 
# 
# 
# Figure 38-10. BigQuery loading job
# 
#     A preview of the created table is as shown in Figure 38-11.
# 
# 
# 
# 
#                                                                                            495
# 
# Chapter 38   Google BigQuery
# 
# 
# 
# 
# Figure 38-11. Preview of loaded table
# 
# 
# The bq Command-Line Utility
# Let’s go through some useful commands on the Cloud Shell terminal with the ‘bq’ utility:
# 
#       •   List the projects that can be accessed.
# 
#           bq ls –p
# 
#                   projectId           friendlyName
#            ----------------------- ------------------
#             secret-country-192905   My First Project
# 
#       •   List datasets in the default project.
# 
#           bq ls
# 
#              datasetId
#            -------------
#             crypto_data
# 
# 
# 496
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Loading Data Using the BigQuery Web UI",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Loading Data Using the BigQuery Web UI"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LoadingData(HierNode):
    def __init__(self):
        super().__init__("Loading Data Using the BigQuery Web UI")
        self.add(Content())

# eof
