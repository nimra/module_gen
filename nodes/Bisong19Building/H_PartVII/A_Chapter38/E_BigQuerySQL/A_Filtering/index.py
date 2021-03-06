# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


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
# Chapter 38   Google BigQuery
# 
# WHERE
#   year = 2018
# ORDER BY
#   fertility_rate DESC
# LIMIT
#   10'
# 
# Waiting on bqjob_r142a3f484f713c4a_0000016626f7f063_1 ... (0s) Current
# status: DONE
# +-------------+----------------+
# |   country   | fertility_rate |
# +-------------+----------------+
# | Niger       |        6.3504 |
# | Angola      |         6.0945 |
# | Burundi     |          5.934 |
# | Mali        |            5.9 |
# | Chad        |            5.9 |
# | Somalia     |          5.702 |
# | Uganda      |           5.62 |
# | Zambia      |          5.582 |
# | Malawi      |         5.4286 |
# | South Sudan |           5.34 |
# +-------------+----------------+
# 
#     In the preceding query, the SQL command SELECT is used to select fields or
# columns from the table. What follows after the SELECT keyboard is the list of the column
# names separated by a comma. The keyword AS is used to give an alternative name to
# the column that will be displayed in the resulting table when the query is executed. The
# keyword FROM is used to point to the table from which the data is being retrieved. In
# BigQuery, using the standard SQL, the table name is prefixed by the database name
# and the project ID is surrounded by a pair of backticks (i.e., ‘project_id.database_name.
# table_name‘).
#     The keyword WHERE is used to filter the rows returned from the query. The keyword
# ORDER BY is used to arrange the retrieved data in either ascending or descending
# order by a specified column or set of columns. The keyword LIMIT truncates the results
# retrieved from the query.
# 
# 
# 500
# 
#                                                            Chapter 38   Google BigQuery
# 
# Aggregation
# The following query selects the average population for each country between the years
# 2000 and 2018 from the ‘midyear_population’ table in the ‘census_bureau_international’
# dataset. The resulting table is arranged in descending order.
# 
# bq query --use_legacy_sql=false 'SELECT
#   country_name AS country,
#   AVG(midyear_population) AS average_population
# FROM
#   `bigquery-public-data.census_bureau_international.midyear_population`
# WHERE
#   year >= 2000 AND year <= 2018
# GROUP BY
#   country
# ORDER BY
#   average_population DESC
# LIMIT
#   20'
# 
# Waiting on bqjob_r95be3d17e726415_000001662890a68f_1 ... (1s) Current
# status: DONE
# +------------------+----------------------+
# |     country      |  average_population  |
# +------------------+----------------------+
# | China            | 1.3285399873157892E9 |
# | India            |  1.154912377105263E9 |
# | United States    | 3.0594302226315784E8 |
# | Indonesia        | 2.3984691394736844E8 |
# | Brazil           |  1.930978929473684E8 |
# | Pakistan         | 1.8112083526315784E8 |
# | Nigeria          | 1.6255564478947365E8 |
# | Bangladesh       |  1.447749475789474E8 |
# | Russia           | 1.4330035963157892E8 |
# | Japan            | 1.2727527184210527E8 |
# | Mexico           | 1.1269223210526317E8 |
# | Philippines      |          9.1357295E7 |
# 
#                                                                                    501
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Filtering",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Filtering"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Filtering(HierNode):
    def __init__(self):
        super().__init__("Filtering")
        self.add(Content())

# eof
