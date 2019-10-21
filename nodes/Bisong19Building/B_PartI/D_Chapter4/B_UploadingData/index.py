# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Uploading Data to a Bucket
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
# 
# Figure 4-3. An empty bucket
# 
# 
# 
# 
# Figure 4-4. Upload an object
# 
# 
# 
# 
# Figure 4-5. Upload successful

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Uploading Data to a Bucket",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Uploading Data to a Bucket"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UploadingData(HierNode):
    def __init__(self):
        super().__init__("Uploading Data to a Bucket")
        self.add(Content())

# eof
