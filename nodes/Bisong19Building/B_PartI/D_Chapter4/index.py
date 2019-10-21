# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk

from .A_Createa.index import Createa as A_Createa
from .B_UploadingData.index import UploadingData as B_UploadingData
from .C_DeleteObjects.index import DeleteObjects as C_DeleteObjects
from .D_FreeUp.index import FreeUp as D_FreeUp
from .E_Workingwith.index import Workingwith as E_Workingwith

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Chapter 4: Google Cloud Storage (GCS)",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Chapter 4: Google Cloud Storage (GCS)"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Chapter4(HierNode):
    def __init__(self):
        super().__init__("Chapter 4: Google Cloud Storage (GCS)")
        self.add(Content())
        self.add(A_Createa())
        self.add(B_UploadingData())
        self.add(C_DeleteObjects())
        self.add(D_FreeUp())
        self.add(E_Workingwith())

# eof
