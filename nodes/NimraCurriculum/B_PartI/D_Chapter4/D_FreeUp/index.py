# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Chapter 4   Google Cloud Storage (GCS)
# 
# 
# Delete Objects from a Bucket
# Click the checkbox beside the file and click ‘DELETE’ as shown in Figure 4-6 to delete an
# object from a bucket.
# 
# 
# 
# 
# Figure 4-6. Delete a file
# 
# 
# Free Up Storage Resource
# To delete a bucket or free up a storage resource to prevent billing on a resource that is not
# used, click the checkbox beside the bucket in question, and click ‘DELETE’ to remove
# the bucket and its contents. This action is not recoverable. See Figures 4-7 and 4-8.
# 
# 
# 
# 
# 30
# 
#                                       Chapter 4   Google Cloud Storage (GCS)
# 
# 
# 
# 
# Figure 4-7. Select bucket to delete
# 
# 
# 
# 
# Figure 4-8. Delete bucket
#                                                                          31
# 
# Chapter 4    Google Cloud Storage (GCS)
# 
# 
# Working with GCS from the Command Line
# In this section, we’ll carry out similar commands for creating and deleting buckets and
# objects on GCS from the command-line interface.
# 
#       •     Creating a bucket: To create a bucket, execute the command
# 
#             gsutil mb gs://[BUCKET_NAME]
# 
#             As an example, we’ll create a bucket titled ‘hwosa_09_docs’.
# 
#             gsutil mb gs://hwosa_09_docs
# 
#             Creating gs://hwosa_09_docs/...
# 
#             List buckets on GCP project.
# 
#             gsutil ls
# 
#             gs://hwosa_09_docs/
#             gs://my-first-bucket-ieee-carleton/
# 
#       •     Uploading objects to cloud bucket: To transfer objects from a local
#             directory to the cloud bucket, execute the command
# 
#             gsutil cp -r [LOCAL_DIR] gs://[DESTINATION BUCKET]
# 
#             Copy an image file from the desktop to a bucket on GCP.
# 
#             gsutil cp -r /Users/ekababisong/Desktop/Howad.jpeg
#             gs://hwosa_09_docs/
# 
#             Copying file:///Users/ekababisong/Desktop/Howad.jpeg
#             [Content-Type=image/jpeg]...
#             - [1 files][ 49.8 KiB/ 49.8 KiB]
#             Operation completed over 1 objects/49.8 KiB.
# 
#             List objects in bucket.
# 
#             gsutil ls gs://hwosa_09_docs
# 
#             gs://hwosa_09_docs/Howad.jpeg
# 
# 
# 
# 
# 32
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Free Up Storage Resource")
        self.add(MarkdownBlock("# Free Up Storage Resource"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FreeUp(HierNode):
    def __init__(self):
        super().__init__("Free Up Storage Resource")
        self.add(Content())

# eof
