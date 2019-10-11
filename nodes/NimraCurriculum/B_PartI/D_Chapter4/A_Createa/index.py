# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHAPTER 4
# 
# 
# 
# Google Cloud Storage
# (GCS)
# Google Cloud Storage is a product for storing a wide range of diverse data objects.
# Cloud storage may be used to store both live and archival data. It has guarantees of
# scalability (can store increasingly large data objects), consistency (the most updated
# version is served on request), durability (data is redundantly placed in separate
# geographic locations to eliminate loss), and high availability (data is always available and
# accessible).
#     Let’s take a brief tour through creating and deleting a storage bucket, as well as
# uploading and deleting files from a cloud storage bucket.
# 
# 
# 
# C
#  reate a Bucket
# A bucket, as the name implies, is a container for storing data objects on GCP. A bucket is
# the base organizational structure on Cloud Storage. It is similar to the topmost directory
# on a file system. Buckets may have a hierarchy of sub-folders containing data assets.
#     To create a bucket,
# 
#        1. Click ‘Create bucket’ on the cloud storage dashboard as shown in
#           Figure 4-1.
# 
#        2. Give the bucket a unique name (see Figure 4-2). Buckets in
#           GCP must have a global unique name. That is to say, no two
#           storage buckets on Google Cloud can have the same name. A
#           common naming convention for buckets is to prefix with your
#           organization’s domain name.
# 
# 
#                                                                                           25
# © Ekaba Bisong 2019
# E. Bisong, Building Machine Learning and Deep Learning Models on Google Cloud Platform,
# https://doi.org/10.1007/978-1-4842-4470-8_4
# 
# Chapter 4   Google Cloud Storage (GCS)
# 
#       3. Select a storage class. A multi-region storage class is for buckets
#          frequently accessed all over the world, whereas the cold-line
#          storage is more or less for storing backup files. For now, the default
#          selection is okay.
# 
#       4. Click ‘Create’ to set up a bucket on Google Cloud Storage.
# 
# 
# 
# 
# Figure 4-1. Cloud Storage Console
# 
# 
# 
# 
# 26
# 
#                                                     Chapter 4   Google Cloud Storage (GCS)
# 
# 
# 
# 
# Figure 4-2. Create a bucket
# 
# 
# Uploading Data to a Bucket
# Individual files or folders can be uploaded into a bucket on GCS. As an example, let’s
# upload a file from the local machine.
#     To upload a file to a cloud storage bucket on GCP,
#       1. Click ‘UPLOAD FILES’ within the red highlight in Figure 4-3.
# 
#       2. Select the file from the file upload window, and click ‘Open’ as
#          shown in Figure 4-4.
# 
#       3. Upon upload completion, the file is uploaded as an object in GCS
#          bucket (see Figure 4-5).
# 
# 
# 
# 
#                                                                                          27
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Create a Bucket")
        self.add(MarkdownBlock("# Create a Bucket"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Createa(HierNode):
    def __init__(self):
        super().__init__("Create a Bucket")
        self.add(Content())

# eof
