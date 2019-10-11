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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Delete Objects from a Bucket")
        self.add(MarkdownBlock("# Delete Objects from a Bucket"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class DeleteObjects(HierNode):
    def __init__(self):
        super().__init__("Delete Objects from a Bucket")
        self.add(Content())

# eof
