# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Stagingthe.index import Stagingthe as A_Stagingthe
from .B_LoadingData.index import LoadingData as B_LoadingData
from .C_Thebq.index import Thebq as C_Thebq
from .D_LoadingData.index import LoadingData as D_LoadingData

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Loading Data into BigQuery",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Loading Data into BigQuery"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LoadingData(HierNode):
    def __init__(self):
        super().__init__("Loading Data into BigQuery")
        self.add(Content())
        self.add(A_Stagingthe())
        self.add(B_LoadingData())
        self.add(C_Thebq())
        self.add(D_LoadingData())

# eof
