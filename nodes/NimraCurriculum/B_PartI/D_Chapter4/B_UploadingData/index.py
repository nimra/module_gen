# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# Chapter 4   Google Cloud Storage (GCS)
# 
# 
# 
# 
# Figure 4-3. An empty bucket
# 
# 
# 
# 
# Figure 4-4. Upload an object
# 28
# 
#                                 Chapter 4   Google Cloud Storage (GCS)
# 
# 
# 
# 
# Figure 4-5. Upload successful
# 
# 
# 
# 
#                                                                    29
# 
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Uploading Data to a Bucket")
        self.add(MarkdownBlock("# Uploading Data to a Bucket"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UploadingData(HierNode):
    def __init__(self):
        super().__init__("Uploading Data to a Bucket")
        self.add(Content())

# eof
