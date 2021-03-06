# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "What BigQuery Is Not",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# What BigQuery Is Not"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class WhatBigQuery(HierNode):
    def __init__(self):
        super().__init__("What BigQuery Is Not")
        self.add(Content())

# eof
