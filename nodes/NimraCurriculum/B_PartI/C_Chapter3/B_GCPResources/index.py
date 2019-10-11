# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 3   The Google Cloud SDK and Web CLI
# 
#       5. Click the icon of three lines in the top-left corner of the page
#          (marked with a circle in Figure 3-3), then click Home (marked
#          with a rectangle in Figure 3-3) to open the Google Cloud Platform
#          dashboard (Figure 3-4).
# 
# 
# 
# 
# Figure 3-4. GCP dashboard
# 
#     The Cloud dashboard provides a bird’s-eye summary of the project such as the
# current billing rate and other resource usage statistics. The activity tab to the right gives
# a breakdown of the resource actions performed on the account. This feature is useful
# when building an audit trail of events.
# 
# 
# 
# GCP Resources: Projects
# All the services and features of the Google Cloud Platform are called resources. These
# resources are arranged in a hierarchical order, with the top level being the project.
# The project is like a container that houses all GCP resources. Billing on an account is
# attached to a project. Multiple projects can be created for an account. A project must be
# created before working with GCP.
# 14
# 
#                                               Chapter 3   The Google Cloud SDK and Web CLI
# 
#    To view the projects in the account in Figure 3-5, click the scope picker in the cloud
# console (marked with an oval in Figure 3-6).
# 
# 
# 
# 
# Figure 3-5. Select projects
# 
# 
# 
# 
# Figure 3-6. Scope picker to select projects
# 
# 
# 
# 
#                                                                                        15
# 
# Chapter 3   The Google Cloud SDK and Web CLI
# 
# 
# Accessing Cloud Platform Services
# To access the resources on the cloud platform, click the triple dash in the top-right
# corner of the window. Grouped service offerings are used to organize the resources. For
# example, in Figure 3-7, we can see the products under STORAGE: Bigtable, Datastore,
# Storage, SQL, and Spanner.
# 
# 
# 
# 
# Figure 3-7. Google Cloud Platform services
# 
# Account Users and Permissions
# GCP allows you to define security roles and permissions for every resource in a
# specific project. This feature is particularly useful when a project scales beyond one
# user. New roles and permissions are created for a user through the IAM & admin tab
# (see Figures 3-­8 and 3-9).
# 
# 
# 
# 
# 16
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("GCP Resources: Projects")
        self.add(MarkdownBlock("# GCP Resources: Projects"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class GCPResources(HierNode):
    def __init__(self):
        super().__init__("GCP Resources: Projects")
        self.add(Content())

# eof
