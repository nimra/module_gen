# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#                                                              Chapter 38    Google BigQuery
# 
#      •   List tables in a Dataset.
# 
#          bq ls crypto_data
# 
#            tableId   Type    Labels   Time Partitioning
#           --------- ------- -------- -------------------
#            markets   TABLE
# 
#      •   List the recent executed jobs. This includes both load jobs and
#          queries executed.
# 
#          bq ls –j
# 
#          jobId                         Job Type  State     Start Time     Duration
#          ---------------------------- -------- -------- --------------- --------
#          bquxjob_767fb332_16625172a52  load      SUCCESS   29 Sep 07:29:27  0:00:10
#          bquxjob_2a33184c_16625141949  load      SUCCESS   29 Sep 07:26:06  0:00:13
#          bquxjob_582a116b_16624b3717a  query     SUCCESS   29 Sep 05:41:20  0:00:01
#          bquxjob_7b18cd73_16624a0f378  query     SUCCESS   29 Sep 05:40:32  0:00:01
# 
# 
# 
# Loading Data Using the Command-Line bq Utility
# The following commands walk through loading a dataset into BigQuery using the bq
# utility via the terminal:
# 
#      •   Create a new Dataset.
# 
#          bq mk crypto_data_terminal
# 
#          Dataset 'secret-country-192905:crypto_data_terminal' successfully
#          created.
# 
#      •   List the datasets to confirm creation of new Dataset.
# 
#          bq ls
# 
#                 datasetId
#           ----------------------
#            crypto_data
#            crypto_data_terminal
# 
# 
# 
#                                                                                       497
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("The bq Command-Line Utility")
        self.add(MarkdownBlock("# The bq Command-Line Utility"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Thebq(HierNode):
    def __init__(self):
        super().__init__("The bq Command-Line Utility")
        self.add(Content())

# eof
