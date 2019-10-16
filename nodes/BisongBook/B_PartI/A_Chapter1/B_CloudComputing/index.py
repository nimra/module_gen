# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Cloud Computing Models
# Cloud computing is also categorized into three models of service delivery. They are
# illustrated as a pyramid as shown in Figure 1-2, where the layers of infrastructure
# abstraction increase as we approach the apex of the pyramid:
# 
#       •   Infrastructure as a Service (IaaS): This model is best suited for
#           enterprises or individuals who want to manage the hardware
#           infrastructure that hosts their data and applications. This level
#           of fine-grained management requires the necessary system
#           administration skills.
# 
#       •   Platform as a Service (PaaS): In the PaaS model, the hardware
#           configuration is managed by the cloud service provider, as well as
#           other system and development tools. This relieves the user to focus
#           on the business logic for quick and easy deployment of application
#           and database solutions. Another concept that comes up together
#           with PaaS is the idea of Serverless, where the cloud service provider
#           manages a scalable infrastructure that utilizes and relinquishes
#           resources according to demand.
# 
#       •   Software as a Service (SaaS): The SaaS model is most recognizable
#           by the general public, as a great deal of users interact with SaaS
#           applications without knowing. The typical examples of SaaS
#             applications are enterprise email suites such as Gmail, Outlook, and
#             Yahoo! Mail. Others include storage platforms like Google Drive and
#             Dropbox, photo software like Google Photos, and CRM e-suites like
#             Salesforce and Oracle E-business Suite.
# 
# 
# 
# 
# Figure 1-2. Models of cloud computing
# 
#     In this chapter, we summarized the practice of cloud computing by explaining the
# different categories of cloud solutions and the models for service delivery over the cloud.
#     The next chapters in Part 1 will provide an introduction to Google Cloud Platform
# Infrastructure and Services and introduce JupyterLab Instances, and Google
# Colaboratory for prototyping machine learning models and doing data science and
# analytics tasks.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Cloud Computing Models",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Cloud Computing Models"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class CloudComputing(HierNode):
    def __init__(self):
        super().__init__("Cloud Computing Models")
        self.add(Content())

# eof
