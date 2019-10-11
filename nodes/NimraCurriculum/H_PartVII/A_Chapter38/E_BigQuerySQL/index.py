# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Filtering.index import Filtering as A_Filtering
from .B_Aggregation.index import Aggregation as B_Aggregation
from .C_Joins.index import Joins as C_Joins
from .D_Subselect.index import Subselect as D_Subselect
from .E_TheCase.index import TheCase as E_TheCase

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                                Chapter 38   Google BigQuery
# 
#                               |- market: string
#                               |- close_ratio: string
#                               |- spread: string
# 
#       •   Delete a table.
# 
#           bq rm crypto_data_terminal.markets_terminal
# 
#       •   Delete a Dataset. This command will delete a Dataset with all its
#           containing tables.
# 
#           bq rm -r crypto_data_terminal
# 
# 
# 
# BigQuery SQL
# In this section, we’ll have an overview of SQL by executing some examples that gives a
# broad perspective of what can be achieved with SQL. New users who have not used SQL
# before will benefit from this section. Also, SQL is amazingly easy and intuitive to use
# that non-technical people like personnel in marketing and sales are experts at this even
# sometimes more than programmers. It is an expressive declarative language.
#     BigQuery works with both the standard SQL which supports SQL 2011 standard and
# the legacy SQL syntax which is a non-standard variant of SQL. However, standard SQL is
# the preferred query syntax for BigQuery. In experimenting with SQL, we will work with
# the census_bureau_international public dataset. The following queries are available in
# the chapter notebook of the book repository.
# 
# 
# Filtering
# The following query selects the fertility rate for each country in the year 2018 from the
# ‘age_specific_fertility_rates’ table in the ‘census_bureau_international’ dataset. The
# resulting table is arranged in descending order.
# 
# bq query --use_legacy_sql=false 'SELECT
#   country_name AS country,
#   total_fertility_rate AS fertility_rate
# FROM
#   `bigquery-public-data.census_bureau_international.age_specific_fertility_
#    rates`
#                                                                                         499
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("BigQuery SQL")
        self.add(MarkdownBlock("# BigQuery SQL"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BigQuerySQL(HierNode):
    def __init__(self):
        super().__init__("BigQuery SQL")
        self.add(Content())
        self.add(A_Filtering())
        self.add(B_Aggregation())
        self.add(C_Joins())
        self.add(D_Subselect())
        self.add(E_TheCase())

# eof
