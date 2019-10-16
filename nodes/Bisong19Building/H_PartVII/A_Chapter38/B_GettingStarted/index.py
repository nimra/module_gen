# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_PublicDatasets.index import PublicDatasets as A_PublicDatasets

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 38   Google BigQuery
# 
# of ­business intelligence and analytics personnel to more easily harness the predictive
# power of using machine learning for business forecasting and decision-making.
# 
# 
# 
# What BigQuery Is Not
# As powerful and widely purposed as BigQuery is, it may not be properly suited for some
# use cases:
# 
#       •   BigQuery is not a replacement for a relational database. Some
#           business use cases may involve a large number of table row updates;
#           in such an instance, BigQuery is most likely not the data storage
#           solution of choice, as relational databases are well suited for such
#           highly transactional tasks. GCP offers the Cloud SQL and Cloud
#           Spanner as parts of its managed relational products.
# 
#       •   BigQuery is not a NoSQL database. Data stored in BigQuery must
#           have a schema. NoSQL is a schema-less data storage solution. GCP
#           also has Cloud BigTable and Cloud Datastore, which are highly
#           scalable and performant managed NoSQL products.
# 
# 
# 
# Getting Started with BigQuery
# BigQuery can be accessed and used via a variety of ways; they include
# 
#       •   The BigQuery web UI
#       •   The command-line tool, ‘bq’
# 
#       •   The client API libraries for programmatic access
# 
#     In this section, we will introduce BigQuery by working with the web UI, because it
# gives a graphical view of the datasets and tables within BigQuery and is good for quick
# execution of queries on the query engine.
#     To open BigQuery from the GCP dashboard, click the triple dash on the top-left
# corner and select BigQuery from the product section labeled Big Data as shown in
# Figure 38-1.
# 
# 
# 
# 
# 486
# 
#                                                          Chapter 38   Google BigQuery
# 
# 
# 
# 
# Figure 38-1. Open BigQuery
# 
#    The BigQuery web UI dashboard is as shown in Figure 38-2.
# 
# 
# 
# 
#                                                                                  487
# 
# Chapter 38    Google BigQuery
# 
# 
# 
# 
# Figure 38-2. BigQuery web UI
# 
#     In Figure 38-2, there are three labeled sections of the BigQuery web UI that we’ll
# briefly explain:
# 
#       1. The navigation panel: This panel contains a set of BigQuery
#          resources such as
# 
#           •    Query history: For viewing previous queries
#           •    Saved queries: For storing frequently used queries
# 
#           •    Job history: For viewing BigQuery jobs such as loading, copying,
#                and exporting of data
# 
#           •    Transfers: Link to the BigQuery Data Transfer Service UI
# 
#           •    Resources: Shows a list of pinned projects and their containing
#                Datasets
# 
# 
# 
# 
# 488
# 
#                                                             Chapter 38   Google BigQuery
# 
#       2. The Query editor: This is where queries are composed using the
#          familiar SQL database language.
# 
#       3. The Details panel: This panel shows the details of projects,
#          datasets, and table when clicked in the Resources tab. Also, this
#          panel shows the results of executed queries.
# 
# 
# P
#  ublic Datasets
# BigQuery comes with access to some public datasets; we will use these datasets to
# explore working with BigQuery. To view the public datasets, go to
# 
# h ttps://console.cloud.google.com/bigquery?p=bigquery-public-­
#  data&page=project.
# 
#     The public datasets will now show in the Resources section of the navigation panel
# (see Figure 38-3).
# 
# 
# 
# 
# Figure 38-3. Public Datasets
# 
# 
# 
#                                                                                     489
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Getting Started with BigQuery",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Getting Started with BigQuery"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GettingStarted(HierNode):
    def __init__(self):
        super().__init__("Getting Started with BigQuery")
        self.add(Content())
        self.add(A_PublicDatasets())

# eof
