# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The Challenge of Big Data
# Due to the expansion of data at the turn of the twenty-first century epitomized by the
# so-called 3Vs of big data, which are volume, velocity, and variety. Volume refers to the
# increasing size of data, velocity the speed at which data is acquired, and variety the
# diverse types of data that are available. For others, this becomes 5Vs with the inclusion
# of value and veracity to mean the usefulness of data and the truthfulness of data,
# respectively. We have observed data volume blowout from the megabyte (MB) to the
# terabyte (TB) scale and now exploding past the petabyte (PB). We have to find new
# and improved means of storing and processing this ever-increasing dataset. Initially,
# this challenge of storage and data processing was addressed by the Hadoop ecosystem
# and other supporting frameworks, but even these have become expensive to manage
# and scale, and this is why there is a pivot to cloud-managed, elastic, secure, and
# high-­availability data storage and processing capabilities.
# 
#      On the other hand, for most applications and business use cases, there is a need to
# carry out real-time analysis on data due to the vast amount of data created and available
# at a given moment. Previously, getting insights from data and unlocking value had
# been down to traditional analysis on batch data workloads using statistical tools such
# as Excel, Minitab, or SPSS. But in the era of big data, this is changing, as more and more
# businesses and institutions want to understand the information in their data at a real-­
# time or at worst near real-time pace.
#      Another vertical to the big data conundrum is that of variety. Formerly, a pre-defined
# structure had to be imposed on data in order to easily store them as well as make it
# easy for data analysis. However, a wide diversity of datasets are now collected and
# stored such as spatial maps, image data, video data, audio data, text data from emails
# and other documents, and sensor data. As a matter of fact, a far larger amount of
# datasets in the wild are unstructured. This led to the development of unstructured
# or semi-structured databases such as Elasticsearch, Solr, HBase, Cassandra, and
# MongoDB, to mention just a few.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "The Challenge of Big Data",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# The Challenge of Big Data"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class TheChallenge(HierNode):
    def __init__(self):
        super().__init__("The Challenge of Big Data")
        self.add(Content())

# eof
