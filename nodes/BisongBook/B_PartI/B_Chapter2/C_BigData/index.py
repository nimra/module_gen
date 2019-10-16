# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Big Data and Analytics
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Big Data and Analytics",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Big Data and Analytics"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class BigData(HierNode):
    def __init__(self):
        super().__init__("Big Data and Analytics")
        self.add(Content())

# eof
