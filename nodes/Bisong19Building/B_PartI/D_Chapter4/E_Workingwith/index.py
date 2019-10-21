# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Working with GCS from the Command Line
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
#       •   Deleting objects from the cloud bucket: To delete a specific file from
#           the bucket, execute
# 
#           gsutil rm -r gs://[SOURCE_BUCKET]/[FILE_NAME]
# 
#           To delete all files from the bucket, execute
# 
#           gsutil rm -a gs://[SOURCE_BUCKET]/**
# 
#           As an example, let’s delete the image file in the bucket ‘gs://hwosa_09_docs’.
# 
#           gsutil rm -r gs://hwosa_09_docs/Howad.jpeg
# 
#           Removing gs://hwosa_09_docs/Howad.jpeg#1537539161893501...
#           / [1 objects]
#           Operation completed over 1 objects.
# 
#       •   Deleting a bucket: When a bucket is deleted, all the files within that
#           bucket are also deleted. This action is irreversible. To delete a bucket,
#           execute the command
# 
#           gsutil rm -r gs://[SOURCE_BUCKET]/
# 
#           Delete the bucket ‘gs://hwosa_09_docs’
# 
#           gsutil rm -r gs://hwosa_09_docs/
# 
#           Removing gs://hwosa_09_docs/...
# 
#     This chapter works through uploading and deleting data from Google Cloud Storage
# using the Cloud GUI console and command-line tools.
#     In the next chapter, we will introduce Google Compute Engines, which are virtual
# machines running on Google’s distributed data centers and are connected via state-of-­
# the-art fiber optic network. These machines are provisioned to lower the cost and speed
# up the processing of computing workloads.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Working with GCS from the Command Line",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Working with GCS from the Command Line"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Workingwith(HierNode):
    def __init__(self):
        super().__init__("Working with GCS from the Command Line")
        self.add(Content())

# eof
