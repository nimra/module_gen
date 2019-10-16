# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Categories of Cloud Solutions
# The cloud is a terminology that describes large sets of computers that are networked
# together in groups called data centers. These clustered machines can be interacted with
# via dashboards, command-line interfaces, REST APIs, and client libraries. Data centers
# are often distributed across multiple geographical locations. The size of data centers is
# over 100,000 sq. ft. (and those are the smaller sizes!). Cloud computing solutions can be
# broadly categorized into three, namely, the public, private, and hybrid cloud. Let’s briefly
# discuss them:
# 
#       •     Public cloud: Public clouds are the conventional cloud computing
#             model, where cloud service providers make available their
#             computing infrastructure and products for general use by other
#             enterprises and individuals (see Figure 1-1). In public clouds, the
#             cloud service provider is responsible for managing the hardware
#             configuration and servicing.
# 
# 
# 
# 
# Figure 1-1. The public cloud
# 
#       •   Private cloud: In a private cloud, an organization is solely responsible
#           for the management and servicing of its computing infrastructure.
#           The machines in a private cloud can be located on-premises, or it
#           can be hosted with a cloud service provider but routed on a private
#           network.
# 
#       •   Hybrid cloud: The hybrid cloud is a compromise between the cost
#           and efficiency of a public cloud and the data sovereignty and in-­
#           house security assurances of the private cloud. Many companies
#           and institutions opt for a hybrid cloud and multi-cloud by using
#           technology solutions to facilitate easy porting and sharing of data and
#           applications between on-premise and cloud-based infrastructures.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Categories of Cloud Solutions",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Categories of Cloud Solutions"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Categoriesof(HierNode):
    def __init__(self):
        super().__init__("Categories of Cloud Solutions")
        self.add(Content())

# eof
