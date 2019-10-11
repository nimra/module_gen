# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Chapter38.index import Chapter38 as A_Chapter38
from .B_Chapter39.index import Chapter39 as B_Chapter39
from .C_Chapter40.index import Chapter40 as C_Chapter40
from .D_Chapter41.index import Chapter41 as D_Chapter41
from .E_Chapter42.index import Chapter42 as E_Chapter42
from .F_Chapter43.index import Chapter43 as F_Chapter43
from .G_Chapter44.index import Chapter44 as G_Chapter44

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PART VII
# 
# Advanced Analytics/
# Machine Learning on
# Google Cloud Platform
# 
# CHAPTER 38
# 
# 
# 
# Google BigQuery
# BigQuery is a Google-managed data warehouse product that is highly scalable, fast, and
# optimized for data analytics with rudimentary in-built machine learning capabilities
# as part of the product offering. It is also one of Google’s many serverless products. This
# means that you do not physically manage the infrastructure assets and the overhead
# responsibilities/costs. It is only used to solve the business use case, and it just works in a
# highly performant manner.
#      BigQuery is suited for storing and analyzing structured data. The idea of structured
# data is that it must have a schema that describes the columns or fields of the dataset. CSV
# or JSON files are examples of structured data formats. BigQuery differentiates itself from
# other relational databases in that it can store a collection of other fields (or columns) as a
# record type, and a particular field in a row can have more than one value. These features
# make BigQuery more expressive for storing datasets without the flat row constraint of
# relational databases.
#      Similar to relational databases, BigQuery organizes rows into tables, and are
# accessed using the familiar Structured Query Language (SQL) for databases. However,
# individual rows in a table cannot be updated by running a SQL Update statement. Tables
# can only be appended to or entirely re-written. Meanwhile, a group of tables in BigQuery
# is organized into datasets.
#      When a query is executed in BigQuery, it runs in parallel on thousands of cores.
# This feature greatly accelerates the performance of query execution and consequently
# the speed of gaining insights from your data. This ability for massive parallel execution
# is one of the major reasons individuals, companies, and institutions are migrating to
# BigQuery as their data warehouse of choice.
#      Also BigQueryML is a powerful platform for building machine learning models
# inside of BigQuery. The models take advantage of automated feature engineering and
# hyper-parameter optimization and are automatically updated based on changes to
# the underlying dataset. This feature is extremely powerful and lowers the threshold
# 
#                                                                                           485
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_38
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Part VII: Advanced Analytics/Machine Learning on Google Cloud Platform")
        self.add(MarkdownBlock("# Part VII: Advanced Analytics/Machine Learning on Google Cloud Platform"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class PartVII(HierNode):
    def __init__(self):
        super().__init__("Part VII: Advanced Analytics/Machine Learning on Google Cloud Platform")
        self.add(Content())
        self.add(A_Chapter38())
        self.add(B_Chapter39())
        self.add(C_Chapter40())
        self.add(D_Chapter41())
        self.add(E_Chapter42())
        self.add(F_Chapter43())
        self.add(G_Chapter44())

# eof
