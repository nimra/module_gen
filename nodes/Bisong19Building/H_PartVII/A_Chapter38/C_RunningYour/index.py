# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 38    Google BigQuery
# 
# 
# Running Your First Query
# For our first query, we will work with the ‘census_bureau_international’ dataset which
# “provides estimates of country populations since 1950 and projections through 2050.” In
# this query, we select a country and their life expectancy (for both sexes) in the year 2018.
# 
# SELECT
#   country_name,
#   life_expectancy
# FROM
#   `bigquery-public-data.census_bureau_international.mortality_life_
#    expectancy`
# WHERE
#   year = 2018
# ORDER BY
#   life_expectancy DESC
# 
#       A sample of the query result is shown in Figure 38-4 under Query results.
# 
# 
# 
# 
# Figure 38-4. First query
# 
# 490
# 
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
            "Running Your First Query",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Running Your First Query"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RunningYour(HierNode):
    def __init__(self):
        super().__init__("Running Your First Query")
        self.add(Content())

# eof
