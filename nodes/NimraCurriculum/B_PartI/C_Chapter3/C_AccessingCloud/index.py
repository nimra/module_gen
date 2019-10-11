# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
        super().__init__("Accessing Cloud Platform Services")
        self.add(MarkdownBlock("# Accessing Cloud Platform Services"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class AccessingCloud(HierNode):
    def __init__(self):
        super().__init__("Accessing Cloud Platform Services")
        self.add(Content())

# eof
