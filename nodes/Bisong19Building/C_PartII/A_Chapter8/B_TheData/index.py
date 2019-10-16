# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The Data Science Opportunity
# In the new age, where data has inevitably and irreversibly become the new gold, the
# greatest needs of organizations are the skills required for data governance and analytics
# to unlock intelligence and value from data as well as the expertise to develop and
# productionize enterprise data products. This has led to new roles within the data science
# umbrella such as
#       •     Data analysts/scientist who specialize in mining intelligence
#             from data using statistical techniques and computational tools by
#             understanding the business use case
# 
#       •     Data engineers/architects who specialize in architecting and
#             managing the infrastructure for efficient big data pipelines by
#             ensuring that the data platform is redundant, scalable, secure, and
#             highly available
# 
#       •     Machine learning engineers who specialize in designing and
#             developing machine learning algorithms as well as incorporating
#             them into production systems for online or batch prediction services

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Data Science Opportunity",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# The Data Science Opportunity"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheData(HierNode):
    def __init__(self):
        super().__init__("The Data Science Opportunity")
        self.add(Content())

# eof
