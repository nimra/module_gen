# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Public Datasets",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Public Datasets"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PublicDatasets(HierNode):
    def __init__(self):
        super().__init__("Public Datasets")
        self.add(Content())

# eof
