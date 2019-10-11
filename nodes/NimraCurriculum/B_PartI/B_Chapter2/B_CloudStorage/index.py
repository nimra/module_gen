# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 2   An Overview of Google Cloud Platform Services
# 
# 
# 
# 
# Figure 2-1. Cloud compute services
# 
#    For our purposes of machine learning modeling, the cloud compute engine is what
# we will concentrate on. As later seen in Chapter 6, JupyterLab will provision a compute
# engine with all the relevant tools, packages, and frameworks for data analytics and
# modeling machine learning and deep learning solutions.
# 
# 
# 
# C
#  loud Storage
# Google Cloud Storage options provide scalable and real-time storage access to live and
# archival data within the cloud perimeter. Cloud storage as an example is set up to cater
# for any conceivable storage demand. Data stored on cloud storage is available anytime
# and from any location around the world. What’s more, this massive storage power comes
# at an almost negligible cost, taking into consideration the size and economic value of
# the stored data. Moreover, acknowledging the accessibility, security, and consistency
# provided by cloud storage, the cost is worth every penny.
#     The cloud storage products shown in Figure 2-2 include Cloud Storage (general-­
# purpose storage platform), Cloud SQL (cloud-managed MySQL and PostgreSQL), Cloud
# Bigtable (NoSQL petabyte-sized storage), Cloud Spanner (scalable/high availability
# transactional storage), Cloud Datastore (transactional NoSQL database), and Persistent
# Disk (block storage for virtual machines).
# 
# 
# 
# 
# 8
# 
#                                 Chapter 2   An Overview of Google Cloud Platform Services
# 
# 
# 
# 
# Figure 2-2. Cloud storage products
# 
# 
# Big Data and Analytics
# Google Cloud Platform offers a range of serverless big data and analytics solutions for
# data warehousing, stream, and batch analytics, cloud-managed Hadoop ecosystems,
# cloud-based messaging systems, and data exploration. These services provide multiple
# perspectives to mining/generating real-time intelligence from big data.
#     Examples of big data services shown in Figure 2-3 include Cloud BigQuery
# (serverless analytics/data warehousing platform), Cloud Dataproc (fully managed
# Hadoop/Apache Spark infrastructure), Cloud Dataflow (Batch/Stream data
# transformation/processing), Cloud Dataprep (serverless infrastructure for cleaning
# unstructured/structured data for analytics), Cloud Datastudio (data visualization/report
# dashboards), Cloud Datalab (managed Jupyter notebook for machine learning/data
# analytics), and Cloud Pub/Sub (serverless messaging infrastructure).
# 
# 
# 
# 
# Figure 2-3. Big data/analytics serverless platforms
# 
# 
#                                                                                        9
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Cloud Storage")
        self.add(MarkdownBlock("# Cloud Storage"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CloudStorage(HierNode):
    def __init__(self):
        super().__init__("Cloud Storage")
        self.add(Content())

# eof
