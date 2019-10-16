# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Cloud Storage
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
# 
# Figure 2-2. Cloud storage products

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Cloud Storage",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Cloud Storage"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CloudStorage(HierNode):
    def __init__(self):
        super().__init__("Cloud Storage")
        self.add(Content())

# eof
