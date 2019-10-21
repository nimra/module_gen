# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create a Bucket
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
# 
# Figure 4-2. Create a bucket

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Create a Bucket",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Create a Bucket"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Createa(HierNode):
    def __init__(self):
        super().__init__("Create a Bucket")
        self.add(Content())

# eof
